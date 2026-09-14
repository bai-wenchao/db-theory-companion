#!/usr/bin/env python3
"""Slim per-chapter digests so chapter agents read ONE small file (0 LLM tokens).

Usage: python3 10_make_digests.py <plan.json> <theory_dir> <digest_dir>
For each chapter: header + per-exemplar note lines (domain/usage/quote) + trimmed
theory extraction (8 statements ≤500 chars, 2 proofs ≤700, 6 bound sentences).
Target ≤ 18KB/chapter vs 100-300KB of raw theory files.
"""
import glob, json, os, sys

plan_f, theory_dir, digest_dir = sys.argv[1], sys.argv[2], sys.argv[3]
plan = json.load(open(plan_f))
os.makedirs(digest_dir, exist_ok=True)

for tool, d in plan["chapters"].items():
    L = [f"# Chapter digest: {tool}", f"n_papers_with_tool: {d['n_papers']}",
         "PODS exemplars are from the PODS'26 issue inside PACMMOD Vol 4 — mark them ^PODS.", ""]
    for e in d["exemplars"]:
        pid = e["id"]
        L += [f"## {pid}{' [PODS]' if e['pods'] else ''} — {e['title']}  (score {e['score']})",
              f"domain: {e.get('domain','')}", f"usage: {e.get('usage','')}",
              f"note-quote: {e.get('quote','')}"]
        f = os.path.join(theory_dir, pid + ".json")
        if os.path.exists(f):
            t = json.load(open(f))
            for s in t.get("statements", [])[:8]:
                L.append(f"  {s['kind'].title()} {s['num']}: {s['text'][:500]}")
            for p in t.get("proofs", [])[:2]:
                L.append(f"  Proof: {p['text'][:700]}")
            for b in t.get("bound_sents", [])[:6]:
                L.append(f"  bound: {b[:280]}")
        L.append("")
    out = os.path.join(digest_dir, tool + ".md")
    open(out, "w").write("\n".join(L))
    print(f"{out}  {os.path.getsize(out)//1024}KB  ({len(d['exemplars'])} exemplars)")
