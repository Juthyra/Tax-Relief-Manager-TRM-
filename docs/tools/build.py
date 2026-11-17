import re, sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
import importlib, shared
importlib.reload(shared)
from shared import *
SRC = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(SRC))
OUT = os.path.join(REPO, "docs", "specs")
fname = {k: v[0] for k, v in DOCS.items()}
TOK = re.compile(r'\b(SRS|URS|FD|SQ|TC|SD|OI)-F([0-5])-(\d\d)\b')

def build(key):
    s = open(f"{SRC}/source/{key.lower()}.md").read()
    s = s.replace("@@CONVENTIONS@@", CONVENTIONS).replace("@@FD00@@", fd00(key)) \
         .replace("@@IFTABLE@@", IFTABLE).replace("@@OWNERSHIP@@", OWNERSHIP) \
         .replace("@@DATA_ADDITIONS@@", DATA_ADDITIONS).replace("@@SEED@@", SEED)
    assert "@@" not in s, "unreplaced placeholder"
    lines, out, fence = s.split("\n"), [], False
    for ln in lines:
        if ln.startswith("```"):
            fence = not fence; out.append(ln); continue
        if fence: out.append(ln); continue
        m = re.match(r'^\| ((?:URS|TC|SD|OI)-F\d-\d\d) \|', ln)
        if m:
            t = m.group(1); ln = ln.replace(f"| {t} |", f'| <a id="{t.lower()}"></a>{t} |', 1)
        def link(mm):
            t = mm.group(0); st = mm.start(); pre = mm.string[max(0, st-8):st]
            if pre.endswith('id="') or pre.endswith('</a>') or pre.endswith('['): return t
            if mm.string[mm.end():mm.end()+2] == '](': return t
            k = "F" + mm.group(2)
            return f"[{t}]({fname[k]}#{t.lower()})"
        ln = TOK.sub(link, ln)
        out.append(ln)
    text = "\n".join(out)
    open(f"{OUT}/{fname[key]}", "w").write(text)
    return text

texts = {k: build(k) for k in DOCS}
# ---------- checks ----------
errs = []
defs = {k: set() for k in DOCS}
for k, t in texts.items():
    for m in re.finditer(r'<a id="((?:srs|urs|fd|sq|tc|sd|oi)-f\d-\d\d)"></a>', t):
        defs[k].add(m.group(1).upper())
for k, t in texts.items():
    # table column consistency
    blk = []
    for i, ln in enumerate(t.split("\n") + [""], 1):
        if ln.startswith("|"):
            blk.append((i, ln))
        else:
            if blk:
                n = len(re.findall(r'(?<!\\)\|', blk[0][1])) 
                for i2, l2 in blk:
                    if len(re.findall(r'(?<!\\)\|', l2)) != n:
                        errs.append(f"{k} line {i2}: table column count differs")
            blk = []
    # references resolve
    plain = re.sub(r'```.*?```', '', t, flags=re.S)
    for m in TOK.finditer(re.sub(r'\]\([^)]*\)', ']', plain)):
        tok = m.group(0); kk = "F" + m.group(2)
        if tok not in defs[kk]: errs.append(f"{k}: reference {tok} has no definition in {kk}")
# per-doc coverage
for k, t in texts.items():
    urs = sorted(d for d in defs[k] if d.startswith("URS"))
    srs = sorted(d for d in defs[k] if d.startswith("SRS"))
    tc = sorted(d for d in defs[k] if d.startswith("TC"))
    sec = re.split(r"\n## B6\. ", t)[1].split("\n## B7. ")[0]
    for u in urs:
        if u not in sec: errs.append(f"{k}: {u} missing from traceability matrix")
    b1 = re.split(r"\n## B1\. ", t)[1].split("\n## B2. ")[0]
    for s_ in srs:
        row = [l for l in b1.split("\n") if f'<a id="{s_.lower()}"></a>' in l]
        if not row: errs.append(f"{k}: {s_} row missing"); continue
        cells = [c.strip() for c in row[0].split("|")]
        # cells: '', id, spec, basis, urs, flow, test, ''
        if len(cells) < 8: errs.append(f"{k}: {s_} bad row"); continue
        if not re.search(r'URS-F\d-\d\d', cells[4]): errs.append(f"{k}: {s_} has no URS")
        if not (re.search(r'FD-F\d-\d\d', cells[5]) or 'not drawn' in cells[5]): errs.append(f"{k}: {s_} has no flow ref")
        if not (re.search(r'TC-F\d-\d\d', cells[6]) or 'none in R1' in cells[6]): errs.append(f"{k}: {s_} has no test")
    # every TC referenced from an SRS or matrix
    for c in tc:
        if c not in t.split("\n## B7. ")[0]: errs.append(f"{k}: {c} not referenced before B7")
# shared blocks identical
for blk, name in [(IFTABLE, 'IF table'), (OWNERSHIP, 'ownership'), (DATA_ADDITIONS, 'DA'), (SEED, 'seed')]:
    for k, t in texts.items():
        norm = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', re.sub(r'<a id="[^"]*"></a>', '', t))
        if blk.replace('<a id="da-list"></a>\n','').replace('<a id="seed-catalogue"></a>\n','') not in norm: errs.append(f"{k}: shared block {name} differs")
# IF table SRS references exist
for m in re.finditer(r'SRS-F(\d)-(\d\d)', IFTABLE):
    tok = m.group(0)
    if tok not in defs["F" + m.group(1)]: errs.append(f"IF table references missing {tok}")
counts = {}
for k, t in texts.items():
    counts[k] = {p: len([d for d in defs[k] if d.startswith(p)]) for p in ("URS", "SRS", "FD", "SQ", "TC", "SD", "OI")}
    counts[k]["mermaid"] = t.count("```mermaid")
    counts[k]["lines"] = t.count("\n") + 1
print(json.dumps(counts, indent=1))
print("ERRORS:", len(errs)); [print(" ", e) for e in errs]
