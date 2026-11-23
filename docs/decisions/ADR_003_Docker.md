# ADR-003: Docker

| Item | Value |
| --- | --- |
| Document ID | ADR-003 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 1.0 |
| Status | Approved on 23/11/2026 (Sail or our own compose file stays open until the project is created) |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (technology direction: portable parts, containers) |
| Source | Owner prompts P-68 to P-78; stack choice of the owner on 23/11/2026 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner: Docker only for development (23/11/2026, P-72 to P-75); approved as a record 23/11/2026 (P-77, P-78); Sail or our own file not decided |

## Question

Are environments built with containers?

## Options

| Option | For | Against |
| --- | --- | --- |
| **A. Laravel Sail** (Laravel's own Docker environment) | Fast to start; one command; the same setup for both developers | Sail is for local development only; I did not confirm that its containers run as a non-root user and use pinned image tags, which this project's rules require. This is checked when the project is created |
| B. Our own `compose.yaml` (PHP, PostgreSQL, front-end build, mail catcher) | Full control of versions, users and healthchecks | More to write and keep |
| ~~C. No containers (PHP and PostgreSQL installed on each laptop)~~ | | **Removed by the owner on 23/11/2026** |

## Decision and reason

**Decided by the owner on 23/11/2026 (P-72 to P-75): 100% on Docker for development. The record and its rules are approved (P-77, P-78).** No PHP, Composer, Node or PostgreSQL is installed on a laptop. Every command runs in a container: `composer`, `artisan`, `npm` or `vite`, the tests and the database. Only Docker and Git are needed on a laptop. The document tools (the Python scripts that build the documents, the change log and the checks) are included in this decision.

**Not decided:** Sail (option A) or our own `compose.yaml` (option B). The owner asked to keep talking about the stack and not start the project yet (P-73), so this is decided when the project is created, by checking Sail against the rules below. If Sail fails one, option B is used.

**Later, when the project is created (not now):** a small container for the document tools (a pinned Python image, a non-root user, one command that runs the build and the four checks) and a change to how the `docs-check` workflow runs. The documents build the same way meanwhile.

| Rule | Reason |
| --- | --- |
| Pinned image tags, never `latest` | The same build on both laptops, in CI and later in staging and production |
| Containers run as a non-root user | Least privilege |
| The PHP and Node versions come from the images, not from a laptop ([ADR-001](ADR_001_Language_And_Framework.md)) | Both laptops and CI run the same versions |
| Services: application, PostgreSQL ([ADR-004](ADR_004_Database.md)), front-end build (Node only builds; it does not run on the server, [ADR-001](ADR_001_Language_And_Framework.md)), and a mail catcher so no real email is sent ([ADR-006](ADR_006_Email_Service.md)) | Matches the stack |
| Health checks on the application and the database | A broken start is seen at once |
| Test data only; no real tax or personal data in any container | AGENTS.md sections 1 and 3 |
| Production images, Kubernetes or another runtime | Not decided here; decided with [ADR-005](ADR_005_Hosting.md). Kubernetes manifests, if used, need probes, resource requests and limits, and a non-root security context |

**What Docker-only costs, to check when the project is created:**

| Point | Effect | Plan |
| --- | --- | --- |
| Speed on a Mac | Mounting the project folder into a container can be slow, especially `vendor` and `node_modules` | Keep both in container volumes, not on the laptop disk; measure the speed first |
| Editor | The editor cannot see `vendor` or `node_modules`, so type hints and go-to-definition may fail | The editor's dev-container mode, or copy the dependencies out; depends on the editor |
| Browser tests | The tax engine tests run in Node, which is fine; tests that drive a real browser need a browser in a container | A test container with its own browser, when those tests are written |
| Hot reload | The Vite dev server must be reachable from the laptop's browser | A published port in the compose file |

## Effect on the specifications

Affects `infra/` and the rules for staging and production in AGENTS.md section 3. No SRS changes.
