#!/usr/bin/env python3
"""Download PDFs for papers.jsonl. Usage:

  python3 02_download_pdfs.py <papers.jsonl> <pdf_dir> [limit]

Strategy v3 (network realities of 2026-09-13):
  0. ONE S2 batch POST (DOI -> arXiv id / openAccessPdf) for all papers.
  1. arXiv PDF by exact S2 arXiv id          (arxiv.org/pdf — works, no Cloudflare)
  2. S2 openAccessPdf.url if non-ACM host    (author copies, openreview, ...)
  3. Unpaywall non-publisher locations       (green OA mirrors)
  4. ACM direct                              (Cloudflare 403s scripts; last resort)
  5. arXiv API title search                  (only if --arxiv-title flag; API was 429-throttled)

Appends {id,status,source,tries,why} to <data_dir>/manifest.jsonl (append-only).
Skips papers with pdf on disk; gives up after 3 failed rounds (tries counted from
previous manifest lines). Politeness: ~1.2s between downloads, backoff on 429s.
"""
import difflib, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

papers_f, pdf_dir = sys.argv[1], sys.argv[2]
limit = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else None
USE_ARXIV_TITLE = "--arxiv-title" in sys.argv
data_dir = os.path.dirname(pdf_dir.rstrip("/"))
manifest_f = os.path.join(data_dir, "manifest.jsonl")

BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
S2_UA = "db-theory-survey/0.1"

papers = [json.loads(l) for l in open(papers_f)]
if limit:
    papers = papers[:limit]

done = {}
if os.path.exists(manifest_f):
    for line in open(manifest_f):
        try:
            r = json.loads(line)
            done.setdefault(r["id"], []).append(r)
        except Exception:
            pass

todo = [p for p in papers
        if not (os.path.exists(os.path.join(pdf_dir, p["id"] + ".pdf"))
                and os.path.getsize(os.path.join(pdf_dir, p["id"] + ".pdf")) > 10000)
        and sum(1 for r in done.get(p["id"], []) if r.get("status") == "fail") < 3]
print(f"[v3] papers={len(papers)} todo={len(todo)}", flush=True)


def fetch(url, timeout=90, binary=True, ua=BROWSER_UA, data=None, headers=None):
    h = {"User-Agent": ua}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read() if binary else r.read().decode("utf-8", "replace")


def is_pdf(b):
    return b[:5] == b"%PDF-"


def s2_batch(dois):
    """One batched S2 lookup: DOI -> {arxiv, oa_url, title}."""
    url = ("https://api.semanticscholar.org/graph/v1/paper/batch"
           "?fields=externalIds,openAccessPdf,title")
    body = json.dumps({"ids": [f"DOI:{d}" for d in dois]}).encode()
    for attempt in range(5):
        try:
            arr = json.loads(fetch(url, binary=False, ua=S2_UA, data=body,
                                   headers={"Content-Type": "application/json"}))
            out = {}
            for d, w in zip(dois, arr):
                if not w:
                    continue
                out[d] = {"arxiv": (w.get("externalIds") or {}).get("ArXiv"),
                          "oa": (w.get("openAccessPdf") or {}).get("url") or ""}
            return out
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503) and attempt < 4:
                time.sleep(25 * (attempt + 1))
                continue
            print(f"[warn] s2 batch HTTP {e.code}", flush=True)
            return {}
        except Exception as e:
            print(f"[warn] s2 batch {type(e).__name__}", flush=True)
            time.sleep(10)
    return {}


def try_download(url):
    try:
        b = fetch(url)
        return b if is_pdf(b) else None
    except Exception:
        return None


def unpaywall_locations(doi):
    try:
        d = json.loads(fetch(f"https://api.unpaywall.org/v2/{doi}?email=survey@example.org",
                             binary=False, ua=S2_UA))
    except Exception:
        return []
    urls = []
    for loc in d.get("oa_locations") or []:
        if loc.get("host_type") == "publisher":
            continue
        for u in (loc.get("url_for_pdf"), loc.get("url")):
            if u and u not in urls:
                urls.append(u)
    return urls


