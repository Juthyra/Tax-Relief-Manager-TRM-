# ADR-002: Architecture

| Item | Value |
| --- | --- |
| Document ID | ADR-002 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 1.0 |
| Status | Approved on 23/11/2026 |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (non-functional and PWA requirements); section 3 (features F0 to F5) |
| Source | Owner prompts P-68 to P-78; stack choice of the owner on 23/11/2026 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner, 23/11/2026 (P-77, P-78) |

## Question

Is the application one deployable unit with a module per feature (F0 to F5), or separate services? The answer depends on [ADR-001](ADR_001_Language_And_Framework.md).

## Options

| Option | For | Against |
| --- | --- | --- |
| **A. Modular monolith: one Laravel application, one module per feature** | One deploy, one database, simple for two developers; module boundaries follow the interfaces IF-01 to IF-21, so a module can be split out later if ever needed | Boundaries are kept by discipline and checks, not by the network |
| B. Separate services per feature | Hard boundaries | Many deploys, network calls between features and no transaction across them; far too heavy for two developers |
| C. Laravel API and a separate front-end app | Clean split | Two codebases; not the owner's stack choice (ADR-001 option C) |

## Decision and reason

**Approved by the owner on 23/11/2026 (P-77, P-78): option A**, a modular monolith. The module names are a starting point and can change by a new version of this record.

| Part | Proposal |
| --- | --- |
| Modules on the server | One folder per feature: Profile (F0), Calculator data (F1: income, estimates, filed status), Rules (F2), Spending (F3), Dashboard (F4), Account (F5). The names are mine and can change |
| Calls between modules | Only through each module's public interface (the IF-nn in the specifications). A module never reads another module's tables directly. Events EV-01 to EV-08 are Laravel events |
| In the browser | One folder per feature in the same way, and the tax engine as its own package with no Vue and no server calls ([ADR-001](ADR_001_Language_And_Framework.md), decision 2) |
| The server's role | Stores and processes data: sign-in, access rules, validation, storage, files, rule publishing. It does not calculate tax |
| Checks | An automated test or lint rule that fails when a module reaches into another's tables or internals, so the boundaries hold. The tool is chosen when the project is created |

## Effect on the specifications

The interfaces IF-01 to IF-21 and events EV-01 to EV-08 are the module boundaries. The interfaces that the specifications describe as calls inside the browser stay inside the browser; the ones that cross to the server become Laravel routes.
