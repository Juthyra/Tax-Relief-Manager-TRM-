# ADR-002: Monolith or microservices

| Item | Value |
| --- | --- |
| Document ID | ADR-002 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.2 |
| Status | Proposed |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (non-functional and PWA requirements) |
| Source | Owner prompt P-18 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner (not decided yet) |

## Question

Is the application one deployable unit with a module per feature (F0 to F5), or separate services? The answer may depend on ADR-001.

## Options

| Option | For | Against |
| --- | --- | --- |
| To be filled when the owner starts this decision | | |

## Decision and reason

Not decided. The owner said on 14/11/2026 that this is not decided yet.

## Effect on the specifications

The interfaces IF-01 to IF-21 and events EV-01 to EV-08 are the module or service boundaries.
