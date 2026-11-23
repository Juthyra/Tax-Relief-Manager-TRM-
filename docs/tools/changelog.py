import re, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "docs", "specs")
REG = os.path.join(REPO, "docs", "registers")
files = {"F0": "URS_SRS_F0_User_Profile.md", "F1": "URS_SRS_F1_Tax_Calculator.md", "F2": "URS_SRS_F2_Relief_Categories.md",
         "F3": "URS_SRS_F3_Spending_Records.md", "F4": "URS_SRS_F4_Dashboard.md", "F5": "URS_SRS_F5_Account_Security.md"}
names = {"F0": "User profile and tax-year history", "F1": "Tax calculator for any year", "F2": "Relief categories and ranges", "F3": "Spending records", "F4": "Dashboard", "F5": "Account and security"}
def clean(x):
    x = re.sub(r'<a id="[^"]*"></a>', '', x)
    x = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', x)
    return x.strip()
def short(x, n=120):
    x = clean(x).replace("**", "")
    return x if len(x) <= n else x[:n].rsplit(" ", 1)[0] + " ..."
changed = {"OI-F2-01":"CHG-011","OI-F2-02":"CHG-012","SRS-F2-08":"CHG-011","SRS-F2-14":"CHG-012","TC-F2-10":"CHG-012",
 "TC-F3-08":"CHG-013","SRS-F3-07":"CHG-013","TC-F1-05":"CHG-014"}
# changed in version 0.3 (prompt P-13)
changed03 = {"SRS-F1-01":"CHG-020","SRS-F1-04":"CHG-020","SRS-F1-15":"CHG-020","SRS-F1-19":"CHG-020","SRS-F1-21":"CHG-020",
 "SRS-F2-04":"CHG-022","SRS-F2-05":"CHG-022","TC-F2-11":"CHG-022","SRS-F3-02":"CHG-023","SRS-F3-14":"CHG-023","SRS-F3-15":"CHG-023",
 "SRS-F4-01":"CHG-024","SRS-F4-10":"CHG-024"}
# added in version 0.3 to a document that already existed
added03 = {"SRS-F1-23":"CHG-021","TC-F1-21":"CHG-021","SD-F1-10":"CHG-021","TC-F2-24":"CHG-022"}
# changed in this round (prompt P-15): F0 version 0.2
changed_p15 = {"SRS-F0-01":"CHG-031","SRS-F0-02":"CHG-031","SRS-F0-16":"CHG-031","OI-F0-03":"CHG-031"}
# added in this round to a document that already existed: id -> (version, CHG)
added_p15 = {"URS-F0-14":("0.2","CHG-031"),"SRS-F0-19":("0.2","CHG-031"),"TC-F0-25":("0.2","CHG-031"),
 "URS-F1-16":("0.4","CHG-032"),"SRS-F1-24":("0.4","CHG-032"),"TC-F1-22":("0.4","CHG-032"),
 "URS-F3-15":("0.4","CHG-033"),"SRS-F3-18":("0.4","CHG-033"),"TC-F3-23":("0.4","CHG-033")}
answered = {"OI-F2-01":"Answered in 0.2 (CHG-011); YA 2026 confirmed in 0.7 (CHG-054)","OI-F2-02":"Answered in 0.2 (CHG-012)",
 "OI-F2-04":"Answered by the owner 23/11/2026 in 0.8: sub-limits, DA-25 approved (CHG-055)", "OI-F0-01":"Answered in 0.2 (CHG-030)","OI-F0-04":"Answered in 0.2 (CHG-030)"}
# changed in prompt P-16 (14/11/2026): id -> CHG ; version by feature
VER16 = {"F0":"0.3","F1":"0.5","F2":"0.5","F3":"0.5","F4":"0.5","F5":"0.2"}
changed_p16 = {}
def _c(chg, ids):
    for i in ids.split(): changed_p16[i] = chg
_c("CHG-036", "SRS-F0-01 SRS-F0-02 SRS-F0-03 SRS-F0-04 SRS-F0-07 SRS-F0-15 SRS-F0-18 TC-F0-02 TC-F0-03 TC-F0-07")
_c("CHG-037", "SRS-F1-04 SRS-F2-04 TC-F2-08 TC-F2-24 SRS-F3-02 SRS-F3-03 SRS-F4-01 SRS-F4-04")
_c("CHG-042", "SRS-F0-19 SRS-F1-24 SRS-F3-18")
_c("CHG-039", "SRS-F5-01 SRS-F5-02 SRS-F5-03 SRS-F5-04 SRS-F5-05 SRS-F5-06 SRS-F5-07 SRS-F5-08 SRS-F5-09 SRS-F5-11 SRS-F5-12 SRS-F5-13 SRS-F5-14 SRS-F5-16 SRS-F5-17 "
   "URS-F5-01 URS-F5-03 URS-F5-05 URS-F5-06 URS-F5-07 URS-F5-09 TC-F5-04 TC-F5-08 TC-F5-10 TC-F5-11 TC-F5-12 TC-F5-14 TC-F5-19 SD-F5-03 SD-F5-04 SD-F5-05 SD-F5-06 SD-F5-07 SD-F5-08 SD-F5-15")
_c("CHG-040", "SRS-F5-10 URS-F5-04 TC-F5-17")
_c("CHG-041", "SRS-F5-15 TC-F5-23 TC-F5-24")
approved16 = {"SD-F0-14":"CHG-036","SD-F5-09":"CHG-041","SD-F5-10":"CHG-040","SD-F5-17":"CHG-039","SD-F5-18":"CHG-040"}
added_p16 = {"URS-F0-15":("0.3","CHG-036"),"SD-F0-14":("0.3","CHG-036"),"TC-F0-26":("0.3","CHG-036"),
 "URS-F5-14":("0.2","CHG-041"),"SRS-F5-21":("0.2","CHG-041"),"TC-F5-29":("0.2","CHG-041"),
 "SD-F5-17":("0.2","CHG-039"),"SD-F5-18":("0.2","CHG-040")}
firstchg = {"F0":"CHG-018","F1":"CHG-001","F2":"CHG-002","F3":"CHG-003","F4":"CHG-004","F5":"CHG-028"}
version = {"F0":"0.6","F1":"0.8","F2":"0.8","F3":"0.8","F4":"0.8","F5":"0.7"}
# changed in prompt P-34 (22/11/2026): F5 version 0.3, CHG-049
changed_p34 = {i: "CHG-049" for i in ("URS-F5-06 URS-F5-07 URS-F5-08 URS-F5-14 SRS-F5-08 SRS-F5-12 SRS-F5-14 SRS-F5-16 SRS-F5-21 "
    "TC-F5-14 TC-F5-19 TC-F5-21 TC-F5-22 TC-F5-29").split()}
approved_p34 = {"SD-F5-09": "Approved by the owner 14/11/2026, confirmed 22/11/2026 (CHG-049)",
    "SD-F5-17": "Approved by the owner 14/11/2026, changed 22/11/2026 (CHG-049)",
    "SD-F5-19": "Approved by the owner 22/11/2026 (CHG-049)"}
