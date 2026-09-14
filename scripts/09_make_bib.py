#!/usr/bin/env python3
"""Emit refs.bib for the corpus (0 LLM tokens).

Usage: python3 scripts/09_make_bib.py <papers.jsonl> <refs.bib>
Keys are sigmod26-NNN so chapter agents can \cite{<id>} without lookup. Ids 001-257 =
PACMMOD Vol 4 (2026); 258-385 = Vol 3 i4-6 (2025, SIGMOD'26 rounds 1-2).
"""
import json, re, sys

papers_f, out_f = sys.argv[1], sys.argv[2]

# pdflatex chokes on raw math unicode in titles; transliterate to LaTeX math
UNI = {"ℓ": r"$\ell$", "ε": r"$\varepsilon$", "δ": r"$\delta$", "α": r"$\alpha$",
       "β": r"$\beta$", "γ": r"$\gamma$", "λ": r"$\lambda$", "μ": r"$\mu$",
       "σ": r"$\sigma$", "ρ": r"$\rho$", "τ": r"$\tau$", "θ": r"$\theta$",
       "κ": r"$\kappa$", "π": r"$\pi$", "ω": r"$\omega$", "φ": r"$\varphi$",
       "Ω": r"$\Omega$", "Θ": r"$\Theta$", "×": r"$\times$", "·": r"$\cdot$",
       "≥": r"$\geq$", "≤": r"$\leq$", "∞": r"$\infty$", "→": r"$\rightarrow$",
       "∼": r"$\sim$", "≈": r"$\approx$", "∥": r"$\|$", "√": r"$\sqrt{}$"}


def uni2tex(s):
    for k, v in UNI.items():
        s = s.replace(k, v)
    return s


def texesc(s):
    return re.sub(r"([&$%#_{}])", r"\\\1", s or "")


with open(out_f, "w", encoding="utf-8") as out:
    n = 0
    for line in open(papers_f, encoding="utf-8"):
        try:
            p = json.loads(line)
        except Exception:
            continue
        pid = p["id"]
        num = int(re.sub(r"\D", "", pid.split("-")[-1]) or 0)
        year = 2026 if num <= 257 else 2025
        vol = 4 if num <= 257 else 3
        authors = " and ".join(p.get("authors") or ["Anonymous"])
        out.write(f"@article{{{pid},\n"
                  f"  title = {{{uni2tex(texesc(p.get('title')))}}},\n"
                  f"  author = {{{uni2tex(texesc(authors))}}},\n"
                  f"  journal = {{Proceedings of the ACM on Management of Data}},\n"
                  f"  volume = {{{vol}}},\n  year = {{{year}}},\n")
        if p.get("doi"):
            out.write(f"  doi = {{{p['doi']}}},\n")
        out.write(f"  note = {{SIGMOD {'2026' if year == 2026 else '2026 (rounds 1-2)'}}},\n}}\n\n")
        n += 1
print(f"wrote {n} entries -> {out_f}")
