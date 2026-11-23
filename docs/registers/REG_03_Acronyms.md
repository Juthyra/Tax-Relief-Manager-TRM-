# REG-03: Acronym register

| Item | Value |
| --- | --- |
| Document ID | REG-03 |
| Document type | Register (acronyms, ID prefixes and code values) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | Running register; changes are listed in the Acronym change log at the bottom |
| Status | Active |
| Date | 2026-11-23 (started 2026-11-13) |
| Owner | Champs (product owner) |
| PRD reference | All of PRD-TRM |
| Source | A scan of every document; checked by docs/tools/check_acronyms.py |
| Change tracking | [REG_01_History_Log.md](REG_01_History_Log.md) (main log), [REG_02_URS_SRS_Change_Log.md](REG_02_URS_SRS_Change_Log.md) (detail log for the documents) |
| Last updated | 2026-11-23 (LTS and UTC added, CHG-061); 2026-11-23 (RULE, RES, REG prefixes and document IDs, CHG-051); 2026-11-18 (CLI added) |

This file lists every acronym and abbreviation used in the PRD, the six URS and SRS documents and the two logs. It is the single place to look up what a short form means.

## How this file works

1. **When to update.** Whenever a document uses a new acronym, or an acronym changes its meaning, this file is updated in the same piece of work. The change is also noted in the Acronym change log at the bottom, and in the process log of REG_01_History_Log.md.
2. **One row per short form.** If one short form has two meanings, it gets two rows and is also listed in section 6 (Collisions), so readers know to check the context.
3. **Nothing is deleted.** A short form that is no longer used stays in the table with status Retired.
4. **Automatic check.** The script `src/check_acronyms.py` scans all documents for capital-letter short forms and fails if one is not listed here. Run it before finishing any change.
5. **Status:** Active (used now), Retired (no longer used), Proposed (used in a draft, waiting for owner confirmation).

Counts: 75 acronyms (sections 1 to 3), 25 ID prefixes (section 4), 21 code values (section 5), 7 collisions (section 6).

## 1. Malaysian tax and government terms

