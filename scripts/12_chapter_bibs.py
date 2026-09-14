#!/usr/bin/env python3
"""Per-chapter distributable bibliographies (0 LLM tokens).

Usage: python3 12_chapter_bibs.py <refs.bib> <chapters_dir>
For every chapters/<tool>.tex, scans \\cite{...} keys and writes
chapters/<tool>-all.bib = the CITED corpus entries (from refs.bib) + the chapter's
background file chapters/<tool>.bib. Each chapter + its -all.bib is then a
self-contained distribution unit (chapterbib renders it as that chapter's reference list).
"""
import glob, os, re, sys

refs_f, ch_dir = sys.argv[1], sys.argv[2]

corpus = {}
entry, key = [], None
for line in open(refs_f, encoding="utf-8"):
    m = re.match(r"@article\{(\S+),", line)
    if m:
        key, entry = m.group(1), [line]
    elif key:
        entry.append(line)
        if line.startswith("}"):
            corpus[key] = "".join(entry)
            key, entry = None, []

n = 0
for tex_f in sorted(glob.glob(os.path.join(ch_dir, "*.tex"))):
    tool = os.path.splitext(os.path.basename(tex_f))[0]
    if tool == "ch0":
        continue
    text = open(tex_f, encoding="utf-8").read()
    cites = set()
    for m in re.finditer(r"\\cite[tp]?\{([^}]+)\}", text):
        for k in m.group(1).split(","):
            cites.add(k.strip())
    out = [f"% auto-generated: cited keys of chapters/{tool}.tex "
           f"+ background refs (12_chapter_bibs.py)\n"]
    bg_f = os.path.join(ch_dir, tool + ".bib")
    if os.path.exists(bg_f):
        out.append(open(bg_f, encoding="utf-8").read())
    missing = []
    for k in sorted(cites):
        if k in corpus:
            out.append(corpus[k])
        elif not os.path.exists(bg_f) or k not in open(bg_f, encoding="utf-8").read():
            missing.append(k)
    open(os.path.join(ch_dir, tool + "-all.bib"), "w").write("\n".join(out))
    n += 1
    if missing:
        print(f"  {tool}: MISSING KEYS {missing}")
print(f"wrote {n} chapter bibs -> {ch_dir}/*-all.bib")
