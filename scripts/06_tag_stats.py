#!/usr/bin/env python3
"""Aggregate tag lines from notes/*.md into counts, cross-tabs, and (prop,tool) pairs.

Usage: python3 06_tag_stats.py <notes_dir> <out_md>
Parses blocks starting '### <id> —' and their 'domain:'/'props:'/'tools:' lines
(pipe-separated tags; ignores '+ free' suffixes).
Writes a compact markdown stats file consumed by the synthesis agent.
"""
import collections, glob, os, re, sys

notes_dir, out_md = sys.argv[1], sys.argv[2]

papers, cur = [], None
for f in sorted(glob.glob(os.path.join(notes_dir, "*.md"))):
    for line in open(f, encoding="utf-8"):
        m = re.match(r"^###\s+(\S+)\s*[—-]\s*(.*)$", line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip()}
            papers.append(cur)
            continue
        if cur is None:
            continue
        for key in ("domain", "props", "tools", "role"):
            m = re.match(rf"^{key}:\s*(.+)$", line.strip())
            if m:
                tags = [t.split("+")[0].strip() for t in m.group(1).split("|")]
                cur[key] = [t for t in tags if t]

def norm_papers(papers):
    out, seen = [], set()
    for p in papers:
        if p["id"] in seen or "props" not in p:
            continue
        seen.add(p["id"])
        for k in ("domain", "tools", "role"):
            p.setdefault(k, [])
        out.append(p)
    return out

papers = norm_papers(papers)

def tally(key):
    c = collections.Counter()
    for p in papers:
        for t in set(p[key]):
            c[t] += 1
    return c

L = [f"# Tag stats — {os.path.basename(notes_dir)}", "",
     f"papers with tags: {len(papers)}", ""]

for key, label in (("props", "PROPERTIES (papers proving/studying)"),
                   ("tools", "TOOLS (papers using)"),
                   ("domain", "DOMAINS (papers in)"),
                   ("role", "ROLE of theory")):
    L.append(f"## {label}")
    for t, n in tally(key).most_common():
        L.append(f"- {t}: {n}")
    L.append("")

def crosstab(a, b):
    """for each value of a, top values of b"""
    tab = collections.defaultdict(collections.Counter)
    for p in papers:
        for x in set(p[a]):
            for y in set(p[b]):
                tab[x][y] += 1
    return tab

L.append("## DOMAIN × PROPS (top per domain)")
for d, c in sorted(crosstab("domain", "props").items(), key=lambda kv: -sum(kv[1].values())):
    top = ", ".join(f"{k}({v})" for k, v in c.most_common(5))
    L.append(f"- {d}: {top}")
L.append("")
L.append("## DOMAIN × TOOLS (top per domain)")
for d, c in sorted(crosstab("domain", "tools").items(), key=lambda kv: -sum(kv[1].values())):
    top = ", ".join(f"{k}({v})" for k, v in c.most_common(5))
    L.append(f"- {d}: {top}")
L.append("")

pairs = collections.defaultdict(list)
for p in papers:
    for x in set(p["props"]):
        for y in set(p["tools"]):
            pairs[(x, y)].append(p["id"])
L.append("## PROP × TOOL pairs (for the playbook; ≥2 papers)")
for (x, y), ids in sorted(pairs.items(), key=lambda kv: -len(kv[1])):
    if len(ids) >= 2:
        L.append(f"- {x} × {y}: {len(ids)} — {', '.join(ids[:6])}")
L.append("")

os.makedirs(os.path.dirname(out_md), exist_ok=True)
open(out_md, "w").write("\n".join(L) + "\n")
print(f"{len(papers)} tagged papers -> {out_md}")
