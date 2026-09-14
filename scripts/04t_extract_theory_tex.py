#!/usr/bin/env python3
r"""Theory extraction from arXiv TeX sources (preferred over PDF text when available).

Usage: python3 04t_extract_theory_tex.py <papers.jsonl> <src_root> <out_dir>

For each paper with <src_root>/<id>/**/*.tex:
  - discover theorem-like environments (\newtheorem{...}) plus the standard set
  - extract statement bodies from \begin{env}[...]{...} BODY \end{env}
  - extract proofs from \begin{proof} / \begin{proof*} / \proof ... \endproof
  - light de-tex for readable text; bound sentences + signal counts on de-texed text
Writes the SAME theory/<id>.{json,md} format as 04 (adds "from": "tex"), overwriting
any pdf-derived extraction for that id. Bound-sentence/metric patterns duplicated
from 04_extract_theory.py — keep in sync.
"""
import glob, json, os, re, sys

papers_f, src_root, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out_dir, exist_ok=True)
meta = {p["id"]: p for p in map(json.loads, open(papers_f))}

STD_ENVS = {"theorem", "lemma", "corollary", "proposition", "claim", "observation",
            "fact", "definition", "conjecture", "hypothesis", "property", "assumption"}
KIND_ALIAS = {"hypothesis": "conjecture", "property": "claim", "assumption": "definition"}
METRICS = {
    "np_hard": r"\bNP-?hard(?:ness)?\b", "lower_bound": r"\blower[\s-]?bounds?\b",
    "upper_bound": r"\bupper[\s-]?bounds?\b", "big_o": r"(?<![A-Za-z])O\s*\(",
    "omega": r"Ω\s*\(|\\Omega\s*\(", "theta": r"Θ\s*\(|\\Theta\s*\(",
    "approx_ratio": r"\bapproximation(?:[\s-]ratio)?\b|\bconstant[\s-]factor\s+approximation\b",
    "whp": r"\bwith\s+high\s+probability\b", "regret": r"\bregrets?\b",
    "dp": r"\bdifferential(?:ly)?\s+privac(?:y|te)\b", "invariant": r"\binvariants?\b",
    "convergence": r"\bconvergen(?:ce|t|ces)\b", "competitive": r"\bcompetitive\s+(?:ratio|analysis)\b",
    "worst_case": r"\bworst[\s-]?case\b", "sketch": r"\bsketch(?:es|ing)?\b",
    "cost_model": r"\bcost\s+models?\b", "cardinality": r"\bcardinalit(?:y|ies)\b",
    "learned": r"\blearned\s+(?:index|model|structure|quer)",
}
BOUND_SENT = re.compile(r"\b(lower[\s-]?bound|upper[\s-]?bound|asymptot\w+\s+optimal|"
                        r"worst[\s-]?case\s+optimal|NP-?hard|approximation\s+ratio|"
                        r"information[-\s]theoretic(?:al)?)\b", re.I)
MAX_STMT, MAX_PROOF_TXT, MAX_SENTS = 1500, 2500, 12

MATH_MAP = {"log": "log", "ln": "ln", "exp": "exp", "max": "max", "min": "min",
            "epsilon": "ε", "delta": "δ", "theta": "θ", "sigma": "σ", "alpha": "α",
            "beta": "β", "lambda": "λ", "mu": "μ", "gamma": "γ", "Omega": "Ω",
            "Theta": "Θ", "Sigma": "Σ", "sqrt": "√", "cdot": "·", "times": "×",
            "leq": "≤", "geq": "≥", "neq": "≠", "approx": "≈", "sim": "~",
            "infty": "∞", "sum": "Σ", "prod": "Π", "ldots": "…", "cdots": "…"}


