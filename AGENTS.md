# Rules for people and AI agents (any tool, any model)

This file is the single source of rules. `CLAUDE.md` and other tool files only point here. Full detail: `docs/registers/PROMPT_RULES.md`.

## 1. How to work

1. **The owner (Champs) decides.** When he is answering questions or making decisions, respond first and change nothing until he says to update.
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
- **Automatic commit and push.** Every time a requirement change or a new requirement is done and the checks pass, commit it on the working branch with a commit message (format above) and push that branch. Do not wait to be asked. Never push directly to `main`. Until the GitHub remote exists, commit locally and push once it is set.
- Until the repository is on GitHub, merge to `main` locally only after the checks pass, and tag approved sets (`docs-v0.5`).