added_p16["SD-F5-19"] = ("0.3", "CHG-049")
# prompt P-42 (23/11/2026): rule corrections from RES-002 (CHG-054)
changed_p42 = {i: "CHG-054" for i in "SRS-F2-08 TC-F2-02 TC-F2-03 OI-F2-03 TC-F3-10 TC-F3-12".split()}
added_p16["TC-F1-23"] = ("0.7", "CHG-054"); added_p16["OI-F2-04"] = ("0.7", "CHG-054")
# changed in prompt P-38 (23/11/2026): wording only, Phase 1 and Phase 2 renamed basic account and launch account (CHG-051)
changed_p38 = {i: "CHG-051" for i in ("SRS-F0-01 URS-F5-01 URS-F5-03 URS-F5-04 URS-F5-05 URS-F5-09 SRS-F5-01 SRS-F5-02 SRS-F5-03 "
    "SRS-F5-04 SRS-F5-05 SRS-F5-06 SRS-F5-07 SRS-F5-08 SRS-F5-09 SRS-F5-10 SRS-F5-11 SRS-F5-12 SRS-F5-13 SRS-F5-15 SRS-F5-16 "
    "SRS-F5-17 TC-F5-04 TC-F5-08 TC-F5-10 TC-F5-11 TC-F5-12 TC-F5-17 TC-F5-23 TC-F5-24 SD-F5-03 SD-F5-04 SD-F5-05 SD-F5-06 "
    "SD-F5-07 SD-F5-08 SD-F5-15").split()}
reg = {}
counts = {}
for k, f in files.items():
    t = open(f"{OUT}/{f}").read()
    rows = []; seen = set()
    for ln in t.split("\n"):
        m = re.match(r'^\| (?:<a id="[^"]*"></a>)?((URS|SRS|TC|SD|OI)-F\d-\d\d) \| (.*)$', ln)
        if not m: continue
        id_, typ = m.group(1), m.group(2)
        if id_ in seen: continue
        seen.add(id_)
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if typ == "URS": d = short(cells[1].replace("The taxpayer must be able to ", "").replace("The user must be able to ", ""))
        elif typ == "SRS":
            mm = re.match(r'\*\*(.+?)\.?\*\*', cells[1]); d = mm.group(1) if mm else short(cells[1], 70)
        elif typ == "TC": d = short(cells[1], 90)
        elif typ == "SD": d = short(cells[1], 120)
        else: d = short(cells[1], 120)
        status = {"URS": "Draft", "SRS": "Draft", "TC": "Draft", "SD": "Needs owner decision", "OI": "Open"}[typ]
        if "**Answered" in cells[1]: status = answered[id_]
        elif id_ in approved_p34: status = approved_p34[id_]
        elif id_ in ("TC-F1-23", "OI-F2-04"): status = "Draft, new" if id_ == "TC-F1-23" else "Answered by the owner 23/11/2026: sub-limits, DA-25 approved (CHG-055)"
        elif id_ in changed_p42: status = f"Draft, changed in {version[k]} ({changed_p42[id_]})"
        elif id_ == "OI-F5-06": status = "Held by the owner 23/11/2026, decided with the stack in ADR-006 (CHG-053)"
        elif id_ in changed_p38: status = f"Draft, wording changed in {version[k]} ({changed_p38[id_]})"
        elif id_ in changed_p34: status = f"Draft, changed in 0.3 ({changed_p34[id_]})"
        elif id_ in approved16: status = f"Approved by the owner 14/11/2026 ({approved16[id_]})"
        elif id_ in added_p16: status = "Draft, new"
        elif id_ in changed_p16: status = f"Draft, changed in {VER16[k]} ({changed_p16[id_]})"
        elif id_ == "SD-F0-01": status = "Approved by the owner 13/11/2026 (CHG-030)"
        elif id_ in changed_p15: status = f"Draft, changed in 0.2 ({changed_p15[id_]})"
        elif id_ in changed03: status = f"Draft, changed in 0.3 ({changed03[id_]})"
        elif id_ in changed: status = f"Draft, changed in 0.2 ({changed[id_]})"
        rows.append((id_, typ, d, status))
    reg[k] = rows
    counts[k] = {p: len([r for r in rows if r[1] == p]) for p in ("URS", "SRS", "TC", "SD", "OI")}
    counts[k]["FD"] = len(set(re.findall(r'<a id="(fd-f\d-\d\d)"></a>', t)))
    counts[k]["SQ"] = len(set(re.findall(r'<a id="(sq-f\d-\d\d)"></a>', t)))
    counts[k]["lines"] = t.count("\n") + 1
tot = {p: sum(counts[k][p] for k in files) for p in ("URS", "SRS", "TC", "SD", "OI", "FD", "SQ")}
L = []
A = L.append
A("""# REG-02: URS and SRS change log

| Item | Value |
| --- | --- |
| Document ID | REG-02 |
| Document type | Register (detail change log of the URS and SRS documents) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | Running log; every entry is dated. Built by docs/tools/changelog.py |
| Status | Active |
| Date | 2026-11-23 (started 2026-11-12) |
| Owner | Champs (product owner) |
| PRD reference | Synced entries record each PRD-TRM change; Pending PRD sync lists the changes waiting for the owner |
| Source | The six URS and SRS documents and the owner prompts (P-nn) |
| Change tracking | This file; the main log is [REG-01 History log](REG_01_History_Log.md) |
| Last updated | 2026-11-23 (document standard, CHG-051: F0 at version 0.4, F1 to F4 at version 0.6, F5 at version 0.4; PRD revision 49 with pending sync items 11, 12, 26 and 27, CHG-052; F5 at version 0.5, email service held, CHG-053; rule corrections from RES-002, PRD revision 50, F0 at 0.5, F1 to F4 at 0.7, F5 at 0.6, CHG-054; DA-25 approved and synced, PRD revision 51, F0 at 0.6, F1 to F4 at 0.8, F5 at 0.7, CHG-055) |

This file records **every detail change** to the six URS and SRS documents (F0 profile, F1 to F4 core features and F5 account and security). The main log of our work is [REG_01_History_Log.md](../registers/REG_01_History_Log.md); this log is the detail log for the documents only.

## How this log works

1. **Version numbers.** Each document starts at 0.1 (first draft). Any change to an ID, a number, a rule or a diagram raises the minor version (0.2, 0.3). When the owner approves a document it becomes 1.0. After that, changes raise 1.1, 1.2.
2. **One entry per detail.** Every change gets the next CHG number and states: the document, the section, the ID changed, the type, what it said before, what it says now, why, and which prompt or finding caused it.
3. **Change types:** Added, Changed, Removed, Clarified, Decided (owner answered an SD or OI), Synced (the PRD was updated to match).
4. **Shared blocks.** The system map FD-00, the interface table (IF-01 to IF-21), the events (EV-01 to EV-08), the data ownership table, the data additions (DA-01 to DA-25) and the category codes are identical in all six documents. A change to one of them is applied to all four in the same CHG entry.
5. **IDs are never reused.** A removed ID stays in the register with status Removed.
6. **Status in the register:** Draft (written, not reviewed), Needs owner decision (SD), Open (OI), Approved, Changed, Removed.

## Document register

| Doc | File | Feature | Version | Date | State | URS | SRS | Flow diagrams (FD) | Sequence (SQ) | Test cases | SD | OI | Lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |""")
for k, f in files.items():
    c = counts[k]
    A(f"| {k} | [{f}](../specs/{f}) | {names[k]} | {version[k]} | 2026-11-13 | Draft for owner review | {c['URS']} | {c['SRS']} | {c['FD']} | {c['SQ']} | {c['TC']} | {c['SD']} | {c['OI']} | {c['lines']} |")
