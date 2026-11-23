"""Fail if a document breaks the document standard (AGENTS.md section 6, RULE-53 to RULE-59).
Checks the file name, the title line and the header table of every Markdown file under docs/.
Usage: python3 docs/tools/check_standard.py   (works from any folder)"""
import glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# file name pattern per type -> how to make the Document ID from the match
TYPES = [
    (re.compile(r"^PRD_(TRM)_[A-Z][A-Za-z0-9]*(?:_[A-Z0-9][A-Za-z0-9]*)*\.md$"), "PRD-{}"),
    (re.compile(r"^URS_SRS_(F[0-9])_[A-Z][A-Za-z0-9]*(?:_[A-Z0-9][A-Za-z0-9]*)*\.md$"), "URS-SRS-{}"),
    (re.compile(r"^ADR_(\d{3})_[A-Z][A-Za-z0-9]*(?:_[A-Z0-9][A-Za-z0-9]*)*\.md$"), "ADR-{}"),
    (re.compile(r"^RES_(\d{3})_[A-Z][A-Za-z0-9]*(?:_[A-Z0-9][A-Za-z0-9]*)*\.md$"), "RES-{}"),
    (re.compile(r"^REG_(\d{2})_[A-Z][A-Za-z0-9]*(?:_[A-Z0-9][A-Za-z0-9]*)*\.md$"), "REG-{}"),
]
ROWS = ["Document ID", "Document type", "Product", "Version", "Status", "Date", "Owner",
        "PRD reference", "Source", "Change tracking"]
STATUS = ("Draft", "Proposed", "Approved", "Active", "Superseded")
TEMPLATES = {"ADR_000_Template.md": "ADR-nnn"}  # a template keeps placeholders


def check(path):
    errs, name = [], os.path.basename(path)
    for rx, fmt in TYPES:
        m = rx.match(name)
        if m:
            doc_id = TEMPLATES.get(name, fmt.format(m.group(1)))
            break
    else:
        return [f"{path}: file name does not follow <type>_<ID>_<Short_Name>.md"]
    lines = open(path, encoding="utf-8").read().split("\n")
    if not lines[0].startswith(f"# {doc_id}: "):
        errs.append(f"{path}: first line must start with '# {doc_id}: '")
    rows = []
    for ln in lines[1:40]:
        if ln.startswith("| ") and not ln.startswith("| ---") and not ln.startswith("| Item |"):
            rows.append([c.strip() for c in ln.strip().strip("|").split("|", 1)])
        elif rows:
            break
    keys = [r[0] for r in rows]
    if keys[:len(ROWS)] != ROWS:
        errs.append(f"{path}: header rows must be {ROWS}, found {keys[:len(ROWS)]}")
        return errs
    vals = dict((r[0], r[1].strip() if len(r) > 1 else "") for r in rows)
    if vals["Document ID"] != doc_id:
        errs.append(f"{path}: Document ID is '{vals['Document ID']}', expected '{doc_id}'")
    if name not in TEMPLATES and not vals["Status"].startswith(STATUS):
        errs.append(f"{path}: Status must start with one of {STATUS}")
    if name not in TEMPLATES and not re.match(r"\d{4}-\d{2}-\d{2}", vals["Date"]):
        errs.append(f"{path}: Date must start with YYYY-MM-DD")
    return errs


files = [f for f in glob.glob(os.path.join(REPO, "docs", "**", "*.md"), recursive=True)
         if "/tools/source/" not in f and os.path.basename(f) != "README.md"]
errors = [e for f in sorted(files) for e in check(f)]
ids = {}
for f in files:
    for rx, fmt in TYPES:
        m = rx.match(os.path.basename(f))
        if m:
            ids.setdefault(fmt.format(m.group(1)), []).append(f)
errors += [f"Document ID {k} is used by more than one file: {v}" for k, v in ids.items() if len(v) > 1]
for e in errors:
    print(" ", e.replace(REPO + os.sep, ""))
print("STANDARD ERRORS:", len(errors), "in", len(files), "documents")
sys.exit(1 if errors else 0)
