# Prompt and Working Rules: Malaysia Tax Relief System (PWA)

Owner: Champs (product owner)
Version: 0.9 (draft, for owner review)
Date: 2026-11-22
Related files: [HISTORY_LOG.md](HISTORY_LOG.md), [AGENTS.md](../../AGENTS.md), [URS_SRS_CHANGE_LOG.md](URS_SRS_CHANGE_LOG.md), [ACRONYMS.md](ACRONYMS.md)

This file collects the standing rules for how we work on the Tax Relief Manager (TRM) documents: how you give a prompt, how I answer, and what I must update. Every rule below came from your messages. When you give a new rule, I add it here and raise the version.

---

## 1. Rules for how I respond

| # | Rule | Source |
| --- | --- | --- |
| R-01 | For **every prompt** I **respond first** with what I understood and what I would change, and **change nothing** until you say "update" or "go ahead". (Widened on 18/11/2026; before, it covered only answering questions and making decisions.) | Prompts of 14/11/2026 00:05 and P-25 |
| R-02 | When you say "update", "please do it" or give a go-ahead after your answers, I apply all of it and tell you what changed. | Prompts P-14 to P-16 |
| R-03 | I give you **only the latest information you gave**. I add no extra information you did not ask for. | Prompt of 14/11/2026 00:20 |
| R-04 | I keep my replies short and in plain language. I say what changed, what is still open and what I read in my own way. | Working practice |
| R-05 | When your words can be read two ways, I choose the most reasonable reading, write it down as a flagged finding in HISTORY_LOG.md and ask you to correct it if it is wrong. | Working practice (F-051) |
| R-06 | I never present my own proposal as a decision. A value or rule that I proposed stays "proposed" until you approve it, and then I record the date. | Working practice (SD, OI, DA) |

## 2. Rules for files

| # | Rule | Source |
| --- | --- | --- |
| R-10 | **Update all the MD files** to control the version and quality of the documents. | Prompt P-13 |
| R-11 | **Only the MD files are updated. I do not update or regenerate any PDF.** I create a PDF only when you ask for it. | Prompt of 14/11/2026 00:05 |
| R-12 | Every change raises the document version and adds an entry to URS_SRS_CHANGE_LOG.md (what, before, after, why, which prompt). | Prompt P-13 |
| R-13 | HISTORY_LOG.md records every prompt (P-nn), finding (F-nn) and step of our work. | Prompt P-13 |
| R-14 | ACRONYMS.md lists every short form. I run the acronym check after each round of changes. | Working practice (F-034) |
| R-15 | After a change I run the build checks (references resolve, every URS in the matrix, every SRS has a URS, a flow and a test, shared blocks identical in all documents). The result must be 0 errors. | Working practice |
| R-16 | I tell you which MD files changed, with a one-line caption. Git keeps the copies now (from 18/11/2026), so I no longer need to send each file. | Working practice; updated in P-26 |

## 3. Rules for the PRD

| # | Rule | Source |
| --- | --- | --- |
| R-20 | The PRD (the Claude Doc "PRD: Malaysia Tax Relief System (PWA)") is changed **only when you tell me to update it**, and only for items you approved. | Prompts P-14 to P-16 |
| R-21 | Items waiting for your approval stay in the "Pending PRD sync" list of URS_SRS_CHANGE_LOG.md. | Working practice |
| R-22 | When the PRD is changed, I change the local PRD .md copy the same way, add a Synced entry (CHG) and note the new revision number. | CHG-044 |

## 4. Rules for the specification documents

| # | Rule | Source |
| --- | --- | --- |
| R-30 | The document set is F0 profile, F1 tax calculator, F2 relief categories, F3 spending records, F4 dashboard and F5 account and security. Each has a URS (what the user needs) and an SRS (how the system behaves). | Prompts P-08 to P-15 |
| R-31 | IDs: URS-Fn-nn, SRS-Fn-nn, FD (flow diagram), SQ (sequence), TC (test case), SD (specification decision), OI (open item), IF (interface), EV (event), DA (data addition). IDs are never reused. | Document conventions |
| R-32 | The shared blocks (conventions, interface table, ownership table, data additions, category codes) are identical in all six documents. | Build check |
| R-33 | Every SRS names its URS, its flow diagram (or "not drawn") and its test case. | Build check |
| R-34 | Tax figures and dates in tests are recomputed by script, not by hand. | Working practice |
| R-35 | Figures from LHDN or other sources are marked with their status (Announced, Gazetted, Confirmed). When a value is not printed yet, I say so and do not invent it. | Documents F1, F2 |
| R-36 | Money is stored as integer sen and shown as "RM 1,449.00". Dates are DD/MM/YYYY. | Document conventions |
| R-37 | The documents are in plain language, without bullet lists inside decisions where a table fits better. | Working practice |

## 4a. Rules for the repository

