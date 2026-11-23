# ADR-004: Database

| Item | Value |
| --- | --- |
| Document ID | ADR-004 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.2 |
| Status | Proposed |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM sections 5 (data model) and 7 (hosting note: PostgreSQL) |
| Source | Owner prompt P-18 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner (not decided yet) |

## Question

Which database holds the data model (PRD section 5, DA-01 to DA-24), including versioned rows and hard deletes for the erase (SRS-F5-21)?

## Options

| Option | For | Against |
| --- | --- | --- |
| To be filled when the owner starts this decision | | |

## Decision and reason

Not decided. The owner said on 14/11/2026 that this is not decided yet.

## Effect on the specifications

Versioned rows (version_no, is_current) and the erase of one YA must be supported.
