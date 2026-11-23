# RES-002: YA 2026 and YA 2027 rule check against primary sources

| Item | Value |
| --- | --- |
| Document ID | RES-002 |
| Document type | Research note (findings only) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.2 |
| Status | Draft. Findings only. Applied to the PRD (revision 50) and the specifications on 23/11/2026 after the owner said "update" (F-063, CHG-054) |
| Date | 2026-11-23 (first written 2026-11-23) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM sections 2.1 to 2.4 and section 9.1 phase 0 (verify every rule for YA 2025, 2026 and 2027) |
| Source | Owner prompts P-41 ("go ahead" for the check) and P-42 ("update"); the sources S1 to S8 below |
| Change tracking | [REG-01 History log](../../registers/REG_01_History_Log.md) |
| Scope | Resident individual rules: tax bands, reliefs, rebates, deductions, filing deadline |

## 1. How this was checked

Two research agents read the primary sources on 23/11/2026, one for each YA, and gave a short quote and the link for every value. I re-read the most important finding myself: the tax bands on the LHDN rate page (S5). Statuses:

| Status | Means |
| --- | --- |
| Gazetted | In the Income Tax Act 1967 as amended by an enacted, gazetted Finance Act |
| Confirmed | Stated by LHDN (public ruling or LHDN page) |
| Bill | In the Finance Bill 2026, first reading in the Dewan Rakyat on 16/11/2026 (D.R.28/2026); not passed, not gazetted |
| Announced | Only in the Budget tax measures of the Ministry of Finance |
| Unchanged | Not mentioned in the Budget 2027 measures; the YA 2026 rule carries forward |

On 23/11/2026 the owner decided that "Announced with a source" is firm enough for YA 2027 (F-062). Every YA 2027 change below is at least Announced, and also in the Bill.

## 2. Sources