def detex(s, drop_display=False):
    if drop_display:
        s = re.sub(r"(?s)\\begin\{(equation|align|table|figure|algorithm)\*?\}.*?\\end\{\1\*?\}",
                   " [display] ", s)
    s = re.sub(r"\\(?:begin|end)\s*\{[^{}]*\}\*?", " ", s)   # env markers (else 'enumerate' leaks)
    s = re.sub(r"\\item\b", "; ", s)
    s = re.sub(r"(?<!\\)%.*", " ", s)
    s = re.sub(r"\\(label|ref|eqref|cite|citep|citet|nocite|url|href|footnote|thanks)\s*(\[[^\]]*\])?(\{[^{}]*\}|\*)?",
               lambda m: " " + ("[ref] " if m.group(1) in ("ref", "eqref") else
                                "[cite] " if m.group(1).startswith("cite") else " "), s)
    for k, v in MATH_MAP.items():
        s = re.sub(r"\\" + k + r"(?![a-zA-Z])", v, s)
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)          # remaining commands
    s = re.sub(r"[{}]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def clip(s, n):
    return s if len(s) <= n else s[:n] + " …"


def find_tex_files(d):
    files = []
    for f in glob.glob(os.path.join(d, "**", "*.tex"), recursive=True):
        files.append(f)
    return sorted(files)


def extract_paper(srcdir):
    texs = [open(f, encoding="utf-8", errors="replace").read() for f in find_tex_files(srcdir)]
    if not texs:
        return None
    allsrc = "\n".join(texs)

    envs = {}  # env name -> kind
    for name in STD_ENVS:
        envs[name] = KIND_ALIAS.get(name, name)
    for m in re.finditer(r"\\newtheorem\*?\s*\{(\w+)\}(?:\[[^\]]*\])?\{(\w+)\}", allsrc):
        env, printed = m.group(1), m.group(2).lower()
        if printed in STD_ENVS or printed.rstrip("s") in STD_ENVS:
            envs[env] = KIND_ALIAS.get(printed.rstrip("s"), printed.rstrip("s"))

    statements, proofs, kinds, seen = [], [], {}, set()
    for env, kind in envs.items():
        for m in re.finditer(r"\\begin\{" + env + r"\}\s*(\[[^\]]*\])?\s*(\{[^{}]*\})?"
                             r"(?s:(.*?)\\end\{" + env + r"\})", allsrc):
            num = (m.group(1) or m.group(2) or "").strip("[]{} ")
            body = clean(detex(m.group(3)))
            if len(body) < 15:
                continue
            k = re.sub(r"\W+", "", body.lower())[:80]
            if k in seen:
                continue
            seen.add(k)
            kinds[kind] = kinds.get(kind, 0) + 1
            statements.append({"kind": kind, "num": num, "text": clip(body, MAX_STMT)})
    for m in re.finditer(r"(?s)\\begin\{proof\*?\}(.*?)\\end\{proof\*?\}", allsrc):
        body = clean(detex(m.group(1)))
        if len(body) < 20:
            continue
        proofs.append({"text": clip(body, MAX_PROOF_TXT)})
    if not proofs:
        m = re.search(r"(?s)\\proof\b(.*?)\\endproof\b", allsrc)
        if m:
            proofs.append({"text": clip(clean(detex(m.group(1))), MAX_PROOF_TXT)})

    flat = detex(allsrc, drop_display=True)
    counts = {k: len(re.findall(p, flat)) for k, p in METRICS.items()}
    sents, bseen = [], set()
    for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", flat):
        if not BOUND_SENT.search(sent) or len(sent) < 60:
            continue
        if len(re.findall(r"\b(19|20)\d{2}\b", sent)) >= 2:
            continue
        s2 = clip(sent.strip(), 300)
        k = re.sub(r"\W+", "", s2.lower())[:60]
        if k in bseen:
            continue
        bseen.add(k)
        sents.append(s2)
        if len(sents) >= MAX_SENTS:
            break
    statements = sorted(statements, key=lambda s: -len(s["text"]))[:30]
    return statements[:30], proofs[:20], kinds, counts, sents, len(allsrc)


def to_md(d):
    L = [f"# {d['id']} — {d['title']}", "",
         f"from={d['from']} flag={d['flag']} score={d['score']} stmts={d['n_stmt']} "
         f"proofs={d['n_proof']} chars={d['n_chars']}",
         f"kinds: {json.dumps(d['kinds'])}", f"counts: {json.dumps(d['counts'])}", "",
         "## Statements"]
    for st in d["statements"]:
        L.append(f"**{st['kind'].title()} {st['num']}.** {st['text']}")
        L.append("")
    L.append("## Proofs")
    for pr in d["proofs"]:
        L.append(f"**Proof.** {pr['text']}")
        L.append("")
    L.append("## Bound sentences")
    for s in d["bound_sents"]:
        L.append(f"- {s}")
    return "\n".join(L) + "\n"


n_tex = 0
for srcdir in sorted(glob.glob(os.path.join(src_root, "*"))):
    pid = os.path.basename(srcdir)
    if pid not in meta or not os.path.isdir(srcdir):
        continue
    r = extract_paper(srcdir)
    if r is None:
        continue
    statements, proofs, kinds, counts, sents, nchars = r
    n_stmt, n_proof = len(statements), len(proofs)
    flag = n_proof >= 1 or n_stmt >= 3 or (counts.get("lower_bound", 0) > 0 and n_stmt >= 1)
    score = n_stmt + 2 * n_proof + (1 if counts.get("lower_bound") else 0) + \
        (1 if counts.get("np_hard") else 0) + (1 if counts.get("approx_ratio") else 0)
    d = {"id": pid, "title": meta[pid]["title"], "from": "tex", "n_stmt": n_stmt,
         "n_proof": n_proof, "kinds": kinds, "counts": counts, "statements": statements,
         "proofs": proofs, "bound_sents": sents, "flag": flag, "score": score,
         "n_chars": nchars}
    json.dump(d, open(os.path.join(out_dir, pid + ".json"), "w"), ensure_ascii=False)
    open(os.path.join(out_dir, pid + ".md"), "w").write(to_md(d))
    n_tex += 1
print(f"tex-extracted {n_tex} papers", flush=True)
