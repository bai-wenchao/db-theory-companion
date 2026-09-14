#!/usr/bin/env python3
"""PODS-vs-SIGMOD tool/property skew audit (pure parsing, no LLM).

Usage: python3 11_pods_audit.py <notes_dir> <papers.jsonl> [plan.json]
Splits tagged papers by the PODS'26 DOI band; reports per-tool and per-property
shares in each cohort, plus PODS share of lecture-note exemplars (plan.json).
"""
import glob, json, os, re, sys

notes_dir, papers_f = sys.argv[1], sys.argv[2]
plan_f = sys.argv[3] if len(sys.argv) > 3 else None

pods_ids = set()
for line in open(papers_f, encoding="utf-8"):
    try:
        p = json.loads(line)
    except Exception:
        continue
    doi = p.get("doi") or ""
    m = re.match(r"\d+\.\d+/(\d+)", doi)
    if m and 3801890 <= int(m.group(1)) <= 3801919:
        pods_ids.add(p["id"])

recs = []
for f in sorted(glob.glob(os.path.join(notes_dir, "*.md"))):
    if os.path.basename(f).startswith(("_queue", "calib")):
        continue
    for b in re.split(r"(?m)^### ", open(f, encoding="utf-8").read()):
        m = re.match(r"(\S+)\s*[—-]", b)
        if not m:
            continue
        rec = {"id": m.group(1), "tools": [], "props": []}
        for line in b.splitlines():
            mm = re.match(r"(props|tools):\s*(.*)", line.strip())
            if mm:
                rec[mm.group(1)] = [t.strip().split(" +")[0].strip()
                                    for t in mm.group(2).split("|")]
        recs.append(rec)

n_pods = sum(1 for r in recs if r["id"] in pods_ids)
print(f"tagged notes: {len(recs)} | PODS-band: {n_pods} ({100*n_pods/len(recs):.1f}%) "
      f"| SIGMOD-proper: {len(recs)-n_pods}")


def dist(key):
    d = {}
    for r in recs:
        for t in r[key]:
            k = t.split("+")[0].strip()
            d.setdefault(k, [0, 0])
            d[k][0 if r["id"] in pods_ids else 1] += 1
    return d


for key in ("tools", "props"):
    d = dist(key)
    print(f"\n== {key.upper()} (PODS / SIGMOD-proper counts, PODS-share, skew vs base "
          f"{100*n_pods/len(recs):.0f}%) ==")
    rows = sorted(d.items(), key=lambda kv: -(kv[1][0] + kv[1][1]))
    for k, (po, si) in rows:
        tot = po + si
        if tot < 3:
            continue
        share = po / tot
        flag = " <== PODS-skewed" if share > n_pods / len(recs) + 0.15 else ""
        print(f"  {k:28s} {po:3d} / {si:3d}   {100*share:4.0f}%{flag}")

if plan_f:
    plan = json.load(open(plan_f))
    tot_ex = pods_ex = 0
    print("\n== lecture-note exemplars by chapter ==")
    for tool, dd in plan["chapters"].items():
        ex = dd["exemplars"]
        po = sum(1 for e in ex if e["pods"])
        tot_ex += len(ex); pods_ex += po
        print(f"  {tool:24s} {po}/{len(ex)} PODS")
    print(f"  TOTAL {pods_ex}/{tot_ex} PODS "
          f"({100*pods_ex/max(1,tot_ex):.0f}% vs {100*n_pods/len(recs):.0f}% corpus base rate)")