def arxiv_title_search(title):
    q = urllib.parse.quote(f'ti:"{title}"')
    try:
        xml = fetch("https://export.arxiv.org/api/query?search_query="
                    f"{q}&max_results=5", binary=False, ua=S2_UA)
    except Exception:
        return None
    ATOM = "{http://www.w3.org/2005/Atom}"
    try:
        root = ET.fromstring(xml)
    except Exception:
        return None
    norm = lambda t: re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()
    for e in root.findall(f"{ATOM}entry"):
        at = " ".join("".join(e.find(f"{ATOM}title").itertext()).split()).rstrip(".")
        if difflib.SequenceMatcher(None, norm(title), norm(at)).ratio() < 0.82:
            continue
        return e.find(f"{ATOM}id").text.rsplit("/", 1)[-1]
    return None


# ---- stage 0: batch metadata (or cached map from data_dir/s2_arxiv_map.json) ----
by_doi = {}
map_f = os.path.join(data_dir, "s2_arxiv_map.json")
if os.path.exists(map_f):
    cached = json.load(open(map_f))
    by_doi = {d: {"arxiv": a, "oa": ""} for d, a in cached.items()}
    print(f"[v3] using cached s2 map: {len(by_doi)} arXiv ids", flush=True)
need = [p for p in todo if p.get("doi") and p["doi"] not in by_doi]
for i in range(0, len(need), 400):
    chunk = [p["doi"] for p in need[i:i + 400]]
    by_doi.update(s2_batch(chunk))
    time.sleep(2)
if need and not os.path.exists(map_f):
    json.dump({d: v["arxiv"] for d, v in by_doi.items() if v["arxiv"]},
              open(map_f, "w"))
print(f"[v3] s2 batch resolved {len(by_doi)}/{len(need)} DOIs "
      f"({sum(1 for v in by_doi.values() if v['arxiv'])} with arXiv id)", flush=True)

# ---- per-paper downloads ----
stats = {"ok": 0, "fail": 0, "skip": 0}
mf = open(manifest_f, "a")
for p in papers:
    pid = p["id"]
    path = os.path.join(pdf_dir, f"{pid}.pdf")
    if os.path.exists(path) and os.path.getsize(path) > 10000:
        stats["skip"] += 1
        continue
    tries = sum(1 for r in done.get(pid, []) if r.get("status") == "fail")
    if tries >= 3 or p not in todo:
        stats["skip"] += 1
        continue

    why = []
    src, blob = None, None
    m = by_doi.get(p.get("doi", ""), {})
    if m.get("arxiv"):
        blob = try_download(f"https://arxiv.org/pdf/{m['arxiv']}")
        if blob:
            src = f"arxiv:{m['arxiv']}"
        else:
            why.append("arxiv-dl")
    if blob is None and m.get("oa") and "dl.acm.org" not in m["oa"] and "doi.org" not in m["oa"]:
        blob = try_download(m["oa"])
        if blob:
            src = f"s2oa:{m['oa'][:70]}"
        else:
            why.append("s2oa")
    if blob is None and p.get("doi"):
        for u in unpaywall_locations(p["doi"]):
            time.sleep(1)
            blob = try_download(u)
            if blob:
                src = f"upw:{u[:70]}"
                break
        if blob is None:
            why.append("upw")
    if blob is None and USE_ARXIV_TITLE:
        aid = arxiv_title_search(p["title"])
        time.sleep(3.2)
        if aid:
            blob = try_download(f"https://arxiv.org/pdf/{aid}")
            if blob:
                src = f"arxtitle:{aid}"
        if blob is None:
            why.append("arx-title")
    if blob is None and p.get("doi"):
        blob = try_download(f"https://dl.acm.org/doi/pdf/{p['doi']}")
        if blob:
            src = "acm"
        else:
            why.append("acm403")

    if blob is None:
        stats["fail"] += 1
        rec = {"id": pid, "status": "fail", "source": "|".join(why) or "unknown",
               "tries": tries + 1}
    else:
        open(path, "wb").write(blob)
        stats["ok"] += 1
        rec = {"id": pid, "status": "ok", "source": src, "bytes": len(blob)}
    mf.write(json.dumps(rec) + "\n")
    mf.flush()
    time.sleep(1.2)
mf.close()
print(json.dumps(stats), flush=True)
