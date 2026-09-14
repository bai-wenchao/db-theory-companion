#!/usr/bin/env python3
"""Build the survey index from papers.jsonl + theory extracts.

Usage: python3 05_build_index.py <data_dir> <out_prefix>
  e.g. python3 05_build_index.py data/sigmod26 index/sigmod26_index
Outputs: <prefix>.csv, <prefix>.md, <prefix>_flagged_ids.txt (score-desc order)
"""
import csv, glob, json, os, sys

data_dir, prefix = sys.argv[1], sys.argv[2]
os.makedirs(os.path.dirname(prefix), exist_ok=True)

KIND_KEYS = ["theorem", "lemma", "corollary", "proposition", "claim",
             "definition", "observation", "fact", "conjecture"]
MET_KEYS = ["np_hard", "lower_bound", "upper_bound", "big_o", "omega", "theta",
            "approx_ratio", "whp", "regret", "dp", "invariant", "convergence",
            "competitive", "worst_case", "sketch", "cost_model", "cardinality", "learned"]

papers = [json.loads(l) for l in open(os.path.join(data_dir, "papers.jsonl"))]
manifest = {}
mp = os.path.join(data_dir, "manifest.jsonl")
if os.path.exists(mp):
    for line in open(mp):
        try:
            r = json.loads(line)
            manifest[r["id"]] = r
        except Exception:
            pass

rows = []
for p in papers:
    pid = p["id"]
    tj = os.path.join(data_dir, "theory", pid + ".json")
    t = json.load(open(tj)) if os.path.exists(tj) else None
    row = {"id": pid, "title": p["title"]}
    if t:
        row.update({"flag": t["flag"], "score": t["score"], "n_stmt": t["n_stmt"],
                    "n_proof": t["n_proof"]})
        for k in KIND_KEYS:
            row[k] = t["kinds"].get(k, 0)
        for k in MET_KEYS:
            row[k] = t["counts"].get(k, 0)
    else:
        row.update({"flag": False, "score": 0, "n_stmt": 0, "n_proof": 0})
        for k in KIND_KEYS + MET_KEYS:
            row[k] = 0
    row["pdf"] = "ok" if os.path.exists(os.path.join(data_dir, "pdfs", pid + ".pdf")) else "no"
    m = manifest.get(pid, {})
    row["source"] = (m.get("source") or "").split(":")[0]
    rows.append(row)

rows.sort(key=lambda r: (-r["score"], r["id"]))
fields = ["id", "title", "flag", "score", "n_stmt", "n_proof"] + KIND_KEYS + MET_KEYS + ["pdf", "source"]
with open(prefix + ".csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

flagged = [r for r in rows if r["flag"]]
with open(prefix + "_flagged_ids.txt", "w") as f:
    for r in flagged:
        f.write(f"{r['id']}\t{r['score']}\t{r['title']}\n")

n = len(rows)
have_pdf = sum(1 for r in rows if r["pdf"] == "ok")
have_th = sum(1 for r in rows if r["n_stmt"] > 0 or r["n_proof"] > 0)
kind_tot = {k: sum(r[k] for r in rows) for k in KIND_KEYS}
met_papers = {k: sum(1 for r in rows if r[k] > 0) for k in MET_KEYS}
tot_stmt = sum(r["n_stmt"] for r in rows)
tot_proof = sum(r["n_proof"] for r in rows)

L = [f"# {os.path.basename(prefix)} — theory signal index", "",
     f"papers={n} pdf_ok={have_pdf} with_any_theory={have_th} flagged={len(flagged)}",
     f"total_statements={tot_stmt} total_proofs={tot_proof}", "",
     "## Statements by kind", " | ".join(f"{k}:{v}" for k, v in kind_tot.items() if v), "",
     "## Signal -> #papers mentioning", " | ".join(f"{k}:{v}" for k, v in
     sorted(met_papers.items(), key=lambda kv: -kv[1]) if v), "",
     "## Top 30 theory papers",
     "| id | th lm co pr cl df | pf | lb ub nph aR | score | title |",
     "|---|---|---|---|---|---|"]
for r in rows[:30]:
    L.append(f"| {r['id']} | {r['theorem']}/{r['lemma']}/{r['corollary']}/{r['proposition']}/"
             f"{r['claim']}/{r['definition']} | {r['n_proof']} | {r['lower_bound']}/"
             f"{r['upper_bound']}/{r['np_hard']}/{r['approx_ratio']} | {r['score']} | "
             f"{r['title'][:70]} |")
L += ["", "## All papers (score desc)", "| id | fl | stmt | pf | score | pdf | title |",
      "|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['id']} | {'Y' if r['flag'] else '.'} | {r['n_stmt']} | {r['n_proof']} | "
             f"{r['score']} | {r['pdf']} | {r['title'][:70]} |")
open(prefix + ".md", "w").write("\n".join(L) + "\n")
print(f"index: {n} papers, {have_pdf} pdfs, {len(flagged)} flagged -> {prefix}.{{csv,md}}")