| # | Rule | Source |
| --- | --- | --- |
| R-40 | One repository carries the project from documentation to development to production. It is on GitHub (public): https://github.com/Juthyra/Tax-Relief-Manager-TRM-, since 18/11/2026. Changes reach `main` through pull requests. | Prompts P-18 and P-23; updated in P-26 |
| R-41 | Git is the master of the PRD from 14/11/2026. The Claude Doc is a copy (last synced at revision 47). | Prompt P-18 |
| R-42 | The built files in `docs/specs/` are never edited by hand. Edit `docs/tools/source/` or `docs/tools/shared.py` and build. | Repository design |
| R-43 | `AGENTS.md` holds the rules for any AI agent and any model. `CLAUDE.md` only points to it. There is no `.mcp.json`. | Prompt P-18 |
| R-44 | Language, framework, architecture, Docker, database and hosting are open decisions, tracked as `docs/decisions/ADR-001` to `ADR-005`. | Prompt P-18 |
| R-45 | Each phase (documentation, development, staging, production) has its own rules, written in `AGENTS.md` section 3. | Prompt P-18 |
| R-46 | No work on `main` on a local machine. Create a branch first: `docs/<ID>-short-name` (documentation only), `feature/<ID>-short-name` (development) or `bug-fixing/<ID>-short-name` (defect fixes). A branch does one kind of work. | Prompt P-19 |
| R-47 | Documentation has its own branch type, `docs/<ID>-short-name`. It is for documentation only, in Phase 1 and in each later phase, which is planned separately. | Prompt P-19 |
| R-48 | A commit message starts with the branch type, then the ID in brackets, then a short plain summary, and ends with the prompt (P-nn) or change (CHG-nn) number when there is one. Examples are in `AGENTS.md` section 5. | Prompt P-20 |
| R-49 | When a requirement change or a new requirement is done and the checks pass, the work is committed on its branch with a commit message and the branch is pushed, automatically, without waiting to be asked. Never push directly to `main`. After the push I open a pull request into `main` with `gh pr create` (template filled, AI agent named) and stop; **I never merge it**, you merge it (R-50). This applies only **after you have said "update"** (R-01); until then I change nothing. This replaces the earlier rule "commit or push only when asked". | Prompts P-21, P-26 and P-28 |
| R-50 | **Review before merge.** Every pull request into `main` is reviewed before it is merged. While you are the only person on the project, you may merge your own pull request without a review (owner bypass). When another developer joins, every pull request needs 1 approving review from someone other than its author; nobody approves or merges their own pull request, except you as owner, who may bypass it for your own. It is enforced on GitHub by R-51. | Prompts P-24 to P-26 and P-30 |
| R-51 | **`main` is protected.** The ruleset `protect-main` (active since 18/11/2026) blocks direct pushes, force pushes and deletion on `main`; every change goes through a pull request, which needs 1 approving review. The only bypass is the repository admin role (the owner), set to **pull requests only**: the owner can merge a pull request without the approval but cannot push straight to `main`. No required status check yet. I do not change this ruleset unless you say "update". | Prompts P-29 and P-30 |

## 5. Decisions you have already made (14/11/2026 and 22/11/2026)

| Topic | Decision | Recorded as |
| --- | --- | --- |
| Profile answers | Every visible profile question is mandatory. Marital status is a choice of status, not Yes or No. Until a year's profile is complete, F1 to F4 are locked for that year (hard gate). | SD-F0-14, DA-20 |
| Admin and passwords | An admin cannot change a taxpayer's email or password. The admin sends a temporary reset link. The taxpayer can change their own email. | SD-F5-10, SD-F5-18 |
| Phases | Phase 1 is the simple account, used only by you and the people you invite (22/11/2026). Sign-in lock, emailed links, staying signed in, two-factor and account deletion are held for Phase 2. Data export, deletion of old records, the security events screen, the new-device notice and the session controls are built with R3, phase 4 of the PRD roadmap (22/11/2026). | SD-F5-17, SD-F5-19, F-049 |
| Deletion | Records can be deleted only after 7 years from the end of the YA, and strictly never before. Deleting is optional, the taxpayer's own choice. The app shows a notice when a YA becomes deletable. | SD-F5-09 (confirmed 22/11/2026) |
| Later | Hosting, consent text and email service are decided during development. Where to store and share the documents is decided after the basic documents are complete. | OI-F5-01, OI-F5-02, OI-F5-06, F-035 |

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
| 0.2 | 2026-11-14 | Added the repository rules R-40 to R-45 (prompt P-18) |
| 0.3 | 2026-11-14 | Added the branch rules R-46 and R-47 (prompt P-19) |
| 0.4 | 2026-11-14 | Added the commit message rule R-48 with examples (prompt P-20) |
| 0.5 | 2026-11-14 | Added the automatic commit and push rule R-49 (prompt P-21) |
| 0.9 | 2026-11-22 | Section 5: Phase 1 only for the owner and invited people; export, deletion of old records and the security screens moved to R3; deletion strictly after 7 years and optional (prompt P-34, CHG-049) |
| 0.8 | 2026-11-18 | New R-51 (`main` protected by the ruleset `protect-main`, owner bypass for pull requests only); R-50 now enforced (prompts P-29 and P-30, CHG-048) |
| 0.7 | 2026-11-18 | R-49 extended: after the push I open a pull request with `gh` and never merge it (prompts P-27 and P-28, CHG-047) |
| 0.6 | 2026-11-18 | R-01 widened to every prompt; R-49 only after "update"; new R-50 (review before merge, owner bypass); R-16 and R-40 brought up to date (prompts P-24 to P-26, CHG-046) |
