# REG-04: Prompt and working rules

| Item | Value |
| --- | --- |
| Document ID | REG-04 |
| Document type | Register (standing rules for prompts and work) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.14 |
| Status | Draft (for owner review) |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | RULE-20 to RULE-22 (how the PRD is changed); AGENTS.md section 6 (the PRD is the master for names and IDs) |
| Source | Owner prompts P-13 to P-46 |
| Change tracking | Section 7 of this file; [REG_01_History_Log.md](REG_01_History_Log.md), [AGENTS.md](../../AGENTS.md), [REG_02_URS_SRS_Change_Log.md](REG_02_URS_SRS_Change_Log.md), [REG_03_Acronyms.md](REG_03_Acronyms.md) |

This file collects the standing rules for how we work on the Tax Relief Manager (TRM) documents: how you give a prompt, how I answer, and what I must update. Every rule below came from your messages. When you give a new rule, I add it here and raise the version.

---

## 1. Rules for how I respond

| # | Rule | Source |
| --- | --- | --- |
| RULE-01 | For **every prompt** I **respond first** with what I understood and what I would change, and **change nothing** until you say "update" or "go ahead". (Widened on 18/11/2026; before, it covered only answering questions and making decisions.) | Prompts of 14/11/2026 00:05 and P-25 |
| RULE-02 | When you say "update", "please do it" or give a go-ahead after your answers, I apply all of it and tell you what changed. | Prompts P-14 to P-16 |
| RULE-03 | I give you **only the latest information you gave**. I add no extra information you did not ask for. | Prompt of 14/11/2026 00:20 |
| RULE-04 | I keep my replies short and in plain language. I say what changed, what is still open and what I read in my own way. | Working practice |
| RULE-05 | When your words can be read two ways, I choose the most reasonable reading, write it down as a flagged finding in REG_01_History_Log.md and ask you to correct it if it is wrong. | Working practice (F-051) |
| RULE-06 | I never present my own proposal as a decision. A value or rule that I proposed stays "proposed" until you approve it, and then I record the date. | Working practice (SD, OI, DA) |

## 2. Rules for files

| # | Rule | Source |
| --- | --- | --- |
| RULE-10 | **Update all the MD files** to control the version and quality of the documents. | Prompt P-13 |
| RULE-11 | **Only the MD files are updated. I do not update or regenerate any PDF.** I create a PDF only when you ask for it. | Prompt of 14/11/2026 00:05 |
| RULE-12 | Every change raises the document version and adds an entry to REG_02_URS_SRS_Change_Log.md (what, before, after, why, which prompt). | Prompt P-13 |
| RULE-13 | REG_01_History_Log.md records every prompt (P-nn), finding (F-nn) and step of our work. | Prompt P-13 |
| RULE-14 | REG_03_Acronyms.md lists every short form. I run the acronym check after each round of changes. | Working practice (F-034) |
| RULE-15 | After a change I run the build checks (references resolve, every URS in the matrix, every SRS has a URS, a flow and a test, shared blocks identical in all documents). The result must be 0 errors. | Working practice |
| RULE-16 | I tell you which MD files changed, with a one-line caption. Git keeps the copies now (from 18/11/2026), so I no longer need to send each file. | Working practice; updated in P-26 |

## 3. Rules for the PRD

| # | Rule | Source |
| --- | --- | --- |
| RULE-20 | The PRD (PRD-TRM, `docs/prd/PRD_TRM_Malaysia_Tax_Relief_System.md`; the Claude Doc is a copy) is changed **only when you tell me to update it**, and only for items you approved. | Prompts P-14 to P-16 |
| RULE-21 | Items waiting for your approval stay in the "Pending PRD sync" list of REG_02_URS_SRS_Change_Log.md with the status "Waiting for owner approval", and the PRD lists them in section 9.4, so it is clear what still needs a proposal approved. | Working practice |
| RULE-22 | When the PRD is changed, I change the local PRD .md copy the same way, add a Synced entry (CHG) and note the new revision number. | CHG-044 |

## 4. Rules for the specification documents

