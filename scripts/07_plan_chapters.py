#!/usr/bin/env python3
"""Plan lecture-note chapters: per-tool exemplar selection (pure parsing, no LLM).

Usage: python3 07_plan_chapters.py <notes_dir> <tags.md> <index.csv> <papers.jsonl> \
           <plan.json> [--max-pods N] [tool1 tool2 ...]
--max-pods N (default 1): cap PODS-band exemplars per chapter — PODS papers have higher
extraction scores, so pure score-ranking over-represents them in showcase positions
(40% of exemplars vs 13% corpus base rate, audit 2026-09-14). PODS picks beyond the cap
are skipped while SIGMOD-proper alternatives remain; forced reuse still allowed.

Reads the tagged notes (### blocks), the score table, and paper metadata; for each tool
(rank order = tags.md count order, or the explicit tool list given) picks up to 6 exemplar
papers sorted by extraction score, GREEDILY DEDUPLICATED across chapters (an id used by an
earlier chapter is skipped while the pool lasts; forced reuse is flagged). PODS'26 ids
(DOI band 3801890-3801919, PACMMOD Vol 4 No 2) are flagged so chapter agents can mark them.
Writes plan.json + prints a compact per-chapter summary for the master's prompts.
"""
import csv, glob, json, os, re, sys

notes_dir, tags_f, idx_f, papers_f, plan_f = sys.argv[1:6]
rest = sys.argv[6:]
max_pods = 1
if "--max-pods" in rest:
    i = rest.index("--max-pods")
    max_pods = int(rest[i + 1])
    del rest[i:i + 2]
chapter_tools = rest

# --- notes: id -> record ---------------------------------------------------------
blocks = {}
for f in sorted(glob.glob(os.path.join(notes_dir, "*.md"))):
    if os.path.basename(f).startswith(("_queue", "calib")):
        continue
    for b in re.split(r"(?m)^### ", open(f, encoding="utf-8").read()):
        if not b.strip():
            continue
        head, rest = b.split("\n", 1)
        m = re.match(r"(\S+)\s*[—-]\s*(.+)", head.strip())
        if not m:
            continue
        rec = {"id": m.group(1), "title": m.group(2).strip(), "file": os.path.basename(f)}
        for line in rest.splitlines():
            mm = re.match(r"(domain|props|tools|usage|role|quote):\s*(.*)", line.strip())
            if mm:
                rec[mm.group(1)] = mm.group(2).strip()
        blocks[rec["id"]] = rec

# --- scores -----------------------------------------------------------------------
score = {}
with open(idx_f, newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        try:
            score[row["id"]] = int(row["score"])
        except (KeyError, ValueError):
            pass

# --- papers: doi -> PODS flag ------------------------------------------------------
pods_ids = set()
for line in open(papers_f, encoding="utf-8"):
    try:
        p = json.loads(line)
    except Exception:
        continue
    doi = p.get("doi") or ""
    mm = re.match(r"\d+\.\d+/(\d+)", doi)
    if mm and 3801890 <= int(mm.group(1)) <= 3801919:
        pods_ids.add(p["id"])

# --- tool ranking from tags.md (if no explicit list) --------------------------------
if not chapter_tools:
    sec, rank = None, []
    for line in open(tags_f, encoding="utf-8"):
        if line.startswith("## "):
            sec = line[3:].strip().upper()
        elif sec and sec.startswith("TOOLS") and (m := re.match(r"- (\S+):\s*(\d+)", line)):
            rank.append((m.group(1), int(m.group(2))))
    chapter_tools = [t for t, _ in rank]

plan, used = {}, set()
for tool in chapter_tools:
    pool = sorted((r for r in blocks.values()
                   if tool in [t.strip() for t in (r.get("tools", "") or "").split("|")]),
                  key=lambda r: -score.get(r["id"], 0))
    kept, n_pods = [], 0
    for r in pool:
        reused = r["id"] in used
        is_pods = r["id"] in pods_ids
        # PODS cap: skip PODS exemplars beyond the quota while SIGMOD-proper options remain
        if is_pods and n_pods >= max_pods and \
                sum(1 for x in pool if x["id"] not in pods_ids) > len(kept):
            continue
        if reused and len(kept) < 4 and sum(1 for x in pool if x["id"] not in used) > 4:
            continue  # prefer fresh exemplars while the pool allows
        if reused and len(kept) >= 4:
            continue
        n_pods += is_pods
        kept.append({k: r.get(k, "") for k in ("id", "title", "domain", "usage", "quote")}
                    | {"score": score.get(r["id"], 0), "pods": r["id"] in pods_ids,
                       "reused": reused})
        used.add(r["id"])
        if len(kept) >= 6:
            break
    plan[tool] = {"n_papers": len(pool), "exemplars": kept}
    if not kept and pool:  # extremely small pools: fall back to top-1
        r = pool[0]
        plan[tool]["exemplars"] = [{k: r.get(k, "") for k in ("id", "title", "domain", "usage", "quote")}
                                   | {"score": score.get(r["id"], 0), "pods": r["id"] in pods_ids,
                                      "reused": True}]

json.dump({"venue": "sigmod26", "chapters": plan}, open(plan_f, "w"), indent=1, ensure_ascii=False)
for t, d in plan.items():
    ex = ", ".join(f"{e['id']}{'*' if e['pods'] else ''}({e['score']})" for e in d["exemplars"])
    print(f"{t:24s} n={d['n_papers']:3d}  exemplars: {ex}")
print(f"[* = PODS'26 band] total unique exemplars: {len(used)}")