| # | Source | Kind |
| --- | --- | --- |
| S1 | [Finance Act 2025, Act 874, gazetted 31/12/2025](https://www.hasil.gov.my/wp-content/uploads/Akta-Kewangan-2025-Akta-874.pdf) | Law (YA 2026) |
| S2 | [LHDN Public Ruling No. 5/2026 of 04/11/2026, resident individual, gifts and allowable deductions](https://www.hasil.gov.my/wp-content/uploads/20261104-PR-5_Taxation-Of-A-Resident-Individualpart-I-Gifts-Or-Contributions-And-Allowable-Deductions.pdf) | LHDN |
| S3 | [LHDN explanatory notes, Form BE YA 2025](https://ef.hasil.gov.my/eBE2026/Pdf/Nota_BE_e.pdf) | LHDN |
| S4 | [LHDN rebates page](https://www.hasil.gov.my/en/individu/rebat/) | LHDN |
| S5 | [LHDN tax rate page, YA 2023, 2024 and 2025](https://www.hasil.gov.my/en/individu/kadar-cukai/) | LHDN |
| S6 | [Ministry of Finance, Budget 2026 tax measures](https://belanjawan.mof.gov.my/pdf/belanjawan2026/ucapan/tax-measures.pdf) | Announced (YA 2026); agrees with S1 |
| S7 | [Ministry of Finance, Budget 2027 tax measures](https://belanjawan.mof.gov.my/pdf/belanjawan2027/ucapan/tax-measures.pdf) and [Malay version](https://belanjawan.mof.gov.my/pdf/belanjawan2027/ucapan/langkah-cukai.pdf) | Announced (YA 2027) |
| S8 | [Parliament bill list](https://www.parlimen.gov.my/bills-dewan-rakyat.html?uweb=dr&lang=en): D.R.28/2026 Finance Bill 2026, first reading 16/11/2026. The bill text link returned "File does not exist"; clause numbers come from KPMG, The Star and Bernama (secondary) | Bill status |

## 3. Tax bands (resident)

| Chargeable income (RM) | YA 2025 and YA 2026 | Status | YA 2027 | Status |
| --- | --- | --- | --- | --- |
| 0 to 5,000 | 0% | Gazetted (S5; Act 874 does not change Schedule 1 Part I, S1) | 0% | Bill; Announced (S7) |
| 5,001 to 20,000 | 1% | Gazetted | 1% | Bill; Announced |
| 20,001 to 35,000 | 3% | Gazetted | 3% | Bill; Announced |
| 35,001 to 50,000 | 6% | Gazetted | 6% | Bill; Announced |
| 50,001 to 70,000 | 11% | Gazetted | 11% | Bill; Announced |
| 70,001 to 100,000 | 19% | Gazetted | 18% | Bill; Announced |
| 100,001 to 150,000 | 25% | Gazetted | 24% (new band) | Bill; Announced |
| 150,001 to 400,000 | 25% | Gazetted | 25% | Bill; Announced |
| 400,001 to 600,000 | **26%** | Gazetted | **26%** | Bill; Announced |
| 600,001 to 1,000,000 | **28%** | Gazetted | **28%** | Bill; Announced |
| 1,000,001 to 2,000,000 | 28% | Gazetted | **30%** | Bill; Announced |
| Above 2,000,000 | 30% | Gazetted | 30% | Bill; Announced |

**Difference from our documents:** PRD section 2.2 and F1 B3.1 have one band "400,001 to 1,000,000 at 26%" and "1,000,001 to 2,000,000 at 28%" (30% for YA 2027). LHDN's table (S5, checked by me) gives 26% only up to 600,000, and 28% from 600,001. The YA 2027 table (S7) also starts 28% at 600,001 and 30% above 1,000,000. The F1 test values TC-F1-01 to TC-F1-06 are not affected (all at or below RM 100,000).

## 4. Reliefs, YA 2026

| Relief | Value found | Status | Same as our documents? |
| --- | --- | --- | --- |
| Individual and dependent relatives | 9,000 | Confirmed (S2) | Yes |
| Disabled individual | 7,000 | Confirmed (S2) | Yes |
| Spouse or alimony | 4,000; alimony is inside the same 4,000 and limited to the amount paid | Confirmed (S2) | Yes |
| Disabled spouse | 6,000 further | Confirmed (S2) | Yes |
| Education fees (self) | 7,000; upskilling sub-limit 2,000 "for YA 2023 up to YA 2026" | Confirmed (S2) | Yes |
| First-home loan interest | 7,000 (home up to 500,000) or 5,000 (500,001 to 750,000); SPA 01/01/2025 to 31/12/2027; 3 consecutive YAs | Confirmed (S2) | Yes |
| Medical (self, spouse, child) | 10,000 overall; vaccination 1,000 (any vaccine registered with NPRA, from YA 2026); dental 1,000; check-up and tests 1,000; child learning-disability programme 10,000 (was 6,000) | Gazetted (S1); Confirmed (S2) | Yes |
| Parents or grandparents | 8,000; check-up and vaccination 1,000 (NPRA-registered vaccines from YA 2026) | Confirmed (S2) | Yes |
| Supporting equipment (disabled) | 6,000 | Confirmed (S2) | Yes |
| Lifestyle | 2,500 | Confirmed (S2) | Yes |
| Sports | 1,000 (parents included from YA 2025) | Confirmed (S2) | Yes |
| EV charging, food waste composter, **food waste grinder**, home CCTV | One cap of 2,500. EV charging has no once-only rule (to YA 2027). The composter is claimed once in YA 2025, 2026 or 2027. The grinder and CCTV are claimed once in YA 2026 or 2027 | Gazetted (S1) | **No**: our documents have no grinder and put the once-only rule on the whole relief |
| Domestic tourism (entrance fees, culture and arts) | 1,000, **YA 2026 only** in the Act | Gazetted (S1) | Yes for YA 2026; see YA 2027 below |
| Life insurance and EPF | 7,000: EPF up to 4,000; life insurance, family takaful and voluntary EPF up to 3,000. **From YA 2026 a policy on the life of the individual's child counts** | Gazetted (S1) | Partly: our documents still say "(confirm)" for the child extension |
| PRS and deferred annuity | 3,000, until YA 2030 | Confirmed (S2) | Yes |
| Education and medical insurance | 4,000 | Confirmed (S2) | Yes; now confirmed for YA 2026 (was "needs confirmation") |
| SOCSO and EIS | 350 | Confirmed (S2) | Yes |
| SSPN net savings | 8,000 (YA 2019 to YA 2027) | Confirmed (S2) | Yes |
| Child under 18; child 18 and above in education | 2,000; 2,000 (matriculation, A-Level) or 8,000 (diploma and above in Malaysia, degree and above abroad) | Confirmed (S2) | Yes |
| Disabled child | 8,000, plus 8,000 in full-time higher education (16,000) | Confirmed (S2) | Yes |
| Childcare | 3,000. **Child 6 and below** at a registered TASKA or TADIKA; **child 12 and below** at a care centre registered under the Care Centres Act 1993 | Gazetted (S1) | **No**: our documents say "child up to 12" for all |
| Breastfeeding equipment | 1,000; child 2 and below; once every 2 YAs; working mothers only | Confirmed (S2) | Yes (the working-mother condition is not in our documents) |
| New "child" definition for the insurance reliefs | Unmarried under 18, or 18 and above in full-time study, or under articles or indentures, or disabled at any age; step-children and adopted children included | Gazetted (S1, s.49(5) and (6)) | Not in our documents |

**Rebates and deductions, YA 2026:** RM 400 personal rebate and RM 400 spouse rebate at chargeable income up to RM 35,000; zakat and fitrah up to the tax charged; departure levy for umrah or other religious travel, at most 2 trips (S3, S4; Act 874 does not change section 6A). Approved donations up to 10% of aggregate income; gifts to the Government without limit; professional subscriptions deductible (S2, S3). All as in our documents.

**Filing deadline for YA 2026:** not found. LHDN has not published the 2027 filing programme yet.

## 5. Reliefs, YA 2027 (Budget 2027)

Only the changes are listed. Every relief not in this table is **Unchanged**: it carries forward from YA 2026.

| Relief | Value found | Status | Same as our documents? |
| --- | --- | --- | --- |
| Individual and dependent relatives | 12,000 (from 9,000) | Bill; Announced (S7) | Yes |
| Education fees, renamed "Education and Skills Training Fees" | 7,000 overall: self, any field from certificate to doctorate; **TVET upskilling for self or spouse up to 3,000**; **2,000 shared** between non-employment courses for self or spouse and children's STEM, arts, language or religion classes | Bill; Announced (S7) | **No**: our documents say skills sub-limit 2,000 |
| Lifestyle | 2,500; upskilling course fees move out to Education and Skills Training Fees; adds AI software and app subscriptions, pet adoption from a registered shelter, pet vaccination and neutering | Bill; Announced (S7) | Partly: the move of upskilling fees is not in our documents |
| Medical, renamed "Health and Well-being" | 10,000 overall; adds postnatal care up to 3,000; **breastfeeding equipment (1,000) moves inside this cap**, claimable by self or spouse | Bill; Announced (S7) | **No**: our documents keep breastfeeding as its own relief |
| Parents or grandparents | 8,000; covers all types of care, not only medical; a carer declaration or work permit and receipts are enough | Bill; Announced (S7) | Yes (the evidence rule is new) |
| Sports | 1,000; adds sports shoes up to 300 | Bill; Announced (S7) | Yes |
| Domestic tourism | **1,000, extended for YA 2027** | Bill; Announced (S7) | **No**: our documents say "not announced" |
| SOCSO and EIS | 350, now also mandatory LINDUNG KENDIRI (passenger transport, goods or food transport, hawkers); plus 150 for voluntary LINDUNG 24 and 17 other LINDUNG KENDIRI sectors | Bill; Announced (S7) | Yes (detail added) |
| Donations | 10% cap unchanged; wider use of the approved school public contribution funds | Announced (S7) | Yes |

Out of scope for TRM v1 (PRD section 1) and not carried into the documents: the 2% tax on LLP profit distributions above RM 100,000 (YA 2026), stamp duty, investor and employer measures, and the REIT withholding tax for non-residents (YA 2027).

## 6. Not checked yet

- The PCB 2026 specification and the TP1 (1/2026) form.
- The LHDN leaflet "Maximise your tax relief" for YA 2026 (the link timed out).
- The bill text of the Finance Bill 2026 (the Parliament link was broken on 23/11/2026).
