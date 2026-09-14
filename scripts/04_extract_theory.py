#!/usr/bin/env python3
"""Extract theory contexts from plain-text papers (pure regex, no LLM).

Usage: python3 04_extract_theory.py <papers.jsonl> <txt_dir> <out_dir>
Writes <out_dir>/<id>.json and <out_dir>/<id>.md per paper.

Extracts:
- formal statements: Theorem/Lemma/Corollary/Proposition/Claim/Observation/Fact/
  Definition/Conjecture N (paragraph-start guard against inline cross-refs)
- proofs: "Proof [of <kind> N] [Sketch]." until QED-marker / next marker / window
- bound sentences (lower/upper bound, NP-hard, approximation ratio, optimality)
- signal counts (big-O/Omega/Theta, whp, regret, DP, invariants, convergence, ...)
"""
import glob, json, os, re, sys

papers_f, txt_dir, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out_dir, exist_ok=True)


def tex_locked(pid):
    """Never overwrite a TeX-derived extraction with a pdf-derived one."""
    f = os.path.join(out_dir, pid + ".json")
    if not os.path.exists(f):
        return False
    try:
        return json.load(open(f)).get("from") == "tex"
    except Exception:
        return False

meta = {}
for line in open(papers_f):
    try:
        p = json.loads(line)
        meta[p["id"]] = p
    except Exception:
        pass

KIND = r"(Theorems?|Lemmas?|Corollaries|Corollary|Propositions?|Claims?|Observations?|Facts?|Definitions?|Conjectures?)"
NUM = r"(\d+(?:\.\d+)*)"
STMT = re.compile(rf"(?<![A-Za-z]){KIND}\s+{NUM}\s*[.:)]")
PROOF = re.compile(r"(?<![A-Za-z])Proof(?:\s+[Ss]ketch)?(?:\s+of\s+(?:the\s+)?"
                   r"(?:Theorem|Lemma|Corollary|Proposition|Claim|Observation|Fact|Conjecture)"
                   r"\s*\d+(?:\.\d+)*)*\s*[.:)]")
QED = re.compile(r"∎|□|⊠|■|\bblack\s?square\b|\bQ\.?\s?E\.?\s?D\b|\bQED\b")

PLURAL = {"theorems": "theorem", "lemmas": "lemma", "corollaries": "corollary",
          "propositions": "proposition", "claims": "claim", "observations": "observation",
          "facts": "fact", "definitions": "definition", "conjectures": "conjecture"}

METRICS = {
    "np_hard": r"\bNP-?hard(?:ness)?\b",
    "lower_bound": r"\blower[\s-]?bounds?\b",
    "upper_bound": r"\bupper[\s-]?bounds?\b",
    "big_o": r"(?<![A-Za-z])O\s*\(",
    "omega": r"Ω\s*\(",
    "theta": r"Θ\s*\(",
    "approx_ratio": r"\bapproximation(?:[\s-]ratio)?\b|\bconstant[\s-]factor\s+approximation\b",
    "whp": r"\bwith\s+high\s+probability\b",
    "regret": r"\bregrets?\b",
    "dp": r"\bdifferential(?:ly)?\s+privac(?:y|te)\b",
    "invariant": r"\binvariants?\b",
    "convergence": r"\bconvergen(?:ce|t|ces)\b",
    "competitive": r"\bcompetitive\s+(?:ratio|analysis)\b",
    "worst_case": r"\bworst[\s-]?case\b",
    "sketch": r"\bsketch(?:es|ing)?\b",
    "cost_model": r"\bcost\s+models?\b",
    "cardinality": r"\bcardinalit(?:y|ies)\b",
    "learned": r"\blearned\s+(?:index|model|structure|quer)",
}

BOUND_SENT = re.compile(r"\b(lower[\s-]?bound|upper[\s-]?bound|asymptot\w+\s+optimal|"
                        r"worst[\s-]?case\s+optimal|NP-?hard|approximation\s+ratio|"
                        r"information[-\s]theoretic(?:al)?)\b", re.I)

MAX_STMT, MAX_PROOF_TXT, MAX_SENTS = 1500, 2500, 12


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def clip(s, n):
    return s if len(s) <= n else s[:n] + " …"


def prev_ok(text, s):
    """Statement/proof must start a sentence or paragraph (kills inline refs)."""
    if s == 0:
        return True
    if text[s - 1] in "\n.;:>-•*":
        return True
    if s >= 2 and text[s - 2:s] in (". ", "? ", "! "):
        return True
    return False