| Short form | Stands for | Meaning in this project | Used in | Status |
| --- | --- | --- | --- | --- |
| CP38 | Form CP38 | LHDN's instruction to an employer to deduct extra tax instalments; not part of PCB paid so far | RES-003, REG-01 | Active |
| CP39 | Form CP39 | The employer's monthly PCB remittance; the PCB schedule is electronic through e-CP39 | RES-003 | Active |
| TP3 | Form TP3 | The form a new employee gives with pay and PCB from an earlier employer in the same year | RES-003, REG-01 | Active |
| LINDUNG 24, LINDUNG KENDIRI | SOCSO scheme names (not short forms) | LINDUNG 24 is the non-employment injury scheme; LINDUNG KENDIRI is the self-employment social security scheme. Both count in the SOCSO relief from YA 2027 | RES-002 | Active |
| LLP | Limited liability partnership | From YA 2026 an LLP's profit paid to an individual partner above RM 100,000 is taxed at 2%; out of scope for TRM v1 | RES-002 | Active |
| NPRA | National Pharmaceutical Regulatory Agency | From YA 2026 any vaccine it registers counts for the vaccination relief | RES-002 | Active |
| REIT | Real estate investment trust | Budget 2027 withholding tax for non-residents; out of scope | RES-002 | Active |
| TADIKA | Taman Didikan Kanak-kanak (kindergarten) | Childcare relief for a child aged 6 and below | RES-002, REG-01 | Active |
| TASKA | Taman Asuhan Kanak-kanak (registered childcare centre) | Childcare relief for a child aged 6 and below | RES-002, REG-01 | Active |
| TVET | Technical and Vocational Education and Training | YA 2027 upskilling sub-limit of RM 3,000 for self or spouse | RES-002, REG-01 | Active |
| BE | Form BE | The income tax return for resident individuals with no business income. The product helps the user prepare to file it. | PRD | Active |
| B | Form B | The return for individuals with business income. Out of scope in v1. | PRD | Active |
| CCTV | Closed-circuit television | Home CCTV, a lifestyle relief item added in YA 2026 and YA 2027 | PRD, F2 | Active |
| EA | Form EA | The employer's yearly statement of an employee's pay. The source of total employment income. | PRD | Active |
| EIS | Employment Insurance System | A payroll contribution counted with SOCSO under the SOCSO and EIS relief | PRD, F1 to F4 | Active |
| EPF | Employees Provident Fund (KWSP) | Retirement savings fund. Employee contributions are relief R14 (category cap 4,000 inside a shared group cap of 7,000). | PRD, F1 to F4 | Active |
| JKM | Jabatan Kebajikan Masyarakat (Department of Social Welfare) | Certifies a disabled individual for the disability relief | PRD | Active |
| LHDN | Lembaga Hasil Dalam Negeri (Inland Revenue Board of Malaysia) | Source of every tax rule, rate and relief cap in the product | All | Active |
| MOH | Ministry of Health | Approves the vaccines that count for the YA 2026 vaccine relief | PRD | Active |
| MTD | Monthly Tax Deduction | English name for PCB | PRD | Active |
| MyTax | MyTax portal | LHDN's online tax portal. Direct submission to it is out of scope in v1. | PRD, F1 | Active |
| MYR | Malaysian ringgit (ISO currency code) | The currency code of the amounts. Shown to users as RM. | PRD | Active |
| PCB | Potongan Cukai Bulanan (monthly tax deduction) | Tax the employer withholds from each month's pay. The system projects the PCB for the whole year. | PRD, F0 to F4 | Active |
| PDPA | Personal Data Protection Act 2010 | Malaysian privacy law. It decides where the public version may be hosted. | PRD | Active |
| PRS | Private Retirement Scheme | Voluntary retirement savings with its own relief (3,000) | PRD, F2 | Active |
| RM | Ringgit Malaysia | The currency. Stored as whole sen, shown as "RM 1,449.00". | All | Active |
| RPGT | Real Property Gains Tax | Out of scope in v1 | PRD | Active |
| SOCSO | Social Security Organisation (PERKESO) | Employee contributions give the SOCSO and EIS relief | PRD, F1 to F4 | Active |
| SPA | Sale and Purchase Agreement | The agreement date decides the first-home loan interest relief (first_home_spa_date) | PRD, F2 | Active |
| SSPN | Skim Simpanan Pendidikan Nasional (national education savings scheme) | Net deposits give the SSPN relief | PRD, F2, F3 | Active |
| STEM | Science, Technology, Engineering and Mathematics | Children's tuition in STEM subjects is part of the education relief wording | PRD | Active |
| TP1 | Form TP1 | The form an employee gives the employer to declare reliefs, which changes the PCB | PRD | Active |
| YA | Year of Assessment | The tax year. YA 2026 covers income and spending dated 1 January to 31 December 2026. | All | Active |

## 2. Product, document and delivery terms

| Short form | Stands for | Meaning in this project | Used in | Status |
| --- | --- | --- | --- | --- |
| CI | Chargeable income | Income after reliefs, the amount tax is worked out on. Used in the PRD tax formula. | PRD, F1 | Active |
| MD | Markdown | The plain-text file format used for all documents and logs | REG-01 | Active |
| MVP | Minimum viable product | Release 1 of the product | PRD, F1 to F4 | Active |
| PRD | Product Requirements Document | The product document the URS and SRS documents come from; document PRD-TRM, the master for names and IDs (revision 48) | All | Active |
| R1, R2, R3, R4 | Release 1, 2, 3, 4 | The releases of PRD section 9.1: R1 is the first build (four core features plus profile, built in PRD phase 1), R2 spouse and family sharing (phase 3), R3 bank import and MyTax assisted entry (phase 4), R4 receipt scanning and non-salary income (phase 5). Not the same as category codes R01 to R24 or rule IDs RULE-nn (see section 6). | PRD | Active |
| SRS | System Requirements Specification | Part B of each feature document: exactly how the application behaves | All | Active |
| TRM | Tax Relief Manager | The working name of the product | PRD, F1 | Active |
| URS | User Requirements Specification | Part A of each feature document: what the user must be able to do | All | Active |

## 3. Technology and standards

