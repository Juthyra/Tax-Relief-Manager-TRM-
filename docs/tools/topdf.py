import re, os, subprocess, glob
# Run only when the owner asks for PDFs. Needs mmdc, pandoc and google-chrome.
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = f"{REPO}/exports"          # PDFs go here (git-ignored)
P = f"{OUT}/pdf"
os.makedirs(P, exist_ok=True)
files = sorted(glob.glob(f"{REPO}/docs/specs/URS_SRS_F*.md"))
css = """@page{size:A4 landscape;margin:12mm 12mm 14mm 12mm}
body{font-family:'DejaVu Sans',Arial,sans-serif;font-size:9.5pt;line-height:1.4;color:#1a1a1a}
h1{font-size:19pt;margin:14px 0 8px}h2{font-size:13.5pt;border-bottom:1px solid #bbb;padding-bottom:2px;margin-top:20px}h3{font-size:11pt;margin-top:14px}
table{border-collapse:collapse;width:100%;margin:6px 0 10px;font-size:7.8pt}
th,td{border:1px solid #b5b5b5;padding:3px 5px;vertical-align:top;text-align:left;overflow-wrap:anywhere}
th{background:#e9eef5;overflow-wrap:normal;word-break:normal}tr{page-break-inside:avoid}
img{max-width:100%;max-height:170mm;display:block;margin:6px auto;page-break-inside:avoid}
code{font-size:8pt;background:#f1f1f1;padding:0 2px}pre{background:#f6f6f6;padding:6px;font-size:7.8pt;white-space:pre-wrap;page-break-inside:avoid}
a{color:#0b4f9c;text-decoration:none}
p:has(+ p img){break-after:avoid;page-break-after:avoid}
h2,h3{break-after:avoid}
"""
open(f"{P}/s.css","w").write(css)
for f in files:
    base = os.path.basename(f)[:-3]; k = base[8:10]
    t = open(f).read()
    n = [0]
    def mm(m):
        n[0] += 1; name = f"{k}_{n[0]:02d}"
        open(f"{P}/{name}.mmd","w").write(m.group(1))
        r = subprocess.run(["mmdc","-q","-b","white","-p",f"{OUT}/pp.json","-w","1400","-i",f"{P}/{name}.mmd","-o",f"{P}/{name}.svg"],capture_output=True,text=True)
        assert r.returncode==0, (name, r.stderr[:300])
        return f"![]({P}/{name}.svg)"
    t = re.sub(r'```mermaid\n(.*?)```', mm, t, flags=re.S)
    def lk(m):
        txt, fn, anc = m.group(1), m.group(2), m.group(3)
        return f"[{txt}](#{anc})" if fn == os.path.basename(f) else txt
    t = re.sub(r'\[([^\]]+)\]\((URS_SRS_F\d_[A-Za-z_]+\.md)#([^)]+)\)', lk, t)
    t = re.sub(r'\[([^\]]+)\]\((?:\.\./registers/)?(?:HISTORY_LOG|URS_SRS_CHANGE_LOG|ACRONYMS)\.md\)', r'\1', t)
    open(f"{P}/{base}.md","w").write(t)
    h = f"{P}/{base}.html"
    r = subprocess.run(["pandoc",f"{P}/{base}.md","-f","gfm","-t","html5","-s","--metadata",f"title={base.replace('_',' ')}","-c",f"{P}/s.css","--embed-resources","-o",h],capture_output=True,text=True)
    assert r.returncode==0, r.stderr[:300]
    s = open(h).read(); s = re.sub(r'<header id="title-block-header">.*?</header>','',s,flags=re.S)
    tokre = re.compile(r'(?<![\w"#/.-])((?:IF|EV|SRS|URS|TC|FD|SQ|SD|OI|DA|FR|BR|NFR)-(?:F\d-)?\d+(?:\.\d+)?|\d{2}/\d{2}/\d{4}|20\d\d)(?![\w-])')
    parts = re.split(r'(<[^>]+>)', s)
    for i, ptxt in enumerate(parts):
        if not ptxt.startswith('<'): parts[i] = tokre.sub(r'<span style="white-space:nowrap">\1</span>', ptxt)
    s = ''.join(parts); open(h,"w").write(s)
    pdf = f"{OUT}/{base}.pdf"
    r = subprocess.run(["google-chrome","--headless","--no-sandbox","--disable-gpu","--no-pdf-header-footer",f"--print-to-pdf={pdf}",h],capture_output=True,text=True)
    print(base, n[0], "diagrams", os.path.getsize(pdf)//1024, "KB")