def extract(text):
    # cut the bibliography before bound-sentence extraction (reference titles like
    # "Worst-case optimal join algorithms." pollute; notation tables too)
    refs = None
    for m in re.finditer(r"(?m)^\s*(References|REFERENCES|Bibliography)\s*$", text):
        refs = m.start()  # keep the LAST standalone header
    body = text[:refs] if refs else text
    marks = []
    for m in STMT.finditer(text):
        if prev_ok(text, m.start()):
            marks.append((m.start(), m.end(), "stmt", m))
    for m in PROOF.finditer(text):
        if prev_ok(text, m.start()):
            marks.append((m.start(), m.end(), "proof", m))
    marks.sort(key=lambda t: t[0])
    stops = [s for s, _, _, _ in marks]

    def stop_after(pos):
        for s in stops:
            if s > pos:
                return s
        return -1

    statements, proofs = [], []
    kinds, seen = {}, set()
    for s, e, typ, m in marks:
        stop = stop_after(e)
        end = stop if stop > 0 else min(len(text), e + 2500)
        if typ == "stmt":
            k = m.group(1).lower()
            k = PLURAL.get(k, k)
            key = (k, m.group(2))
            if key in seen or len(statements) >= 30:
                continue
            seen.add(key)
            kinds[k] = kinds.get(k, 0) + 1
            statements.append({"kind": k, "num": m.group(2),
                               "text": clip(clean(text[e:end]), MAX_STMT)})
        else:
            if len(proofs) >= 20:
                continue
            seg = text[e:end]
            qm = QED.search(seg)
            body = seg[:qm.end()] if qm else seg[:3000]
            proofs.append({"text": clip(clean(body), MAX_PROOF_TXT)})

    counts = {k: len(re.findall(p, text)) for k, p in METRICS.items()}
    flat = clean(body)
    sents, bseen = [], set()
    for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", flat):
        if not BOUND_SENT.search(sent):
            continue
        if len(sent) < 60:  # titles / fragments (often reference titles)
            continue
        if len(re.findall(r"\b(19|20)\d{2}\b", sent)) >= 2 or sent.lstrip().startswith("["):
            continue  # citation-like
        s2 = clip(sent.strip(), 300)
        k = re.sub(r"\W+", "", s2.lower())[:60]
        if k in bseen:
            continue
        bseen.add(k)
        sents.append(s2)
        if len(sents) >= MAX_SENTS:
            break
    return statements, proofs, kinds, counts, sents


def to_md(d):
    L = [f"# {d['id']} — {d['title']}", "",
         f"flag={d['flag']} score={d['score']} stmts={d['n_stmt']} proofs={d['n_proof']} "
         f"chars={d['n_chars']}",
         f"kinds: {json.dumps(d['kinds'])}", f"counts: {json.dumps(d['counts'])}", ""]
    L.append("## Statements")
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
    L.append("")
    return "\n".join(L)


n_flag = 0
for txt_f in sorted(glob.glob(os.path.join(txt_dir, "*.txt"))):
    pid = os.path.splitext(os.path.basename(txt_f))[0]
    if pid not in meta or tex_locked(pid):
        continue
    text = open(txt_f, encoding="utf-8", errors="replace").read()
    statements, proofs, kinds, counts, sents = extract(text)
    n_stmt, n_proof = len(statements), len(proofs)
    flag = n_proof >= 1 or n_stmt >= 3 or (counts.get("lower_bound", 0) > 0 and n_stmt >= 1)
    score = n_stmt + 2 * n_proof + (1 if counts.get("lower_bound") else 0) + \
        (1 if counts.get("np_hard") else 0) + (1 if counts.get("approx_ratio") else 0)
    d = {"id": pid, "title": meta[pid]["title"], "n_stmt": n_stmt, "n_proof": n_proof,
         "kinds": kinds, "counts": counts, "statements": statements, "proofs": proofs,
         "bound_sents": sents, "flag": flag, "score": score, "n_chars": len(text)}
    json.dump(d, open(os.path.join(out_dir, pid + ".json"), "w"), ensure_ascii=False)
    open(os.path.join(out_dir, pid + ".md"), "w").write(to_md(d))
    n_flag += flag
print(f"extracted {len(glob.glob(os.path.join(out_dir, '*.json')))} papers, {n_flag} flagged")
