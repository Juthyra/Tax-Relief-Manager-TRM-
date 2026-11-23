# RES-003: YA 2025 rule check and the PCB 2026 specification

| Item | Value |
| --- | --- |
| Document ID | RES-003 |
| Document type | Research note (findings only) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.2 |
| Status | Draft. Findings only. Proposals (a) to (d) approved by the owner on 23/11/2026 and applied (F-067, CHG-057) |
| Date | 2026-11-23 (first written 2026-11-23) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM sections 2.1 to 2.5 (YA 2025 rule set), FR-1.9 and FR-1.10 (PCB projection), section 9.1 phase 0 |
| Source | Owner prompts P-43 and P-44 (focus on YA 2025 and YA 2026); the sources S1 to S7 below |
| Change tracking | [REG-01 History log](../../registers/REG_01_History_Log.md) |
| Scope | Part A: every YA 2025 rule. Part B: the PCB 2026 specification and the TP1 and TP3 forms (1/2026), checked against F1 |

## 1. Sources

All read on 23/11/2026 by two research agents, one for each part. Every value has a quote and a link in their reports.

| # | Source | Kind |
| --- | --- | --- |
| S1 | [LHDN explanatory notes, Form BE YA 2025](https://ef.hasil.gov.my/eBE2026/Pdf/Nota_BE_e.pdf), items G1 to G23 | LHDN |
| S2 | [LHDN tax rate page](https://www.hasil.gov.my/en/individu/kadar-cukai/) (YA 2023 to YA 2025) | LHDN |
| S3 | [LHDN rebates page](https://www.hasil.gov.my/en/individu/rebat/) | LHDN |
| S4 | [LHDN return form filing programme for 2026](https://www.hasil.gov.my/wp-content/uploads/rf-filing-programme-for-2026.pdf) | LHDN |
| S5 | [Specification for monthly tax deduction calculations using computerised calculation for 2026](https://www.hasil.gov.my/wp-content/uploads/spesifikasi-kaedah-pengiraan-berkomputer-pcb-2026.pdf), updated 01/01/2026 | LHDN |
| S6 | [Form TP1 (1/2026)](https://www.hasil.gov.my/wp-content/uploads/bi-tp1-form-2026.pdf) and its [explanatory notes](https://www.hasil.gov.my/wp-content/uploads/bi-explanatory-notes-for-from-tp1-2026-1.pdf); [Form TP3 (1/2026)](https://www.hasil.gov.my/wp-content/uploads/bi-tp3-form-2026.pdf) | LHDN |
| S7 | [LHDN article: PCB as final tax](https://www.hasil.gov.my/wp-content/uploads/202509_dewan-siswa-bil-092025-potongan-cukai-bulanan-sebagai-cukai-muktamad.pdf) (September 2025) | LHDN |

## Part A. YA 2025 rule check

**Result: every YA 2025 value in our PRD and seed catalogue matches LHDN. No correction is needed.** Status: Confirmed (S1 to S4).

| Rule | LHDN value (YA 2025) | Same as ours? |
| --- | --- | --- |
| Tax bands | Same 10 bands; cumulative tax 84,400 at 400,000, 136,400 at 600,000, 528,400 at 2,000,000 | Yes |
| Individual (G1) | 9,000, automatic | Yes |
| Disabled individual (G4) | 7,000 | Yes |
| Spouse or alimony (G14); disabled spouse (G15) | 4,000 together; 6,000 further | Yes |
| Education fees (G5) | 7,000; upskilling courses up to 2,000 (YA 2024 to YA 2026) | Yes |
| First-home loan interest (G22) | 7,000 (price up to 500,000) or 5,000 (up to 750,000); SPA 01/01/2025 to 31/12/2027; 3 consecutive YAs; one unit, not earning income | Yes |
| Medical (G6 to G8) | 10,000 overall; vaccination 1,000; dental 1,000; check-up, tests, self-test device and mental health 1,000; child learning disability 6,000 (child 18 and below) | Yes |
| Parents or grandparents (G2) | 8,000; check-up with vaccination 1,000; parents living in Malaysia | Yes |
| Supporting equipment (G3) | 6,000 | Yes |
| Lifestyle (G9); sports (G10) | 2,500; 1,000 (parents included) | Yes |
| EV charging and composter (G21) | 2,500 together; composter once in YA 2025 to YA 2027 | Yes |
| Domestic tourism | Not in YA 2025 (no item among G1 to G22) | Yes |
| Life insurance and EPF (G17) | 3,000 plus 4,000, 7,000 in total | Yes |
| PRS and deferred annuity (G18) | 3,000 (YA 2025 to YA 2030) | Yes |
| Education and medical insurance (G19) | 4,000 | Yes |
| SOCSO and EIS (G20) | 350 | Yes |
| SSPN (G13) | 8,000 net | Yes |
| Child reliefs (G16a to G16c) | 2,000; 2,000 or 8,000; disabled 8,000 plus 8,000 | Yes |
| Childcare (G12) | 3,000, child 6 and below, centre registered with JKM or the Ministry of Education | Yes |
| Breastfeeding (G11) | 1,000, women only, child 2 and below, once every 2 YAs | Yes |
| Rebates | 400 personal; 400 spouse when the spouse relief applies; zakat up to the tax charged; departure levy, 2 trips in a lifetime | Yes |
| Deductions | Donations up to 10% of aggregate income (some gifts without a cap); professional subscriptions | Yes |
| **Filing deadline** | **Form BE YA 2025 due 30/04/2026; e-Filing accepted to 15/05/2026** (S4) | New: our TaxYear row for YA 2025 has no deadline yet |

**Conditions LHDN states that our documents do not hold yet** (they decide whether a relief applies, not its cap):

| # | Condition | Where it would go |
| --- | --- | --- |
| A1 | Spouse relief is not allowed when a non-disabled spouse has foreign income above RM 4,000 | R03 eligibility (F0 profile question) |
| A2 | Child relief can be shared 50/50 between people who are not a couple living together (for example divorced parents); no relief for a child whose own income exceeds the relief | R20 to R22 |
| A3 | A pensionable public servant claims only the 3,000 insurance part of the 7,000 (no EPF part) | R14 eligibility |
| A4 | Serious diseases and fertility treatment are items inside the medical 10,000 with no smaller limit | R07 description |
| A5 | First-home loan: one unit only, and the home must not earn income | R06 eligibility |

## Part B. PCB 2026 specification and the TP1 form

**Result: the F1 projection agrees with LHDN's own method.** LHDN projects the annual PCB on normal pay as the PCB paid so far plus this month's PCB times the months left (S5, step 1[E]). That is SRS-F1-12. LHDN takes the PCB on a bonus once, in the bonus month, which is how F1 counts pcb_additional (TC-F1-08). The PCB formula did not change for 2026; only the TP1 items changed (S5).

| # | Finding | Effect on F1 |
| --- | --- | --- |
| B1 | In a bonus month the payslip PCB is the normal PCB plus the PCB on the bonus | F1 already keeps them apart (pcb_monthly and pcb_additional). The entry screen should say "enter the bonus PCB separately", or the bonus would be repeated for every remaining month |
| B2 | "PCB paid so far" excludes extra PCB the employee asked for and CP38 instalments | Not in F1. Proposed: a note on the entry screen, or a separate field |
| B3 | A new employee's PCB from an earlier employer in the same year (Form TP3) counts in "PCB paid so far" | F1 records PCB per month, so it fits if the user enters both employers. Proposed: say so on the screen |
| B4 | PCB is the final tax only when all 5 conditions hold (one employer for 12 months, one source of employment income, tax not paid by the employer, PCB deducted under the rules, separate assessment) and the person does not file | Proposed: a one-line notice; the estimate still applies to everyone who files |
| B5 | LHDN's worked example: PCB January to March 328.20, April normal PCB 106.20, bonus PCB 727.50, April payslip 833.70, projected normal PCB 1,284.00 | Proposed new test for SRS-F1-12 |
| B6 | TP1 limits match the YA 2026 reliefs (C1 to C17; C17 domestic tourism 1,000; C15 grinder and CCTV; C8 child 12 and below at a care centre) | Confirms RES-002. Three errors in LHDN's own TP1 notes: C13 says 3,000 (the form says 4,000); C11 still says a policy on a child's life does not count; both are older wording. We follow the Act and the form |
| B7 | PCB rounding: truncate to 2 decimals, round up to the next 5 sen; no deduction below RM 10 | Only for computing PCB from salary (FR-1.11, R2). Not needed in R1 |
| B8 | No PDF PCB schedule for 2026; it is electronic only (e-CP39) | None |

## 2. Not checked

- The LHDN YA 2026 relief leaflet (link timed out on 23/11/2026).
- The YA 2026 filing deadline: LHDN has not published the 2027 filing programme yet.
- The Finance Act 2024 text (YA 2025 values rest on LHDN's notes, status Confirmed).