| Short form | Stands for | Meaning in this project | Used in | Status |
| --- | --- | --- | --- | --- |
| DKIM | DomainKeys Identified Mail | A signature on sent email that proves it came from the domain | ADR-006 | Active |
| DMARC | Domain-based Message Authentication, Reporting and Conformance | The domain's rule for mail that fails SPF or DKIM | ADR-006 | Active |
| KPMG | KPMG (a tax and audit firm; a name) | Its Finance Bill 2026 summary was a secondary source in RES-002 | RES-002 | Active |
| SMTP | Simple Mail Transfer Protocol | The standard way a server sends email | ADR-006 | Active |
| LTS | Long-term support | A Node.js release line that gets fixes for a long time; used to build the front end | ADR-001 | Active |
| UTC | Coordinated Universal Time | The one time zone the database stores times in | ADR-004 | Active |
| SPF | Sender Policy Framework | The domain's list of servers allowed to send its email | ADR-006 | Active |
| AA | Level AA (of WCAG) | The accessibility level the PWA must meet | PRD, F4 | Active |
| ADR | Architecture decision record | One short file per technical decision in docs/decisions | README, decision records | Active |
| AI | Artificial intelligence | A YA 2027 lifestyle item (AI subscriptions) in the PRD; also the AI agents that work on the repository | PRD, AGENTS.md | Active |
| API | Application programming interface | How the front end and back end talk | PRD | Active |
| ARIA | Accessible Rich Internet Applications | Labels that let screen readers describe the screens | F4 | Active |
| AWS | Amazon Web Services | One possible host for the public version | PRD | Active |
| CSV | Comma-separated values | Plain text table format used in the data export (F5) | F5 | Active |
| DD | Day | Date format DD/MM/YYYY | PRD, F0 to F4 | Active |
| HEIC | High Efficiency Image Container | Phone photo format accepted for receipts | F3 | Active |
| HTML | HyperText Markup Language | The language a web page is written in; Blade and Livewire send it from the server | Front-end findings | Active |
| HTTP | Hypertext Transfer Protocol | The unencrypted web protocol; F5 requires redirecting it to HTTPS | F5 | Active |
| HTTPS | Hypertext Transfer Protocol Secure | Encrypted connection | PRD | Active |
| ID | Identifier | A unique value for a row or a requirement | All | Active |
| IP | Internet Protocol (address) | The network address of a device; kept 30 days in a security event (SD-F5-15) | F5 | Active |
| JPEG | Joint Photographic Experts Group | Receipt image format, compressed to quality 80 | F3 | Active |
| JSON | JavaScript Object Notation | Structured text format for eligibility tests (DA-04) | F1 to F4 | Active |
| MB | Megabyte | File size limit: receipts are at most 10 MB | F3 | Active |
| MCP | Model Context Protocol | The way an AI agent connects to outside tools; approved servers are listed in AGENTS.md | AGENTS.md | Active |
| MM | Month | Date format DD/MM/YYYY | PRD, F0 to F4 | Active |
| OCR | Optical character recognition | Reading text from a receipt photo. Release 4. | PRD, F3 | Active |
| PC | Personal computer | A lifestyle relief item (books, phone, tablet, PC) | PRD | Active |
| PDF | Portable Document Format | Export format of the documents and the user summary | All | Active |
| PHP | PHP: Hypertext Preprocessor | The language Laravel is written in | Front-end findings | Active |
| PNG | Portable Network Graphics | Receipt image format | F3 | Active |
| PR | Pull request | A proposed change on GitHub that is reviewed and checked before it is merged | README, AGENTS.md, REG-01 | Active |
| CLI | Command line interface | A program used by typing commands in the terminal, such as `gh` (GitHub CLI) | AGENTS.md, REG-04, REG-01 | Active |
| PWA | Progressive Web App | The kind of application being built: a web app that installs and works offline | All | Active |
| QR | Quick response (code) | The square code the authenticator app scans to set up two-factor login | F5 | Active |
| REST | Representational State Transfer | The style of the server interface | PRD | Active |
| SMS | Short message service | Text-message codes; deliberately not used for two-factor login (SD-F5-05) | F5 | Active |
| TOTP | Time-based one-time password | The 6-digit code an authenticator app makes every 30 seconds | F5 | Active |
| UUID | Universally unique identifier (version 7) | The id the app creates on the phone before it reaches the server | F0 to F4 | Active |
| WCAG | Web Content Accessibility Guidelines | The accessibility standard the PWA follows | PRD, F4 | Active |
| YYYY | Four-digit year | Date format DD/MM/YYYY | PRD, F0 to F4 | Active |
| ZIP | ZIP archive | The single file that holds a data export | F5 | Active |

## 4. Document ID prefixes

These are not acronyms in the usual sense, but they are the short forms readers meet most. The number part is never reused.

