# ADR-001: Language and framework

| Item | Value |
| --- | --- |
| Document ID | ADR-001 |
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

Which language and framework build the application (offline-first PWA, sync, tax calculation)?

## Options

| Option | For | Against |
| --- | --- | --- |
| To be filled when the owner starts this decision | | |

Front-end findings (Blade, Livewire, Vue 3, React, Angular, Svelte, with Laravel): [RES-001](research/RES_001_Frontend_Frameworks.md). These are findings, not a decision.

## Decision and reason

Not decided. The owner said on 14/11/2026 that this is not decided yet.

## Effect on the specifications

Offline sync and money as integer sen (conventions in every spec) must hold in any choice.
