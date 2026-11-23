# PRD-TRM: Malaysia Tax Relief System (PWA)

| Item | Value |
| --- | --- |
| Document ID | PRD-TRM |
| Document type | PRD (product requirements) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | Revision 53 |
| Status | Active (the owner's document; changed only when the owner says so, RULE-20) |
| Date | 2026-11-23 (first written 2026-11-07) |
| Owner | Champs (product owner) |
| PRD reference | This document. It is the master for feature names, IDs, releases and phases (AGENTS.md section 6) |
| Source | Owner prompts P-01 to P-06, P-16, P-38, P-42, P-44, P-46 and P-60 to P-67. The Claude Doc is a copy, last synced at revision 47; revisions 48 to 53 are in Git only |
| Change tracking | Synced entries in [REG-02 URS and SRS change log](../registers/REG_02_URS_SRS_Change_Log.md); work history in [REG-01 History log](../registers/REG_01_History_Log.md) |

## 1. Product overview

This PRD defines a Progressive Web App (PWA) that lets a Malaysian resident taxpayer calculate yearly income tax under LHDN rules, record spending that qualifies for tax relief, and see how much relief is still left to claim. The working name used here is **Tax Relief Manager (TRM)**.

**Problem.** Relief limits, categories and tax bands change with each Budget. Taxpayers keep receipts in photos, chats and email, then guess at filing time which spending counts and how much tax they will owe.

**Product goals**

- Calculate estimated tax payable per Year of Assessment (YA) from salary income and claimed reliefs, using the rules LHDN announces for that YA.
- Show every relief category with its cap, conditions and required proof.
- Record each qualifying expense with a receipt, and auto-cap it at the category limit.
- Show on a dashboard how much relief has been claimed, how much is left, and what it does to tax payable.

**Target users**

| User | Need |
| --- | --- |
| Salaried resident taxpayer (primary) | Estimate tax, track receipts, file Form BE with confidence |
| Product owner / admin | Maintain yearly LHDN rules without a code release |
| Spouse or family member (R2) | Share dependants and see which reliefs apply to whom |

**In scope (v1):** resident individuals, employment income (Form BE), reliefs, rebates, zakat, PCB tracking, receipt records, dashboard, yearly rules management.

**Out of scope (v1):** non-resident tax, business or partnership income (Form B), direct submission to MyTax, corporate tax, RPGT, and payroll PCB calculation for employers.

**Assumptions**

- Rates, relief limits and rules come from LHDN and Budget announcements. The system estimates tax; it does not replace LHDN e-Filing or a tax agent.
- Currency is MYR. Dates and the YA follow the calendar year (YA 2026 = income earned 1 Jan to 31 Dec 2026).
- The PWA is the first delivery channel; native apps are not planned. R1 is for the product owner's personal use. The system is not a government system and only displays tax information. The system opens to the public only after its features are proven, and items needed only for a public launch are marked in sections 7 and 9.

## 2. Malaysia LHDN reference data

The system must store tax rules per Year of Assessment (YA), because Budget 2027 (tabled 9 October 2026) already changes the YA 2027 rates and raises the individual relief from RM9,000 to RM12,000. YA 2026 (income earned 1 Jan to 31 Dec 2026) is the current year and is filed in 2027. All figures below are for **resident individuals**.

### 2.1 How tax is calculated

1. Total employment income (from the EA form) and other taxable income.
2. Less tax deductions (approved donations, professional body subscriptions) gives aggregate income.
3. Less personal reliefs gives **chargeable income**.
4. Apply the progressive bands to chargeable income to get tax before rebates.
5. Less rebates (RM400 personal rebate, zakat and fitrah, departure levy) gives tax payable.
6. Less Monthly Tax Deduction (PCB/MTD) already paid gives the balance to pay or the refund.

### 2.2 Resident tax bands

Bands are unchanged from YA 2023 to YA 2026 (LHDN, Gazetted; the Finance Act 2025 does not change them). Budget 2027 cuts two bands by one point and applies 30% to all income above RM1,000,000 from YA 2027 (Announced; Finance Bill 2026, first reading 16/11/2026).

| Chargeable income (RM) | YA 2023 to YA 2026 | YA 2027 (announced) |
| --- | --- | --- |
| 0 to 5,000 | 0% | 0% |
| 5,001 to 20,000 | 1% | 1% |
| 20,001 to 35,000 | 3% | 3% |
| 35,001 to 50,000 | 6% | 6% |
| 50,001 to 70,000 | 11% | 11% |
| 70,001 to 100,000 | 19% | 18% |
| 100,001 to 150,000 | 25% | 24% |
| 150,001 to 400,000 | 25% | 25% |
| 400,001 to 600,000 | 26% | 26% |
| 600,001 to 1,000,000 | 28% | 28% |
| 1,000,001 to 2,000,000 | 28% | 30% |
| Above 2,000,000 | 30% | 30% |

The table shows the first ringgit of each band (5,001). The system stores each band's lower threshold (5,000 for the 1% band), which is the L of the formula in section 6; the tax is the same (approved 23/11/2026).

Sources: [LHDN tax rate page](https://www.hasil.gov.my/en/individu/kadar-cukai/) (YA 2023 to YA 2025, read 23/11/2026); [Finance Act 2025, Act 874](https://www.hasil.gov.my/wp-content/uploads/Akta-Kewangan-2025-Akta-874.pdf) (YA 2026); [Ministry of Finance, Budget 2027 tax measures, appendix 1](https://belanjawan.mof.gov.my/pdf/belanjawan2027/ucapan/tax-measures.pdf) (YA 2027). Checked in RES-002.

### 2.3 Relief categories and caps

This is the seed data for the rules table, with one column per YA. YA 2026 values are Gazetted (Finance Act 2025) or Confirmed by LHDN (Public Ruling 5/2026). YA 2027 values equal YA 2026 unless Budget 2027 announced a change, and stay Announced until the Finance Act 2026 is gazetted. Checked against these sources on 23/11/2026 (RES-002).

| Category | YA 2025 (RM) | YA 2026 (RM) | YA 2027 (RM, announced) | Key conditions and scope changes |
| --- | --- | --- | --- | --- |
| Individual and dependent relatives | 9,000 | 9,000 | 12,000 | Automatic for every resident |
| Disabled individual | 7,000 | 7,000 | 7,000 | Certified by Department of Social Welfare (JKM) |
| Spouse or alimony | 4,000 | 4,000 | 4,000 | Spouse has no income, or joint assessment. Not allowed when a non-disabled spouse has income from outside Malaysia above 4,000 |
| Disabled spouse | 6,000 | 6,000 | 6,000 | Spouse certified disabled |
| Education fees (self) | 7,000 (upskilling sub-limit 2,000) | 7,000 (upskilling sub-limit 2,000) | 7,000 (TVET upskilling 3,000; other courses and children's classes 2,000) | Recognised institution. YA 2027 renames it Education and Skills Training Fees: any field from certificate to doctorate; TVET upskilling for self or spouse up to 3,000; non-employment courses for self or spouse and children's STEM, arts, language or religion classes share 2,000 |
| First-home loan interest | 7,000 or 5,000 | 7,000 or 5,000 | 7,000 or 5,000 | 7,000 for a home up to 500,000; 5,000 for 500,001 to 750,000. Interest only; SPA signed 1 Jan 2025 to 31 Dec 2027; up to 3 consecutive YAs; one unit only, not earning income |
| Medical (self, spouse, child) | 10,000 overall; child learning-disability programme 6,000 | 10,000 overall; child programme 10,000 | 10,000 overall; child programme 10,000; postnatal care up to 3,000; breastfeeding equipment 1,000 | Sub-limits of 1,000 each for vaccination, dental exam and medical check-up. YA 2026: any vaccine registered with NPRA. YA 2027 renames it Health and Well-being and moves breastfeeding equipment inside it |
| Parents or grandparents (medical and care) | 8,000 | 8,000 | 8,000 | Medical, dental, special needs, nursing home; check-up and vaccination sub-limit 1,000. YA 2027: all types of care expense; a carer declaration or work permit and receipts are enough |
| Supporting equipment for disabled person | 6,000 | 6,000 | 6,000 | Person registered with JKM |
| Lifestyle | 2,500 | 2,500 | 2,500 | Books, phone, tablet, PC, internet bill, skills courses. YA 2027 moves skills courses to Education and Skills Training Fees and adds AI subscriptions, pet adoption from a registered shelter, pet vaccination and neutering fees |
| Sports (additional lifestyle) | 1,000 | 1,000 | 1,000 | Equipment, facility fees, competition fees, gym. YA 2027: sports shoes up to 300 within the cap |
| EV charging, food waste composter or grinder, home CCTV | 2,500 (EV charging, composter) | 2,500 (grinder and CCTV added) | 2,500 | One shared cap. EV charging each year to YA 2027. The composter is claimed once in YA 2025, 2026 or 2027; the grinder and the CCTV once in YA 2026 or 2027 |
| Domestic tourism | Not available | 1,000 | 1,000 (extended for YA 2027) | Entrance fees to local attractions; art and cultural programmes. YA 2026 in the Finance Act 2025; YA 2027 extension announced in Budget 2027 |
| Life insurance and EPF | 7,000 combined | 7,000 combined | 7,000 combined | One shared cap of 7,000: up to 4,000 for mandatory EPF (or an approved scheme) and up to 3,000 for life insurance, family takaful and additional voluntary EPF (LHDN, YA 2023 to YA 2025; carried forward for YA 2026 and YA 2027, needs confirmation; decision 5). From YA 2026 a life policy on the individual's child also counts (Finance Act 2025) A pensionable public servant claims only the 3,000 insurance part |
| PRS and deferred annuity | 3,000 | 3,000 | 3,000 | PRS relief extended to YA 2030 |
| Education and medical insurance | 4,000 (LHDN, Confirmed) | 4,000 (LHDN, Confirmed) | 4,000 (unchanged by Budget 2027) | Premiums for self, spouse, child. LHDN gives 4,000 from YA 2025 (3,000 for YA 2018 to YA 2024), confirmed for YA 2026 in Public Ruling 5/2026. See decision 4 |
| SOCSO and EIS | 350 | 350 | 350 plus 150 | YA 2027: the 350 also covers mandatory Lindung Kendiri (passenger transport, goods or food transport, hawkers); extra 150 for voluntary Lindung 24 Jam or the other Lindung Kendiri sectors |
| SSPN net savings | 8,000 | 8,000 | 8,000 | Deposits minus withdrawals in the year |
| Child under 18 | 2,000 per child | 2,000 per child | 2,000 per child | Unmarried. For every child relief: shared 50/50 between people who are not a couple living together; none for a child whose own income is above the relief |
| Child 18 and above, full-time education | 2,000 or 8,000 | 2,000 or 8,000 | 2,000 or 8,000 | 8,000 for diploma and above in Malaysia or degree and above overseas |
| Disabled child | 8,000 | 8,000 | 8,000 | Unmarried; extra 8,000 if 18 and above in higher education |
| Childcare or kindergarten fees | 3,000 (child up to 6) | 3,000 (child up to 6; up to 12 at a care centre) | 3,000 (child up to 6; up to 12 at a care centre) | Registered TASKA or TADIKA for a child aged 6 and below; from YA 2026 also a care centre registered under the Care Centres Act 1993 for a child aged 12 and below |
| Breastfeeding equipment | 1,000 | 1,000 | Inside medical (1,000) | Child aged 2 and below; once every 2 YAs; working mothers. YA 2027 moves it inside Health and Well-being, claimable by self or spouse |

**Tax deductions** (reduce aggregate income, not chargeable income): approved donations, generally capped at 10% of aggregate income; professional body subscriptions at actual cost with no cap.

**Rebates** (reduce tax payable): RM400 if chargeable income is RM35,000 or below, with a further RM400 when the spouse relief applies; zakat and fitrah, ringgit for ringgit; departure levy paid on religious travel.

No change to deductions or rebates was announced for YA 2026 or YA 2027 in the sources read, so both carry forward unchanged.

Sources: [Finance Act 2025, Act 874](https://www.hasil.gov.my/wp-content/uploads/Akta-Kewangan-2025-Akta-874.pdf); [LHDN Public Ruling No. 5/2026](https://www.hasil.gov.my/wp-content/uploads/20261104-PR-5_Taxation-Of-A-Resident-Individualpart-I-Gifts-Or-Contributions-And-Allowable-Deductions.pdf); [LHDN rebates](https://www.hasil.gov.my/en/individu/rebat/); [Ministry of Finance, Budget 2027 tax measures](https://belanjawan.mof.gov.my/pdf/belanjawan2027/ucapan/tax-measures.pdf). Earlier secondary sources: [RinggitPlus, YA 2025 relief list](https://ringgitplus.com/en/blog/tax/everything-you-can-claim-as-income-tax-relief-in-malaysia-2026-filing-for-ya-2025.html); [BrioHR, YA 2026 relief updates](https://support.briohr.com/knowledge/payroll-malaysia-key-tax-relief-updates-for-the-year-2026). Every row checked on 23/11/2026 (RES-002).

### 2.4 Filing and record rules

- Employees without business income file **Form BE** through MyTax. For YA 2025 the return was due 30 April 2026 and e-Filing was accepted to 15 May 2026 ([LHDN filing programme for 2026](https://www.hasil.gov.my/wp-content/uploads/rf-filing-programme-for-2026.pdf)). The system stores each YA's deadline as data. The YA 2026 deadline was not in the sources read; the YA 2025 pattern (due 30 April, e-Filing accepted to 15 May) is only a guide until LHDN publishes it.
- Receipts must be kept for 7 years from the end of the YA.
- The same expense cannot be claimed under two categories.
- Employers use form PCB TP1 (1/2026) to collect an employee's relief declarations for monthly deductions.

### 2.5 Rule sets loaded in R1

R1 ships with all three rule sets complete, so the calculator, catalogue and dashboard work for YA 2026 now and for YA 2027 from 1 January 2027 without a code release. Real use starts with YA 2026, the return filed in 2027; YA 2025 is the reference year, the return filed in 2026. YA 2025 and YA 2026 are the focus of verification; YA 2027 stays loaded as Announced and is re-checked later (owner, 23/11/2026).

| Rule set | Used for | Status in the system | What an admin confirms before publishing |
| --- | --- | --- | --- |
| YA 2025 | Reference and year comparison (return filed in 2026) | Confirmed after verification | Bands and caps in sections 2.2 and 2.3 |
| YA 2026 | Current year: relief planning now and filing in 2027 | In force: Gazetted (Finance Act 2025) and Confirmed by LHDN (Public Ruling 5/2026), checked 23/11/2026 | The filing deadline, when LHDN publishes it |
| YA 2027 | Planning 2027 spending and filing in 2028 | Announced (Budget 2027; Finance Bill 2026, first reading 16/11/2026); becomes Gazetted when the Finance Act 2026 is gazetted | Every YA 2027 change against the gazetted Finance Act 2026: individual relief 12,000, the 18%, 24% and 30% bands, each scope change |

**Verification note.** On 23/11/2026 every figure was checked against the Finance Act 2025, LHDN and the [Budget 2027 tax-measures document](https://belanjawan.mof.gov.my/pdf/belanjawan2027/ucapan/tax-measures.pdf) (RES-002). An admin still records the confirmation date on each rule when loading it, and re-checks YA 2027 when the Finance Act 2026 is gazetted.

## 3. Core features (must-have)

Four features make up the minimum product (sections 3.1 to 3.4, F1 to F4). Two supporting features keep them accurate and safe: the user profile and tax-year history (section 3.5, F0) and account and security (section 3.6, F5), added on 23/11/2026. Every requirement below is **Must** priority for R1 unless marked R2, R3 or launch account. Requirement IDs (FR-x.y) are used later in the data model and roadmap.

### 3.1 Tax calculator for any year

**User story.** As a taxpayer, I want to see my estimated tax for any YA from my income and claimed reliefs, so I know whether I will owe tax or get a refund.

| ID | Requirement |
| --- | --- |
| FR-1.1 | Capture per YA, by month: salary, bonus, allowances, benefits-in-kind, employee EPF, SOCSO/EIS, zakat paid, departure levy paid and optional other income. Only the months the user has entered are used; a month not entered yet counts as nothing and is never projected or filled in. |
| FR-1.2 | Calculate using the rule set of the selected YA (bands, relief caps, rebates). No rate or cap is hard-coded. |
| FR-1.3 | Show the full chain: total income, deductions, reliefs by category, chargeable income, tax before rebates, rebates, tax payable, PCB paid to date, balance or refund, effective rate and marginal rate. |
| FR-1.4 | Show a band-by-band breakdown of how the tax was reached. |
| FR-1.5 | Compare all stored YAs side by side, including announced rules (for example YA 2027) labelled "announced". |
| FR-1.6 | Recalculate instantly on every change, including offline. |
| FR-1.7 | What-if mode: enter extra spending in a category and see the tax saved. |
| FR-1.8 | **PCB records:** record the PCB deducted each month from the payslip. PCB on a bonus or other additional pay is kept as a separate line. |
| FR-1.9 | **PCB to date:** the regular PCB plus the PCB on bonus or other extra pay of every entered month from January, each counted once. The total is rebuilt after every change, so it follows the latest amounts entered. PCB is not projected for months not entered. |
| FR-1.10 | **PCB against tax:** show PCB to date beside the estimated tax payable on the income entered so far, with the balance to pay or refund, updated whenever reliefs change. While the YA has not ended the balance is labelled "so far"; once it has ended the balance is final (BR-9). The PCB on a bonus is entered apart from the regular PCB and counted once, as in LHDN's PCB 2026 specification. |
| FR-1.11 | **(R2) PCB estimate from salary:** estimate the monthly PCB from salary and relief declarations using LHDN's published PCB calculation method, to compare with the payslip. The method must be verified against LHDN's specification before it is built. |

**Acceptance criteria**

- Chargeable income RM100,000 under YA 2026 rules returns tax of RM9,400.
- Chargeable income RM35,000 returns RM200 (RM600 tax less the RM400 rebate); RM35,001 returns no rebate.
- The section 6 worked example returns RM1,449 under YA 2026 rules and RM1,269 under YA 2027 rules.
- With RM125 PCB recorded for each month from January to October and no bonus, PCB to date is RM1,250; against RM1,449 tax the balance so far is RM199 to pay. A RM300 PCB on a March bonus adds RM300 once (RM1,550 to date).
- With all 12 months entered after the YA has ended, PCB is RM1,500, and against RM1,449 tax the result is a RM51 refund.

### 3.2 Relief categories and ranges

**User story.** As a taxpayer, I want to see every relief category for a YA with its cap, conditions and required proof, so I know what I can claim and how much.

| ID | Requirement |
| --- | --- |
| FR-2.1 | List all categories per YA with: name, group, annual cap, sub-limits, shared-cap group, eligibility conditions, required documents, claim frequency (for example once every 2 YAs). |
| FR-2.2 | Group, search and filter categories; mark each as New or Changed against the previous YA. |
| FR-2.3 | Filter by profile (marital status, children and ages, disability, first-home purchase) so only applicable reliefs show. Every profile question is mandatory; until the profile of a YA is complete, the calculator, relief categories, spending records and dashboard stay locked for that YA. |
| FR-2.4 | Show cap, claimed and remaining amount on each category. |
| FR-2.5 | Ship pre-loaded with the data in section 2; an admin can add or edit rules per YA without a code release. |
| FR-2.6 | Each rule carries a status (Announced, Gazetted, Confirmed against LHDN), a source link and a confirmation date. |
| FR-2.7 | Ship with complete rule sets for YA 2025 (reference), YA 2026 and YA 2027, so 2026 spending can be claimed in 2027 and planning for 2027 can start on 1 January 2027 (section 2.5). |

**Acceptance criteria**

- Opening YA 2025 shows the individual relief as RM9,000; YA 2026 shows RM9,000 and a RM1,000 domestic tourism relief; YA 2027 shows RM12,000 with status Announced.
- Life insurance and EPF shows one combined RM7,000 cap, not two separate caps.
- Switching the YA selector from 2026 to 2027 changes the caps and bands without reloading data.

### 3.3 Spending records

**User story.** As a taxpayer, I want to record each qualifying expense with its receipt, so I can see what counts toward tax relief and keep proof for 7 years.

| ID | Requirement |
| --- | --- |
| FR-3.1 | Create a record with: date, amount (RM), category, merchant, description, payment method, notes and receipt (camera capture, image or PDF). The YA is derived from the date. |
| FR-3.2 | Validate: amount above zero, date inside the YA, category eligible, receipt attached (warning, not a block), possible duplicate (same merchant, date, amount). |
| FR-3.3 | Compute **claimable amount** per record against the remaining category cap, sub-limits and shared caps; display actual spend and claimable amount side by side. |
| FR-3.4 | One expense can be split across categories, but the parts must sum to the total, so it cannot be claimed twice. |
| FR-3.5 | Edit, soft-delete, search and filter by YA, category, date and receipt status. |
| FR-3.6 | Work offline and sync when back online. |
| FR-3.7 | Warn before deleting any record or receipt that belongs to a filed YA. |

**Acceptance criteria**

- Lifestyle spending of RM3,000 shows RM3,000 actual and RM2,500 claimable.
- Adding a vaccination of RM1,500 under medical shows RM1,000 claimable for that sub-limit, and RM500 flagged as over the sub-limit.
- Adding a record while offline appears on the dashboard immediately and syncs later without duplication.

### 3.4 Dashboard

**User story.** As a product owner and taxpayer, I want one view of how much relief I have claimed, how much I can still claim, and what it does to my tax, so I can act before year-end.

| ID | Requirement |
| --- | --- |
| FR-4.1 | A YA selector that defaults to the current YA. |
| FR-4.2 | Summary cards: estimated tax payable, tax saved by reliefs, total relief claimed, total relief still available, PCB paid to date, and the expected balance or refund ("so far" until the YA ends). |
| FR-4.3 | Per category: claimed vs cap as a progress bar, remaining RM, number of receipts, number missing a receipt. |
| FR-4.4 | **Reliefs to claim:** the count of categories with room left, and the list ranked by potential tax saving: the difference in tax payable when that category's room is used, worked out by the calculator. The marginal rate is shown as information. |
| FR-4.5 | Tax payable now vs tax payable if all remaining room were used. |
| FR-4.6 | Multi-year trend of tax payable and relief claimed. |
| FR-4.7 | Alerts: category at 90% or more of its cap, missing receipts, days left in the YA, filing deadline countdown. |
| FR-4.8 | PCB panel: PCB deducted per month for the year, the total to date, and the total against estimated tax payable (FR-1.8 to FR-1.10). Months not entered yet are shown empty. |

**Acceptance criteria**

- A category with RM0 claimed still appears in "reliefs to claim" with its full cap.
- Adding a record updates the cards, the category bar and the tax estimate without a page reload.

### 3.5 User profile and tax-year history

**User story.** As a taxpayer, I want one profile per YA with every fact my reliefs depend on, and a history of my tax years, so the right reliefs are offered and each year keeps the facts it was calculated with.

| ID | Requirement |
| --- | --- |
| FR-0.1 | One profile per user per YA, created the first time in short steps that can be finished later. A new YA's profile starts as a copy of the previous one, so a later change never rewrites an earlier year. |
| FR-0.2 | Ask residency, marital status, the spouse's situation, own disability, pension scheme, first-home loan and the LHDN conditions of each relief. Every visible question is mandatory; until the profile of a YA is complete, F1 to F4 stay locked for that YA (FR-2.3). |
| FR-0.3 | Add, change and remove dependants (children and parents) with the facts that decide their reliefs. Each person keeps one key across the yearly copies and a display name, so history follows the same child and an expense can name who it is for. |
| FR-0.4 | Show the whole profile on one screen: what is answered, what is missing, and which reliefs each answer affects. Compare the profiles of two YAs. |
| FR-0.5 | When a fact changes, the user chooses whether it also applies to later YAs that are not filed. The profile of a filed YA cannot change unless the YA is reopened. |
| FR-0.6 | Tax-year history: for each YA its stage (not started, in progress, calculated, filed), its main result and its saved calculations, each with the profile version it used. Opening a YA leads to its calculator, spending list or dashboard. |
| FR-0.7 | Keep the history of every profile change: who changed what, when, from which value to which, including support. An admin helps with profile fields without seeing income, tax or spending. |
| FR-0.8 | Use and change the profile offline; changes arrive once and in order. Name and language are kept with the profile. The profile is included in the data export (R3) and removed when the account is deleted (launch account). |

### 3.6 Account and security

**User story.** As a taxpayer, I want a private account that only I can open, so my tax data stays mine; as an admin, I want to help people without seeing their data.

Built in parts: the **basic account** in R1, the **launch account** before the public launch, and some parts in R3 (section 9.1).

| ID | Requirement |
| --- | --- |
| FR-5.1 | Create an account with a single-use invitation from an admin, an email and a password (R1). Launch account: public sign-up, and the email is verified before first use. |
| FR-5.2 | Read and accept the data consent before use; see later what was accepted and when; be asked again when the text changes. |
| FR-5.3 | Sign in and out, and be signed out after a period of no use (section 7). Launch account: stay signed in on an own device, and a sign-in lock after repeated failures. |
| FR-5.4 | A forgotten password is handled by an admin sending a temporary reset link (valid 1 hour, single use). Launch account: the user can also ask for one. |
| FR-5.5 | Change the own password and email. R3: see where the account is signed in and sign out another device. |
| FR-5.6 | Use the app offline, and stay safe when a device is shared, lost or offline for a long time. An admin can never see tax data or change a user's email or password. |
| FR-5.7 | Admin account tools: invite people, see the status of accounts, disable or enable an account, send a reset link, without seeing any credential or tax data. |
| FR-5.8 | One Settings screen for language, security, privacy, export and deletion; parts not built yet are hidden. |
| FR-5.9 | Later parts: two-factor login and deletion of the whole account (launch account); the security events screen, data export and deletion of a YA's records once its 7 years have ended (R3). |

## 4. Supporting features and release phasing

Release 1 (MVP) delivers the four core features plus the minimum needed to keep them accurate: a taxpayer profile, household data structures for the later spouse feature, admin support tools, and complete rule sets for YA 2026 and YA 2027. Everything else is phased so the first release stays small.

| Feature | What it does | Release |
| --- | --- | --- |
| Taxpayer profile and dependants | Stores marital status, spouse income status, children with ages and disability status, first-home purchase date; drives which reliefs apply (FR-2.3) | R1 |
| Rule sets for YA 2026 and YA 2027 | Bands, relief caps, rebates and deadlines loaded for both years, plus YA 2025 for reference (FR-2.7) | R1 |
| Yearly rules admin | Admin adds a new YA's bands, caps and rebates, sets status and source; past YAs stay unchanged. Each rule keeps its own change history with a reason per version; taxpayers see "Last changed on" | R1 |
| Audit fields on every record | created\_at, created\_by, updated\_at, updated\_by on every entity; edits to rules and records add a new version, so every change stays in the data (section 5) | R1 |
| Household data structures | Spouse link and joint-assessment fields, tables and test data only, no screens, so R2 can be built and tested on them | R1 |
| Admin support tools | Admin helps with profile details, name and language, and sends a temporary password-reset link (including marital status, children and disability) and runs upload, download or delete on files to help with a failed or broken file, without opening confidential data (section 8) | R1 |
| PWA basics | Installable, offline entry, background sync, secure login | R1 |
| Year-end optimizer | Lists unused room per category and ranks what to spend on before 31 December by tax saved | R2 |
| Spouse and family sharing | Screens for linked profiles, joint assessment calculation and a shared view of who claims what, built on the R1 data structures | R2 |
| PCB estimate from salary | Estimates monthly PCB from salary and relief declarations (FR-1.11) | R2 |
| Reminders and push notifications | Q4 year-end nudge, monthly receipt reminder, filing deadline countdown | R2 |
| Receipt rules engine | Flags non-qualifying items, wrong-year dates, over-cap spending and duplicates | R2 |
| Filing export | PDF and Excel summary ordered like the Form BE relief sections, with a receipt archive | R2 |
| Rule change log view | One combined view of which announcement changed which limit, by YA, read from the version rows and their reasons (R1 keeps the per-rule history) | R2 |
| Bank and e-wallet import | Imports transactions and suggests a relief category | R3 |
| MyTax assisted entry | Export formatted for manual copy into MyTax e-Filing; direct submission is out of scope | R3 |
| Receipt OCR | Reads merchant, date and amount from a photo to pre-fill the record | R4 |
| Non-salary income | Business or other income (Form B), partnership and dividend income | R4 |

**Notes**

- R1 covers the four needs you listed. Nothing in R2, R3 or R4 is required for them to work.
- Direct submission to MyTax is out of scope for all three releases, so filing stays manual and the system prepares the numbers.

## 5. Data model

The key design choice is that every rule (band, cap, rebate) is a row tied to a YA, so a new Budget means new rows, not new code. Computed amounts such as claimable spend are derived at read time; only the final estimate is saved as a snapshot.

**Audit fields on every entity.** Every row carries created\_at, created\_by, updated\_at and updated\_by. When the system itself creates or changes a row (seeding rules, sync jobs, computed snapshots), created\_by and updated\_by hold the id of a reserved SYSTEM user. These fields replace a separate audit table.

One row's updated\_at and updated\_by show only its latest change. To keep **every** movement in the entity itself, the entities marked Yes under Versioned also carry version\_no, is\_current, deleted\_at and deleted\_by. An edit never overwrites: it inserts a new row with the next version\_no and sets is\_current to false on the old one, so the full history stays in the same table.

| Entity | Key fields | Versioned | Notes |
| --- | --- | --- | --- |
| User | id, name, email, role (user, admin or system), status (active, disabled, deletion\_pending), email\_verified\_at, deletion\_requested\_at, deletion\_due\_on, last\_sign\_in\_at | Yes | The reserved SYSTEM row is the default created\_by and updated\_by. The verification and deletion dates are filled from the launch account |
| Credential | user\_id, password\_hash, hash\_algorithm, password\_changed\_at, failed\_attempts, locked\_until, totp\_secret\_encrypted, totp\_enabled, recovery\_codes\_hash | Yes | One per user; never returned by any interface. R1 builds the password fields; the lock fields and two-factor fields come with the launch account |
| Session | id, user\_id, device\_label, remembered, created\_at, last\_seen\_at, expires\_at, revoked\_at, revoked\_reason, token\_hash | No | Hashed token only. R1 builds the session and its expiry; remembered comes with the launch account and device\_label with the R3 device list |
| Invitation | id, code\_hash, created\_by, created\_at, expires\_at, used\_by, used\_at | No | Single use, valid 7 days (R1) |
| ConsentRecord | id, user\_id, purpose, text\_version, language, accepted\_at, withdrawn\_at | No | Insert only, except withdrawn\_at (R1) |
| DataRequest | id, user\_id, type (export, delete, delete\_ya), ya, status, requested\_at, ready\_at, due\_on, expires\_at, file\_ref | Yes | Built with export (R3) and account deletion (launch account) |
| SecurityEvent | id, user\_id, type, at, device\_label, actor\_id, reason, ip\_address | No | Insert only; built with the R3 security events screen. Until then admin actions are traced by the audit fields |
| TaxpayerProfile | user\_id, year, copied\_from\_year, state (draft or active), residency\_status, marital\_status, spouse\_has\_income, spouse\_is\_disabled, pays\_alimony, joint\_assessment, is\_disabled, has\_first\_home, first\_home\_spa\_date, first\_home\_price, dependants\_confirmed, spouse\_foreign\_income\_above\_limit, is\_pensionable\_public\_servant, first\_home\_earns\_income | Yes | One per user per YA, copied forward from the previous YA so a later change never rewrites an earlier year; drives applicable reliefs. Every visible question is mandatory: null only while a question is open or not shown |
| HouseholdLink | user\_id, linked\_user\_id, relationship, joint\_assessment, link\_status | Yes | R1 holds the table and test data; screens and calculation come in R2 |
| Dependant | profile\_id, person\_key, display\_name, type (child or parent), date\_of\_birth, is\_disabled, is\_unmarried, education\_level, relief\_shared, own\_income\_above\_relief | Yes | person\_key is shared by every yearly copy of the same person. Eligibility follows the LHDN condition on each relief rule |
| TaxYear | year, period\_start, period\_end, filing\_deadline, efiling\_deadline, publish\_state, change\_set\_id | Yes | Shared by all users. YA 2027 exists as announced |
| UserTaxYear | user\_id, year, status (open or filed), filed\_on | Yes | "Filed" is per user, so it is not on the shared TaxYear |
| TaxBand | year, income\_from, income\_to, rate, status, source\_url, confirmed\_on, publish\_state, change\_set\_id | Yes | Ordered rows per YA; income\_from is the lower threshold (5,000, not 5,001) |
| ReliefCategory | id, code, name, group, kind (relief or deduction), amount\_source (automatic, profile, income, spending) | Yes | Stable across years |
| ReliefRule | category\_id, year, cap, cap\_basis (fixed, per\_dependant, tiered, percent\_of\_aggregate), cap\_percent\_bp, shared\_cap\_group, eligibility, eligibility\_rule, claim\_frequency, frequency\_n, period\_from\_year, period\_to\_year, max\_claim\_years, required\_documents, needs\_confirmation, notes, retired\_on, change\_reason, status, source\_url, confirmed\_on, publish\_state, change\_set\_id | Yes | One row per category per YA. eligibility\_rule is the machine-readable test next to the text |
| RuleTier | rule\_id, tier\_name, condition, cap, publish\_state, change\_set\_id | Yes | A cap that depends on a fact, such as the first-home price band or the child's education level |
| SubLimit | rule\_id, name, cap, eligibility\_rule, claim\_frequency, frequency\_n, period\_from\_year, period\_to\_year, publish\_state, change\_set\_id | Yes | For example vaccination 1,000 inside medical. A rule that applies to one item of a category is held on its sub-limit, with its own eligibility test and claim frequency: the once-only green-technology items, the child's age by type of childcare centre (approved 23/11/2026, DA-25) |
| RebateRule | year, type, amount, income\_threshold, publish\_state, change\_set\_id | Yes | RM400 rebate, zakat, departure levy |
| IncomeRecord | user\_id, year, month, type, amount, pcb\_monthly, pcb\_additional, epf\_employee, socso\_eis, zakat\_paid, departure\_levy\_paid | Yes | One row per month and type, only for months entered; pcb\_additional is PCB on bonus or other extra pay |
| Expense | user\_id, year, date, amount, merchant, description, payment\_method, notes, do\_not\_claim | Yes | Year derived from date |
| ExpenseAllocation | expense\_id, relief\_category\_id, sub\_limit\_id, allocated\_amount, beneficiary\_dependant\_id | Yes | Splits one expense; parts sum to the total; names who the expense is for when the relief depends on it |
| Receipt | expense\_id, file\_reference, file\_name, file\_size, mime\_type, upload\_state (pending, uploaded, failed), uploaded\_at, retain\_until | Yes | retain\_until = end of YA plus 7 years; a replaced file is a new version; a pending receipt counts as attached |
| TaxEstimate | user\_id, year, chargeable\_income, tax\_before\_rebates, rebates, tax\_payable, pcb\_to\_date, balance, is\_estimate, trigger (user, filed, system), profile\_id, profile\_version\_no, computed\_at | No | Insert-only snapshot for history and comparison, with the profile version it used |

**Data rules**

- Store money as integer sen to avoid rounding errors; display in RM.
- Every record created offline takes a client-generated UUID v7 as its key, so a sync never creates a duplicate.
- A rule change is saved as a draft change set and published as one unit after the calculator tests pass (NFR-10).
- A rule's status (Announced, Gazetted, Confirmed) is selectable, so the calculator can run on announced rules and label the result as an estimate.
- Deleting is soft: deleted\_at and deleted\_by are set on the current version. A ReliefRule used by any Expense cannot be deleted; it is end-dated instead.
- When an admin edits a user's profile or acts on a user's file (upload, download or delete), the admin's id and the reason are written to created\_by or updated\_by and the version history, so support actions are traceable.
- Receipts and records of a filed YA need explicit confirmation to delete (FR-3.7).

## 6. Calculation logic and business rules

Tax payable is the sum of tax on each band, less rebates, never below zero. CI is chargeable income, L and U are a band's lower and upper limits.

```latex
\text{Tax payable} = \max\left(0,\ \sum_{b} \text{rate}_b \times \max\left(0,\ \min(CI, U_b) - L_b\right) - \text{rebates}\right)
```

| ID | Business rule |
| --- | --- |
| BR-1 | The calculator reads the rule set whose year equals the selected YA. A result built on rules with status Announced is labelled "estimate". |
| BR-2 | Claimable amount of an expense = the part that fits in the category's remaining cap. Expenses fill the cap in date order; the rest is shown as over cap. The user can mark an expense "do not claim". |
| BR-3 | Sub-limits apply first (for example vaccination 1,000), then the category cap applies to the sum. |
| BR-4 | Categories in a shared-cap group (life insurance and EPF) use one combined cap, with the limits published on LHDN's site. |
| BR-5 | A category with claim frequency "once every 2 YAs" blocks a second claim in the next YA. |
| BR-6 | The RM400 rebate applies only when chargeable income is RM35,000 or below, so one ringgit more removes it. The calculator must show this cliff when a what-if crosses it. |
| BR-7 | Deductions (donations, professional subscriptions) reduce aggregate income; reliefs reduce chargeable income; rebates reduce tax. The three are never mixed. |
| BR-8 | One expense cannot be claimed under two categories except as a split whose parts sum to the total. |
| BR-9 | Balance = tax payable minus PCB to date (FR-1.9). Nothing is projected. While the YA has not ended the balance is labelled "so far"; once the year is closed, meaning the YA has ended (after 31 December), not that it is filed, the balance is final. A negative balance is shown as a refund estimate. |
| BR-10 | Tax follows LHDN's Form BE method: tax on the first part of chargeable income from the schedule plus the rate times the balance, shown to the sen (RM0.01), not rounded to the ringgit. Bank Negara's 5-sen rounding is for cash and does not apply. A fraction of a sen is rounded half-up until LHDN's treatment of sen in chargeable income is confirmed (finding F-072). |
| BR-11 | Age, status and other eligibility tests (for example a child's age) follow LHDN's published condition for each relief. The ReliefRule records the exact test and its source. |

### Worked example (YA 2026 rules)

A salaried taxpayer earns RM6,000 a month. This case is also the first test for the calculator.

| Step | Amount (RM) | Working |
| --- | --- | --- |
| Total employment income | 72,000 | 6,000 x 12 |
| Individual relief | 9,000 | Automatic |
| EPF and life insurance | 7,000 | EPF 7,920 plus insurance 3,500, capped at the combined 7,000 |
| SOCSO and EIS | 350 | Actual 504, capped at 350 |
| Lifestyle | 2,500 | Spent 3,000, capped at 2,500 |
| Medical | 1,600 | Check-up 600 plus vaccination 1,200 capped at 1,000 |
| Education and medical insurance | 2,400 | Premiums paid, under the 4,000 cap |
| **Total reliefs** | **22,850** |  |
| **Chargeable income** | **49,150** | 72,000 less 22,850 |
| Tax on first 35,000 | 600 | 150 + 450 |
| Tax on 35,001 to 49,150 | 849 | 14,150 x 6% |
| Rebate | 0 | Chargeable income above 35,000 |
| **Tax payable** | **1,449** |  |
| PCB already paid | 1,500 | 125 x 12, every month entered |
| **Balance** | **-51** | Refund estimate of RM51 |

What-if: spending a further RM1,000 on sports gear lowers chargeable income to 48,150 and tax to RM1,389, a saving of RM60 (RM1,000 at the 6% marginal rate).

PCB during the year: RM125 a month recorded from January to October is RM1,250 to date. November and December are not filled in, so against tax of RM1,449 the balance so far is RM199 to pay. Once all 12 months are entered and the YA has ended, PCB is RM1,500 and the taxpayer can expect a refund of RM51.

Same taxpayer under YA 2027 rules: the individual relief rises to RM12,000, so total reliefs are RM25,850 and chargeable income is RM46,150. Tax is RM600 on the first RM35,000 plus RM669 (11,150 x 6%), which is RM1,269, RM180 less than under YA 2026. The bands in this income range do not change.

## 7. Non-functional and PWA requirements

The PWA must work offline for the tasks a taxpayer does daily (add a spending record, check the dashboard) and must treat tax and receipt data as sensitive personal data. Targets below are starting values for the team to confirm.

| ID | Area | Requirement |
| --- | --- | --- |
| NFR-1 | PWA | Web app manifest and service worker so the app installs to the home screen on Android, iOS and desktop. |
| NFR-2 | Offline | Records, rules for the selected YA and the last calculation are cached in the browser (IndexedDB). Entries made offline sync automatically with conflict handling by last edit time per record. |
| NFR-3 | Receipts | Camera capture and file upload; images compressed on the device before upload; upload retried in the background. |
| NFR-4 | Notifications | Web push for reminders where the browser supports it; in-app reminders as the fallback. |
| NFR-5 | Performance | Calculation result in under 200 ms after any change; first meaningful screen in under 2.5 s on a mid-range phone over 4G. |
| NFR-6 | Security | HTTPS only; encrypted storage for data and receipts; role-based access (user, admin); optional two-factor login; session timeout. |
| NFR-7 | Privacy | Before public launch: compliance with Malaysia's Personal Data Protection Act 2010 (as amended): consent at sign-up, purpose limitation, export on request and deletion once the 7-year period of NFR-8 has ended, no tax data in analytics or logs. |
| NFR-8 | Retention | Receipts and records are kept 7 years from the end of the YA. After that the app tells the taxpayer that the records of that YA can be deleted, and the taxpayer deletes them. Nothing is deleted before the 7 years end or automatically. |
| NFR-9 | Audit | Every entity carries created\_at, created\_by, updated\_at and updated\_by, and edits to rules and records add a new version row, so every change stays in the data itself (section 5). |
| NFR-10 | Accuracy | Calculator covered by automated tests built from worked examples (section 6) for every stored YA; a rule change cannot be published if a test fails. |
| NFR-11 | Localisation | English and Bahasa Malaysia; amounts in RM; dates in DD/MM/YYYY. |
| NFR-12 | Accessibility | WCAG 2.1 AA; usable one-handed on a 360 px wide screen. |
| NFR-13 | Availability and backup | Daily backup of data and receipts with a tested restore. Before public launch: 99.5% monthly availability target. |
| NFR-14 | Disclaimer | Every estimate screen states that the figure is an estimate and that LHDN's assessment prevails. |

**Suggested technology direction** (to be decided by the engineering lead): a single-page web app with a service worker and local database, a REST API with a relational database for rules and records, and private object storage for receipts. The tax engine should be one shared, pure function so the same code runs in the browser for offline use and on the server for verification.

**Sign-in values of the basic account (R1)** (approved 23/11/2026): sign-up only with a single-use invitation code from an admin, valid 7 days; passwords of 12 to 128 characters, checked against a list of common passwords, with no composition rules and no forced change; a session ends 14 days after the last server contact for a taxpayer and 30 minutes for an admin. The launch account values (email verification, sign-in lock, staying signed in, two-factor login) wait for the owner (section 9.4).

**Personal use in R1.** R1 serves one user, so the items marked "before public launch" (NFR-7 and NFR-13) are built for the public launch, not R1. Encryption, backups, offline sync and the accuracy tests (NFR-10) stay in R1.

**Hosting.** The choice is split in two. For the product owner's personal use in R1, DigitalOcean or AWS both work. Before the public launch, the hosting location must be decided against PDPA compliance; this is not a government system, so assume the PDPA applies in full once it is public. Facts to weigh:

- AWS has a Malaysia region (ap-southeast-5, three availability zones) that opened in August 2024 ([AWS announcement](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-malaysia-region/)).
- DigitalOcean lists 16 datacenters for new resources and none is in Malaysia; the nearest is Singapore, SGP1 ([DigitalOcean regional availability](https://docs.digitalocean.com/platform/regional-availability/), verified 28 October 2026).
- Under the PDPA as amended in 2024, personal data may leave Malaysia only when a listed condition is met, such as the person's consent or equivalent protection in the destination, backed by an impact assessment and transfer records; the change took effect on 1 April 2025 ([Rödl newsflash](https://www.roedl.com/en/insights/malaysia-part3-personal-data-protection-amendment-act-2024/)).

For personal use in R1, either provider works. At the public launch, a Malaysian region avoids the cross-border question, while Singapore would need a documented basis; confirm this with a PDPA adviser. Building on portable parts (containers, PostgreSQL, S3-compatible object storage) keeps a later move to a deployment change.

## 8. Screens, user flow and roles

A taxpayer's year follows one loop: set up once, add spending as it happens, check the dashboard, and export before filing.

**Main user flow**

1. Sign up and accept the data consent.
2. Complete the profile and dependants.
3. Pick the YA (defaults to the current one) and enter income, EPF, SOCSO and PCB.
4. Add each qualifying expense with its receipt when it happens.
5. Open the dashboard to see claimed, remaining and estimated tax.
6. In the final quarter, use the reliefs-to-claim list and what-if to decide remaining spending.
7. Export the summary before filing Form BE.

**Screens**

| Screen | Purpose | Requirements | Release |
| --- | --- | --- | --- |
| Sign in and onboarding | Account, consent, language | FR-5.1 to FR-5.4, NFR-6, NFR-7 | R1 |
| Profile and dependants | Drives applicable reliefs | FR-0.1 to FR-0.5, FR-0.7, FR-2.3 | R1 |
| Tax-year history | Stage and result of each YA, saved calculations | FR-0.6 | R1 |
| Dashboard | Claimed, remaining, estimated tax, PCB panel | FR-4.1 to FR-4.8 | R1 |
| Tax calculator | Chain, band breakdown, what-if | FR-1.1 to FR-1.7 | R1 |
| Relief catalogue and detail | Caps, conditions, proof, expenses under each category | FR-2.1 to FR-2.4 | R1 |
| Add or edit spending | Form with camera capture, split lines | FR-3.1 to FR-3.4 | R1 |
| Spending list | Search and filter, receipt status | FR-3.5 | R1 |
| Income and PCB | Monthly salary, EPF, SOCSO, PCB, zakat | FR-1.1 | R1 |
| Year comparison | Side-by-side YAs | FR-1.5, FR-4.6 | R1 |
| Settings | Language, password and email; data export (R3) and deletion (launch account) appear when built | FR-5.5, FR-5.8, NFR-7 | R1 |
| Admin: rules manager | Bands, relief rules, rebates, status, source, change history per rule with reasons | FR-2.5, FR-2.6 | R1 |
| Admin: accounts | Invite, status, disable or enable, send a reset link | FR-5.7 | R1 |
| Year-end optimizer | Unused room ranked by tax saved | Section 4 | R2 |

**Roles and permissions**

| Capability | User | Admin |
| --- | --- | --- |
| Manage own account and profile: name, email, language, marital status, spouse status, children and dependants, disability | Yes | Profile, name and language only, on the user's behalf; never the email or the password |
| Manage own income, PCB, spending, receipts and tax estimates | Yes | No |
| See confidential data: income, PCB, spending amounts, tax estimates, receipt contents | Own data only | No |
| View rules, run the calculator | Yes | Yes |
| Create or edit rules per YA and set rule status | No | Yes |
| View change history of rules | No | Yes |
| Disable or enable user accounts; send a user a temporary password-reset link | No | Yes |
| Upload, download or delete a user's files on request, by file name and type only, to help with a failed or broken file | Own files | Yes |

Admin support covers the full profile (name and language, marital status, spouse status, children and dependants, disability) and upload, download and delete actions on files. Admins never open confidential data: income, PCB, spending, tax estimates or receipt contents, which only the profile owner manages. A file an admin downloads goes to the admin only to help with a failed or broken file; the admin does not open its contents and is personally responsible for the file and whatever happens to it (approved 23/11/2026). An admin cannot change a user's email or password: for a forgotten password the admin sends the user a temporary reset link (valid 1 hour, single use) and never sees the link or the new password. An admin sees a Filed flag for each YA (whether the taxpayer has finished it) but no stage and no figures. Each admin action is written to the row's created\_by or updated\_by (section 5).

## 9. Roadmap, risks and open questions

R1 should be live early enough to enter YA 2026 receipts before filing in 2027 and to track YA 2027 from 1 January 2027, when the Budget 2027 changes begin. Durations are for the engineering lead to estimate.

### 9.1 Phases and exit criteria

| Phase | Scope | Exit criteria |
| --- | --- | --- |
| 0. Discovery | Research decision 4; verify every rule in section 2 for YA 2025, 2026 and 2027 against LHDN and Ministry of Finance documents; choose the stack | Each rule marked Confirmed, or Announced with a source; decision 4 answered |
| 1. R1 build | Four core features with PCB to date (no projection), the profile and tax-year history (section 3.5), household data structures, rule sets for YA 2026 and YA 2027, rules admin, admin support tools, audit fields, PWA offline; the **basic account** of account and security (section 3.6): invitation-only sign-up, password sign-in, a simple session, the consent record, change of the own password and email, a temporary reset link sent by an admin, admin account tools and the Settings screen (SD-F5-17, approved 14/11/2026) | All R1 FR and NFR items pass; calculator tests match section 6 for YA 2025, 2026 and 2027 |
| 2. Personal use | The product owner enters real YA 2026 receipts and tracks YA 2027 from 1 January 2027 | Estimate matches an independent calculation for YA 2026; no data loss from offline sync; owner judges the features proven |
| 3. R2 | Year-end optimizer, spouse sharing and joint assessment on the R1 structures, PCB estimate from salary, reminders, filing export, receipt rules | Spouse flows tested with the R1 test data; export layout accepted by a tax-literate reviewer |
| 4. R3 | Bank and e-wallet import, MyTax assisted entry; from account and security: data export, deletion of the records of a YA once its 7 years have ended (with its notice), the security events screen, the new-device notice and the session controls (SD-F5-19, approved 22/11/2026) | Per-feature acceptance set before start |
| 5. R4 | Receipt OCR, non-salary income | Per-feature acceptance set before start |
| Public launch gate | Decided by the owner once the features are proven; the **launch account** of account and security is built before it: sign-in lockout, emailed links (verification, self-service forgot password, email change), staying signed in, two-factor login, deletion of the whole account (SD-F5-17) | Items marked "before public launch" done: consent, user export and deletion, two-factor login, availability target, hosting decision, PDPA review. User export is built with R3, so whether the launch waits for R3 is still open (finding F-058) |

### 9.2 Risks

| Risk | Effect | Mitigation |
| --- | --- | --- |
| Rule data is wrong, or an announced measure changes before it becomes law | Wrong tax estimate | Status on every rule, source link and confirmation date; estimate label; admin verification before publish |
| Taxpayer relies on the estimate and over-claims | Penalty risk at LHDN review | Disclaimer on every estimate; receipt and eligibility checks; 7-year receipt retention |
| Receipts and income data leak | Personal data breach under PDPA | Encryption, private storage, no admin access to confidential data, audit fields on every entity |
| Offline sync creates duplicates or lost edits | Wrong claimed totals | Client-generated record IDs; conflict handling per record; sync tests |
| iOS limits on push and storage in PWAs | Missed reminders; cleared offline cache | In-app reminders; server as the source of truth; export option |
| Scope grows into e-Filing submission | Delay | Out of scope; export only |
| Opening to the public before the PDPA and hosting work is done | Legal exposure and a data breach affecting other people | Public launch gate in 9.1; no public sign-up until it is passed |

### 9.3 Decisions and open items

| # | Question | Decision or status | Effect on this PRD |
| --- | --- | --- | --- |
| 1 | Who uses v1? | Product owner only; opens to the public once the features are proven | Section 1 assumptions; public-launch items in sections 7 and 9 |
| 2 | Spouse sharing and joint assessment | Build in R2; the data structures are ready in R1 so R2 can be developed and tested | Household data structures in R1; screens and calculation in R2 |
| 3 | OCR and non-salary income | Moved to R4 | Section 4 |
| 4 | Education and medical insurance cap (RM3,000 in one source, RM4,000 in another) | **Answered for YA 2025 (12/11/2026, OI-F2-01):** LHDN gives RM4,000 for YA 2025 and RM3,000 for YA 2018 to YA 2024. YA 2026 and YA 2027 carry RM4,000 forward until LHDN prints their tables | Section 2.3; the YA 2026 and YA 2027 values are confirmed at the phase 0 verification |
| 5 | EPF and life insurance caps | **Answered (12/11/2026, OI-F2-02):** combined cap RM7,000; RM4,000 for mandatory EPF and RM3,000 for life insurance, family takaful and additional voluntary EPF (LHDN, YA 2023 to YA 2025) | BR-4; section 2.3; YA 2026 and YA 2027 confirmed at verification |
| 6 | Admin access to user data | Admin manages the full profile (including marital status, children and disability) and upload, download and delete of files. Admin never accesses income, tax, PCB, spending or receipts; the profile owner manages those | Section 8 roles; data rule on admin actions |
| 7 | Child age test and rounding | Follow LHDN's condition for each relief; tax worked out by LHDN's Form BE method, to the sen, not by Bank Negara's cash rounding (23/11/2026) | BR-10, BR-11 |
| 8 | Hosting | Split: the owner's personal use first on DigitalOcean or AWS; before public launch, the hosting location is decided against PDPA compliance. Not a government system; it only displays tax information | Hosting note in section 7; public launch gate |
| 9 | Audit design | Confirmed as needed: audit fields on every entity, with every change kept in the entity itself. Implemented as a new version row per edit | Section 5 |
| 10 | PCB projection | No projection: only the months entered count; PCB and balance are "to date" until the YA ends (23/11/2026) | FR-1.1, FR-1.9, FR-1.10, FR-4.2, FR-4.8, BR-9, section 6 |
| 11 | Account tables | All six approved, built by phase: Credential, Session, Invitation and ConsentRecord in R1; DataRequest and SecurityEvent and the later fields with their part (23/11/2026) | Section 5 |

### 9.4 Items waiting for owner approval

These changes come from the URS and SRS documents. They are **proposals, not part of this PRD yet**. Each one waits for the owner's approval and then is written in here with a Synced entry. The full list is Pending PRD sync in [REG-02](../registers/REG_02_URS_SRS_Change_Log.md#pending-prd-sync). On 23/11/2026 the owner approved items 1 to 10, 14, 15, 17, 20, 21, 25 and the basic account part of item 22; they are synced in revision 53. The owner keeps the rest for the launch account and R3.

| Item | PRD place | Proposal | Status |
| --- | --- | --- | --- |
| 22 (launch account part) | Section 7, NFR-6 | Email verified before first use (link 24 hours); 5 failed sign-ins in 15 minutes lock the account for 15 minutes; emailed links valid 1 hour and 24 hours; 2 hours on a shared device | Waiting for owner approval (kept for the launch account) |
| 23 | Section 7 Settings, NFR-7, NFR-8 | Export as a ZIP (R3); deletion of the whole account with a 14-day grace period (launch account); backups purged 35 days after an erase; consent purposes and text headings | Waiting for owner approval (kept for later) |
| 24 | NFR-6 | Two-factor by authenticator app, optional for taxpayers, required for admins; no SMS; 10 recovery codes (launch account) | Waiting for owner approval (kept for the launch account) |

### Sources

Pages opened for this document; all figures were read on 7 November 2026.

- [Finance Act 2025, Act 874](https://www.hasil.gov.my/wp-content/uploads/Akta-Kewangan-2025-Akta-874.pdf), [LHDN Public Ruling No. 5/2026](https://www.hasil.gov.my/wp-content/uploads/20261104-PR-5_Taxation-Of-A-Resident-Individualpart-I-Gifts-Or-Contributions-And-Allowable-Deductions.pdf), [LHDN tax rate page](https://www.hasil.gov.my/en/individu/kadar-cukai/) and [Budget 2027 tax measures](https://belanjawan.mof.gov.my/pdf/belanjawan2027/ucapan/tax-measures.pdf), read on 23 November 2026 (RES-002, F-063)
- [LHDN, tax reliefs](https://www.hasil.gov.my/en/individual/individual-life-cycle/income-declaration/tax-reliefs/?pg=) and [LHDN, Maximise your tax relief leaflet](https://www.hasil.gov.my/wp-content/uploads/T2026_maximise-your-tax-relief.pdf), read on 12 November 2026 for decisions 4 and 5 (F-029)
- [3E Accounting, Malaysia Personal Income Tax Rate](https://www.3ecpa.com.my/resources/malaysia-taxation/individual-income-tax/malaysia-personal-income-tax-rate/)
- [RinggitPlus, Everything You Can Claim As Income Tax Relief (YA 2025)](https://ringgitplus.com/en/blog/tax/everything-you-can-claim-as-income-tax-relief-in-malaysia-2026-filing-for-ya-2025.html)
- [BrioHR, Key Tax Relief Updates for 2026](https://support.briohr.com/knowledge/payroll-malaysia-key-tax-relief-updates-for-the-year-2026)
- [RinggitPlus, Budget 2027: What Changes For Your Money](https://ringgitplus.com/en/blog/budget-2027/budget-2027-what-changes-for-your-money-in-2027.html)
- [AWS, Now open: AWS Asia Pacific (Malaysia) Region](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-malaysia-region/)
- [DigitalOcean, Regional Availability](https://docs.digitalocean.com/platform/regional-availability/)
- [Rödl, Cross Border Personal Data Transfer Guidelines (PDPA)](https://www.roedl.com/en/insights/malaysia-part3-personal-data-protection-amendment-act-2024/)