A(f"| | Total | | | | | {tot['URS']} | {tot['SRS']} | {tot['FD']} | {tot['SQ']} | {tot['TC']} | {tot['SD']} | {tot['OI']} | |")
A("""
Shared across all six: 21 interfaces, 8 events, 25 data additions, 26 category codes (R01 to R24, D01, D02), the FD-00 system map.

## Change register

| CHG | Date | Doc | Section | ID | Type | Before | After | Reason | Trigger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CHG-001 | 2026-11-12 | F1 | Whole document | URS-F1-01 to URS-F1-15, SRS-F1-01 to SRS-F1-22, FD-F1-01 to FD-F1-08, SQ-F1-01, TC-F1-01 to TC-F1-20, SD-F1-01 to SD-F1-09, OI-F1-01 to OI-F1-04 | Added | Nothing | Version 0.1 | First draft of the tax calculator and PCB URS and SRS from PRD section 3.1 | Prompt P-08 |
| CHG-002 | 2026-11-12 | F2 | Whole document | URS-F2-01 to URS-F2-12, SRS-F2-01 to SRS-F2-17, FD-F2-01 to FD-F2-07, TC-F2-01 to TC-F2-23, SD-F2-01 to SD-F2-09, OI-F2-01 to OI-F2-03 | Added | Nothing | Version 0.1 | First draft of relief categories and rule sets, from PRD section 3.2 and the admin rules (sections 4 and 8) | Prompt P-08 |
| CHG-003 | 2026-11-12 | F3 | Whole document | URS-F3-01 to URS-F3-14, SRS-F3-01 to SRS-F3-17, FD-F3-01 to FD-F3-08, SQ-F3-01, TC-F3-01 to TC-F3-22, SD-F3-01 to SD-F3-04, OI-F3-01 to OI-F3-04 | Added | Nothing | Version 0.1 | First draft of spending records, from PRD section 3.3 | Prompt P-08 |
| CHG-004 | 2026-11-12 | F4 | Whole document | URS-F4-01 to URS-F4-13, SRS-F4-01 to SRS-F4-16, FD-F4-01 to FD-F4-07, SQ-F4-01, TC-F4-01 to TC-F4-19, SD-F4-01 to SD-F4-07, OI-F4-01 to OI-F4-02 | Added | Nothing | Version 0.1 | First draft of the dashboard, from PRD section 3.4 | Prompt P-08 |
| CHG-005 | 2026-11-12 | F1, F2, F3, F4 | A5 and B2 | FD-00, IF-01 to IF-15, EV-01 to EV-05, data ownership table, DA-01 to DA-15, category codes | Added | Nothing | Identical blocks in all four documents | Makes the four documents one connected set: every interface names a provider SRS and a consumer SRS | Prompt P-08 |
| CHG-006 | 2026-11-12 | F1 | SRS-F1-10, TC-F1-11 | SRS-F1-10, TC-F1-11 | Clarified | Cliff message wording unclear; TC-F1-11 had no numbers | Cliff message shown from RM 35,000.01 to RM 36,000.00; TC-F1-11 states tax before rebates 570.00, payable 170.00, saved 490.00 | Found while checking values by script, before first review | Self-check |
| CHG-007 | 2026-11-12 | F1, F2 | SRS-F1-18, IF-09 | SRS-F1-18, IF-09 | Added | Scenarios: no_reliefs, use_room, use_all_room | Added scenario as_recorded (estimate for any stored YA) | The F4 trend needs an estimate for each YA, not only the selected one | Self-check while writing F4 (SRS-F4-07) |
| CHG-008 | 2026-11-12 | F1, F2, F3, F4 | DA-05, DA-11, seed D01 | DA-05, DA-11, D01 | Changed | DA-05 had three cap bases; DA-11 had file name and size only | DA-05 adds percent_of_aggregate and cap_percent_bp; DA-11 adds upload_state | Donation cap is a percentage of income; a pending receipt must count as attached | Self-check while writing F3 |
| CHG-009 | 2026-11-12 | F2 | SRS-F2-02, SRS-F2-04, TC-F2-03, TC-F2-05, TC-F2-06 | same | Clarified | Search fields omitted sub-limit names; JSON operators written with a pipe that breaks the table; TC-F2-03 listed four changed categories; TC-F2-06 listed only four rows | Search includes sub-limit names; operators written as a list; TC-F2-03 lists seven changed categories; TC-F2-06 allows other categories with room | Corrected against the PRD table before first review | Self-check |
| CHG-010 | 2026-11-12 | F3 | SRS-F3-15 | SRS-F3-15 | Clarified | A prefilled YA always set the date to a day not after today | Date rule per case: ended YA gives 31 December; current YA gives today; a YA not started leaves the date empty | A future date is a validation error | Self-check |
| CHG-011 | 2026-11-12 | F2 | A6 item 3, SRS-F2-08, OI-F2-01 | OI-F2-01, SRS-F2-08 | Decided | R17 loaded at RM 4,000 and marked needs_confirmation for every YA; OI-F2-01 open | R17 is RM 4,000 per LHDN for YA 2025 (RM 3,000 applied to YA 2018 to YA 2024); needs_confirmation stays only for YA 2026 and YA 2027 | LHDN tax reliefs page read on 2026-11-12 answers PRD decision 4 for YA 2025 | Prompt P-09, finding F-029 |
| CHG-012 | 2026-11-12 | F2 | SRS-F2-14, TC-F2-10, B3.2, OI-F2-02 | OI-F2-02, SRS-F2-14, TC-F2-10 | Decided | Group cap 7,000 with no sub-limits; EPF 2,000 plus insurance 6,000 gave 7,000 | R14 EPF capped at 4,000 and R15 life insurance at 3,000 inside the group cap of 7,000; the same inputs now give 5,000; TC-F2-10 now expects room 0 on both members | LHDN lists RM 4,000 and RM 3,000 sub-limits for YA 2023 to YA 2025; answers PRD decision 5 | Prompt P-09, finding F-029 |
| CHG-013 | 2026-11-12 | F3 | SRS-F3-07, TC-F3-08 | SRS-F3-07, TC-F3-08 | Changed | TC-F3-08: EPF applied 7,000 and insurance 0 (group cap only) | EPF applied 4,000 and insurance 3,000 with CATEGORY_CAP 500; second case added (5,000 combined); additional voluntary EPF is entered under R15 | Follows CHG-012 | Prompt P-09 |
| CHG-014 | 2026-11-12 | F1 | TC-F1-05, B3.3 | TC-F1-05 | Clarified | Worked example showed EPF and insurance as one capped 7,000 | Shows EPF counted to 4,000 and insurance to 3,000; every total is unchanged (22,850.00, 49,150.00, 1,449.00) | Follows CHG-012; the worked example result does not change | Prompt P-09 |
| CHG-015 | 2026-11-12 | F4 | B3.2 note | none | Clarified | R17 used "RM 4,000 pending decision 4" | R17 uses the LHDN YA 2025 figure carried forward; no number changes | Follows CHG-011 | Prompt P-09 |
| CHG-016 | 2026-11-12 | F1, F2, F3, F4 | B2.3 category codes (shared) | R14, R15, R17 | Changed | R14 and R15 "own sub-limit to be loaded from LHDN"; R17 "4,000 (confirm)" | R14 category cap 4,000; R15 category cap 3,000 (includes additional voluntary EPF); R17 4,000 with a source note; same text in all four documents | Shared block, applied to all four in one entry (rule 4) | Prompt P-09 |
| CHG-017 | 2026-11-12 | F1, F2, F3, F4 | Header | Document version | Changed | 0.1 | 0.2 | CHG-011 to CHG-016 | Prompt P-09 |
| CHG-018 | 2026-11-13 | F0 | Whole document | URS-F0-01 to URS-F0-13, SRS-F0-01 to SRS-F0-18, FD-F0-01 to FD-F0-08, SQ-F0-01, TC-F0-01 to TC-F0-24, SD-F0-01 to SD-F0-13, OI-F0-01 to OI-F0-04 | Added | Nothing | Version 0.1 of the profile document: guided creation, profile screen, one profile per YA, apply to later YAs, lock of a filed YA, tax-year history, comparison, change history, admin support | Owner asked for a profile document covering how to create a profile, the profile screen and the history of tax years | Prompt P-13, F-032, F-033 |
| CHG-019 | 2026-11-13 | F0, F1, F2, F3, F4 | A5 and B2 shared blocks | FD-00, IF-11 to IF-13, IF-16, IF-17, EV-03, EV-06, data ownership table, DA-16 to DA-20 | Changed | The profile was an unnamed supporting feature; IF-11 to IF-13 had no provider spec; EV-03 named no YA; the ownership table had a Profile column; DA-01 to DA-15 | The profile is document F0; IF-11 to IF-13 point to SRS-F0-15; IF-16 (F1 to F0) and IF-17 (F0 to F1, F3, F4) added; EV-03 carries the YA; EV-06 YearStatusChanged added; the ownership column is F0 with rows for UserTaxYear and TaxEstimate; DA-16 to DA-20 added; FD-00 redrawn with F0 and Admin support | Gives the profile its own owner and makes a profile per YA and the history possible | Prompt P-13 |
| CHG-020 | 2026-11-13 | F1 | SRS-F1-01, SRS-F1-04, SRS-F1-15, SRS-F1-19, SRS-F1-21, A5.4, B2.1, FD-F1-02, data diagram, SQ-F1-01 | same | Changed | One profile per user; EV-03 recalculated every YA; snapshots kept no profile reference; filing raised only EV-02 | F1 reads the profile of the selected YA; recalculates only the YA in EV-03; each snapshot stores profile_id and profile_version_no (DA-18); mark as filed and reopen raise EV-06; opens on a YA chosen in the F0 history (IF-17); diagram names updated | Follows CHG-019 | Prompt P-13 |
| CHG-021 | 2026-11-13 | F1 | SRS-F1-23, TC-F1-21, SD-F1-10, matrix row URS-F1-05 | SRS-F1-23, TC-F1-21, SD-F1-10 | Added | Nothing | Tax-year summary for the history (IF-16) with its test and decision | F0 shows the figures of each YA and must not calculate them | Prompt P-13 |
| CHG-022 | 2026-11-13 | F2 | SRS-F2-04, SRS-F2-05, TC-F2-11, TC-F2-24, A5.4, B2.1, interface diagram | same | Changed | Facts came from "the profile"; no rule for an unconfirmed dependants list; R06 had no source for the home price | Facts come from the selected YA's profile; adds has_first_home, first_home_price and dependants_confirmed; the dependant count test is unknown while dependants_confirmed is false; R06 tiers read first_home_price; R21 and R22 read education_level; TC-F2-24 added | Follows CHG-019; F-036 | Prompt P-13 |
| CHG-023 | 2026-11-13 | F3 | SRS-F3-02, SRS-F3-14, SRS-F3-15, A5.4, B2.1, interface diagram | same | Changed | Beneficiary choices from "the profile"; EV-03 recalculated every YA | Choices come from the profile of the YA the date falls in; a removed dependant shows "(removed)" on old expenses; recalculates on EV-03 for its YA only; the list opens from the F0 history (IF-17) | Follows CHG-019 | Prompt P-13 |
| CHG-024 | 2026-11-13 | F4 | SRS-F4-01, SRS-F4-10, A5.4, FD-F4-02, live-update diagram | same | Changed | Listened to EV-01 to EV-05 | Also listens to EV-06 and opens on a YA chosen in the F0 history (IF-17) | Follows CHG-019 | Prompt P-13 |
| CHG-025 | 2026-11-13 | F0, F1, F2, F3, F4 | Section 0 and the DA row of 0.2 | "four documents" text; DA location "section B2.3" | Clarified | The text said four documents; the DA row named section B2.3, which was the wrong section in F1 to F4 | The text says five documents; the DA row says "Part B2 under Data additions" | Five documents now; a wrong cross-reference found while editing | Prompt P-13 |
| CHG-026 | 2026-11-13 | F0, F1, F2, F3, F4 | B2.3 category codes (shared) | R06 | Changed | R06 "tiered by home price" with no field that holds the price | R06 tiered by home price (profile fact first_home_price, DA-19) | F-036 | Prompt P-13 |
| CHG-027 | 2026-11-13 | F0, F1, F2, F3, F4 | Header | Document version | Changed | F1 to F4 at 0.2 | F1 to F4 at 0.3; F0 at 0.1 | CHG-018 to CHG-026 | Prompt P-13 |
| CHG-028 | 2026-11-13 | F5 | Whole document | URS-F5-01 to URS-F5-13, SRS-F5-01 to SRS-F5-20, FD-F5-01 to FD-F5-12, SQ-F5-01, SQ-F5-02, TC-F5-01 to TC-F5-28, SD-F5-01 to SD-F5-16, OI-F5-01 to OI-F5-07 | Added | Nothing | Version 0.1 of the account and security document: sign-up, verification, consent, sign-in, two-factor login, sessions, password and email, settings, export, deletion, admin account tools | The owner asked for it ("as it a specification we need", "please do it and share to me") and answered OI-F0-01; closes F-041 | Prompts P-14, P-15 |
| CHG-029 | 2026-11-13 | F0, F1, F2, F3, F4, F5 | Section 0, A5 and B2 shared blocks | FD-00, IF-18 to IF-21, EV-07, EV-08, data ownership table, DA-21 to DA-24, terms Session, Fresh sign-in, Grace period, Retention period | Added | Five documents; 17 interfaces, 6 events, 20 data additions; ownership table without an account owner | Six documents; 21 interfaces, 8 events, 24 data additions; F5 column and account rows in the ownership table; DA table has a Status column | F5 gives every feature its identity, export and erase; the owner's decisions of 13/11/2026 are shown where the data additions are listed | Prompts P-14, P-15 |
| CHG-030 | 2026-11-13 | F0, F1, F2, F3, F4, F5 | B8 of F0; DA table (shared) | SD-F0-01, DA-16, DA-19, OI-F0-01, OI-F0-04, DA-20 | Decided | SD-F0-01 "to be confirmed"; DA-16 and DA-19 proposed; OI-F0-01 and OI-F0-04 open | SD-F0-01, DA-16 and DA-19 approved on 13/11/2026; OI-F0-01 answered (own document F5); OI-F0-04 answered (admin sees a Filed flag only, no stage and no figures); DA-20 stays proposed, explained, awaiting the owner's yes | Owner's replies to the six items | Prompt P-14 |
| CHG-031 | 2026-11-13 | F0 | A1, A2, A3, A5.4, SRS-F0-01, SRS-F0-02, SRS-F0-16, SRS-F0-19 (new), B2.1, B5, B6, B7, FD-F0-02, FD-F0-03, OI-F0-03 | URS-F0-14, SRS-F0-19, TC-F0-25 added; SRS-F0-01, SRS-F0-02, SRS-F0-16, OI-F0-03 changed | Changed | Account step asked name, email and language; an admin could change account details including the email; F0 had no export or erase part; sign-in was "out of scope" with no owner | Account step asks name and language and shows the email read only; an admin cannot change the email or the password; F0 supplies its export part and erases its data (IF-19, IF-20); sign-in is specified in F5; change history is deleted with the account | Moves the account to F5 (SD-F5-13) and applies SD-F5-10 | Prompt P-15 |
| CHG-032 | 2026-11-13 | F1 | A3, A5.4, SRS-F1-24 (new), B5, B6, B7 | URS-F1-16, SRS-F1-24, TC-F1-22 | Added | Nothing | F1 supplies its export part, erases income, filed status and saved calculations, and reads the identity from F5 | IF-18 to IF-20 and EV-07, EV-08 need a provider in F1 | Prompt P-15 |
| CHG-033 | 2026-11-13 | F3 | A3, A5.4, SRS-F3-18 (new), B5, B6, B7 | URS-F3-15, SRS-F3-18, TC-F3-23 | Added | Nothing | F3 supplies its export part with the receipt files, erases rows and stored files, and reads the identity from F5 | IF-18 to IF-20 and EV-07, EV-08 need a provider in F3 | Prompt P-15 |
| CHG-034 | 2026-11-13 | F2, F4 | Section 0 | Shared text "five documents" | Changed | Five documents | Six documents; the shared blocks changed, so the documents move to version 0.4. F2 and F4 get no new SRS row (OI-F5-05) | Keeps the six documents one set | Prompt P-15 |
| CHG-035 | 2026-11-13 | F0, F1, F2, F3, F4, F5 | Header | Document version | Changed | F0 at 0.1; F1 to F4 at 0.3 | F0 at 0.2; F1 to F4 at 0.4; F5 at 0.1 | CHG-028 to CHG-034 | Prompt P-15 |
| CHG-036 | 2026-11-14 | F0 | A5, A5.4, A3, SRS-F0-01, SRS-F0-02, SRS-F0-03, SRS-F0-04, SRS-F0-07, SRS-F0-15, SRS-F0-18, B3.1, B3.3, B3.4, B4, B6, TC-F0-02, TC-F0-03, TC-F0-07, B8, FD-F0-03 | URS-F0-15, SD-F0-14, TC-F0-26 added; the SRS and TC listed changed | Changed | Yes, No and not answered; only residency, marital status and spouse income were required; three profile statuses (Incomplete, Basic, Complete); a missing answer left a relief "unknown" and nothing was blocked; "Skip for now" on every optional step | Every visible question is mandatory (marital status is a choice of four statuses); two statuses (Incomplete, Complete); a hard gate: while a YA's profile is Incomplete, F1 to F4 do not calculate, show reliefs or accept income or expenses for that YA; no Skip; a dependant must be fully answered before the list can be confirmed; IF-11 to IF-13 carry a complete flag | Owner decision of 14/11/2026: "Gate, no is supposedly need to give the answers. as it needed for assessment year. Marital Status, is supposedly base on status. not on yes or no." | Prompt P-16 |
| CHG-037 | 2026-11-14 | F1, F2, F3, F4 | SRS-F1-04, SRS-F2-04, SRS-F3-02, SRS-F3-03, SRS-F4-01, SRS-F4-04, A5.4, B4, FD-F2-03, IF-02 result, TC-F2-08, TC-F2-24 | same | Changed | A relief with unknown facts was 0 with a notice; F2 had a third result "unknown"; F3 offered unknown categories with a warning; F4 listed unknown categories | Each feature shows the gate "Complete your profile for YA {y}" while the profile is Incomplete; relief results are applicable or not applicable only; F3 refuses an expense for an Incomplete YA; F4 lists applicable categories only | Applies CHG-036 | Prompt P-16 |
| CHG-038 | 2026-11-14 | F0, F1, F2, F3, F4, F5 | Shared blocks: DA table, IF-11 to IF-13, IF-20 | DA-20, IF-11, IF-12, IF-13, IF-20, DA-24 | Changed | DA-20 proposed (null means not answered); IF-20 erased everything; DataRequest type export or delete | DA-20 approved on 14/11/2026 with a change (null only while a question is open or not shown); IF-11 to IF-13 carry the complete flag; IF-20 can name a YA; DataRequest type delete_ya with a ya field | Owner decisions of 14/11/2026 | Prompt P-16 |
| CHG-039 | 2026-11-14 | F5 | A1, A2, A3, A4 titles, A5.4, A6, SRS titles, B3.1, B3.6 (new), B4, B7, SD-F5-03 to SD-F5-08, SD-F5-15, SD-F5-17 (new) | SD-F5-17 added; the SRS, URS, TC and SD listed changed | Changed | One release (R1) for everything except two-factor and export | Two phases: Phase 1 is the simple account; Phase 2 holds sign-in lockout, emailed links (verification, self-service forgot password, email change), staying signed in, two-factor login, deletion of the whole account and the security events screen. B3.6 says what is built in Phase 1 for each SRS. Admins have no two-factor in Phase 1 (A6 item 8) | Owner decision of 14/11/2026: "for 1st phase we proceed on simple. can hold the feature of sign in lock, links, staying signed in, two-factor, deletion and security to another phase" | Prompt P-16 |
| CHG-040 | 2026-11-14 | F5 | SRS-F5-10, SRS-F5-17, SRS-F5-11, A2, SD-F5-10, SD-F5-18 (new) | SD-F5-18 added; SD-F5-10 approved | Changed | SD-F5-10 "to be confirmed"; the reset email was a convenience for the user | SD-F5-10 approved: an admin cannot change an email or a password; the admin sends a temporary reset link (1 hour, single use), never sees the link or the password; a taxpayer changes the own email in Settings (SD-F5-18) | Owner decision of 14/11/2026: "for admin only; as taxpayer they can change the email; the admin gives a temporary link, not directly change on behalf of the taxpayer" | Prompt P-16 |
| CHG-041 | 2026-11-14 | F5 | A3, FD-F5-10, FD-F5-13 (new), SRS-F5-15, SRS-F5-21 (new), B3.1, B3.4, B3.6, B4, B5, B6, TC-F5-23, TC-F5-24, TC-F5-29 (new), SD-F5-09 | URS-F5-14, SRS-F5-21, FD-F5-13, TC-F5-29 added; SRS-F5-15, TC-F5-23, TC-F5-24 changed; SD-F5-09 approved | Changed | A user could delete the account before the 7 years ended, after a warning | Records can be deleted only after the 7-year period (31 December of the YA plus 7 years). The app shows a notice when a YA becomes deletable; the user deletes one YA at a time (Phase 1); deleting the whole account (Phase 2) is allowed only when every YA is past its period. The worked example now runs to 2035 | Owner decision of 14/11/2026: "make a notification that taxpayer can delete data that is more than 7 years"; "for a moment, let keep it as i give the answer. to allow delete after 7 years" | Prompt P-16 |
| CHG-042 | 2026-11-14 | F0, F1, F3 | SRS-F0-19, SRS-F1-24, SRS-F3-18, SRS-F0-01 | same | Changed | Erase deleted everything of the user | Erase can name one YA and then deletes only that YA's rows and files; the first sign-in trigger of F0 follows sign-up (Phase 1) or verification (Phase 2) | Applies CHG-041 | Prompt P-16 |
| CHG-043 | 2026-11-14 | F0, F1, F2, F3, F4, F5 | Header | Document version | Changed | F0 at 0.2; F1 to F4 at 0.4; F5 at 0.1 | F0 at 0.3; F1 to F4 at 0.5; F5 at 0.2 | CHG-036 to CHG-042 | Prompt P-16 |
| CHG-044 | 2026-11-14 | PRD | Section 3.2 FR-2.3, section 4 (admin support tools), section 5 (TaxpayerProfile), NFR-7, NFR-8, section 8 (roles and admin support paragraph) | Pending sync items 13, 16, 18 and 19 | Synced | The PRD (revision 37) had one profile per user, no mandatory rule, an admin who managed the account on the user's behalf, and records "offered for deletion" after 7 years | PRD revision 47: TaxpayerProfile is one per user per YA with year, copied_from_year, state, has_first_home, first_home_price and dependants_confirmed, and every visible question is mandatory with the calculator, relief categories, spending records and dashboard locked until it is complete; an admin cannot change the email or the password and sends a temporary reset link; an admin sees a Filed flag only; records are kept 7 years and the taxpayer is told when a YA can be deleted | Owner approvals of 13/11/2026 and 14/11/2026 (SD-F0-01, DA-16, DA-19, DA-20, SD-F0-14, SD-F5-10, SD-F5-09) | Prompt P-16 |
| CHG-045 | 2026-11-14 | F0, F1, F2, F3, F4, F5 | Links to the registers | Links to REG_01_History_Log.md, REG_02_URS_SRS_Change_Log.md and REG_03_Acronyms.md | Clarified | Links pointed to files in the same folder | Links point to ../registers/ because the files moved into the repository layout (docs/specs, docs/registers, docs/tools). No requirement changed, so the document versions stay at 0.3 and 0.5 and 0.2 | The owner asked for one repository from documentation to production | Prompt P-18 |
| CHG-046 | 2026-11-18 | AGENTS.md, REG_04_Prompt_Rules.md, PR template | AGENTS.md sections 1 and 5; REG-04 RULE-01, RULE-16, RULE-40, RULE-49, RULE-50; pull request checklist | Rules for how I respond, for review and for the repository | Added | RULE-01 covered only questions and decisions; no review rule; RULE-40 said the repository was local only; RULE-16 said files are sent to the owner; RULE-49 pushed automatically with no condition | RULE-01 covers every prompt (information first); RULE-50: every pull request into main is reviewed, the owner may bypass while alone, and with a second developer 1 review by someone other than the author is needed; RULE-49 applies only after "update"; RULE-40 and RULE-16 brought up to date; PR template has a review line. REG-04 at version 0.6. No requirement document changed, so F0 to F5 keep their versions | The owner asked for a review rule on merge requests and for information first on every prompt | Prompts P-24 to P-26 |
| CHG-047 | 2026-11-18 | AGENTS.md, REG_04_Prompt_Rules.md | AGENTS.md section 5 (automatic commit and push); REG-04 RULE-49 | Automatic commit and push rule | Clarified | RULE-49 ended at commit and push; the owner opened the pull request by hand | RULE-49 continues: after the push the agent opens a pull request with `gh pr create` and stops; the agent never merges. REG-04 at version 0.7. No requirement document changed | The owner installed the GitHub CLI (`gh`) and asked for the agent to open pull requests | Prompts P-27 and P-28 |
| CHG-048 | 2026-11-18 | AGENTS.md, REG_04_Prompt_Rules.md | AGENTS.md section 5 (review before merge); REG-04 RULE-50 and new RULE-51 | Protection of the main branch | Added | The review rule was written only; GitHub did not enforce it and `main` was not protected | GitHub ruleset `protect-main` is active: no direct push, no force push, no deletion on `main`, pull request with 1 approval required; owner bypass for pull requests only. REG-04 at version 0.8. No requirement document changed | The owner asked to protect `main` so that changes go only through a pull request | Prompts P-29 and P-30 |
| CHG-049 | 2026-11-22 | F5 | Header, A1, A2, A3, FD-F5-09 and FD-F5-13 titles, A5.4, A6 items 7 and 8, SRS-F5-08, SRS-F5-12, SRS-F5-14, SRS-F5-16, SRS-F5-21, B3.6, B4, B7, SD-F5-09, SD-F5-17, SD-F5-19 (new) | SD-F5-19 added; URS-F5-06, URS-F5-07, URS-F5-08, URS-F5-14, the SRS listed and TC-F5-14, TC-F5-19, TC-F5-21, TC-F5-22, TC-F5-29 changed | Changed | Phase 1 held data export and the deletion of a YA's records past 7 years; Phase 2 held the security events screen, the new-device notice and the list of devices; B3.6 had two columns; A6 item 8 said only that the owner accepted the risk | Data export, deletion of a YA's records past 7 years (with its notice and the one-YA erase run), the security events screen, the new-device notice and the session controls are built with R3, phase 4 of the PRD roadmap (SD-F5-19); B3.6 has a third column for R3; A6 item 8 records that Phase 1 is used only by the owner and invited people; SD-F5-09 confirmed: deletion is optional after the period and never before. F5 at version 0.3 | Owner answers of 22/11/2026 to F-049 and F-051: "yes for me and invited only"; "move it to phase 4 (r3)"; "deletio is optional after 7 years. strictly no delete before 7 years of YA" | Prompts P-33 and P-34 |
| CHG-050 | 2026-11-22 | AGENTS.md, REG_04_Prompt_Rules.md, CODEOWNERS | AGENTS.md section 5 (review requests); REG-04 RULE-52 (new); `.github/CODEOWNERS` | Review requests on pull requests | Added | CODEOWNERS covered only docs/prd, docs/decisions, docs/registers and AGENTS.md, so a pull request that touched other paths asked nobody for a review | CODEOWNERS starts with `*` (every path) for the owner, with a note on how to add developers; GitHub asks the code owners for a review on every pull request and notifies them. REG-04 at version 0.10. No requirement document changed | The owner asked for a notice when a pull request is opened, so that the owner and later developers see it (option B) | Prompt P-34 |
| CHG-051 | 2026-11-23 | PRD, F0, F1, F2, F3, F4, F5, ADR-000 to ADR-005, RES-001, REG-01 to REG-04, AGENTS.md, README, docs-check workflow | File names, title line and header of every document; section 0 shared blocks (document set, FD-00, terms); F5 A1, B3.1, B3.6, SD-F5-17 and every row that said Phase 1 or Phase 2; SRS-F0-01; IF-20; AGENTS.md sections 2, 3 and 6 (new); REG-04 RULE-53 to RULE-59 (new) | The SRS, URS, TC and SD listed in the ID register as "wording changed in 0.4" or "0.6" | Changed | Each type of document had its own file name style (PRD_..., URS_SRS_..., ADR-001-..., HISTORY_LOG.md) and header; F1 and F2 had titles that differ from the PRD headings; "Phase" meant the PRD roadmap, the two parts of F5 and the stages; rule IDs R-nn and research R-001 looked like releases R1 to R4 and relief codes R01 to R24 | One standard (AGENTS.md section 6): file names `<type>_<ID>_<Short_Name>.md` (PRD_TRM, URS_SRS_F0 to F5, ADR_001, RES_001, REG_01 to REG_04); first line `# <Document ID>: <Title>`; the same header rows in every document; the PRD is the master for names and IDs, so F1 is "Tax calculator for any year" and F2 "Relief categories and ranges"; "Phase" means only a PRD roadmap phase; F5 Phase 1 and Phase 2 renamed basic account (R1) and launch account (before public launch), meaning unchanged; stages in AGENTS.md section 3; rule IDs RULE-nn; research RES-001; a new check docs/tools/check_standard.py runs in the workflow. PRD to revision 48 (header and file name only, no requirement changed); F0 to 0.4, F1 to F4 to 0.6, F5 to 0.4 (the shared blocks changed); REG-04 to 0.11 | The owner asked for one standard for every document, with names that follow the PRD IDs and the PRD winning when there is a conflict, so the work can be managed and tracked during development | Prompts P-37 and P-38 |
| CHG-052 | 2026-11-23 | PRD | Section 2.3 (education and medical insurance; life insurance and EPF), section 9.1 (phase 1, phase 4, public launch gate), section 9.3 decisions 4 and 5, section 9.4 (new), Sources | Pending sync items 11, 12, 26 and 27 | Synced | Revision 48: education and medical insurance "4,000 (confirm)" for every YA; EPF and life insurance sub-limits "as published on LHDN's site"; decisions 4 and 5 kept in view; section 9.1 had no account and security parts; no list of the items waiting for approval | Revision 49: RM 4,000 for YA 2025 from LHDN, carried forward for YA 2026 and YA 2027 with needs confirmation; EPF up to 4,000 and life insurance, family takaful and additional voluntary EPF up to 3,000 inside 7,000; decisions 4 and 5 answered with the LHDN source; phase 1 holds the basic account, phase 4 (R3) the export, old-record deletion, security screens and session controls, and the public launch gate the launch account; F-058 named as open; section 9.4 lists the 19 items still waiting for owner approval | The owner said "update the PRD" for the items that have approval; the others wait and are marked (OI-F2-01, OI-F2-02 answered from LHDN on 12/11/2026; SD-F5-17 approved 14/11/2026; SD-F5-19 approved 22/11/2026) | Prompt P-38 |
| CHG-053 | 2026-11-23 | F5, ADR-006 | A6 item 6, OI-F5-06, header; new docs/decisions/ADR_006_Email_Service.md | OI-F5-06 | Changed | OI-F5-06: the email service is chosen at development | OI-F5-06 is held by the owner (no domain yet) and decided with the stack in ADR-006, which lists the emails of the basic account and the launch account and what the choice needs (domain with SPF, DKIM and DMARC; provider region and data terms under the PDPA). F5 to 0.5. The YA 2026 and YA 2027 rule check is written in RES-002; no rule value in the documents is changed (F-063 waits for the owner) | Owner answer of 23/11/2026: "not yet, not sure which one to use. can we hold this for moment. can remarks for next stack" | Prompt P-41 |
| CHG-054 | 2026-11-23 | PRD, F0, F1, F2, F3, F4, F5 | PRD sections 2.2, 2.3, 2.5, 9.4, Sources; F1 B3.1, B7; F2 A6 item 3, SRS-F2-08, B7, B8; F3 B7; shared seed catalogue (B2.3) and DA table | SRS-F2-08, TC-F2-02, TC-F2-03, OI-F2-01, OI-F2-03, TC-F3-10, TC-F3-12 changed; TC-F1-23, OI-F2-04, DA-25 added | Changed | One band 400,001 to 1,000,000 at 26% (28% to 2,000,000; YA 2027 30% from 1,000,001); R12 once-only for the whole relief and no grinder; R23 child up to 12 everywhere from YA 2026; R15 child policy "confirm"; R17 YA 2026 and YA 2027 "needs confirmation"; R13 not available in YA 2027; R05 skills sub-limit 2,000 in YA 2027; R24 a separate relief in YA 2027; YA rule rows from secondary sources | Bands 400,001 to 600,000 at 26% and 600,001 to 1,000,000 at 28% (YA 2027 the same, then 30% above 1,000,000), with TC-F1-23 (RM 700,000 gives 164,400.00 for YA 2026 and 163,600.00 for YA 2027); R12 sub-limits EV_CHARGING, COMPOSTER, GRINDER, CCTV with their own once-only rules; R23 sub-limits TASKA_TADIKA (6) and CARE_CENTRE (12); R15 child policy counts from YA 2026; R17 Confirmed for YA 2026; R13 1,000 in YA 2027; R05 YA 2027 sub-limits TVET 3,000 and COURSES_CLASSES 2,000; R24 moves into R07 as BREASTFEEDING from YA 2027; R07 and R05 take their YA 2027 names; DA-25 and OI-F2-04 proposed for item-level rules; PRD revision 50 with primary sources and pending sync item 28. TC-F1-01 to TC-F1-06 recomputed by script: no change | The owner said "update" for the F-063 corrections found by the YA 2026 and YA 2027 check (RES-002) | Prompt P-42 |
| CHG-055 | 2026-11-23 | PRD, F0, F1, F2, F3, F4, F5 | PRD section 5 (SubLimit), section 2.5, section 9.4; F2 B8 OI-F2-04; DA table (shared) | OI-F2-04, DA-25; pending sync item 28 | Decided | DA-25 and OI-F2-04 proposed; pending sync item 28 waiting; PRD section 2.5 did not say which YA is used for real | DA-25 approved: an item-level rule is a SubLimit row with its own eligibility test and claim frequency; OI-F2-04 answered; PRD revision 51: SubLimit has eligibility_rule and claim-frequency fields, item 28 synced and removed from section 9.4; section 2.5 says real use starts with YA 2026, YA 2025 is the reference year, YA 2025 and YA 2026 are the verification focus and YA 2027 stays loaded as Announced (option a). The YA 2027 breastfeeding detail is kept in view. F0 to 0.6, F1 to F4 to 0.8, F5 to 0.7 (the shared DA table changed) | Owner: "let make it a sub-limit"; "focus on YA 2025 and YA 2026"; "the target is to use it from YA 2026 and above"; option (a); "update and update the PRD" | Prompts P-43 and P-44 |
| CHG-056 | 2026-11-23 | None (research note) | docs/decisions/research/RES_003_YA2025_And_PCB_2026_Check.md | None | Added | YA 2025 checked only from secondary sources and the LHDN reliefs page; PCB method not checked against LHDN | RES-003: every YA 2025 value matches LHDN (Form BE YA 2025 notes); the PCB 2026 specification uses the same projection as SRS-F1-12; proposals in F-067. No requirement document changed, so the versions stay | Owner asked to focus on YA 2025 and YA 2026 and to check them (P-43, P-44) | Prompts P-44 and P-45 |

## Pending PRD sync

These are the changes the PRD needs if the owner approves the matching item. Items 13, 16, 18 and 19 were done in PRD revision 47 on 14/11/2026 (CHG-044), items 11, 12, 26 and 27 in revision 49 on 23/11/2026 (CHG-052), and item 28 in revision 51 on 23/11/2026 (CHG-055); their numbers are not reused. 19 items are still pending. Every pending item is a proposal and keeps the status "Waiting for owner approval" until the owner approves it; the PRD lists them in section 9.4. When one is done, a CHG entry of type Synced is added.

| # | PRD place | Change | Matching IDs | Status |
| --- | --- | --- | --- | --- |
| 1 | Section 5, data model | Add DA-01 to DA-15 (new fields, RuleTier, UserTaxYear) | DA-01 to DA-15 | Waiting for owner approval |
| 2 | Section 5, TaxYear | Remove status open or filed (moves to UserTaxYear) | DA-12 | Waiting for owner approval |
| 3 | FR-1.9 | State that PCB on bonus is counted once | SRS-F1-12, OI-F1-02 | Waiting for owner approval |
| 4 | FR-1.1 and FR-1.9 | State that income of months with no record is projected, and how | SD-F1-02 | Waiting for owner approval |
| 5 | FR-4.4 | Replace "using the current marginal rate" with the tax difference from scenario | SD-F4-04 | Waiting for owner approval |
| 6 | Section 2.2 and 5 | Bands store the lower threshold | SD-F1-09 | Waiting for owner approval |
| 7 | BR-9 | Define "closed" | OI-F1-03 | Waiting for owner approval |
| 8 | Section 8 roles | Say what "download" means for an admin | OI-F3-01 | Waiting for owner approval |
| 9 | BR-10 | State the rounding rule | SD-F1-05 | Waiting for owner approval |
| 10 | Section 4 | Rule change log R1 per-rule history, R2 consolidated | SD-F2-08 | Waiting for owner approval |
| 14 | Section 5, Dependant | Add person_key and display_name | DA-17 | Waiting for owner approval |
| 15 | Section 5, TaxEstimate | Add profile_id and profile_version_no | DA-18 | Waiting for owner approval |
| 17 | Section 3 (features) | Add the profile and tax-year history feature F0 with its own FR block (proposed FR-0.1 to FR-0.8) and screens | URS-F0-01 to URS-F0-15 | Waiting for owner approval |
| 20 | Section 5, User | Add status, email_verified_at, deletion_requested_at, deletion_due_on, last_sign_in_at | DA-21 | Waiting for owner approval |
| 21 | Section 5 | Add Credential, Session, ConsentRecord, Invitation, DataRequest and SecurityEvent | DA-22 to DA-24 | Waiting for owner approval |
| 22 | Section 7, Sign in and onboarding | Sign-up by invitation and password rules (basic account); email verified before use, session lengths and sign-in lockout (launch account, SD-F5-17) | SD-F5-01 to SD-F5-04, SD-F5-06 | Waiting for owner approval |
| 23 | Section 7 Settings, NFR-7, NFR-8 | Export as a ZIP; deletion of the whole account with a 14-day grace period (launch account); consent purposes and text headings. The 7-year rule is already in the PRD (CHG-044) | SD-F5-08, SD-F5-09, SD-F5-12, SD-F5-14 | Waiting for owner approval |
| 24 | NFR-6 | Two-factor by authenticator app, optional for taxpayers, required for admins; no SMS (launch account) | SD-F5-05, SD-F5-07 | Waiting for owner approval |
| 25 | Section 3 (features) | Add the account and security feature F5 with its own FR block (proposed FR-5.1 to FR-5.9) and screens | URS-F5-01 to URS-F5-14 | Waiting for owner approval |

## Consistency checks

| Date | Check | Result |
| --- | --- | --- |
| 2026-11-12 | Every referenced URS, SRS, FD, SQ, TC, SD, OI ID is defined in the right document | 0 errors |
| 2026-11-12 | Every URS appears in its traceability matrix | 0 errors |
| 2026-11-12 | Every SRS names at least one URS, a flow diagram (or "not drawn") and a test case (or "none in R1") | 0 errors |
| 2026-11-12 | Table columns match their header in every table | 0 errors |
| 2026-11-12 | Interface table, ownership table, data additions and category codes are identical in the four documents | 0 differences |
| 2026-11-12 | Every provider and consumer SRS named in the interface table exists | 0 errors |
| 2026-11-12 | All 37 Mermaid diagrams (30 FD, 3 SQ, 4 copies of FD-00) render (version 0.2) | 37 of 37 |
| 2026-11-12 | After version 0.2: all checks above repeated | 0 errors |
| 2026-11-12 | Tax test values (TC-F1-01 to TC-F1-06, TC-F1-10, TC-F1-11, TC-F1-17, F4 B3.1 and B3.2) recomputed by script | All match |
| 2026-11-13 | After F0 and version 0.3: all checks above repeated over five documents (shared blocks identical in all five) | 0 errors |
| 2026-11-13 | Acronym check (src/check_acronyms.py) over all documents | Passed |
| 2026-11-13 | All 47 Mermaid diagrams (38 FD, 4 SQ, 5 copies of FD-00) render | 47 of 47 |
| 2026-11-13 | F0 test values recomputed by script: YA 2025 example (chargeable income 45,150.00, tax 1,209.00), TC-F0-24 (42,150.00, tax 1,029.00), children's ages for YA 2026 to YA 2028, completeness percentages | All match |
| 2026-11-13 | After F5, F0 version 0.2 and F1 to F4 version 0.4: all checks above repeated over six documents (shared blocks identical in all six) | 0 errors |
| 2026-11-13 | Acronym check (src/check_acronyms.py) after adding 7 acronyms and 3 code values | Passed |
| 2026-11-13 | All 62 Mermaid diagrams (50 FD, 6 SQ, 6 copies of FD-00) render | 62 of 62 |
| 2026-11-13 | F5 dates recomputed by script: grace end 27/11/2026, backup purge 01/01/2027, 7-year ends 31/12/2032, 31/12/2033 and 31/12/2034, lock until 10:15:00, session expiries 27/11/2026 09:00, 04/12/2026 09:00, 12:00 and 10:30 | All match |
| 2026-11-14 | After the owner decisions of P-16 (mandatory answers, phase split, 7-year rule): all checks above repeated over six documents (shared blocks identical in all six) | 0 errors |
| 2026-11-14 | Acronym check (src/check_acronyms.py) | Passed (119 register rows) |
| 2026-11-14 | All Mermaid diagrams render (FD-F2-03, FD-F0-03, FD-F5-10 changed; FD-F5-13 new) | The 4 changed or new diagrams render (FD-F0-03, FD-F2-03, FD-F5-10, FD-F5-13); the others are unchanged |
| 2026-11-14 | New F5 dates recomputed by script: YA 2025 retention ends 31/12/2032 and is deletable from 01/01/2033; YA 2026 and YA 2027 from 01/01/2034 and 01/01/2035; deletion due 19/01/2035 (05/01/2035 plus 14 days); backup purge 23/02/2035 (19/01/2035 plus 35 days) | All match |
| 2026-11-18 | After the rules change (CHG-046): build, change log and acronym check repeated over six documents | 0 errors; acronym check passed |
| 2026-11-18 | After the pull request rule (CHG-047): build, change log and acronym check repeated over six documents | 0 errors; acronym check passed |
| 2026-11-18 | After the protected main rule (CHG-048): build, change log and acronym check repeated over six documents | 0 errors; acronym check passed |
| 2026-11-22 | After the R3 move in F5 (CHG-049): build, change log and acronym check repeated over six documents; only F5 changed | 0 errors; acronym check passed |
| 2026-11-22 | After the review requests rule (CHG-050): build, change log and acronym check repeated over six documents | 0 errors; acronym check passed |
| 2026-11-23 | After the document standard (CHG-051): build, change log, acronym check and the new document standard check (check_standard.py) over every document under docs/ | 0 errors; acronym check passed; standard check 0 errors |
| 2026-11-23 | After the PRD sync (CHG-052): build, change log, acronym check and standard check; Pending PRD sync has 19 rows, each with the status Waiting for owner approval, and PRD section 9.4 lists the same 19 items | 0 errors; acronym check passed; standard check 0 errors; 19 of 19 |
| 2026-11-23 | After the phase 0 answers (CHG-053): build, change log, acronym check and standard check; RES-002 tax bands above RM 400,000 re-read on the LHDN rate page | 0 errors; acronym check passed; standard check 0 errors; LHDN table matches RES-002 |
| 2026-11-23 | After the rule corrections (CHG-054): build, change log, acronym check and standard check; band tax recomputed by script for TC-F1-01 to TC-F1-06, TC-F1-10, TC-F1-11, TC-F1-17 (unchanged) and TC-F1-23 (new); cumulative tax at 400,000, 600,000 and 2,000,000 equals LHDN's table (84,400.00, 136,400.00, 528,400.00); Pending PRD sync and PRD section 9.4 both list 20 items | 0 errors; acronym check passed; standard check 0 errors; all values match |
| 2026-11-23 | After DA-25 approval and sync (CHG-055): build, change log, acronym check and standard check; Pending PRD sync and PRD section 9.4 both list 19 items | 0 errors; acronym check passed; standard check 0 errors; 19 of 19 |

## ID register

Every URS, SRS, test case, specification decision and open item. "Added in" is the version that created the ID; "Status" shows later changes. Later changes refer to these IDs.
""")
for k, f in files.items():
    A(f"\n### {k}. {names[k]} ({f})\n")
    A("| ID | Type | Short description | Added in | Status |")
    A("| --- | --- | --- | --- | --- |")
    for id_, typ, d, st in reg[k]:
        A(f"| {id_} | {typ} | {d} | {('0.3 (' + added03[id_] + ')') if id_ in added03 else (added_p15[id_][0] + ' (' + added_p15[id_][1] + ')') if id_ in added_p15 else (added_p16[id_][0] + ' (' + added_p16[id_][1] + ')') if id_ in added_p16 else ('0.1 (' + firstchg[k] + ')')} | {st} |")
open(f"{REG}/REG_02_URS_SRS_Change_Log.md", "w").write("\n".join(L) + "\n")
print(json.dumps(counts), tot)
