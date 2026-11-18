# Rules for people and AI agents (any tool, any model)

This file is the single source of rules. `CLAUDE.md` and other tool files only point here. Full detail: `docs/registers/PROMPT_RULES.md`.

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
3. Add the prompt, findings and steps to `docs/registers/HISTORY_LOG.md`.
4. List any new short form in `docs/registers/ACRONYMS.md`.
5. Run the build and the acronym check. Both must pass.
6. If the PRD must change, change it only when the owner says to, and add a Synced entry to the change log.

## 3. Rules by phase and environment

| Phase | Where | Rules |
| --- | --- | --- |
| Documentation | `docs/` | Markdown only; version raised; change log updated; build 0 errors |
| Development | `src/`, `tests/` | Every code change names its requirement ID (for example SRS-F1-04); every test case TC has an automated test or a recorded reason; test data only |
| Staging | `infra/staging` | Same build as production; test data only; rehearse the held Phase 2 features of F5 here |
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
| Documentation | `docs/<ID>-short-name` | Documentation work only: PRD, URS/SRS, registers, ADRs, rules. `<ID>` is the document (F0 to F5, PRD) or the change number (CHG-046). No code in a docs branch. This covers Phase 1 documentation and each later phase's documentation, planned separately per phase. |
| Feature | `feature/<ID>-short-name` | New development work. `<ID>` is the requirement ID (for example SRS-F1-04). |
| Bug fixing | `bug-fixing/<ID>-short-name` | Fixing a defect. `<ID>` is the bug or finding number (for example F-054) or the requirement ID. |
| Decision | `decision/<topic>` | An ADR or open decision. |

- A branch does one kind of work. Documentation and code are not mixed in one branch.
- Commit messages start with the branch type, then the ID in brackets, then a short summary in plain language. Add the prompt (P-nn) or change (CHG-nn) number at the end when there is one. Examples:
  - `docs(F5): split sign-in rules into Phase 1 and Phase 2 (CHG-046, P-19)`
  - `docs(PRD): sync admin support paragraph (CHG-044)`
  - `feature(SRS-F1-04): calculate chargeable income from total income and reliefs`
  - `bug-fixing(F-054): fix wrong YA shown on the dashboard`
  - `decision(ADR-001): choose the language and framework`
- Pull requests need the template filled and the checks green.
- **Review before merge.** Every pull request into `main` is reviewed before it is merged.
  - **While the owner is the only person on the project:** the owner may merge their own pull request without a review (owner bypass). The owner reads it before merging.
  - **When another developer joins:** every pull request needs **1 approving review from someone other than its author**. Nobody approves or merges their own pull request, except the owner, who may bypass this for their own.
  - **Enforced on GitHub since 18/11/2026** by the ruleset `protect-main` on `main`: no direct push, no force push, no deletion; changes only by pull request with 1 approval. Only the repository owner may bypass, and only **for pull requests** (the owner merges a pull request without the approval, but cannot push straight to `main`). The owner changes the ruleset in GitHub: Settings, Rules, Rulesets.
- **Automatic commit and push.** After the owner has said "update", every time a requirement change or a new requirement is done and the checks pass, commit it on the working branch with a commit message (format above) and push that branch. Do not wait to be asked again. Then open a pull request into `main` with `gh pr create` (template filled, AI agent named) and stop. **An AI agent never merges a pull request**; the owner merges it (see Review before merge). Never push directly to `main`.
- `main` changes only through a merged pull request. Tag approved sets (`docs-v0.5`).
