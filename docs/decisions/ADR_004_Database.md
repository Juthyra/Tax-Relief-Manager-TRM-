# ADR-004: Database

| Item | Value |
| --- | --- |
| Document ID | ADR-004 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 1.0 |
| Status | Approved on 23/11/2026 |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 5 (data model) and section 7 |
| Source | Owner prompts P-68 to P-78; stack choice of the owner on 23/11/2026 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner, 23/11/2026 (P-77, P-78) |

## Question

Which database holds the data model (PRD section 5, DA-01 to DA-27), including versioned rows and hard deletes for the erase (SRS-F5-21)?

## Options

| Option | For | Against |
| --- | --- | --- |
| **A. PostgreSQL (the owner's choice)** | Real `uuid`, `jsonb`, partial unique indexes and check constraints, which fit the design below; supported by Laravel | One more service to run locally (a container, [ADR-003](ADR_003_Docker.md)) |
| B. MySQL or MariaDB | Common with Laravel | Not the owner's choice; weaker constraints for the one-current-row rule |
| C. SQLite | No server | Not for this data, and tests must run on the same database as production |

## Facts checked on 23/11/2026

| Item | Fact | Source |
| --- | --- | --- |
| PostgreSQL 19 | Released 19/11/2026, four days before this record | [PostgreSQL versioning policy](https://www.postgresql.org/support/versioning/) |
| PostgreSQL 18 | Current minor 18.7; supported until 14/11/2030 | same |
| PostgreSQL 17 | Supported until 08/11/2029 | same |
| Laravel | Lists PostgreSQL 10.0 or later as supported, so no limit comes from Laravel | [Laravel 13 database](https://laravel.com/docs/13.x/database) |

## Decision and reason

PostgreSQL is the owner's choice (P-69). **Approved by the owner on 23/11/2026 (P-77, P-78)** for PostgreSQL 18 and the design points below:

| # | Proposal | Reason |
| --- | --- | --- |
| 1 | **PostgreSQL 18**, not 19 | 19 is four days old and 18 is supported until 2030; move up later when 19 has had its first minor releases |
| 2 | Money as integer sen (`bigint`) | Convention in every specification; no rounding errors |
| 3 | Primary keys are `uuid`; records created on the device carry a UUID v7 made there (DA-02); the server accepts only a valid UUID v7 for those tables | Offline sync without duplicates |
| 4 | Versioned entities: a partial unique index on the entity's key where `is_current` is true, so only one current row exists. Example: IncomeRecord by user, year, month and type | The database enforces the versioned-row rule |
| 5 | Rule conditions (`eligibility_rule`, tiers) as `jsonb` next to the readable text | DA-04, DA-05, DA-25 |
| 6 | Hard delete for the erase and for a YA past its 7 years, with foreign keys and a deletion order planned per entity | SRS-F1-24, SRS-F3-18, SRS-F0-19 |
| 7 | Dates as `date`, times in UTC | One clear rule |
| 8 | Tests run on PostgreSQL, not SQLite | The behaviour of the indexes and constraints must match |
| 9 | Migrations are Laravel migrations in the repository | Reviewable and repeatable |

## Effect on the specifications

Versioned rows (version_no, is_current) and the erase of one YA must be supported; both are possible. No SRS changes.