| # | Rule | Source |
| --- | --- | --- |
| RULE-30 | The document set is F0 profile, F1 tax calculator for any year, F2 relief categories and ranges, F3 spending records, F4 dashboard and F5 account and security (F1 to F4 take their names from PRD sections 3.1 to 3.4). Each has a URS (what the user needs) and an SRS (how the system behaves). | Prompts P-08 to P-15 |
| RULE-31 | IDs: URS-Fn-nn, SRS-Fn-nn, FD (flow diagram), SQ (sequence), TC (test case), SD (specification decision), OI (open item), IF (interface), EV (event), DA (data addition). IDs are never reused. | Document conventions |
| RULE-32 | The shared blocks (conventions, interface table, ownership table, data additions, category codes) are identical in all six documents. | Build check |
| RULE-33 | Every SRS names its URS, its flow diagram (or "not drawn") and its test case. | Build check |
| RULE-34 | Tax figures and dates in tests are recomputed by script, not by hand. | Working practice |
| RULE-35 | Figures from LHDN or other sources are marked with their status (Announced, Gazetted, Confirmed). When a value is not printed yet, I say so and do not invent it. | Documents F1, F2 |
| RULE-36 | Money is stored as integer sen and shown as "RM 1,449.00". Dates are DD/MM/YYYY. | Document conventions |
| RULE-37 | The documents are in plain language, without bullet lists inside decisions where a table fits better. | Working practice |

## 4a. Rules for the repository

| # | Rule | Source |
| --- | --- | --- |
| RULE-40 | One repository carries the project from documentation to development to production. It is on GitHub (public): https://github.com/Juthyra/Tax-Relief-Manager-TRM-, since 18/11/2026. Changes reach `main` through pull requests. | Prompts P-18 and P-23; updated in P-26 |
| RULE-41 | Git is the master of the PRD from 14/11/2026. The Claude Doc is a copy (last synced at revision 47). | Prompt P-18 |
| RULE-42 | The built files in `docs/specs/` are never edited by hand. Edit `docs/tools/source/` or `docs/tools/shared.py` and build. | Repository design |
| RULE-43 | `AGENTS.md` holds the rules for any AI agent and any model. `CLAUDE.md` only points to it. There is no `.mcp.json`. | Prompt P-18 |
| RULE-44 | Language, framework, architecture, Docker, database and hosting are open decisions, tracked as `docs/decisions/ADR-001` to `ADR-005`. | Prompt P-18 |
| RULE-45 | Each stage (documentation, development, staging, production) has its own rules, written in `AGENTS.md` section 3. | Prompt P-18 |
| RULE-46 | No work on `main` on a local machine. Create a branch first: `docs/<ID>-short-name` (documentation only), `feature/<ID>-short-name` (development) or `bug-fixing/<ID>-short-name` (defect fixes). A branch does one kind of work. | Prompt P-19 |
| RULE-47 | Documentation has its own branch type, `docs/<ID>-short-name`. It is for documentation only, in PRD phase 1 and in each later PRD phase, which is planned separately. | Prompt P-19 |
| RULE-48 | A commit message starts with the branch type, then the ID in brackets, then a short plain summary, and ends with the prompt (P-nn) or change (CHG-nn) number when there is one. Examples are in `AGENTS.md` section 5. | Prompt P-20 |
| RULE-49 | When a requirement change or a new requirement is done and the checks pass, the work is committed on its branch with a commit message and the branch is pushed, automatically, without waiting to be asked. Never push directly to `main`. After the push I open a pull request into `main` with `gh pr create` (template filled, AI agent named) and stop; **I never merge it**, you merge it (RULE-50). This applies only **after you have said "update"** (RULE-01); until then I change nothing. This replaces the earlier rule "commit or push only when asked". | Prompts P-21, P-26 and P-28 |
| RULE-50 | **Review before merge.** Every pull request into `main` is reviewed before it is merged. While you are the only person on the project, you may merge your own pull request without a review (owner bypass). When another developer joins, every pull request needs 1 approving review from someone other than its author; nobody approves or merges their own pull request, except you as owner, who may bypass it for your own. It is enforced on GitHub by RULE-51. | Prompts P-24 to P-26 and P-30 |
| RULE-51 | **`main` is protected.** The ruleset `protect-main` (active since 18/11/2026) blocks direct pushes, force pushes and deletion on `main`; every change goes through a pull request, which needs 1 approving review. The only bypass is the repository admin role (the owner), set to **pull requests only**: the owner can merge a pull request without the approval but cannot push straight to `main`. No required status check yet. I do not change this ruleset unless you say "update". | Prompts P-29 and P-30 |
| RULE-52 | **Review requests.** `.github/CODEOWNERS` names the code owners for every path (`*`), so GitHub asks them for a review on every new pull request and notifies them. When a developer joins, you add their GitHub username to CODEOWNERS. GitHub never notifies the author of a pull request, so the pull requests I open under your account show in your Pull requests list, not as a notification. The ruleset does not require a code owner's review; the 1 approval of RULE-51 is enough. | Prompt P-34 |

