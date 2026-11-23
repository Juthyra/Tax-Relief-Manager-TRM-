# ADR-003: Docker

| Item | Value |
| --- | --- |
| Document ID | ADR-003 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.3 |
| Status | Proposed |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (technology direction: portable parts, containers) |
| Source | Owner prompts P-68 to P-71; stack choice of the owner on 23/11/2026 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner (not decided yet; proposal below) |

## Question

Are environments built with containers?

## Options

| Option | For | Against |
| --- | --- | --- |
| **A. Laravel Sail** (Laravel's own Docker environment) | Fast to start; one command; the same setup for both developers | Sail is for local development only; I did not confirm that its containers run as a non-root user and use pinned image tags, which this project's rules require. This is checked when the project is created |
| B. Our own `compose.yaml` (PHP, PostgreSQL, front-end build, mail catcher) | Full control of versions, users and healthchecks | More to write and keep |
| C. No containers (PHP and PostgreSQL installed on each laptop) | No Docker | Two laptops drift apart; no path to the later environments |

## Decision and reason

Proposed: **containers for local development, starting with option A**, and moving to option B if Sail cannot meet the rules below. The owner has not decided yet. The owner said local development comes first and the later environments are decided later.

| Rule | Reason |
| --- | --- |
| Pinned image tags, never `latest` | The same build on both laptops and later in staging and production |
| Containers run as a non-root user | Least privilege |
| Services: application, PostgreSQL ([ADR-004](ADR_004_Database.md)), front-end build (Node only builds; it does not run on the server, [ADR-001](ADR_001_Language_And_Framework.md)), and a mail catcher so no real email is sent ([ADR-006](ADR_006_Email_Service.md)) | Matches the stack |
| Health checks on the application and the database | A broken start is seen at once |
| Test data only; no real tax or personal data in any container | AGENTS.md sections 1 and 3 |
| Production images, Kubernetes or another runtime | Not decided here; decided with [ADR-005](ADR_005_Hosting.md). Kubernetes manifests, if used, need probes, resource requests and limits, and a non-root security context |

## Effect on the specifications

Affects `infra/` and the rules for staging and production in AGENTS.md section 3. No SRS changes.
