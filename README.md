# Tax Relief Manager (TRM): Malaysia tax relief system (PWA)

TRM helps a Malaysian resident individual taxpayer plan and track income tax reliefs for each Year of Assessment (YA). This one repository carries the project from documentation to development to production.

Owner: Champs (product owner)

## Where things are

| Folder or file | What it holds | Phase |
| --- | --- | --- |
| `docs/prd/` | The product requirements (PRD). Git is the master from 14/11/2026 | Documentation |
| `docs/specs/` | URS and SRS for F0 profile, F1 tax calculator, F2 relief categories, F3 spending records, F4 dashboard, F5 account and security. These files are **built**; do not edit them by hand | Documentation |
| `docs/tools/` | `source/` (the files that are edited), the shared blocks and the build and check scripts | Documentation |
| `docs/registers/` | History log, change log, acronyms, working rules | Documentation |
| `docs/decisions/` | One decision record (ADR) per technical decision | All |
| `src/` | The application code. Empty until the technology is chosen | Development |
| `tests/` | Automated tests and the map from each test case (TC) to its test | Development |
| `infra/` | Environment set-up: `local`, `staging`, `production`. Empty until decided | Environments |
| `ops/` | Runbooks: backup, restore, incidents | Production |
| `exports/` | PDFs, only when the owner asks. Not committed | Documentation |

## Start here

1. Read `AGENTS.md` (the rules for people and AI agents) and `docs/registers/PROMPT_RULES.md`.
2. To change a specification, edit the file in `docs/tools/source/` (or `docs/tools/shared.py` for the shared blocks), then run:

```
python3 docs/tools/build.py
python3 docs/tools/changelog.py
python3 docs/tools/check_acronyms.py
```

The build must end with `ERRORS: 0`. Then update the change log entries and `docs/registers/HISTORY_LOG.md` as `AGENTS.md` says.

## Open technical decisions

Language, framework, architecture (monolith or microservices), Docker and database are not decided. They are tracked as `docs/decisions/ADR-001` to `ADR-005`.