## 4b. Rules for the document standard

| # | Rule | Source |
| --- | --- | --- |
| RULE-53 | **The PRD is the master for names and IDs.** Feature IDs and names, requirement IDs (FR, BR, NFR), releases and phases come from PRD-TRM. When another document disagrees, the PRD wins: I change the other document, or, when the PRD looks wrong, I write a finding and a Pending PRD sync item and wait for you. | Prompt P-38 |
| RULE-54 | **File names** are `<type>_<ID>_<Short_Name>.md` with underscores: PRD_TRM, URS_SRS_F0 to F5, ADR_nnn, RES_nnn, REG_nn (AGENTS.md section 6). README.md, AGENTS.md, CLAUDE.md, `.github/` and the build inputs `docs/tools/source/f0.md` to `f5.md` keep their names. | Prompt P-38 |
| RULE-55 | **Title and header.** The first line is `# <Document ID>: <Title>`. The header table follows with the rows Document ID, Document type, Product, Version, Status, Date, Owner, PRD reference, Source, Change tracking, in this order. | Prompt P-38 |
| RULE-56 | **Terms.** "Phase" means only a phase of the PRD roadmap (section 9.1). R1 to R4 are releases. Documentation, development, staging and production are stages. F5 has the basic account (R1) and the launch account (before public launch). | Prompt P-38 |
| RULE-57 | **IDs that look alike are kept apart.** Working rules are RULE-nn (were R-nn), research notes RES-nnn (was R-001), so they cannot be mixed up with releases R1 to R4 or relief codes R01 to R24. | Prompt P-38 |
| RULE-58 | **Waiting items are marked.** What you have not approved says "Proposed"; a PRD change that waits keeps the status "Waiting for owner approval" (RULE-21). | Prompt P-38 |
| RULE-59 | **Checked.** `docs/tools/check_standard.py` checks file names, titles and headers, and runs in the `docs-check` workflow. It must pass, like the build and the acronym check. | Prompt P-38 |

## 5. Decisions you have already made (14/11/2026, 22/11/2026 and 23/11/2026)

| Topic | Decision | Recorded as |
| --- | --- | --- |
| Profile answers | Every visible profile question is mandatory. Marital status is a choice of status, not Yes or No. Until a year's profile is complete, F1 to F4 are locked for that year (hard gate). | SD-F0-14, DA-20 |
| Admin and passwords | An admin cannot change a taxpayer's email or password. The admin sends a temporary reset link. The taxpayer can change their own email. | SD-F5-10, SD-F5-18 |
| F5 parts | The basic account (called Phase 1 until 23/11/2026) is the simple account, built in R1 and used only by you and the people you invite (22/11/2026). Sign-in lock, emailed links, staying signed in, two-factor and account deletion are held for the launch account (called Phase 2 until 23/11/2026), built before the public launch. Data export, deletion of old records, the security events screen, the new-device notice and the session controls are built with R3, phase 4 of the PRD roadmap (22/11/2026). | SD-F5-17, SD-F5-19, F-049 |
| Deletion | Records can be deleted only after 7 years from the end of the YA, and strictly never before. Deleting is optional, the taxpayer's own choice. The app shows a notice when a YA becomes deletable. | SD-F5-09 (confirmed 22/11/2026) |
| Document standard | Every document follows one standard: names follow the PRD IDs and the PRD wins in a conflict; underscore file names; the same title and header; basic account and launch account for F5 (23/11/2026) | RULE-53 to RULE-59, CHG-051 |
| Phase 0 | YA 2026 and YA 2027 are checked against primary sources before phase 1; a YA 2027 rule that is Announced with a source counts as firm. The stack (ADR-001 to ADR-006) is chosen after the confirmations are firm (23/11/2026) | F-062, RES-002 |
| Year focus | Real use starts with YA 2026 (filed in 2027); YA 2025 (filed in 2026) is the reference. Requirements and checks focus on YA 2025 and YA 2026. YA 2027 stays in R1 as Announced and its re-checks are kept in view (23/11/2026) | PRD section 2.5, F-065, F-066 |
| Item-level rules | A rule on one item of a category is a sub-limit with its own eligibility test and claim frequency (23/11/2026) | DA-25, OI-F2-04 |
| LHDN conditions and PCB help | LHDN's eligibility conditions are asked in the profile (Q11 to Q13, child relief shared or child with own income); the YA 2025 deadline is stored; PCB entry has help text and LHDN's PCB example is a test (23/11/2026) | F-067, DA-26, RES-003 |
| Email service | Held: no domain yet; decided with the stack (23/11/2026) | ADR-006, OI-F5-06 |
| Later | Hosting and consent text are decided during development. Where to store and share the documents is decided after the basic documents are complete. | OI-F5-01, OI-F5-02, OI-F5-06, F-035 |

