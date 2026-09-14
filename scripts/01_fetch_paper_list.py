#!/usr/bin/env python3
"""Fetch paper list for one PACMMOD volume (= one SIGMOD year) into papers.jsonl.

Usage: python3 01_fetch_paper_list.py <vol> <out.jsonl> <label> [issues]
  e.g. python3 01_fetch_paper_list.py 4 data/sigmod26/papers.jsonl sigmod26
       python3 01_fetch_paper_list.py 3 data/sigmod26/papers_r12.jsonl sigmod26 '4|5|6'
  (issues: restrict to these issues, e.g. SIGMOD'26 rounds 1-2 live in Vol 3 issues 4-6)

Primary source: OpenAlex (source lookup + biblio.volume filter, cursor pagination).
Fallback: dblp search API then volume .bib export (currently unreachable via local proxy).
"""
import json, os, re, sys, time, urllib.parse, urllib.request

vol = sys.argv[1] if len(sys.argv) > 1 else "4"
out = sys.argv[2] if len(sys.argv) > 2 else "data/sigmod26/papers.jsonl"
label = sys.argv[3] if len(sys.argv) > 3 else f"sigmod{22 + int(vol)}"
issues = sys.argv[4] if len(sys.argv) > 4 else None
UA = {"User-Agent": "db-theory-survey/0.1 (mailto:survey@example.org)"}

SKIP_TITLE = re.compile(
    r"^(editorial|reviewers?|letter from|preface|table of contents|acknowledg|front matter|in memoriam)", re.I)


def get(url, timeout=40):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def openalex():
    r = get("https://api.openalex.org/sources?search=" +
            urllib.parse.quote("Proceedings of the ACM on Management of Data"))
    src = next((s["id"].rsplit("/", 1)[-1] for s in r["results"]
                if "Management of Data" in s["display_name"]), None)
    if not src:
        raise RuntimeError("PACMMOD source not found on OpenAlex")
    papers, cursor = [], "*"
    filt = f"primary_location.source.id:{src},biblio.volume:{vol}"
    if issues:
        filt += ",biblio.issue:" + "|".join(urllib.parse.quote(i) for i in issues.split("|"))
    base = (f"https://api.openalex.org/works?filter={filt}"
            f"&per-page=200&select=title,doi,authorships,open_access,locations&cursor=")
    while cursor:
        data = get(base + urllib.parse.quote(cursor))
        for w in data.get("results", []):
            t = (w.get("title") or "").strip().rstrip(".")
            if not t or SKIP_TITLE.match(t):
                continue
            urls = []
            for loc in w.get("locations") or []:
                for u in (loc.get("pdf_url"), loc.get("landing_page_url")):
                    if u and u not in urls and "dl.acm.org" not in u:
                        urls.append(u)
            papers.append({
                "title": t,
                "authors": [a.get("author", {}).get("display_name", "")
                            for a in w.get("authorships", [])],
                "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
                "oa_urls": urls,
                "src": "openalex",
            })
        cursor = (data.get("meta") or {}).get("next_cursor")
        time.sleep(0.3)
    return papers


def dblp_api():
    q = urllib.parse.quote(f"toc:journals/pacmmod/pacmmod{vol}")
    papers, first = [], 0
    while True:
        data = get(f"https://dblp.org/search/publ/api?q={q}&h=500&f={first}&format=json")
        hits = data.get("result", {}).get("hits", {})
        total = int(hits.get("@total", 0))
        batch = hits.get("hit") or []
        if not batch:
            break
        for h in batch:
            i = h.get("info", {})
            t = (i.get("title") or "").strip().rstrip(".")
            if not t or SKIP_TITLE.match(t):
                continue
            au = i.get("authors", {}).get("author", [])
            if isinstance(au, dict):
                au = [au]
            papers.append({"title": t,
                           "authors": [a.get("text", "") if isinstance(a, dict) else str(a) for a in au],
                           "doi": i.get("doi") or "", "oa_urls": [], "src": "dblp"})
        first += len(batch)
        if first >= total:
            break
        time.sleep(2)
    return papers


papers = []
for fn in (openalex, dblp_api):
    for attempt in range(3):
        try:
            papers = fn()
            break
        except Exception as e:
            print(f"[warn] {fn.__name__} attempt {attempt + 1}: {type(e).__name__} {str(e)[:100]}",
                  file=sys.stderr)
            time.sleep(3)
    if papers:
        break
if not papers:
    sys.exit("FATAL: could not fetch paper list from any source")

seen, uniq = set(), []
for p in papers:
    k = (p.get("doi") or p["title"]).lower()
    if k in seen:
        continue
    seen.add(k)
    uniq.append(p)
uniq.sort(key=lambda p: p["title"].lower())
for i, p in enumerate(uniq, 1):
    p["id"] = f"{label}-{i:03d}"

os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    for p in uniq:
        f.write(json.dumps(p, ensure_ascii=False) + "\n")
print(f"{len(uniq)} papers ({label}, PACMMOD vol {vol}) -> {out}")