| Prefix | Stands for | Meaning | Defined in | Status |
| --- | --- | --- | --- | --- |
| BR | Business rule | PRD rule ID, for example BR-11 | PRD | Active |
| CHG | Change | One detail change in the URS and SRS change log, for example CHG-017 | REG-02 | Active |
| DA | Data addition | A field or table the specification needs that the PRD data model lacks, for example DA-05. Proposed until the owner approves. | F0 to F4, Part B2 | Active |
| EV | Event | A message that tells other features to refresh, for example EV-03 ProfileChanged | F0 to F4, section A5 | Active |
| F-nnn | Finding | A finding in REG_01_History_Log.md, for example F-030 | REG-01 | Active |
| F0 to F5 | Feature 0 to 5 | F0 User profile and tax-year history, F1 Tax calculator for any year, F2 Relief categories and ranges, F3 Spending records, F4 Dashboard, F5 Account and security (F1 to F4 follow PRD sections 3.1 to 3.4) | All | Active |
| FD | Flow diagram | A diagram in Part A that an SRS row works from, for example FD-F1-02 | F0 to F4 | Active |
| FR | Functional requirement | PRD requirement ID, for example FR-1.3 | PRD | Active |
| GRP | Group | Prefix of a shared-cap group code, for example GRP-INS-EPF | F2, F3 | Active |
| IF | Interface | Data one feature passes to another, for example IF-04 | F0 to F4, section A5 | Active |
| NFR | Non-functional requirement | PRD requirement on quality, for example NFR-11 | PRD | Active |
| OI | Open item | An unresolved question, for example OI-F2-01 | F0 to F4 | Active |
| P-nn | Prompt | One owner prompt in the prompt register of REG_01_History_Log.md | REG-01 | Active |
| Rnn | Relief category code | R01 to R24, for example R14 (EPF) | F0 to F4, Part B2 | Active |
| PRD-TRM, URS-SRS-Fn, ADR-nnn, RES-nnn, REG-nn | Document ID | The ID on the first line and in the header of every document, for example URS-SRS-F1; the file name is the same with underscores (AGENTS.md section 6) | AGENTS.md | Active |
| REG | Register | A running register: REG-01 History log, REG-02 URS and SRS change log, REG-03 Acronyms, REG-04 Prompt and working rules | AGENTS.md, registers | Active |
| RES | Research note | Findings only, no decision, for example RES-001 (front-end frameworks); was R-001 until 23/11/2026 | docs/decisions/research | Active |
| RULE | Working rule | A rule in REG-04, for example RULE-50; was R-nn until 23/11/2026 | REG-04, AGENTS.md | Active |
| Dnn | Deduction category code | D01 and D02, for example D01 (donations) | F0 to F4, Part B2 | Active |
| SD | Specification decision | A detail the PRD does not state, filled in by me, needing the owner's yes or no, for example SD-F1-07 | F0 to F4 | Active |
| SQ | Sequence diagram | A diagram that shows one behaviour across features, for example SQ-F1-01 | F1, F3, F4 | Active |
| SRS-Fn-nn | System requirement | See section 2 | F0 to F4 | Active |
| TC | Test case | Exact inputs and expected outputs, for example TC-F1-05 | F0 to F4 | Active |
| URS-Fn-nn | User requirement | See section 2 | F0 to F4 | Active |
| A1 to A6, B1 to B3 | Section references | Section numbers inside the feature documents, for example "A5" (interfaces) and Part B2 (data additions) | F1 to F4 | Active |

## 5. Code values (capital letters that are data, not acronyms)

These appear in capitals because they are values stored in the system or in tests.

| Value | Meaning | Where |
| --- | --- | --- |
| ERRORS | The word the build prints with the error count (ERRORS: 0) | README, AGENTS.md |
| CHECKUP | Sub-limit code: medical check-up (inside R07) | F2, F3 |
| COMPOSTER | Sub-limit code: food waste composter (inside R12, once in YA 2025 to YA 2027) | F2, F3 |
| GRINDER | Sub-limit code: food waste grinder (inside R12, once in YA 2026 or YA 2027) | F2, F3 |
| CORE | Consent purpose code: the required consent to process the user's data to run TRM | F5 |
| DELETE | The word the user types to confirm an account deletion | F5 |
| DENTAL | Sub-limit code: dental exam (inside R07) | F2, F3 |
| FREQUENCY | Reason code on an expense kept with applied 0 because the claim-frequency rule was already used | F3 |
| INS | Insurance, as in GRP-INS-EPF | F2, F3 |
| MANDATORY | Sub-limit code: mandatory item (350 in YA 2027, inside R18) | F2, F3 |
| POSTNATAL | Sub-limit code: postnatal care (3,000, YA 2027 only, inside R07) | F2, F3 |
| PERSONAL | Rebate code: individual rebate RM 400 | F1, F2 |
| README | The name of the text file at the top of a data export | F5 |
| SGP1 | DigitalOcean Singapore region code, the nearest region to Malaysia | PRD |
| SHOES | Sub-limit code: sports shoes (YA 2027, inside R11) | F2 |
| SKILLS | Sub-limit code: skills course | F2 |
| SPOUSE | Rebate code: spouse rebate | F1, F2 |
| SUBLIMIT | Code of the sub-limit table or a limit type | F2, F3 |
| SYSTEM | The user id written to created_by and updated_by when the system acts | PRD, F0 to F4 |
| VACC | Sub-limit code: vaccination (inside R07) | F2, F3 |
| VOLUNTARY | Sub-limit code: voluntary item (150 in YA 2027, inside R18) | F2, F3 |
| ZAKAT | Rebate code: zakat, ringgit for ringgit | F1, F2 |
| AND | Logic word in pseudocode and rule tests | F1, F2 |
| GRP-INS-EPF | The shared cap group holding EPF (R14) and life insurance (R15), group cap 7,000 | F2, F3 |