## 6. How to write a prompt to me

You can write in your own words. These short forms help me act correctly.

| You want | Write something like | I will |
| --- | --- | --- |
| To answer my questions and see my understanding first | "Number 1: yes. Number 2: no, change to X. Respond first, do not change." | Reply with my understanding and change nothing |
| To apply your answers | "Update all the documents." or "Update the PRD." | Change the MD files (and the PRD only if you say so), update the logs, send the files |
| A new feature or document | "Create the document for [feature]. Cover: [list]." | Write it as the next document, add it to the shared blocks and logs |
| A new rule for how we work | "New rule: [rule]." | Add it to this file and raise the version |
| A PDF | "Create the PDF for [file]." | Make only that PDF |
| A question only | "Explain [item]." | Explain in plain language and change nothing |

## 7. Change history of this file

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-11-14 | First version, from the standing rules in prompts P-13 to P-16 |
| 0.2 | 2026-11-14 | Added the repository rules RULE-40 to RULE-45 (prompt P-18) |
| 0.3 | 2026-11-14 | Added the branch rules RULE-46 and RULE-47 (prompt P-19) |
| 0.4 | 2026-11-14 | Added the commit message rule RULE-48 with examples (prompt P-20) |
| 0.5 | 2026-11-14 | Added the automatic commit and push rule RULE-49 (prompt P-21) |
| 0.14 | 2026-11-23 | Section 5: LHDN conditions and PCB help approved (prompt P-46, CHG-057) |
| 0.13 | 2026-11-23 | Section 5: year focus (YA 2025 and YA 2026, YA 2027 kept in view) and item-level rules as sub-limits (prompts P-43 and P-44, CHG-055) |
| 0.12 | 2026-11-23 | Section 5: phase 0 order and the email service held for the stack (prompt P-41, CHG-053) |
| 0.11 | 2026-11-23 | New section 4b, RULE-53 to RULE-59 (document standard); rule IDs renamed R-nn to RULE-nn; RULE-20, RULE-21, RULE-30, RULE-45, RULE-47 and section 5 brought in line (prompt P-38, CHG-051) |
| 0.10 | 2026-11-22 | New RULE-52: CODEOWNERS covers every path, so every pull request asks the code owners for a review (prompt P-34, CHG-050) |
| 0.9 | 2026-11-22 | Section 5: Phase 1 only for the owner and invited people; export, deletion of old records and the security screens moved to R3; deletion strictly after 7 years and optional (prompt P-34, CHG-049) |
| 0.8 | 2026-11-18 | New RULE-51 (`main` protected by the ruleset `protect-main`, owner bypass for pull requests only); RULE-50 now enforced (prompts P-29 and P-30, CHG-048) |
| 0.7 | 2026-11-18 | RULE-49 extended: after the push I open a pull request with `gh` and never merge it (prompts P-27 and P-28, CHG-047) |
| 0.6 | 2026-11-18 | RULE-01 widened to every prompt; RULE-49 only after "update"; new RULE-50 (review before merge, owner bypass); RULE-16 and RULE-40 brought up to date (prompts P-24 to P-26, CHG-046) |
