# Rules for people and AI agents (any tool, any model)

This file is the single source of rules. `CLAUDE.md` and other tool files only point here. Full detail: `docs/registers/REG_04_Prompt_Rules.md`.

## 1. How to work

1. **The owner (Champs) decides. Information first.** For every prompt, respond first with what you understood and what you would change, and change nothing until the owner says "update" or "go ahead".
2. **Never present your own proposal as a decision.** Mark it "proposed" until the owner approves, then record the date.
3. **Plain language.** Short replies. Say what changed, what is open and what you read in your own way.
4. **Documents are Markdown.** Do not create or regenerate PDFs unless the owner asks.
5. **Never edit built files** in `docs/specs/`. Edit `docs/tools/source/` or `docs/tools/shared.py`, then build.
6. **No real tax data, no secrets, no personal data** in the repository. Tests use test families such as Aisyah.
7. **Do not invent tax figures or dates.** Use the status Announced, Gazetted or Confirmed and the source. Recompute test values by script.

## 2. After every change to the documents

1. Raise the document version in its header.
2. Add an entry to `docs/tools/changelog.py` (what, before, after, why, which prompt) and run it.
3. Add the prompt, findings and steps to `docs/registers/REG_01_History_Log.md`.
4. List any new short form in `docs/registers/REG_03_Acronyms.md`.
5. Run the build, the acronym check and the document standard check (section 6). All must pass.
6. If the PRD must change, change it only when the owner says to, and add a Synced entry to the change log.

## 3. Rules by stage and environment

A stage is where the work happens. It is not a phase: "phase" means only a phase of the PRD roadmap (section 6).

| Stage | Where | Rules |
| --- | --- | --- |
| Documentation | `docs/` | Markdown only; version raised; change log updated; build 0 errors |
| Development | `src/`, `tests/` | Every code change names its requirement ID (for example SRS-F1-04); every test case TC has an automated test or a recorded reason; test data only |
| Staging | `infra/staging` | Same build as production; test data only; rehearse the held launch account features of F5 here |
| Production | `infra/production` | Tagged release only; secrets outside Git; backups and the 35-day purge (SD-F5-08); PDPA items OI-F5-01 to OI-F5-04 closed before public launch |

## 4. AI agents and MCP servers

- Any agent may be used, with any model. The rules above apply to all.
- Approved MCP servers: none are required. Add each approved server here with its purpose.
- Forbidden: any server or tool that can reach production data or secrets; any tool that sends tax data to a third party.
- Keys and tokens belong to each person and are never committed.
- Say in the pull request when an AI agent wrote the change. A human reviews it.

## 5. Git

**Never work on `main` on your local machine.** Always create a branch first. `main` changes only through a reviewed merge.

| Branch | Name | Use |
| --- | --- | --- |
| Documentation | `docs/<ID>-short-name` | Documentation work only: PRD, URS/SRS, registers, ADRs, rules. `<ID>` is the document (F0 to F5, PRD) or the change number (CHG-046). No code in a docs branch. This covers the documentation of PRD phase 1 and of each later PRD phase, planned separately per phase. |
| Feature | `feature/<ID>-short-name` | New development work. `<ID>` is the requirement ID (for example SRS-F1-04). |
| Bug fixing | `bug-fixing/<ID>-short-name` | Fixing a defect. `<ID>` is the bug or finding number (for example F-054) or the requirement ID. |
| Decision | `decision/<topic>` | An ADR or open decision. |

- A branch does one kind of work. Documentation and code are not mixed in one branch.
- Commit messages start with the branch type, then the ID in brackets, then a short summary in plain language. Add the prompt (P-nn) or change (CHG-nn) number at the end when there is one. Examples:
  - `docs(F5): split sign-in rules into the basic account and the launch account (CHG-046, P-19)`
  - `docs(PRD): sync admin support paragraph (CHG-044)`
  - `feature(SRS-F1-04): calculate chargeable income from total income and reliefs`
  - `bug-fixing(F-054): fix wrong YA shown on the dashboard`
  - `decision(ADR-001): choose the language and framework`
- Pull requests need the template filled and the checks green.
- **Review before merge.** Every pull request into `main` is reviewed before it is merged.
  - **While the owner is the only person on the project:** the owner may merge their own pull request without a review (owner bypass). The owner reads it before merging.
  - **When another developer joins:** every pull request needs **1 approving review from someone other than its author**. Nobody approves or merges their own pull request, except the owner, who may bypass this for their own.
  - **Enforced on GitHub since 18/11/2026** by the ruleset `protect-main` on `main`: no direct push, no force push, no deletion; changes only by pull request with 1 approval. Only the repository owner may bypass, and only **for pull requests** (the owner merges a pull request without the approval, but cannot push straight to `main`). The owner changes the ruleset in GitHub: Settings, Rules, Rulesets.
