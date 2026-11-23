# ADR-005: Hosting

| Item | Value |
| --- | --- |
| Document ID | ADR-005 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.3 |
| Status | Proposed (held by the owner on 23/11/2026) |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (hosting) and section 9.3 decision 8 |
| Source | Owner prompts P-68 to P-71; stack choice of the owner on 23/11/2026 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner (held; decided later) |

## Question

Where is the data hosted, and what is the basis for any transfer outside Malaysia?

## Options

| Option | For | Against |
| --- | --- | --- |
| **A. Local machines only (now)** | No cost; no real data leaves the laptop; fits development with test data | Not a deployment |
| B. DigitalOcean | Simple to run; works for the owner's personal use in R1 (PRD section 7) | No Malaysian datacenter; the nearest is Singapore (SGP1, verified 28/10/2026 in the PRD), so a public launch needs a documented basis under the PDPA |
| C. AWS | Has a Malaysia region (ap-southeast-5, three availability zones, opened August 2024), which avoids the cross-border question at a public launch | More services to learn and run |
| D. A Malaysian provider | Not researched | Not researched |

Facts for B and C are from PRD section 7 and were not re-read for this record. Prices and terms are read from each provider's own pages when this decision starts.

## Decision and reason

Not decided. On 23/11/2026 (P-68) the owner said the work is done on a local machine for development, the next environment is thought about later, and no provider is chosen yet. Until then the only environment is local, with test data (AGENTS.md section 3).

## Effect on the specifications

Same question as OI-F5-01. A PDPA adviser's input is needed before the public launch. Staging and production rules in AGENTS.md section 3 apply when those environments exist.
