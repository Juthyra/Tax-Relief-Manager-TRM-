# ADR-001: Language and framework

| Item | Value |
| --- | --- |
| Document ID | ADR-001 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.3 |
| Status | Proposed (the owner's stack is recorded; the offline approach is open) |
| Date | 2026-11-23 (first written 2026-11-14) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (non-functional and PWA requirements) |
| Source | Owner prompts P-68 to P-71; stack choice of the owner on 23/11/2026 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner stated the stack on 23/11/2026; this record stays Proposed until the owner approves it |

## Question

Which language and framework build the application (offline-first PWA, sync, tax calculation)?

## What the owner stated (23/11/2026, P-68)

| Layer | Choice |
| --- | --- |
| Front end | Vue 3, Inertia, TypeScript |
| Back end | Laravel (PHP) |
| Database | PostgreSQL ([ADR-004](ADR_004_Database.md)) |
| Team | The owner and one other developer |
| Environment | Local machine for development; the later environments are decided later ([ADR-005](ADR_005_Hosting.md)) |

## Options

Front-end findings (Blade, Livewire, Vue 3, React, Angular, Svelte, with Laravel): [RES-001](research/RES_001_Frontend_Frameworks.md). These are findings, not a decision.

| Option | For | Against |
| --- | --- | --- |
| **A. Laravel + Inertia + Vue 3 + TypeScript (the owner's choice)** | One codebase for routes, sign-in, validation and policies in Laravel; Vue gives a smooth app and a good base for an offline PWA; the official Laravel starter kit for Vue uses Inertia and TypeScript | Two languages (PHP and TypeScript); Inertia loads each page from the server, so offline needs its own design (open item below) |
| B. TypeScript end to end (Node server and Vue) | One language | Sign-in, validation and admin need more assembly than in Laravel; not the owner's choice |
| C. Laravel API and a separate Vue PWA, without Inertia | Clean split between server and app | Two codebases and a full API for two developers; gives up Inertia |
| D. Blade or Livewire | Simplest for forms | Every interaction needs the server, so offline use and the live calculator are weak (RES-001) |

## Facts checked on 23/11/2026

| Item | Fact | Source |
| --- | --- | --- |
| Laravel | Laravel 13, released 17/03/2026; needs PHP 8.3 to 8.5; bug fixes until Q3 2027, security fixes until 17/03/2028. Laravel 12: bug fixes ended 13/08/2026, security fixes until 24/02/2027 | [Laravel 13 release notes](https://laravel.com/docs/13.x/releases) |
| PHP | 8.5 (released 20/11/2025): active support until 31/12/2027, security until 31/12/2029. 8.6 was released on 19/11/2026 but is outside the range Laravel 13 lists | [PHP supported versions](https://www.php.net/supported-versions.php) |
| Vue | The latest Vue 3 release read was 3.5.46 | [Vue core releases](https://github.com/vuejs/core/releases/latest) |
| Inertia | Version 3 is current and the default in the documentation; version 2 is the legacy line. The 12.x Laravel notes say its starter kits use Inertia 2. Which version the Laravel 13 Vue starter kit installs was not confirmed | [Inertia upgrade guide](https://inertiajs.com/docs/v3/getting-started/upgrade-guide) |
| Node | Used only to build the front end. Node 26 and 24 are LTS; 22 is in maintenance | [Node.js releases](https://nodejs.org/en/about/previous-releases) |

## Decision and reason

Proposed, not approved by the owner yet. The proposals below follow the owner's stack and answers.

| # | Proposal | Reason | Date and source |
| --- | --- | --- | --- |
| 1 | Laravel 13 on PHP 8.5; Vue 3.5; Inertia (version 3 unless the starter kit needs 2, to be checked when the project is created); TypeScript in strict mode; Node 26 LTS for the build | Newest Laravel line with the longest support; versions are pinned in the lock files and the container images | Owner 23/11/2026 (stack); versions are my proposal |
| 2 | **The tax engine is one pure TypeScript function that runs only in the browser.** The server stores and processes data, applies access rules and never calculates tax | One engine, one set of tests. A second engine in PHP could disagree with the first, and a wrong tax figure is the worst fault this product can have | **Owner 23/11/2026 (P-69, P-70)** |
| 3 | The rule publish gate runs the calculator tests in the admin's browser; the server stores the passing run with a hash of the draft rows and accepts Publish only for that hash; the same tests run in CI before each deploy (SD-F2-10, DA-27) | The server has no engine to run them. Risk accepted: the server cannot re-check the result; only an admin can publish, and in R1 the admins are the two developers | **Owner 23/11/2026 (P-70, option A)** |
| 4 | The browser makes the month-end snapshot at the first visit after month-end; nothing is compared with a server figure after sync (SRS-F1-19, SRS-F4-10) | The server cannot calculate. A month with no visit gets no snapshot | **Owner 23/11/2026 (P-70)** |
| 5 | **Offline is built later.** The build is online-first for local development; the offline approach is an open item (OI-F1-05). Offline is still required: phase 1 cannot exit without it (PRD section 9.1) | The owner asked to decide it when the build is ready (P-69) | **Owner 23/11/2026 (P-69)** |
| 6 | From the start, hold three rules so offline can be added without rewriting screens: (a) records get their ids on the device (UUID v7, DA-02); (b) the engine is a package with no Vue, no browser and no server calls; (c) every save goes through one data layer | These are cheap now and expensive to add later | Proposed |

**Offline approaches recorded for the later decision (nothing decided):**

| Approach | How | Trade-off |
| --- | --- | --- |
| Hybrid | Inertia for online screens (sign-in, Settings, admin, rules manager). Income, spending, calculator and dashboard read and write a device store and sync through Laravel JSON endpoints | Fits the offline rules; two ways of loading data in one app |
| Service worker over Inertia pages | One pattern | Offline writes and sync are awkward; the 200 ms offline rule (NFR-5) is not shown to hold |
| Separate Vue PWA on a Laravel API | Clean split | Gives up Inertia (option C) |

## Effect on the specifications

- SD-F1-11, SD-F2-10, DA-27, OI-F1-05 and the changes to SRS-F1-19, SRS-F2-11 and SRS-F4-10 are in the documents of 23/11/2026 (CHG-062).
- PRD section 7 ("suggested technology direction") says the same engine should also run on the server for verification. This decision differs; it waits in Pending PRD sync item 29 and the PRD is not changed.
- Offline sync and money as integer sen (conventions in every spec) hold in any choice.