## 6. Collisions: one short form, more than one meaning

Read the context before you assume a meaning.

| Short form | Meaning 1 | Meaning 2 | How to tell them apart |
| --- | --- | --- | --- |
| EV | Event ID prefix (EV-03) | Electric vehicle, in the YA 2026 "EV charging" relief item | With a hyphen and number it is an event |
| R1 and R01 | Release 1 | Relief category code R01 (individual) | R01 to R24 have two digits; releases have one; working rules are RULE-nn and research notes RES-nnn |
| F1 and F-001 | Feature 1 | Finding number 1 in the history log | Findings have a hyphen and three digits |
| CI | Chargeable income (tax formula) | Continuous integration (automatic checks in the proposed Git repository) | Tax formula or Git discussion |
| SD | Specification decision | none yet | Listed so a second meaning is caught early |
| D01 and DD | Deduction code D01 | Day in a date format | D01 has a number; DD is a date pattern |
| B and BE | Form B (business income) | Form BE (employment income) | The extra letter |

## Acronym change log

| Date | Change | Short form | Reason | Trigger |
| --- | --- | --- | --- | --- |
| 2026-11-13 | Added | All 53 acronyms, 21 ID prefixes, 18 code values, 7 collisions | Register created from a scan of the PRD, F1 to F4, and both logs | Prompt P-12 |
| 2026-11-13 | Changed | "Used in" columns now say F0 to F4 where the profile document uses the short form; F1 to F4 in the feature row became F0 to F4 | Document F0 (user profile) added; no new acronym was needed | Prompt P-13 |
| 2026-11-13 | Added | CSV, HTTP, IP, QR, SMS, TOTP, ZIP (section 3); CORE, DELETE, README (section 5) | Document F5 (account and security) uses them; the row "F0 to F4" became "F0 to F5" | Prompt P-15 |
| 2026-11-14 | Added | ADR, MCP, PR (section 3); ERRORS (section 5); AI row extended | README, AGENTS.md and the decision records use them | Prompt P-18 |
| 2026-11-14 | Added | HTML, PHP (section 3) | The front-end findings file RES-001 uses them | Prompt P-22 |
| 2026-11-23 | Added and changed | RULE, RES, REG, document IDs (PRD-TRM, URS-SRS-Fn, ADR-nnn, RES-nnn, REG-nn); R3 added to the releases row; F1 and F2 names follow the PRD | Document standard: rule IDs R-nn became RULE-nn and research R-001 became RES-001 so they no longer look like releases or relief codes | Prompt P-38, CHG-051 |
| 2026-11-23 | Added | LINDUNG, KENDIRI, LLP, NPRA, REIT, TADIKA, TASKA, TVET (section 1); DKIM, DMARC, KPMG, SMTP, SPF (section 3) | RES-002 (YA 2026 and YA 2027 check) and ADR-006 (email service) use them | Prompt P-41, CHG-053 |
| 2026-11-23 | Added | COMPOSTER, GRINDER (section 5) | New R12 sub-limit codes from the rule corrections | Prompt P-42, CHG-054 |
| 2026-11-23 | Added | CP38, CP39, TP3 (section 1) | RES-003 (PCB 2026 check) uses them | CHG-056 |
| 2026-11-23 | Added | LTS, UTC (section 3) | ADR-001 and ADR-004 use them | CHG-061 |