- **Review requests.** `.github/CODEOWNERS` names the code owners for every path (`*`). GitHub asks them for a review on every new pull request and sends them a notification. When a developer joins, the owner adds their GitHub username to CODEOWNERS. GitHub never notifies the author of a pull request, so a pull request that an agent opens under the owner's account appears in the owner's Pull requests list, not as a notification.
- **Automatic commit and push.** After the owner has said "update", every time a requirement change or a new requirement is done and the checks pass, commit it on the working branch with a commit message (format above) and push that branch. Do not wait to be asked again. Then open a pull request into `main` with `gh pr create` (template filled, AI agent named) and stop. **An AI agent never merges a pull request**; the owner merges it (see Review before merge). Never push directly to `main`.
- `main` changes only through a merged pull request. Tag approved sets (`docs-v0.5`).

## 6. Document standard (from 23/11/2026)

Every document follows the same names and the same header, so each one can be found and tracked during development. Full rules: RULE-53 to RULE-59 in `docs/registers/REG_04_Prompt_Rules.md`.

1. **The PRD is the master.** Feature IDs and names (F1 to F4 follow PRD sections 3.1 to 3.4), requirement IDs (FR, BR, NFR), releases (R1 to R4) and phases come from the PRD (`PRD-TRM`). When another document disagrees with the PRD, the PRD wins: change the other document, or, when the PRD looks wrong, write a finding and a Pending PRD sync item and wait for the owner.
2. **File names:** `<type>_<ID>_<Short_Name>.md`, with underscores and each word of the short name starting with a capital.

   | Type | ID | Example | Document ID |
   | --- | --- | --- | --- |
   | `PRD` | `TRM` (one PRD) | `PRD_TRM_Malaysia_Tax_Relief_System.md` | PRD-TRM |
   | `URS_SRS` | `F0` to `F5` | `URS_SRS_F1_Tax_Calculator.md` | URS-SRS-F1 |
   | `ADR` | `001`, `002` ... | `ADR_001_Language_And_Framework.md` | ADR-001 |
   | `RES` (research note) | `001`, `002` ... | `RES_001_Frontend_Frameworks.md` | RES-001 |
   | `REG` (register) | `01` to `04` | `REG_01_History_Log.md` | REG-01 |

   Kept as they are, because tools need these names: `README.md`, `AGENTS.md`, `CLAUDE.md`, `.github/`, and the build inputs `docs/tools/source/f0.md` to `f5.md` (built into `URS_SRS_F0` to `F5`).
3. **Title:** the first line is `# <Document ID>: <Title>`. A feature title uses the PRD heading.
4. **Header table** right under the title, rows in this order: Document ID, Document type, Product, Version, Status, Date, Owner, PRD reference, Source, Change tracking. Extra rows (for example Decided by, Scope) come after them.
   - Version: the PRD counts revisions (Revision 48); other documents use 0.1, 0.2 while draft and 1.0 when the owner approves; a log says it is a running log.
   - Status: Draft, Proposed, Approved, Active (a living register or the PRD) or Superseded.
   - Date: YYYY-MM-DD of the last change, with the first date in brackets. Dates shown in the product stay DD/MM/YYYY.
5. **Terms:**

   | Term | Means only | Not |
   | --- | --- | --- |
   | Phase 0 to 5 | A phase of the PRD roadmap, section 9.1 (phase 1 = R1 build, 4 = R3) | F5 parts, stages |
   | R1 to R4 | A release (PRD section 9.1) | R01 to R24, relief category codes (two digits) |
   | Stage | Documentation, development, staging, production (section 3) | A phase |
   | Basic account | The part of F5 built in R1 (SD-F5-17); called Phase 1 until 23/11/2026 | |
   | Launch account | The part of F5 held until before the public launch; called Phase 2 until 23/11/2026 | |
   | RULE-nn | A working rule in REG-04 (was R-nn) | |
   | RES-nnn | A research note (was R-001) | |
6. **Waiting items are marked.** Anything not approved by the owner says "Proposed". A PRD change that waits for approval stays in Pending PRD sync (REG-02) with the status "Waiting for owner approval", and the PRD lists it in section 9.4. Approved items record the date.
7. **Check:** `python3 docs/tools/check_standard.py` checks file names, titles and header rows. It runs in the `docs-check` workflow with the build.
8. **Renamed on 23/11/2026** (old name, new name): `PRD_Malaysia_Tax_Relief_System_PWA.md`, `PRD_TRM_Malaysia_Tax_Relief_System.md`; `HISTORY_LOG.md`, `REG_01_History_Log.md`; `URS_SRS_CHANGE_LOG.md`, `REG_02_URS_SRS_Change_Log.md`; `ACRONYMS.md`, `REG_03_Acronyms.md`; `PROMPT_RULES.md`, `REG_04_Prompt_Rules.md`; `ADR-001-language-and-framework.md` (and ADR-000 to ADR-005 the same way), `ADR_001_Language_And_Framework.md`; `R-001-frontend-frameworks.md`, `RES_001_Frontend_Frameworks.md`. Older log entries use the new names.
