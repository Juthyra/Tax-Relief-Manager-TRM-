"""Fail if a capital-letter short form is used in the documents but not listed in REG_03_Acronyms.md.
Usage: python3 docs/tools/check_acronyms.py   (works from any folder)"""
import re, sys, glob, os
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
reg = open(os.path.join(REPO, 'docs', 'registers', 'REG_03_Acronyms.md')).read()
known = set()
for line in reg.splitlines():
    if line.startswith('|') and not line.startswith('| ---'):
        first = line.split('|')[1]
        known.update(re.findall(r'[A-Z][A-Za-z0-9]*', first))
# tokens inside the Stands-for/Meaning text of section 6 and ID prefixes such as SRS-F1-04
known.update(['SRS', 'URS', 'FD', 'SQ', 'TC', 'SD', 'OI', 'IF', 'EV', 'DA', 'CHG', 'FR', 'BR', 'NFR', 'GRP'])
docs = [f for f in glob.glob(os.path.join(REPO, 'docs', '**', '*.md'), recursive=True) + glob.glob(os.path.join(REPO, '*.md'))
        if os.path.basename(f) != 'REG_03_Acronyms.md' and '/tools/source/' not in f]
missing = {}
for f in docs:
    t = open(f).read()
    t = re.sub(r'```.*?```', '', t, flags=re.S)
    t = re.sub(r'[\w-]+\.(?:md|py|pdf|json)\b|https?://\S+|\]\([^)]*\)|<a id="[^"]*">', '', t)
    for m in re.finditer(r'\b[A-Z][A-Z0-9]{1,8}\b', t):
        tok = m.group(0)
        if re.fullmatch(r'[A-Z]\d+', tok) or re.fullmatch(r'RM\d+', tok) or tok in known:
            continue
        missing.setdefault(tok, set()).add(f)
if missing:
    print('Acronyms used but not in REG_03_Acronyms.md:')
    for k, v in sorted(missing.items()):
        print(' ', k, sorted(v))
    sys.exit(1)
rows = [l for l in reg.splitlines() if l.startswith('|') and not l.startswith('| ---')]
print('OK: all short forms are listed.', len(rows), 'register rows,', len(docs), 'documents scanned')
