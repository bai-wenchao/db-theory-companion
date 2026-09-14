#!/usr/bin/env python3
"""Download arXiv TeX sources (e-print tarballs) for papers with a known arXiv id.

Usage: python3 02t_download_tex.py <papers.jsonl> <s2_map.json> <src_root> [limit] [--only-missing-pdf]
  e.g. python3 02t_download_tex.py data/sigmod26/papers.jsonl data/sigmod26/s2_arxiv_map.json data/sigmod26/src

Extracts each tarball to <src_root>/<id>/. Skips ids already extracted. Appends
{id,status,source,bytes} lines to <src_root>/manifest_tex.jsonl. Throttle ~1.5s.
Handles: tar.gz / tar / gzipped single .tex / plain tex.
"""
import gzip, io, json, os, sys, tarfile, time, urllib.request

papers_f, map_f, src_root = sys.argv[1], sys.argv[2], sys.argv[3]
args = [a for a in sys.argv[4:] if not a.startswith("--")]
limit = int(args[0]) if args else None
os.makedirs(src_root, exist_ok=True)
manifest_f = os.path.join(src_root, "manifest_tex.jsonl")

UA = {"User-Agent": "db-theory-survey/0.1 (arXiv e-print; academic survey)"}
doi2arxiv = json.load(open(map_f))
id2doi = {p["id"]: p.get("doi", "") for p in map(json.loads, open(papers_f))}


def fetch(url, timeout=120):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def already(dest):
    return os.path.isdir(dest) and any(f.endswith(".tex") for f in os.listdir(dest))


def extract_any(blob, dest):
    os.makedirs(dest, exist_ok=True)
    bio = io.BytesIO(blob)
    if tarfile.is_tarfile(bio):
        with tarfile.open(fileobj=bio) as tf:
            tf.extractall(dest, filter="data")
        return any(f.endswith(".tex") for _, _, files in os.walk(dest) for f in files)
    if blob[:2] == b"\x1f\x8b":
        raw = gzip.decompress(blob)
        if b"\\documentclass" in raw or b"\\begin{document}" in raw:
            open(os.path.join(dest, "main.tex"), "wb").write(raw)
            return True
    if b"\\documentclass" in blob or b"\\begin{document}" in blob:
        open(os.path.join(dest, "main.tex"), "wb").write(blob)
        return True
    return False


targets = [(pid, doi2arxiv[doi]) for pid, doi in id2doi.items()
           if doi in doi2arxiv and doi2arxiv[doi]]
if limit:
    targets = targets[:limit]

stats = {"ok": 0, "skip": 0, "fail": 0}
mf = open(manifest_f, "a")
for pid, aid in targets:
    dest = os.path.join(src_root, pid)
    if already(dest):
        stats["skip"] += 1
        continue
    try:
        blob = fetch(f"https://arxiv.org/e-print/{aid}")
        if extract_any(blob, dest):
            stats["ok"] += 1
            rec = {"id": pid, "status": "ok", "source": f"arxiveprint:{aid}", "bytes": len(blob)}
        else:
            stats["fail"] += 1
            rec = {"id": pid, "status": "fail", "source": f"arxiveprint:{aid}",
                   "why": "no-tex-after-extract"}
    except Exception as e:
        stats["fail"] += 1
        rec = {"id": pid, "status": "fail", "source": f"arxiveprint:{aid}",
               "why": type(e).__name__}
    mf.write(json.dumps(rec) + "\n")
    mf.flush()
    time.sleep(1.5)
mf.close()
print(json.dumps(stats), flush=True)
