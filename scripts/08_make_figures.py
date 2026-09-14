#!/usr/bin/env python3
"""Make lecture-note figures from tags.md (matplotlib, 0 LLM tokens).

Usage: ~/anaconda3/bin/python3 scripts/08_make_figures.py <tags.md> <figures_dir>

Parses generic `- name: count` bullets under `## SECTION` headers and emits:
  f_props.pdf / f_tools.pdf / f_domains.pdf (top-12/12/10 horizontal bars)
  f_pairs.pdf  (top-10 (prop,tool) pairs) — section header containing 'PAIR'
  f_roles.pdf  (role distribution)         — section header containing 'ROLE'
Run with anaconda python (system python3 lacks matplotlib).
"""
import os, re, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

tags_f, out_dir = sys.argv[1], sys.argv[2]
os.makedirs(out_dir, exist_ok=True)

ACCENT = "#1f4e8c"; BAR = "#8fb3dc"; TXT = "#222222"
plt.rcParams.update({"font.size": 9, "text.color": TXT, "axes.edgecolor": "#999999",
                     "axes.labelcolor": TXT, "xtick.color": "#555555", "ytick.color": TXT,
                     "axes.spines.top": False, "axes.spines.right": False})

sections = {}  # upper(header) -> [(name, count)]
cur = None
for line in open(tags_f, encoding="utf-8"):
    if line.startswith("## "):
        cur = line[3:].strip().upper()
        sections.setdefault(cur, [])
    elif cur and (m := re.match(r"-\s+(.+?):\s*(\d+)", line)):
        sections[cur].append((m.group(1).strip(), int(m.group(2))))


def find(kw):
    for k, v in sections.items():
        if kw in k and v:
            return v
    return []


def hbar(items, fname, title, top=12, split=None):
    items = sorted(items, key=lambda t: -t[1])[:top][::-1]
    labels = [n.replace(split, "\n× ") if split else n for n, _ in items]
    vals = [v for _, v in items]
    fig, ax = plt.subplots(figsize=(4.6, 0.34 * len(items) + 0.7))
    ax.barh(labels, vals, color=BAR, edgecolor="none")
    for i, v in enumerate(vals):
        ax.text(v + max(vals) * 0.015, i, str(v), va="center", fontsize=8, color="#555555")
    ax.set_xlim(0, max(vals) * 1.12)
    ax.set_title(title, fontsize=9.5, loc="left", color=ACCENT, pad=5)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, fname))
    plt.close(fig)
    print(fname, "->", len(items), "bars")


n = sum(v for _, v in find("PROPERT"))
hbar(find("PROPERT"), "f_props.pdf", f"Properties (top 12 of {n} tags)")
hbar(find("TOOLS"), "f_tools.pdf", "Theoretical tools (top 12)")
hbar(find("DOMAIN"), "f_domains.pdf", "Paper domains (top 10)")
hbar(find("PAIR"), "f_pairs.pdf", "Top property × tool pairings", split="×")
roles = {}
for name, c in find("ROLE"):  # role lines are "role — clause: count"; aggregate on role
    roles[name.split(" — ")[0].strip()] = roles.get(name.split(" — ")[0].strip(), 0) + c
hbar(list(roles.items()), "f_roles.pdf", "Where theory sits (role)", top=6)
