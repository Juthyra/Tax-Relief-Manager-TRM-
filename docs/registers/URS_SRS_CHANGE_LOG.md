# URS and SRS Change Log: Malaysia Tax Relief System (PWA)

This file records **every detail change** to the six URS and SRS documents (F0 profile, F1 to F4 core features and F5 account and security). The main log of our work is [HISTORY_LOG.md](../registers/HISTORY_LOG.md); this log is the detail log for the documents only.

Owner: Champs (product owner)
Started: 2026-11-12
Last updated: 2026-11-18 (F0 at version 0.3, F1 to F4 at version 0.5, F5 at version 0.2)

## How this log works

1. **Version numbers.** Each document starts at 0.1 (first draft). Any change to an ID, a number, a rule or a diagram raises the minor version (0.2, 0.3). When the owner approves a document it becomes 1.0. After that, changes raise 1.1, 1.2.
2. **One entry per detail.** Every change gets the next CHG number and states: the document, the section, the ID changed, the type, what it said before, what it says now, why, and which prompt or finding caused it.
3. **Change types:** Added, Changed, Removed, Clarified, Decided (owner answered an SD or OI), Synced (the PRD was updated to match).
4. **Shared blocks.** The system map FD-00, the interface table (IF-01 to IF-21), the events (EV-01 to EV-08), the data ownership table, the data additions (DA-01 to DA-24) and the category codes are identical in all six documents. A change to one of them is applied to all four in the same CHG entry.
5. **IDs are never reused.** A removed ID stays in the register with status Removed.
6. **Status in the register:** Draft (written, not reviewed), Needs owner decision (SD), Open (OI), Approved, Changed, Removed.

## Document register

| Doc | File | Feature | Version | Date | State | URS | SRS | Flow diagrams (FD) | Sequence (SQ) | Test cases | SD | OI | Lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F0 | [URS_SRS_F0_User_Profile.md](URS_SRS_F0_User_Profile.md) | User profile and tax-year history | 0.3 | 2026-11-13 | Draft for owner review | 15 | 19 | 8 | 1 | 26 | 14 | 4 | 775 |
| F1 | [URS_SRS_F1_Tax_Calculator.md](URS_SRS_F1_Tax_Calculator.md) | Tax calculator and PCB | 0.5 | 2026-11-13 | Draft for owner review | 16 | 24 | 8 | 1 | 22 | 10 | 4 | 759 |
| F2 | [URS_SRS_F2_Relief_Categories.md](URS_SRS_F2_Relief_Categories.md) | Relief categories and rule sets | 0.5 | 2026-11-13 | Draft for owner review | 12 | 17 | 7 | 0 | 24 | 9 | 3 | 646 |
| F3 | [URS_SRS_F3_Spending_Records.md](URS_SRS_F3_Spending_Records.md) | Spending records | 0.5 | 2026-11-13 | Draft for owner review | 15 | 18 | 8 | 1 | 23 | 4 | 4 | 722 |
| F4 | [URS_SRS_F4_Dashboard.md](URS_SRS_F4_Dashboard.md) | Dashboard | 0.5 | 2026-11-13 | Draft for owner review | 13 | 16 | 7 | 1 | 19 | 7 | 2 | 672 |
| F5 | [URS_SRS_F5_Account_Security.md](URS_SRS_F5_Account_Security.md) | Account and security | 0.2 | 2026-11-13 | Draft for owner review | 14 | 21 | 13 | 2 | 29 | 18 | 7 | 982 |
| | Total | | | | | 85 | 115 | 51 | 6 | 143 | 62 | 24 | |

Shared across all six: 21 interfaces, 8 events, 24 data additions, 26 category codes (R01 to R24, D01, D02), the FD-00 system map.

## Change register

| CHG | Date | Doc | Section | ID | Type | Before | After | Reason | Trigger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CHG-001 | 2026-11-12 | F1 | Whole document | URS-F1-01 to URS-F1-15, SRS-F1-01 to SRS-F1-22, FD-F1-01 to FD-F1-08, SQ-F1-01, TC-F1-01 to TC-F1-20, SD-F1-01 to SD-F1-09, OI-F1-01 to OI-F1-04 | Added | Nothing | Version 0.1 | First draft of the tax calculator and PCB URS and SRS from PRD section 3.1 | Prompt P-08 |
| CHG-002 | 2026-11-12 | F2 | Whole document | URS-F2-01 to URS-F2-12, SRS-F2-01 to SRS-F2-17, FD-F2-01 to FD-F2-07, TC-F2-01 to TC-F2-23, SD-F2-01 to SD-F2-09, OI-F2-01 to OI-F2-03 | Added | Nothing | Version 0.1 | First draft of relief categories and rule sets, from PRD section 3.2 and the admin rules (sections 4 and 8) | Prompt P-08 |
| CHG-003 | 2026-11-12 | F3 | Whole document | URS-F3-01 to URS-F3-14, SRS-F3-01 to SRS-F3-17, FD-F3-01 to FD-F3-08, SQ-F3-01, TC-F3-01 to TC-F3-22, SD-F3-01 to SD-F3-04, OI-F3-01 to OI-F3-04 | Added | Nothing | Version 0.1 | First draft of spending records, from PRD section 3.3 | Prompt P-08 |
| CHG-004 | 2026-11-12 | F4 | Whole document | URS-F4-01 to URS-F4-13, SRS-F4-01 to SRS-F4-16, FD-F4-01 to FD-F4-07, SQ-F4-01, TC-F4-01 to TC-F4-19, SD-F4-01 to SD-F4-07, OI-F4-01 to OI-F4-02 | Added | Nothing | Version 0.1 | First draft of the dashboard, from PRD section 3.4 | Prompt P-08 |
| CHG-005 | 2026-11-12 | F1, F2, F3, F4 | A5 and B2 | FD-00, IF-01 to IF-15, EV-01 to EV-05, data ownership table, DA-01 to DA-15, category codes | Added | Nothing | Identical blocks in all four documents | Makes the four documents one connected set: every interface names a provider SRS and a consumer SRS | Prompt P-08 |
| CHG-006 | 2026-11-12 | F1 | SRS-F1-10, TC-F1-11 | SRS-F1-10, TC-F1-11 | Clarified | Cliff message wording unclear; TC-F1-11 had no numbers | Cliff message shown from RM 35,000.01 to RM 36,000.00; TC-F1-11 states tax before rebates 570.00, payable 170.00, saved 490.00 | Found while checking values by script, before first review | Self-check |
| CHG-007 | 2026-11-12 | F1, F2 | SRS-F1-18, IF-09 | SRS-F1-18, IF-09 | Added | Scenarios: no_reliefs, use_room, use_all_room | Added scenario as_recorded (estimate for any stored YA) | The F4 trend needs an estimate for each YA, not only the selected one | Self-check while writing F4 (SRS-F4-07) |
| CHG-008 | 2026-11-12 | F1, F2, F3, F4 | DA-05, DA-11, seed D01 | DA-05, DA-11, D01 | Changed | DA-05 had three cap bases; DA-11 had file name and size only | DA-05 adds percent_of_aggregate and cap_percent_bp; DA-11 adds upload_state | Donation cap is a percentage of income; a pending receipt must count as attached | Self-check while writing F3 |
| CHG-009 | 2026-11-12 | F2 | SRS-F2-02, SRS-F2-04, TC-F2-03, TC-F2-05, TC-F2-06 | same | Clarified | Search fields omitted sub-limit names; JSON operators written with a pipe that breaks the table; TC-F2-03 listed four changed categories; TC-F2-06 listed only four rows | Search includes sub-limit names; operators written as a list; TC-F2-03 lists seven changed categories; TC-F2-06 allows other categories with room | Corrected against the PRD table before first review | Self-check |
| CHG-010 | 2026-11-12 | F3 | SRS-F3-15 | SRS-F3-15 | Clarified | A prefilled YA always set the date to a day not after today | Date rule per case: ended YA gives 31 December; current YA gives today; a YA not started leaves the date empty | A future date is a validation error | Self-check |
| CHG-011 | 2026-11-12 | F2 | A6 item 3, SRS-F2-08, OI-F2-01 | OI-F2-01, SRS-F2-08 | Decided | R17 loaded at RM 4,000 and marked needs_confirmation for every YA; OI-F2-01 open | R17 is RM 4,000 per LHDN for YA 2025 (RM 3,000 applied to YA 2018 to YA 2024); needs_confirmation stays only for YA 2026 and YA 2027 | LHDN tax reliefs page read on 2026-11-12 answers PRD decision 4 for YA 2025 | Prompt P-09, finding F-029 |
| CHG-012 | 2026-11-12 | F2 | SRS-F2-14, TC-F2-10, B3.2, OI-F2-02 | OI-F2-02, SRS-F2-14, TC-F2-10 | Decided | Group cap 7,000 with no sub-limits; EPF 2,000 plus insurance 6,000 gave 7,000 | R14 EPF capped at 4,000 and R15 life insurance at 3,000 inside the group cap of 7,000; the same inputs now give 5,000; TC-F2-10 now expects room 0 on both members | LHDN lists RM 4,000 and RM 3,000 sub-limits for YA 2023 to YA 2025; answers PRD decision 5 | Prompt P-09, finding F-029 |
| CHG-013 | 2026-11-12 | F3 | SRS-F3-07, TC-F3-08 | SRS-F3-07, TC-F3-08 | Changed | TC-F3-08: EPF applied 7,000 and insurance 0 (group cap only) | EPF applied 4,000 and insurance 3,000 with CATEGORY_CAP 500; second case added (5,000 combined); additional voluntary EPF is entered under R15 | Follows CHG-012 | Prompt P-09 |
| CHG-014 | 2026-11-12 | F1 | TC-F1-05, B3.3 | TC-F1-05 | Clarified | Worked example showed EPF and insurance as one capped 7,000 | Shows EPF counted to 4,000 and insurance to 3,000; every total is unchanged (22,850.00, 49,150.00, 1,449.00) | Follows CHG-012; the worked example result does not change | Prompt P-09 |
| CHG-015 | 2026-11-12 | F4 | B3.2 note | none | Clarified | R17 used "RM 4,000 pending decision 4" | R17 uses the LHDN YA 2025 figure carried forward; no number changes | Follows CHG-011 | Prompt P-09 |
| CHG-016 | 2026-11-12 | F1, F2, F3, F4 | B2.3 category codes (shared) | R14, R15, R17 | Changed | R14 and R15 "own sub-limit to be loaded from LHDN"; R17 "4,000 (confirm)" | R14 category cap 4,000; R15 category cap 3,000 (includes additional voluntary EPF); R17 4,000 with a source note; same text in all four documents | Shared block, applied to all four in one entry (rule 4) | Prompt P-09 |
| CHG-017 | 2026-11-12 | F1, F2, F3, F4 | Header | Document version | Changed | 0.1 | 0.2 | CHG-011 to CHG-016 | Prompt P-09 |
| CHG-018 | 2026-11-13 | F0 | Whole document | URS-F0-01 to URS-F0-13, SRS-F0-01 to SRS-F0-18, FD-F0-01 to FD-F0-08, SQ-F0-01, TC-F0-01 to TC-F0-24, SD-F0-01 to SD-F0-13, OI-F0-01 to OI-F0-04 | Added | Nothing | Version 0.1 of the profile document: guided creation, profile screen, one profile per YA, apply to later YAs, lock of a filed YA, tax-year history, comparison, change history, admin support | Owner asked for a profile document covering how to create a profile, the profile screen and the history of tax years | Prompt P-13, F-032, F-033 |
| CHG-019 | 2026-11-13 | F0, F1, F2, F3, F4 | A5 and B2 shared blocks | FD-00, IF-11 to IF-13, IF-16, IF-17, EV-03, EV-06, data ownership table, DA-16 to DA-20 | Changed | The profile was an unnamed supporting feature; IF-11 to IF-13 had no provider spec; EV-03 named no YA; the ownership table had a Profile column; DA-01 to DA-15 | The profile is document F0; IF-11 to IF-13 point to SRS-F0-15; IF-16 (F1 to F0) and IF-17 (F0 to F1, F3, F4) added; EV-03 carries the YA; EV-06 YearStatusChanged added; the ownership column is F0 with rows for UserTaxYear and TaxEstimate; DA-16 to DA-20 added; FD-00 redrawn with F0 and Admin support | Gives the profile its own owner and makes a profile per YA and the history possible | Prompt P-13 |
| CHG-020 | 2026-11-13 | F1 | SRS-F1-01, SRS-F1-04, SRS-F1-15, SRS-F1-19, SRS-F1-21, A5.4, B2.1, FD-F1-02, data diagram, SQ-F1-01 | same | Changed | One profile per user; EV-03 recalculated every YA; snapshots kept no profile reference; filing raised only EV-02 | F1 reads the profile of the selected YA; recalculates only the YA in EV-03; each snapshot stores profile_id and profile_version_no (DA-18); mark as filed and reopen raise EV-06; opens on a YA chosen in the F0 history (IF-17); diagram names updated | Follows CHG-019 | Prompt P-13 |
| CHG-021 | 2026-11-13 | F1 | SRS-F1-23, TC-F1-21, SD-F1-10, matrix row URS-F1-05 | SRS-F1-23, TC-F1-21, SD-F1-10 | Added | Nothing | Tax-year summary for the history (IF-16) with its test and decision | F0 shows the figures of each YA and must not calculate them | Prompt P-13 |
| CHG-022 | 2026-11-13 | F2 | SRS-F2-04, SRS-F2-05, TC-F2-11, TC-F2-24, A5.4, B2.1, interface diagram | same | Changed | Facts came from "the profile"; no rule for an unconfirmed dependants list; R06 had no source for the home price | Facts come from the selected YA's profile; adds has_first_home, first_home_price and dependants_confirmed; the dependant count test is unknown while dependants_confirmed is false; R06 tiers read first_home_price; R21 and R22 read education_level; TC-F2-24 added | Follows CHG-019; F-036 | Prompt P-13 |
| CHG-023 | 2026-11-13 | F3 | SRS-F3-02, SRS-F3-14, SRS-F3-15, A5.4, B2.1, interface diagram | same | Changed | Beneficiary choices from "the profile"; EV-03 recalculated every YA | Choices come from the profile of the YA the date falls in; a removed dependant shows "(removed)" on old expenses; recalculates on EV-03 for its YA only; the list opens from the F0 history (IF-17) | Follows CHG-019 | Prompt P-13 |
| CHG-024 | 2026-11-13 | F4 | SRS-F4-01, SRS-F4-10, A5.4, FD-F4-02, live-update diagram | same | Changed | Listened to EV-01 to EV-05 | Also listens to EV-06 and opens on a YA chosen in the F0 history (IF-17) | Follows CHG-019 | Prompt P-13 |
| CHG-025 | 2026-11-13 | F0, F1, F2, F3, F4 | Section 0 and the DA row of 0.2 | "four documents" text; DA location "section B2.3" | Clarified | The text said four documents; the DA row named section B2.3, which was the wrong section in F1 to F4 | The text says five documents; the DA row says "Part B2 under Data additions" | Five documents now; a wrong cross-reference found while editing | Prompt P-13 |
| CHG-026 | 2026-11-13 | F0, F1, F2, F3, F4 | B2.3 category codes (shared) | R06 | Changed | R06 "tiered by home price" with no field that holds the price | R06 tiered by home price (profile fact first_home_price, DA-19) | F-036 | Prompt P-13 |
| CHG-027 | 2026-11-13 | F0, F1, F2, F3, F4 | Header | Document version | Changed | F1 to F4 at 0.2 | F1 to F4 at 0.3; F0 at 0.1 | CHG-018 to CHG-026 | Prompt P-13 |
| CHG-028 | 2026-11-13 | F5 | Whole document | URS-F5-01 to URS-F5-13, SRS-F5-01 to SRS-F5-20, FD-F5-01 to FD-F5-12, SQ-F5-01, SQ-F5-02, TC-F5-01 to TC-F5-28, SD-F5-01 to SD-F5-16, OI-F5-01 to OI-F5-07 | Added | Nothing | Version 0.1 of the account and security document: sign-up, verification, consent, sign-in, two-factor login, sessions, password and email, settings, export, deletion, admin account tools | The owner asked for it ("as it a specification we need", "please do it and share to me") and answered OI-F0-01; closes F-041 | Prompts P-14, P-15 |
| CHG-029 | 2026-11-13 | F0, F1, F2, F3, F4, F5 | Section 0, A5 and B2 shared blocks | FD-00, IF-18 to IF-21, EV-07, EV-08, data ownership table, DA-21 to DA-24, terms Session, Fresh sign-in, Grace period, Retention period | Added | Five documents; 17 interfaces, 6 events, 20 data additions; ownership table without an account owner | Six documents; 21 interfaces, 8 events, 24 data additions; F5 column and account rows in the ownership table; DA table has a Status column | F5 gives every feature its identity, export and erase; the owner's decisions of 13/11/2026 are shown where the data additions are listed | Prompts P-14, P-15 |
| CHG-030 | 2026-11-13 | F0, F1, F2, F3, F4, F5 | B8 of F0; DA table (shared) | SD-F0-01, DA-16, DA-19, OI-F0-01, OI-F0-04, DA-20 | Decided | SD-F0-01 "to be confirmed"; DA-16 and DA-19 proposed; OI-F0-01 and OI-F0-04 open | SD-F0-01, DA-16 and DA-19 approved on 13/11/2026; OI-F0-01 answered (own document F5); OI-F0-04 answered (admin sees a Filed flag only, no stage and no figures); DA-20 stays proposed, explained, awaiting the owner's yes | Owner's replies to the six items | Prompt P-14 |
| CHG-031 | 2026-11-13 | F0 | A1, A2, A3, A5.4, SRS-F0-01, SRS-F0-02, SRS-F0-16, SRS-F0-19 (new), B2.1, B5, B6, B7, FD-F0-02, FD-F0-03, OI-F0-03 | URS-F0-14, SRS-F0-19, TC-F0-25 added; SRS-F0-01, SRS-F0-02, SRS-F0-16, OI-F0-03 changed | Changed | Account step asked name, email and language; an admin could change account details including the email; F0 had no export or erase part; sign-in was "out of scope" with no owner | Account step asks name and language and shows the email read only; an admin cannot change the email or the password; F0 supplies its export part and erases its data (IF-19, IF-20); sign-in is specified in F5; change history is deleted with the account | Moves the account to F5 (SD-F5-13) and applies SD-F5-10 | Prompt P-15 |
| CHG-032 | 2026-11-13 | F1 | A3, A5.4, SRS-F1-24 (new), B5, B6, B7 | URS-F1-16, SRS-F1-24, TC-F1-22 | Added | Nothing | F1 supplies its export part, erases income, filed status and saved calculations, and reads the identity from F5 | IF-18 to IF-20 and EV-07, EV-08 need a provider in F1 | Prompt P-15 |
| CHG-033 | 2026-11-13 | F3 | A3, A5.4, SRS-F3-18 (new), B5, B6, B7 | URS-F3-15, SRS-F3-18, TC-F3-23 | Added | Nothing | F3 supplies its export part with the receipt files, erases rows and stored files, and reads the identity from F5 | IF-18 to IF-20 and EV-07, EV-08 need a provider in F3 | Prompt P-15 |
| CHG-034 | 2026-11-13 | F2, F4 | Section 0 | Shared text "five documents" | Changed | Five documents | Six documents; the shared blocks changed, so the documents move to version 0.4. F2 and F4 get no new SRS row (OI-F5-05) | Keeps the six documents one set | Prompt P-15 |
| CHG-035 | 2026-11-13 | F0, F1, F2, F3, F4, F5 | Header | Document version | Changed | F0 at 0.1; F1 to F4 at 0.3 | F0 at 0.2; F1 to F4 at 0.4; F5 at 0.1 | CHG-028 to CHG-034 | Prompt P-15 |
| CHG-036 | 2026-11-14 | F0 | A5, A5.4, A3, SRS-F0-01, SRS-F0-02, SRS-F0-03, SRS-F0-04, SRS-F0-07, SRS-F0-15, SRS-F0-18, B3.1, B3.3, B3.4, B4, B6, TC-F0-02, TC-F0-03, TC-F0-07, B8, FD-F0-03 | URS-F0-15, SD-F0-14, TC-F0-26 added; the SRS and TC listed changed | Changed | Yes, No and not answered; only residency, marital status and spouse income were required; three profile statuses (Incomplete, Basic, Complete); a missing answer left a relief "unknown" and nothing was blocked; "Skip for now" on every optional step | Every visible question is mandatory (marital status is a choice of four statuses); two statuses (Incomplete, Complete); a hard gate: while a YA's profile is Incomplete, F1 to F4 do not calculate, show reliefs or accept income or expenses for that YA; no Skip; a dependant must be fully answered before the list can be confirmed; IF-11 to IF-13 carry a complete flag | Owner decision of 14/11/2026: "Gate, no is supposedly need to give the answers. as it needed for assessment year. Marital Status, is supposedly base on status. not on yes or no." | Prompt P-16 |
| CHG-037 | 2026-11-14 | F1, F2, F3, F4 | SRS-F1-04, SRS-F2-04, SRS-F3-02, SRS-F3-03, SRS-F4-01, SRS-F4-04, A5.4, B4, FD-F2-03, IF-02 result, TC-F2-08, TC-F2-24 | same | Changed | A relief with unknown facts was 0 with a notice; F2 had a third result "unknown"; F3 offered unknown categories with a warning; F4 listed unknown categories | Each feature shows the gate "Complete your profile for YA {y}" while the profile is Incomplete; relief results are applicable or not applicable only; F3 refuses an expense for an Incomplete YA; F4 lists applicable categories only | Applies CHG-036 | Prompt P-16 |
| CHG-038 | 2026-11-14 | F0, F1, F2, F3, F4, F5 | Shared blocks: DA table, IF-11 to IF-13, IF-20 | DA-20, IF-11, IF-12, IF-13, IF-20, DA-24 | Changed | DA-20 proposed (null means not answered); IF-20 erased everything; DataRequest type export or delete | DA-20 approved on 14/11/2026 with a change (null only while a question is open or not shown); IF-11 to IF-13 carry the complete flag; IF-20 can name a YA; DataRequest type delete_ya with a ya field | Owner decisions of 14/11/2026 | Prompt P-16 |
| CHG-039 | 2026-11-14 | F5 | A1, A2, A3, A4 titles, A5.4, A6, SRS titles, B3.1, B3.6 (new), B4, B7, SD-F5-03 to SD-F5-08, SD-F5-15, SD-F5-17 (new) | SD-F5-17 added; the SRS, URS, TC and SD listed changed | Changed | One release (R1) for everything except two-factor and export | Two phases: Phase 1 is the simple account; Phase 2 holds sign-in lockout, emailed links (verification, self-service forgot password, email change), staying signed in, two-factor login, deletion of the whole account and the security events screen. B3.6 says what is built in Phase 1 for each SRS. Admins have no two-factor in Phase 1 (A6 item 8) | Owner decision of 14/11/2026: "for 1st phase we proceed on simple. can hold the feature of sign in lock, links, staying signed in, two-factor, deletion and security to another phase" | Prompt P-16 |
| CHG-040 | 2026-11-14 | F5 | SRS-F5-10, SRS-F5-17, SRS-F5-11, A2, SD-F5-10, SD-F5-18 (new) | SD-F5-18 added; SD-F5-10 approved | Changed | SD-F5-10 "to be confirmed"; the reset email was a convenience for the user | SD-F5-10 approved: an admin cannot change an email or a password; the admin sends a temporary reset link (1 hour, single use), never sees the link or the password; a taxpayer changes the own email in Settings (SD-F5-18) | Owner decision of 14/11/2026: "for admin only; as taxpayer they can change the email; the admin gives a temporary link, not directly change on behalf of the taxpayer" | Prompt P-16 |
| CHG-041 | 2026-11-14 | F5 | A3, FD-F5-10, FD-F5-13 (new), SRS-F5-15, SRS-F5-21 (new), B3.1, B3.4, B3.6, B4, B5, B6, TC-F5-23, TC-F5-24, TC-F5-29 (new), SD-F5-09 | URS-F5-14, SRS-F5-21, FD-F5-13, TC-F5-29 added; SRS-F5-15, TC-F5-23, TC-F5-24 changed; SD-F5-09 approved | Changed | A user could delete the account before the 7 years ended, after a warning | Records can be deleted only after the 7-year period (31 December of the YA plus 7 years). The app shows a notice when a YA becomes deletable; the user deletes one YA at a time (Phase 1); deleting the whole account (Phase 2) is allowed only when every YA is past its period. The worked example now runs to 2035 | Owner decision of 14/11/2026: "make a notification that taxpayer can delete data that is more than 7 years"; "for a moment, let keep it as i give the answer. to allow delete after 7 years" | Prompt P-16 |
| CHG-042 | 2026-11-14 | F0, F1, F3 | SRS-F0-19, SRS-F1-24, SRS-F3-18, SRS-F0-01 | same | Changed | Erase deleted everything of the user | Erase can name one YA and then deletes only that YA's rows and files; the first sign-in trigger of F0 follows sign-up (Phase 1) or verification (Phase 2) | Applies CHG-041 | Prompt P-16 |
| CHG-043 | 2026-11-14 | F0, F1, F2, F3, F4, F5 | Header | Document version | Changed | F0 at 0.2; F1 to F4 at 0.4; F5 at 0.1 | F0 at 0.3; F1 to F4 at 0.5; F5 at 0.2 | CHG-036 to CHG-042 | Prompt P-16 |
| CHG-044 | 2026-11-14 | PRD | Section 3.2 FR-2.3, section 4 (admin support tools), section 5 (TaxpayerProfile), NFR-7, NFR-8, section 8 (roles and admin support paragraph) | Pending sync items 13, 16, 18 and 19 | Synced | The PRD (revision 37) had one profile per user, no mandatory rule, an admin who managed the account on the user's behalf, and records "offered for deletion" after 7 years | PRD revision 47: TaxpayerProfile is one per user per YA with year, copied_from_year, state, has_first_home, first_home_price and dependants_confirmed, and every visible question is mandatory with the calculator, relief categories, spending records and dashboard locked until it is complete; an admin cannot change the email or the password and sends a temporary reset link; an admin sees a Filed flag only; records are kept 7 years and the taxpayer is told when a YA can be deleted | Owner approvals of 13/11/2026 and 14/11/2026 (SD-F0-01, DA-16, DA-19, DA-20, SD-F0-14, SD-F5-10, SD-F5-09) | Prompt P-16 |
| CHG-045 | 2026-11-14 | F0, F1, F2, F3, F4, F5 | Links to the registers | Links to HISTORY_LOG.md, URS_SRS_CHANGE_LOG.md and ACRONYMS.md | Clarified | Links pointed to files in the same folder | Links point to ../registers/ because the files moved into the repository layout (docs/specs, docs/registers, docs/tools). No requirement changed, so the document versions stay at 0.3 and 0.5 and 0.2 | The owner asked for one repository from documentation to production | Prompt P-18 |
| CHG-046 | 2026-11-18 | AGENTS.md, PROMPT_RULES.md, PR template | AGENTS.md sections 1 and 5; PROMPT_RULES R-01, R-16, R-40, R-49, R-50; pull request checklist | Rules for how I respond, for review and for the repository | Added | R-01 covered only questions and decisions; no review rule; R-40 said the repository was local only; R-16 said files are sent to the owner; R-49 pushed automatically with no condition | R-01 covers every prompt (information first); R-50: every pull request into main is reviewed, the owner may bypass while alone, and with a second developer 1 review by someone other than the author is needed; R-49 applies only after "update"; R-40 and R-16 brought up to date; PR template has a review line. PROMPT_RULES at version 0.6. No requirement document changed, so F0 to F5 keep their versions | The owner asked for a review rule on merge requests and for information first on every prompt | Prompts P-24 to P-26 |
| CHG-047 | 2026-11-18 | AGENTS.md, PROMPT_RULES.md | AGENTS.md section 5 (automatic commit and push); PROMPT_RULES R-49 | Automatic commit and push rule | Clarified | R-49 ended at commit and push; the owner opened the pull request by hand | R-49 continues: after the push the agent opens a pull request with `gh pr create` and stops; the agent never merges. PROMPT_RULES at version 0.7. No requirement document changed | The owner installed the GitHub CLI (`gh`) and asked for the agent to open pull requests | Prompts P-27 and P-28 |

## Pending PRD sync

These are the changes the PRD needs if the owner approves the matching item. Items 13, 16, 18 and 19 were done in PRD revision 47 on 14/11/2026 (CHG-044); their numbers are not reused. 22 items are still pending. When one is done, a CHG entry of type Synced is added.

| # | PRD place | Change | Matching IDs |
| --- | --- | --- | --- |
| 1 | Section 5, data model | Add DA-01 to DA-15 (new fields, RuleTier, UserTaxYear) | DA-01 to DA-15 |
| 2 | Section 5, TaxYear | Remove status open or filed (moves to UserTaxYear) | DA-12 |
| 3 | FR-1.9 | State that PCB on bonus is counted once | SRS-F1-12, OI-F1-02 |
| 4 | FR-1.1 and FR-1.9 | State that income of months with no record is projected, and how | SD-F1-02 |
| 5 | FR-4.4 | Replace "using the current marginal rate" with the tax difference from scenario | SD-F4-04 |
| 6 | Section 2.2 and 5 | Bands store the lower threshold | SD-F1-09 |
| 7 | BR-9 | Define "closed" | OI-F1-03 |
| 8 | Section 8 roles | Say what "download" means for an admin | OI-F3-01 |
| 9 | BR-10 | State the rounding rule | SD-F1-05 |
| 10 | Section 4 | Rule change log R1 per-rule history, R2 consolidated | SD-F2-08 |
| 11 | Section 2.3 and decision 4 | Education and medical insurance: RM 4,000 for YA 2025 per LHDN (RM 3,000 for YA 2018 to YA 2024); remove "(confirm)" for YA 2025 | OI-F2-01 |
| 12 | Section 2.3 and decision 5 | EPF limit RM 4,000 and life insurance limit RM 3,000 inside RM 7,000; additional voluntary EPF counts in the RM 3,000 | OI-F2-02 |
| 14 | Section 5, Dependant | Add person_key and display_name | DA-17 |
| 15 | Section 5, TaxEstimate | Add profile_id and profile_version_no | DA-18 |
| 17 | Section 3 (features) | Add the profile and tax-year history feature F0 with its own FR block (proposed FR-0.1 to FR-0.8) and screens | URS-F0-01 to URS-F0-15 |
| 20 | Section 5, User | Add status, email_verified_at, deletion_requested_at, deletion_due_on, last_sign_in_at | DA-21 |
| 21 | Section 5 | Add Credential, Session, ConsentRecord, Invitation, DataRequest and SecurityEvent | DA-22 to DA-24 |
| 22 | Section 7, Sign in and onboarding | Sign-up by invitation and password rules (Phase 1); email verified before use, session lengths and sign-in lockout (Phase 2, SD-F5-17) | SD-F5-01 to SD-F5-04, SD-F5-06 |
| 23 | Section 7 Settings, NFR-7, NFR-8 | Export as a ZIP; deletion of the whole account with a 14-day grace period (Phase 2); consent purposes and text headings. The 7-year rule is already in the PRD (CHG-044) | SD-F5-08, SD-F5-09, SD-F5-12, SD-F5-14 |
| 24 | NFR-6 | Two-factor by authenticator app, optional for taxpayers, required for admins; no SMS (Phase 2) | SD-F5-05, SD-F5-07 |
| 25 | Section 3 (features) | Add the account and security feature F5 with its own FR block (proposed FR-5.1 to FR-5.9) and screens | URS-F5-01 to URS-F5-14 |
| 26 | Section 9.1 (phases) | Account and security is built in two phases: Phase 1 the simple account, Phase 2 the held features (SD-F5-17) | SD-F5-17 |

## Consistency checks

| Date | Check | Result |
| --- | --- | --- |
| 2026-11-12 | Every referenced URS, SRS, FD, SQ, TC, SD, OI ID is defined in the right document | 0 errors |
| 2026-11-12 | Every URS appears in its traceability matrix | 0 errors |
| 2026-11-12 | Every SRS names at least one URS, a flow diagram (or "not drawn") and a test case (or "none in R1") | 0 errors |
| 2026-11-12 | Table columns match their header in every table | 0 errors |
| 2026-11-12 | Interface table, ownership table, data additions and category codes are identical in the four documents | 0 differences |
| 2026-11-12 | Every provider and consumer SRS named in the interface table exists | 0 errors |
| 2026-11-12 | All 37 Mermaid diagrams (30 FD, 3 SQ, 4 copies of FD-00) render (version 0.2) | 37 of 37 |
| 2026-11-12 | After version 0.2: all checks above repeated | 0 errors |
| 2026-11-12 | Tax test values (TC-F1-01 to TC-F1-06, TC-F1-10, TC-F1-11, TC-F1-17, F4 B3.1 and B3.2) recomputed by script | All match |
| 2026-11-13 | After F0 and version 0.3: all checks above repeated over five documents (shared blocks identical in all five) | 0 errors |
| 2026-11-13 | Acronym check (src/check_acronyms.py) over all documents | Passed |
| 2026-11-13 | All 47 Mermaid diagrams (38 FD, 4 SQ, 5 copies of FD-00) render | 47 of 47 |
| 2026-11-13 | F0 test values recomputed by script: YA 2025 example (chargeable income 45,150.00, tax 1,209.00), TC-F0-24 (42,150.00, tax 1,029.00), children's ages for YA 2026 to YA 2028, completeness percentages | All match |
| 2026-11-13 | After F5, F0 version 0.2 and F1 to F4 version 0.4: all checks above repeated over six documents (shared blocks identical in all six) | 0 errors |
| 2026-11-13 | Acronym check (src/check_acronyms.py) after adding 7 acronyms and 3 code values | Passed |
| 2026-11-13 | All 62 Mermaid diagrams (50 FD, 6 SQ, 6 copies of FD-00) render | 62 of 62 |
| 2026-11-13 | F5 dates recomputed by script: grace end 27/11/2026, backup purge 01/01/2027, 7-year ends 31/12/2032, 31/12/2033 and 31/12/2034, lock until 10:15:00, session expiries 27/11/2026 09:00, 04/12/2026 09:00, 12:00 and 10:30 | All match |
| 2026-11-14 | After the owner decisions of P-16 (mandatory answers, phase split, 7-year rule): all checks above repeated over six documents (shared blocks identical in all six) | 0 errors |
| 2026-11-14 | Acronym check (src/check_acronyms.py) | Passed (119 register rows) |
| 2026-11-14 | All Mermaid diagrams render (FD-F2-03, FD-F0-03, FD-F5-10 changed; FD-F5-13 new) | The 4 changed or new diagrams render (FD-F0-03, FD-F2-03, FD-F5-10, FD-F5-13); the others are unchanged |
| 2026-11-14 | New F5 dates recomputed by script: YA 2025 retention ends 31/12/2032 and is deletable from 01/01/2033; YA 2026 and YA 2027 from 01/01/2034 and 01/01/2035; deletion due 19/01/2035 (05/01/2035 plus 14 days); backup purge 23/02/2035 (19/01/2035 plus 35 days) | All match |
| 2026-11-18 | After the rules change (CHG-046): build, change log and acronym check repeated over six documents | 0 errors; acronym check passed |
| 2026-11-18 | After the pull request rule (CHG-047): build, change log and acronym check repeated over six documents | 0 errors; acronym check passed |

## ID register

Every URS, SRS, test case, specification decision and open item. "Added in" is the version that created the ID; "Status" shows later changes. Later changes refer to these IDs.


### F0. User profile and tax-year history (URS_SRS_F0_User_Profile.md)

| ID | Type | Short description | Added in | Status |
| --- | --- | --- | --- | --- |
| URS-F0-01 | URS | Create my profile the first time I use the app, in short steps that I can leave and finish later | 0.1 (CHG-018) | Draft |
| URS-F0-02 | URS | Tell the app my residency, marital status, my spouse's situation, my own disability and my first-home loan, so that ... | 0.1 (CHG-018) | Draft |
| URS-F0-03 | URS | Add, change and remove dependants (children and parents) with the facts that decide their reliefs | 0.1 (CHG-018) | Draft |
| URS-F0-04 | URS | See my whole profile on one screen: what is answered, what is missing, and which reliefs each answer affects | 0.1 (CHG-018) | Draft |
| URS-F0-05 | URS | Have a separate profile for each YA, which starts as a copy of the previous year, so that a change in a later year ... | 0.1 (CHG-018) | Draft |
| URS-F0-06 | URS | When I change a fact, choose whether it also applies to the later YAs that are not filed | 0.1 (CHG-018) | Draft |
| URS-F0-07 | URS | See the history of my tax years: for each YA, whether it is not started, in progress, calculated or filed, and its main ... | 0.1 (CHG-018) | Draft |
| URS-F0-08 | URS | Open one tax year to see the profile it used and its saved calculations, and jump to the calculator, the spending list ... | 0.1 (CHG-018) | Draft |
| URS-F0-09 | URS | Be sure that the profile of a filed YA cannot change unless I reopen the YA, and see which profile version each saved ... | 0.1 (CHG-018) | Draft |
| URS-F0-10 | URS | See the history of changes to a profile: who changed what, when, and from which value to which value, including changes ... | 0.1 (CHG-018) | Draft |
| URS-F0-11 | URS | Compare the profiles of two YAs and see what changed | 0.1 (CHG-018) | Draft |
| URS-F0-12 | URS | Let an admin help me with my profile fields without the admin seeing my income, tax or spending | 0.1 (CHG-018) | Draft |
| URS-F0-13 | URS | Use and change my profile offline, and have the changes arrive once and in order when I am online again | 0.1 (CHG-018) | Draft |
| URS-F0-14 | URS | Keep my name and language with my profile, and have my profile data included when I export my data and removed when I ... | 0.2 (CHG-031) | Draft |
| URS-F0-15 | URS | Be asked for every fact that my reliefs depend on, and be unable to calculate, see reliefs or record spending for a ... | 0.3 (CHG-036) | Draft, new |
| SRS-F0-01 | SRS | Guided creation of the first profile | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| SRS-F0-02 | SRS | Questions, answers and visibility | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| SRS-F0-03 | SRS | Completeness and the gate | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| SRS-F0-04 | SRS | Profile of a new YA (copy forward) | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| SRS-F0-05 | SRS | Profile screen | 0.1 (CHG-018) | Draft |
| SRS-F0-06 | SRS | Validation of facts | 0.1 (CHG-018) | Draft |
| SRS-F0-07 | SRS | Dependants | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| SRS-F0-08 | SRS | Saving and versions | 0.1 (CHG-018) | Draft |
| SRS-F0-09 | SRS | Apply a change to later YAs | 0.1 (CHG-018) | Draft |
| SRS-F0-10 | SRS | Lock of a filed YA | 0.1 (CHG-018) | Draft |
| SRS-F0-11 | SRS | Tax-year history list | 0.1 (CHG-018) | Draft |
| SRS-F0-12 | SRS | Tax-year detail | 0.1 (CHG-018) | Draft |
| SRS-F0-13 | SRS | Compare two YAs | 0.1 (CHG-018) | Draft |
| SRS-F0-14 | SRS | Change history of a profile | 0.1 (CHG-018) | Draft |
| SRS-F0-15 | SRS | Serving profile facts (IF-11, IF-12, IF-13) and EV-03 | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| SRS-F0-16 | SRS | Admin support | 0.1 (CHG-018) | Draft, changed in 0.2 (CHG-031) |
| SRS-F0-17 | SRS | Offline, sync and ids | 0.1 (CHG-018) | Draft |
| SRS-F0-18 | SRS | Layout, language, accessibility, performance | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| SRS-F0-19 | SRS | Account fields, identity, export and erase (links to F5) | 0.2 (CHG-031) | Draft, changed in 0.3 (CHG-042) |
| TC-F0-01 | TC | New user, name and language empty, first sign-in on 13/11/2026; at step 2 answer "No", ... | 0.1 (CHG-018) | Draft |
| TC-F0-02 | TC | Same user answers step 2 Yes and step 3 single, then leaves the app and returns | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| TC-F0-03 | TC | Married, spouse_has_income not answered; then answered No; then Q4, Q6, Q7 (I have no ... | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| TC-F0-04 | TC | Married, spouse_has_income No, spouse_is_disabled Yes; change marital status to divorced | 0.1 (CHG-018) | Draft |
| TC-F0-05 | TC | Add a dependant with date of birth 01/01/1900; then a future date; then an empty ... | 0.1 (CHG-018) | Draft |
| TC-F0-06 | TC | The three children of B3.2; test ages for YA 2026, YA 2027 and YA 2028 and the R20 test | 0.1 (CHG-018) | Draft |
| TC-F0-07 | TC | Aisyah has an active YA 2026 profile; open YA 2027 in F4 for the first time | 0.1 (CHG-018) | Draft, changed in 0.3 (CHG-036) |
| TC-F0-08 | TC | Open YA 2027 a second time; then change a fact in YA 2026 and decline the dialog | 0.1 (CHG-018) | Draft |
| TC-F0-09 | TC | YA 2026 marital status single to married; YA 2027 profile has marital status single ... | 0.1 (CHG-018) | Draft |
| TC-F0-10 | TC | As TC-F0-09, but YA 2027 marital status was set to widowed by hand | 0.1 (CHG-018) | Draft |
| TC-F0-11 | TC | YA 2025 is filed. Open its profile; try to change a fact; try the same through the ... | 0.1 (CHG-018) | Draft |
| TC-F0-12 | TC | YA 2026 is open; in F1 mark it filed | 0.1 (CHG-018) | Draft |
| TC-F0-13 | TC | Profile of the F1 worked example is at version 4; save an estimate; change a fact ... | 0.1 (CHG-018) | Draft |
| TC-F0-14 | TC | Stored YAs as in B3.3 | 0.1 (CHG-018) | Draft |
| TC-F0-15 | TC | Open the detail of YA 2025 (filed) | 0.1 (CHG-018) | Draft |
| TC-F0-16 | TC | Open the detail of YA 2027 with no profile row and no income | 0.1 (CHG-018) | Draft |
| TC-F0-17 | TC | Compare YA 2026 and YA 2027 after TC-F0-07 | 0.1 (CHG-018) | Draft |
| TC-F0-18 | TC | Three edits to YA 2026: one by the user, one by an admin, one made offline and still in ... | 0.1 (CHG-018) | Draft |
| TC-F0-19 | TC | An admin opens Aisyah; tries to open YA 2026's figures; edits is_disabled in YA 2026; ... | 0.1 (CHG-018) | Draft |
| TC-F0-20 | TC | Two devices, both offline, each create the YA 2027 profile; then the same field is ... | 0.1 (CHG-018) | Draft |
| TC-F0-21 | TC | Device B edits YA 2026 offline; device A marks YA 2026 filed; device B syncs | 0.1 (CHG-018) | Draft |
| TC-F0-22 | TC | first_home_spa_date 31/12/2024; first_home_price RM 800,000.00; first_home_price RM 0.00 | 0.1 (CHG-018) | Draft |
| TC-F0-23 | TC | 360 px screen, language Bahasa Malaysia | 0.1 (CHG-018) | Draft |
| TC-F0-24 | TC | F1 worked example (single, no dependants); set is_disabled to Yes in YA 2026 and apply to ... | 0.1 (CHG-018) | Draft |
| TC-F0-25 | TC | Aisyah (YA 2025 filed, YA 2026 calculated, YA 2027 in progress; profile versions as in ... | 0.2 (CHG-031) | Draft |
| TC-F0-26 | TC | Aisyah's YA 2027 profile was copied and dependants_confirmed is false; open F1 and F2 for ... | 0.3 (CHG-036) | Draft, new |
| SD-F0-01 | SD | One profile per YA, copied forward from the nearest earlier YA (finding F-033, option 1). Approved by the owner on ... | 0.1 (CHG-018) | Approved by the owner 13/11/2026 (CHG-030) |
| SD-F0-02 | SD | The first profile is made for the current YA. A new YA gets a draft copy with dependants_confirmed reset to false | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-03 | SD | The profile screen shows, for each answer, chips naming the reliefs it affects; completeness is a count of visible ... | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-04 | SD | A residency answer of "No" is not accepted in R1 | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-05 | SD | A change is offered to later unfiled YAs, ticked by default, and applies only where the later YA still holds the old or ... | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-06 | SD | Data minimisation: nickname instead of legal name, no identity numbers, no addresses; marital status values single, ... | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-07 | SD | joint_assessment is stored but has no control in R1 | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-08 | SD | An admin's change applies to the edited YA only, with no later-years dialog | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-09 | SD | Profile rows use a deterministic UUID v5 per user and year; other new rows keep UUID v7 (DA-02) | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-10 | SD | education_level values: none, school, pre_university, diploma_or_above_my, degree_or_above_overseas, other. F2's R21 ... | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-11 | SD | Stage is Filed, Calculated (income exists), In progress (profile exists), Not started. "Calculated" does not need a ... | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-12 | SD | The lock is derived from UserTaxYear.status, not stored in the profile | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-13 | SD | A removed dependant stays on old expenses as "(removed)" and is not offered for new ones | 0.1 (CHG-018) | Needs owner decision |
| SD-F0-14 | SD | Every visible question is mandatory and the profile is a hard gate: until a YA's profile is Complete, F1 to F4 do not ... | 0.3 (CHG-036) | Approved by the owner 14/11/2026 (CHG-036) |
| OI-F0-01 | OI | Answered 2026-11-13 (version 0.2). Sign-in, password, two-factor login, consent text, data export and account deletion ... | 0.1 (CHG-018) | Answered in 0.2 (CHG-030) |
| OI-F0-02 | OI | Should an admin's views of a user's profile be logged, not only edits? | 0.1 (CHG-018) | Open |
| OI-F0-03 | OI | How long is profile change history kept, and what happens to it when an account is deleted? | 0.1 (CHG-018) | Draft, changed in 0.2 (CHG-031) |
| OI-F0-04 | OI | Answered 2026-11-13 (version 0.2). May an admin see that a YA is filed (not the figures)? | 0.1 (CHG-018) | Answered in 0.2 (CHG-030) |

### F1. Tax calculator and PCB (URS_SRS_F1_Tax_Calculator.md)

| ID | Type | Short description | Added in | Status |
| --- | --- | --- | --- | --- |
| URS-F1-01 | URS | Enter, for any YA and month, salary, bonus, allowances, benefits-in-kind, employee EPF, SOCSO/EIS, zakat paid, ... | 0.1 (CHG-001) | Draft |
| URS-F1-02 | URS | See estimated tax for a chosen YA, calculated with the rules announced for that YA, with nothing hard-coded | 0.1 (CHG-001) | Draft |
| URS-F1-03 | URS | See the full chain: total income, deductions, reliefs by category, chargeable income, tax before rebates, rebates, tax ... | 0.1 (CHG-001) | Draft |
| URS-F1-04 | URS | See how the tax was reached band by band | 0.1 (CHG-001) | Draft |
| URS-F1-05 | URS | Compare the stored YAs side by side, with announced rules labelled, and see what one YA's data would give under another ... | 0.1 (CHG-001) | Draft |
| URS-F1-06 | URS | See every figure change instantly when anything changes, with or without a connection | 0.1 (CHG-001) | Draft |
| URS-F1-07 | URS | Try extra spending in a category and see the tax saved, including a warning at the RM35,000 rebate cliff | 0.1 (CHG-001) | Draft |
| URS-F1-08 | URS | Record the PCB deducted each month from the payslip, with PCB on a bonus or other extra pay as a separate line | 0.1 (CHG-001) | Draft |
| URS-F1-09 | URS | See the PCB projected for the whole year, and override any future month | 0.1 (CHG-001) | Draft |
| URS-F1-10 | URS | See projected PCB beside estimated tax payable, with the expected balance to pay or refund, updated whenever reliefs ... | 0.1 (CHG-001) | Draft |
| URS-F1-11 | URS | Have reliefs picked up automatically from the profile, from income records and from spending records, so each relief is ... | 0.1 (CHG-001) | Draft |
| URS-F1-12 | URS | Know when a figure is an estimate (announced rules or projected months) and that LHDN's assessment prevails | 0.1 (CHG-001) | Draft |
| URS-F1-13 | URS | Mark a YA as filed and reopen it, so records behind a filed return are protected | 0.1 (CHG-001) | Draft |
| URS-F1-14 | URS | See the history of every change to an income or PCB entry | 0.1 (CHG-001) | Draft |
| URS-F1-15 | URS | (R2) Estimate the monthly PCB from salary to compare with the payslip | 0.1 (CHG-001) | Draft |
| URS-F1-16 | URS | Have my income, PCB and saved calculations included in my data export and deleted when I delete my account | 0.4 (CHG-032) | Draft |
| SRS-F1-01 | SRS | YA selection and rule loading | 0.1 (CHG-001) | Draft, changed in 0.3 (CHG-020) |
| SRS-F1-02 | SRS | Income and PCB screen | 0.1 (CHG-001) | Draft |
| SRS-F1-03 | SRS | Validation and storage of income entries | 0.1 (CHG-001) | Draft |
| SRS-F1-04 | SRS | Automatic and profile-derived reliefs | 0.1 (CHG-001) | Draft, changed in 0.5 (CHG-037) |
| SRS-F1-05 | SRS | Income-sourced reliefs and IF-05 | 0.1 (CHG-001) | Draft |
| SRS-F1-06 | SRS | Receive the allocation result | 0.1 (CHG-001) | Draft |
| SRS-F1-07 | SRS | Calculation chain | 0.1 (CHG-001) | Draft |
| SRS-F1-08 | SRS | Rebates | 0.1 (CHG-001) | Draft |
| SRS-F1-09 | SRS | Band breakdown | 0.1 (CHG-001) | Draft |
| SRS-F1-10 | SRS | Effective and marginal rate; rebate cliff | 0.1 (CHG-001) | Draft |
| SRS-F1-14 | SRS | Estimate label and disclaimer | 0.1 (CHG-001) | Draft |
| SRS-F1-15 | SRS | Recalculation | 0.1 (CHG-001) | Draft, changed in 0.3 (CHG-020) |
| SRS-F1-11 | SRS | PCB records | 0.1 (CHG-001) | Draft |
| SRS-F1-12 | SRS | Annual PCB projection | 0.1 (CHG-001) | Draft |
| SRS-F1-13 | SRS | PCB against tax, balance | 0.1 (CHG-001) | Draft |
| SRS-F1-16 | SRS | What-if | 0.1 (CHG-001) | Draft |
| SRS-F1-17 | SRS | Year comparison | 0.1 (CHG-001) | Draft |
| SRS-F1-18 | SRS | Scenario service (IF-09) | 0.1 (CHG-001) | Draft |
| SRS-F1-19 | SRS | Estimate snapshots | 0.1 (CHG-001) | Draft, changed in 0.3 (CHG-020) |
| SRS-F1-20 | SRS | Audit and versions of income entries | 0.1 (CHG-001) | Draft |
| SRS-F1-21 | SRS | Mark YA as filed and reopen | 0.1 (CHG-001) | Draft, changed in 0.3 (CHG-020) |
| SRS-F1-22 | SRS | (R2) PCB estimate from salary, reserved | 0.1 (CHG-001) | Draft |
| SRS-F1-23 | SRS | Tax-year summary for the history (IF-16) | 0.3 (CHG-021) | Draft |
| SRS-F1-24 | SRS | Identity, export and erase (links to F5) | 0.4 (CHG-032) | Draft, changed in 0.5 (CHG-042) |
| TC-F1-01 | TC | YA 2026, chargeable income RM 100,000.00 | 0.1 (CHG-001) | Draft |
| TC-F1-02 | TC | YA 2026, chargeable income RM 35,000.00 | 0.1 (CHG-001) | Draft |
| TC-F1-03 | TC | YA 2026, chargeable income RM 35,001.00 | 0.1 (CHG-001) | Draft |
| TC-F1-04 | TC | YA 2026, chargeable income RM 20,000.00 | 0.1 (CHG-001) | Draft |
| TC-F1-05 | TC | YA 2026, the worked example in B3.3 (single, resident, no children; EPF 7,920 counted up ... | 0.1 (CHG-001) | Draft, changed in 0.2 (CHG-014) |
| TC-F1-06 | TC | Same data as TC-F1-05, rules of YA 2027 (mode B) | 0.1 (CHG-001) | Draft |
| TC-F1-07 | TC | PCB RM 125 recorded January to October, no bonus, YA 2026 current, tax payable 1,449.00 | 0.1 (CHG-001) | Draft |
| TC-F1-08 | TC | Same as TC-F1-07 plus PCB on bonus RM 300 in March (pcb_additional) | 0.1 (CHG-001) | Draft |
| TC-F1-09 | TC | Tax before rebates 1,449.00, zakat paid 2,000.00 | 0.1 (CHG-001) | Draft |
| TC-F1-10 | TC | TC-F1-05 plus what-if sports (R11) RM 1,000.00 | 0.1 (CHG-001) | Draft |
| TC-F1-11 | TC | Chargeable income 36,000.00 plus what-if relief RM 2,000.00 | 0.1 (CHG-001) | Draft |
| TC-F1-12 | TC | Enter salary RM 6,000.00 for January, then change it to RM 6,200.00 | 0.1 (CHG-001) | Draft |
| TC-F1-13 | TC | YA 2027 selected | 0.1 (CHG-001) | Draft |
| TC-F1-14 | TC | A YA with no rule set | 0.1 (CHG-001) | Draft |
| TC-F1-15 | TC | Network off, change salary | 0.1 (CHG-001) | Draft |
| TC-F1-16 | TC | Change 3 inputs within 100 ms | 0.1 (CHG-001) | Draft |
| TC-F1-17 | TC | Scenario no_reliefs on TC-F1-05 | 0.1 (CHG-001) | Draft |
| TC-F1-18 | TC | Profile: 2 unmarried children under 18 | 0.1 (CHG-001) | Draft |
| TC-F1-19 | TC | Mark YA 2026 as filed | 0.1 (CHG-001) | Draft |
| TC-F1-20 | TC | Edit a salary in a filed YA | 0.1 (CHG-001) | Draft |
| TC-F1-21 | TC | Stored YAs: 2025 filed on 20/04/2026 (final snapshot: chargeable income 45,150.00, ... | 0.3 (CHG-021) | Draft |
| TC-F1-22 | TC | Aisyah's data: YA 2025 filed with its final snapshot, YA 2026 with 2 snapshots and ... | 0.4 (CHG-032) | Draft |
| SD-F1-01 | SD | The YA selector defaults to the current YA each time the app opens; the choice is kept only until the app closes | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-02 | SD | Income for months with no record is projected (carry forward the latest salary, allowance, EPF and SOCSO/EIS; never ... | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-03 | SD | Marginal rate = rate of the band holding the last sen of chargeable income | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-04 | SD | A month missing between two recorded months is flagged, not filled | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-05 | SD | Each band's tax is rounded half-up to the sen, then summed | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-06 | SD | Year comparison has two modes (own data, same data under other rules) | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-07 | SD | Snapshots are saved on "Save estimate", on "Mark as filed" and at each month-end by the SYSTEM user | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-08 | SD | A filed YA can be reopened; filing and reopening are versioned | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-09 | SD | Bands store the lower threshold (5,000.00), not the displayed start (5,001.00) | 0.1 (CHG-001) | Needs owner decision |
| SD-F1-10 | SD | IF-16 gives F0 the live figure of each stored YA through the scenario as_recorded, and the saved figures through the ... | 0.3 (CHG-021) | Needs owner decision |
| OI-F1-01 | OI | On which date is a child's age tested (period end, period start or the date of expense)? BR-11 says to follow LHDN. | 0.1 (CHG-001) | Open |
| OI-F1-02 | OI | Confirm the PCB projection counts bonus PCB once (SRS-F1-12) | 0.1 (CHG-001) | Open |
| OI-F1-03 | OI | BR-9 says "once the year is closed". Does closed mean the YA has ended, or that it is filed? | 0.1 (CHG-001) | Open |
| OI-F1-04 | OI | Departure levy needs an input field (DA-09) | 0.1 (CHG-001) | Open |

### F2. Relief categories and rule sets (URS_SRS_F2_Relief_Categories.md)

| ID | Type | Short description | Added in | Status |
| --- | --- | --- | --- | --- |
| URS-F2-01 | URS | See every relief category of a YA with name, group, annual cap, sub-limits, shared-cap group, conditions, required ... | 0.1 (CHG-002) | Draft |
| URS-F2-02 | URS | Group, search and filter categories, and see which are New or Changed against the previous YA | 0.1 (CHG-002) | Draft |
| URS-F2-03 | URS | See only the reliefs that apply to my profile (marital status, children and ages, disability, first-home purchase) | 0.1 (CHG-002) | Draft |
| URS-F2-04 | URS | See, on each category, the cap, the amount claimed and the amount remaining | 0.1 (CHG-002) | Draft |
| URS-F2-05 | URS | Open the app with complete rules for YA 2025, YA 2026 and YA 2027 already loaded | 0.1 (CHG-002) | Draft |
| URS-F2-06 | URS | (Admin) Add or edit bands, relief rules, sub-limits, rebates and dates for a YA without a code release | 0.1 (CHG-002) | Draft |
| URS-F2-07 | URS | See on every rule its status (Announced, Gazetted, Confirmed), source link and confirmation date | 0.1 (CHG-002) | Draft |
| URS-F2-08 | URS | Switch the YA and see caps and bands change at once, without reloading data | 0.1 (CHG-002) | Draft |
| URS-F2-09 | URS | (Admin) Maintain tax bands, rebates, filing deadline and the YA period | 0.1 (CHG-002) | Draft |
| URS-F2-10 | URS | (Admin) Be stopped from publishing a rule change that breaks a calculator test | 0.1 (CHG-002) | Draft |
| URS-F2-11 | URS | (Admin) See the history of every change to a rule | 0.1 (CHG-002) | Draft |
| URS-F2-12 | URS | Open the expenses recorded under a category, or add one, from the category | 0.1 (CHG-002) | Draft |
| SRS-F2-01 | SRS | Catalogue list | 0.1 (CHG-002) | Draft |
| SRS-F2-02 | SRS | Group, search, filter | 0.1 (CHG-002) | Draft |
| SRS-F2-03 | SRS | New and Changed flags | 0.1 (CHG-002) | Draft |
| SRS-F2-04 | SRS | Profile relevance and the eligibility test | 0.1 (CHG-002) | Draft, changed in 0.5 (CHG-037) |
| SRS-F2-05 | SRS | Effective cap, claimed, remaining, room | 0.1 (CHG-002) | Draft, changed in 0.3 (CHG-022) |
| SRS-F2-06 | SRS | Category detail | 0.1 (CHG-002) | Draft |
| SRS-F2-07 | SRS | Switching the YA | 0.1 (CHG-002) | Draft |
| SRS-F2-08 | SRS | Seed data | 0.1 (CHG-002) | Draft, changed in 0.2 (CHG-011) |
| SRS-F2-09 | SRS | Admin rules manager | 0.1 (CHG-002) | Draft |
| SRS-F2-10 | SRS | Status, source and confirmation | 0.1 (CHG-002) | Draft |
| SRS-F2-11 | SRS | Publish gate and RuleSetChanged | 0.1 (CHG-002) | Draft |
| SRS-F2-12 | SRS | Delete and retire | 0.1 (CHG-002) | Draft |
| SRS-F2-13 | SRS | Serving rules to other features (IF-01, IF-02, IF-07) | 0.1 (CHG-002) | Draft |
| SRS-F2-14 | SRS | Shared-cap groups and claim frequency (configuration) | 0.1 (CHG-002) | Draft, changed in 0.2 (CHG-012) |
| SRS-F2-15 | SRS | Bands, rebates and TaxYear | 0.1 (CHG-002) | Draft |
| SRS-F2-16 | SRS | Audit and rule history | 0.1 (CHG-002) | Draft |
| SRS-F2-17 | SRS | (R2) Consolidated rule change log, reserved | 0.1 (CHG-002) | Draft |
| TC-F2-01 | TC | Open the catalogue for YA 2025 | 0.1 (CHG-002) | Draft |
| TC-F2-02 | TC | YA 2026, then YA 2027 | 0.1 (CHG-002) | Draft |
| TC-F2-03 | TC | YA 2027 flags against YA 2026 | 0.1 (CHG-002) | Draft |
| TC-F2-04 | TC | YA 2025 | 0.1 (CHG-002) | Draft |
| TC-F2-05 | TC | Search "vaccin" | 0.1 (CHG-002) | Draft |
| TC-F2-06 | TC | Filter Has room on, with the F1 worked example | 0.1 (CHG-002) | Draft |
| TC-F2-07 | TC | Profile: single, no children, not disabled; Applies to me on | 0.1 (CHG-002) | Draft |
| TC-F2-08 | TC | The marital status question is open (profile Incomplete) | 0.1 (CHG-002) | Draft, changed in 0.5 (CHG-037) |
| TC-F2-09 | TC | Profile: 2 unmarried children aged 5 and 9 | 0.1 (CHG-002) | Draft |
| TC-F2-10 | TC | Group GRP-INS-EPF, EPF applied 4,000 and life insurance applied 3,000 | 0.1 (CHG-002) | Draft, changed in 0.2 (CHG-012) |
| TC-F2-11 | TC | R06 first-home loan, profile first_home_price RM 600,000 (DA-19) | 0.1 (CHG-002) | Draft, changed in 0.3 (CHG-022) |
| TC-F2-12 | TC | Open R10 detail with 3 expenses | 0.1 (CHG-002) | Draft |
| TC-F2-13 | TC | Switch YA 2026 to 2027, network off | 0.1 (CHG-002) | Draft |
| TC-F2-14 | TC | Run the seed twice | 0.1 (CHG-002) | Draft |
| TC-F2-15 | TC | Band set with a gap (20,000 to 30,000 then 35,000 to 50,000) | 0.1 (CHG-002) | Draft |
| TC-F2-16 | TC | Status Confirmed without confirmed_on | 0.1 (CHG-002) | Draft |
| TC-F2-17 | TC | Edit cap on a Confirmed rule | 0.1 (CHG-002) | Draft |
| TC-F2-18 | TC | Draft YA 2026 band 4 rate changed 6% to 7% | 0.1 (CHG-002) | Draft |
| TC-F2-19 | TC | Valid draft that keeps all tests passing | 0.1 (CHG-002) | Draft |
| TC-F2-20 | TC | Delete R10 YA 2026 with 3 expenses | 0.1 (CHG-002) | Draft |
| TC-F2-21 | TC | Online device with tag older than 7 days | 0.1 (CHG-002) | Draft |
| TC-F2-22 | TC | Breastfeeding R24 claimed in YA 2025 (data in F3) | 0.1 (CHG-002) | Draft |
| TC-F2-23 | TC | Admin edits R10 cap twice | 0.1 (CHG-002) | Draft |
| TC-F2-24 | TC | Profile of YA 2027 copied from YA 2026 (Aisyah, F0 B3.2), dependants_confirmed false; ... | 0.3 (CHG-022) | Draft, changed in 0.5 (CHG-037) |
| SD-F2-01 | SD | Nine groups in a fixed order (B2.3) | 0.1 (CHG-002) | Needs owner decision |
| SD-F2-02 | SD | The YA selector always starts on the current YA and is not remembered | 0.1 (CHG-002) | Needs owner decision |
| SD-F2-03 | SD | filing_deadline stays empty until published; F4 shows "Deadline not published" | 0.1 (CHG-002) | Needs owner decision |
| SD-F2-04 | SD | Seed status: YA 2025 and YA 2026 Gazetted, YA 2027 Announced, none Confirmed until an admin verifies | 0.1 (CHG-002) | Needs owner decision |
| SD-F2-05 | SD | Draft rows and change sets for admin edits | 0.1 (CHG-002) | Needs owner decision |
| SD-F2-06 | SD | A value edit on a Confirmed rule resets it to Gazetted | 0.1 (CHG-002) | Needs owner decision |
| SD-F2-07 | SD | No override on the publish gate; band tests are generated for new YAs | 0.1 (CHG-002) | Needs owner decision |
| SD-F2-08 | SD | A taxpayer sees only "Last changed on"; a change_reason text is stored on every rule version | 0.1 (CHG-002) | Needs owner decision |
| SD-F2-09 | SD | Bilingual name and condition fields on categories | 0.1 (CHG-002) | Needs owner decision |
| OI-F2-01 | OI | Answered 2026-11-12 (version 0.2). Decision 4, education and medical insurance cap. LHDN's tax reliefs page gives RM ... | 0.1 (CHG-002) | Answered in 0.2 (CHG-011) |
| OI-F2-02 | OI | Answered 2026-11-12 (version 0.2). Decision 5, EPF and life insurance. LHDN gives a total of RM 7,000 with a limit of ... | 0.1 (CHG-002) | Answered in 0.2 (CHG-012) |
| OI-F2-03 | OI | Which YA 2027 changes are Gazetted yet (Finance Act)? | 0.1 (CHG-002) | Open |

### F3. Spending records (URS_SRS_F3_Spending_Records.md)

| ID | Type | Short description | Added in | Status |
| --- | --- | --- | --- | --- |
| URS-F3-01 | URS | Record an expense with date, amount, category, merchant, description, payment method, notes and receipt (camera, image ... | 0.1 (CHG-003) | Draft |
| URS-F3-02 | URS | Pick only categories that apply to me, have the YA worked out from the date, and see the sub-limit choices of a category | 0.1 (CHG-003) | Draft |
| URS-F3-03 | URS | Be stopped by real errors and only warned about the rest: amount, date, eligibility; missing receipt; possible duplicate | 0.1 (CHG-003) | Draft |
| URS-F3-04 | URS | See the actual spend and the claimable amount of each expense side by side, and why any part does not count | 0.1 (CHG-003) | Draft |
| URS-F3-05 | URS | Split one expense across categories so the parts add up to the total and nothing is claimed twice | 0.1 (CHG-003) | Draft |
| URS-F3-06 | URS | Edit, delete (without losing it), search and filter expenses by YA, category, date and receipt status | 0.1 (CHG-003) | Draft |
| URS-F3-07 | URS | Add and edit expenses offline, and have them sync later without duplicates or lost edits | 0.1 (CHG-003) | Draft |
| URS-F3-08 | URS | Be warned, and confirm, before deleting or changing anything that belongs to a filed YA | 0.1 (CHG-003) | Draft |
| URS-F3-09 | URS | Keep each receipt for 7 years from the end of the YA, and see its upload state | 0.1 (CHG-003) | Draft |
| URS-F3-10 | URS | Mark an expense "do not claim" so it stays recorded but does not count | 0.1 (CHG-003) | Draft |
| URS-F3-11 | URS | See, right after saving, what the expense did to the category's remaining room and the estimate | 0.1 (CHG-003) | Draft |
| URS-F3-12 | URS | See the history of every change to an expense or receipt | 0.1 (CHG-003) | Draft |
| URS-F3-13 | URS | Say who an expense is for (me, spouse, a child, a parent) where the relief depends on it | 0.1 (CHG-003) | Draft |
| URS-F3-14 | URS | (Admin) Help with a user's files by file name and type, without opening any confidential data | 0.1 (CHG-003) | Draft |
| URS-F3-15 | URS | Have my spending records and receipt files included in my data export and deleted when I delete my account | 0.4 (CHG-033) | Draft |
| SRS-F3-01 | SRS | Expense form | 0.1 (CHG-003) | Draft |
| SRS-F3-02 | SRS | YA, category, sub-limit, beneficiary | 0.1 (CHG-003) | Draft, changed in 0.5 (CHG-037) |
| SRS-F3-03 | SRS | Validation | 0.1 (CHG-003) | Draft, changed in 0.5 (CHG-037) |
| SRS-F3-04 | SRS | Duplicate detection | 0.1 (CHG-003) | Draft |
| SRS-F3-05 | SRS | Receipts | 0.1 (CHG-003) | Draft |
| SRS-F3-06 | SRS | Claim allocator (one implementation for F1, F3 and F4) | 0.1 (CHG-003) | Draft |
| SRS-F3-07 | SRS | Income inputs, shared caps and deductions | 0.1 (CHG-003) | Draft, changed in 0.2 (CHG-013) |
| SRS-F3-08 | SRS | Claim frequency | 0.1 (CHG-003) | Draft |
| SRS-F3-09 | SRS | Split | 0.1 (CHG-003) | Draft |
| SRS-F3-10 | SRS | Edit and versions | 0.1 (CHG-003) | Draft |
| SRS-F3-11 | SRS | Soft delete, restore, filed-YA guard | 0.1 (CHG-003) | Draft |
| SRS-F3-12 | SRS | Search and filter | 0.1 (CHG-003) | Draft |
| SRS-F3-13 | SRS | Offline capture and sync | 0.1 (CHG-003) | Draft |
| SRS-F3-14 | SRS | Outputs and events | 0.1 (CHG-003) | Draft, changed in 0.3 (CHG-023) |
| SRS-F3-15 | SRS | Entry points (IF-10, IF-15) | 0.1 (CHG-003) | Draft, changed in 0.3 (CHG-023) |
| SRS-F3-16 | SRS | History view | 0.1 (CHG-003) | Draft |
| SRS-F3-17 | SRS | Admin file support | 0.1 (CHG-003) | Draft |
| SRS-F3-18 | SRS | Identity, export and erase (links to F5) | 0.4 (CHG-033) | Draft, changed in 0.5 (CHG-042) |
| TC-F3-01 | TC | One lifestyle (R10) expense of RM 3,000.00 | 0.1 (CHG-003) | Draft |
| TC-F3-02 | TC | Medical (R07) with sub-limit VACC, vaccination RM 1,500.00 | 0.1 (CHG-003) | Draft |
| TC-F3-03 | TC | Network off; add an expense; then network on | 0.1 (CHG-003) | Draft |
| TC-F3-04 | TC | Expense RM 1,000.00 split R10 600.00 and R11 400.00; then R10 600.00 and R11 300.00 | 0.1 (CHG-003) | Draft |
| TC-F3-05 | TC | Second expense with same merchant (any case), date and amount | 0.1 (CHG-003) | Draft |
| TC-F3-06 | TC | YA 2026 marked filed; delete an expense dated in 2026 | 0.1 (CHG-003) | Draft |
| TC-F3-07 | TC | R10: 10 Jan RM 2,000.00 and 15 Feb RM 1,000.00; then edit January to RM 500.00 | 0.1 (CHG-003) | Draft |
| TC-F3-08 | TC | Group GRP-INS-EPF cap 7,000; R14 cap 4,000; R15 cap 3,000; EPF prior 7,920.00 from IF-05; ... | 0.1 (CHG-003) | Draft, changed in 0.2 (CHG-013) |
| TC-F3-09 | TC | Total income 72,000.00; donations RM 10,000.00; then again with professional ... | 0.1 (CHG-003) | Draft |
| TC-F3-10 | TC | R24 breastfeeding RM 1,000.00 applied in YA 2025; then RM 800.00 in YA 2026; then RM ... | 0.1 (CHG-003) | Draft |
| TC-F3-11 | TC | R10 expense RM 3,000.00 with do not claim on | 0.1 (CHG-003) | Draft |
| TC-F3-12 | TC | R23 childcare for a child aged 14 in YA 2026 (limit 12) | 0.1 (CHG-003) | Draft |
| TC-F3-13 | TC | Expense with no receipt; then add a receipt that is still uploading | 0.1 (CHG-003) | Draft |
| TC-F3-14 | TC | Same expense edited on two devices while offline; the later client time was on device B | 0.1 (CHG-003) | Draft |
| TC-F3-15 | TC | Date tomorrow | 0.1 (CHG-003) | Draft |
| TC-F3-16 | TC | Admin opens a user's file list | 0.1 (CHG-003) | Draft |
| TC-F3-17 | TC | Receipt for an expense dated 10 Jun 2026 | 0.1 (CHG-003) | Draft |
| TC-F3-18 | TC | R06 home loan interest claimed in YA 2025, 2026 and 2027; expense in YA 2028 | 0.1 (CHG-003) | Draft |
| TC-F3-19 | TC | Open the list from F4 with filter receipt_status = missing | 0.1 (CHG-003) | Draft |
| TC-F3-20 | TC | Profile with no children; try R23 | 0.1 (CHG-003) | Draft |
| TC-F3-21 | TC | The same create item is sent twice (retry after a lost reply) | 0.1 (CHG-003) | Draft |
| TC-F3-22 | TC | YA 2027 R18: SOCSO prior 504.00 from IF-05; voluntary Lindung expense RM 200.00 with ... | 0.1 (CHG-003) | Draft |
| TC-F3-23 | TC | Aisyah has 12 expenses and 9 receipts (8 uploaded, 1 pending on a phone); one expense was ... | 0.4 (CHG-033) | Draft |
| SD-F3-01 | SD | The error and warning split in SRS-F3-03, including blocking a category that the profile says does not apply and a date ... | 0.1 (CHG-003) | Needs owner decision |
| SD-F3-02 | SD | Up to 5 receipts per expense; images compressed to 1,600 px long edge, JPEG 80; at most 10 MB; background retries 5 s ... | 0.1 (CHG-003) | Needs owner decision |
| SD-F3-03 | SD | "Recently deleted" list with Restore | 0.1 (CHG-003) | Needs owner decision |
| SD-F3-04 | SD | Conflict rule: later client edit time wins, loser kept as conflict_loser | 0.1 (CHG-003) | Needs owner decision |
| OI-F3-01 | OI | PRD role table lets an admin "upload, download or delete a user's files, by file name and type only" yet says admins ... | 0.1 (CHG-003) | Open |
| OI-F3-02 | OI | Donation cap base: LHDN's limit is 10% of aggregate income. Is that before donations and after professional ... | 0.1 (CHG-003) | Open |
| OI-F3-03 | OI | SSPN net savings (R19) is "deposits minus withdrawals". An expense amount must be above zero, so withdrawals cannot be ... | 0.1 (CHG-003) | Open |
| OI-F3-04 | OI | Zakat paid is captured in F1's income record (PRD data model), so a zakat receipt cannot be attached | 0.1 (CHG-003) | Open |

### F4. Dashboard (URS_SRS_F4_Dashboard.md)

| ID | Type | Short description | Added in | Status |
| --- | --- | --- | --- | --- |
| URS-F4-01 | URS | Choose the YA, starting from the current YA | 0.1 (CHG-004) | Draft |
| URS-F4-02 | URS | See summary cards: estimated tax payable, tax saved by reliefs, total relief claimed, total relief still available, PCB ... | 0.1 (CHG-004) | Draft |
| URS-F4-03 | URS | See, for each category, claimed against cap as a progress bar, the remaining amount, the number of receipts and the ... | 0.1 (CHG-004) | Draft |
| URS-F4-04 | URS | See how many reliefs I can still claim, ranked by how much tax each would save | 0.1 (CHG-004) | Draft |
| URS-F4-05 | URS | See my tax now against my tax if I used all remaining room | 0.1 (CHG-004) | Draft |
| URS-F4-06 | URS | See the trend of tax payable and relief claimed across years | 0.1 (CHG-004) | Draft |
| URS-F4-07 | URS | Be alerted when a category is at 90% of its cap or more, when receipts are missing, how many days are left in the YA, ... | 0.1 (CHG-004) | Draft |
| URS-F4-08 | URS | See the PCB deducted per month, the projected year total, and the projection against the estimated tax | 0.1 (CHG-004) | Draft |
| URS-F4-09 | URS | See every figure update after any change, with no page reload and without a connection | 0.1 (CHG-004) | Draft |
| URS-F4-10 | URS | Jump from a figure to the place that explains or changes it | 0.1 (CHG-004) | Draft |
| URS-F4-11 | URS | Know when a figure is an estimate, which rules it rests on, and how fresh the data is | 0.1 (CHG-004) | Draft |
| URS-F4-12 | URS | See a helpful screen when there is no data yet | 0.1 (CHG-004) | Draft |
| URS-F4-13 | URS | Be sure that no one else, including an admin, can open my dashboard | 0.1 (CHG-004) | Draft |
| SRS-F4-01 | SRS | YA selector | 0.1 (CHG-004) | Draft, changed in 0.5 (CHG-037) |
| SRS-F4-02 | SRS | Data assembly | 0.1 (CHG-004) | Draft |
| SRS-F4-03 | SRS | Summary cards | 0.1 (CHG-004) | Draft |
| SRS-F4-04 | SRS | Per-category progress | 0.1 (CHG-004) | Draft, changed in 0.5 (CHG-037) |
| SRS-F4-05 | SRS | Reliefs to claim | 0.1 (CHG-004) | Draft |
| SRS-F4-06 | SRS | Tax now against tax if all room were used | 0.1 (CHG-004) | Draft |
| SRS-F4-07 | SRS | Multi-year trend | 0.1 (CHG-004) | Draft |
| SRS-F4-08 | SRS | Alerts | 0.1 (CHG-004) | Draft |
| SRS-F4-09 | SRS | PCB panel | 0.1 (CHG-004) | Draft |
| SRS-F4-10 | SRS | Live update, offline, freshness | 0.1 (CHG-004) | Draft, changed in 0.3 (CHG-024) |
| SRS-F4-11 | SRS | Drill-down and navigation | 0.1 (CHG-004) | Draft |
| SRS-F4-12 | SRS | Estimate labels | 0.1 (CHG-004) | Draft |
| SRS-F4-13 | SRS | Empty and error states | 0.1 (CHG-004) | Draft |
| SRS-F4-14 | SRS | Layout and accessibility | 0.1 (CHG-004) | Draft |
| SRS-F4-15 | SRS | Access control | 0.1 (CHG-004) | Draft |
| SRS-F4-16 | SRS | Performance | 0.1 (CHG-004) | Draft |
| TC-F4-01 | TC | Open the app on 12 Nov 2026 | 0.1 (CHG-004) | Draft |
| TC-F4-02 | TC | Open the dashboard with the F1 estimate delayed | 0.1 (CHG-004) | Draft |
| TC-F4-03 | TC | Worked example | 0.1 (CHG-004) | Draft |
| TC-F4-04 | TC | Category with RM 0 claimed (R11 Sports) | 0.1 (CHG-004) | Draft |
| TC-F4-05 | TC | Worked example | 0.1 (CHG-004) | Draft |
| TC-F4-06 | TC | Same data but tax payable already RM 0.00 | 0.1 (CHG-004) | Draft |
| TC-F4-07 | TC | Worked example | 0.1 (CHG-004) | Draft |
| TC-F4-08 | TC | Stored YAs 2025 (no data), 2026 (live), 2027 (no data) | 0.1 (CHG-004) | Draft |
| TC-F4-09 | TC | Lifestyle at 2,250.00 of 2,500.00 (90%) | 0.1 (CHG-004) | Draft |
| TC-F4-10 | TC | 2 expenses without receipt; date 5 Dec 2026, YA 2026 current | 0.1 (CHG-004) | Draft |
| TC-F4-11 | TC | YA 2025 ended, not filed, deadline stored 15 May 2026, today 12 Nov 2026 | 0.1 (CHG-004) | Draft |
| TC-F4-12 | TC | PCB 125 Jan to Oct; bonus PCB 300 in March | 0.1 (CHG-004) | Draft |
| TC-F4-13 | TC | Add an expense while offline | 0.1 (CHG-004) | Draft |
| TC-F4-14 | TC | Rule set cached 9 days ago, device offline | 0.1 (CHG-004) | Draft |
| TC-F4-15 | TC | Tap Missing receipts | 0.1 (CHG-004) | Draft |
| TC-F4-16 | TC | YA 2027 selected | 0.1 (CHG-004) | Draft |
| TC-F4-17 | TC | New user, YA 2026 | 0.1 (CHG-004) | Draft |
| TC-F4-18 | TC | 360 px wide screen | 0.1 (CHG-004) | Draft |
| TC-F4-19 | TC | Admin requests another user's dashboard data | 0.1 (CHG-004) | Draft |
| SD-F4-01 | SD | The selector defaults to the current YA on each app open and is not remembered | 0.1 (CHG-004) | Needs owner decision |
| SD-F4-02 | SD | "Total relief claimed" includes automatic reliefs (for example the RM 9,000 individual relief); "still available" ... | 0.1 (CHG-004) | Needs owner decision |
| SD-F4-03 | SD | Reliefs to claim includes deductions with a cap (D01), excludes D02 (no cap), and counts a shared group once | 0.1 (CHG-004) | Needs owner decision |
| SD-F4-04 | SD | Potential saving is the difference F1 returns when that entry's room is used, not room times marginal rate; the ... | 0.1 (CHG-004) | Needs owner decision |
| SD-F4-05 | SD | Scenarios run in a Web Worker; ranking may lag by up to 500 ms | 0.1 (CHG-004) | Needs owner decision |
| SD-F4-06 | SD | The trend uses live estimates, or the final snapshot for a filed YA | 0.1 (CHG-004) | Needs owner decision |
| SD-F4-07 | SD | Alert thresholds: A3 shown from 90 days; high severity at 30 days or 14 days to the deadline; top 3 shown | 0.1 (CHG-004) | Needs owner decision |
| OI-F4-01 | OI | Should "total relief still available" also include deductions with a cap (donations)? | 0.1 (CHG-004) | Open |
| OI-F4-02 | OI | Should the dashboard remember the last YA the owner looked at? | 0.1 (CHG-004) | Open |

### F5. Account and security (URS_SRS_F5_Account_Security.md)

| ID | Type | Short description | Added in | Status |
| --- | --- | --- | --- | --- |
| URS-F5-01 | URS | Create an account with an invitation, an email and a password (Phase 2: and prove the email is mine before I use the ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| URS-F5-02 | URS | Read the data consent before I use the app, accept it, see later what I accepted and when, and be asked again if the ... | 0.1 (CHG-028) | Draft |
| URS-F5-03 | URS | Sign in and out and be signed out after a period of no use (Phase 2: stay signed in on my own device) | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| URS-F5-04 | URS | Get back into my account when I forget my password: in Phase 1 an administrator sends me a temporary link; in Phase 2 I ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-040) |
| URS-F5-05 | URS | (Phase 2) Turn two-factor login on and off with an authenticator app, keep recovery codes, and recover if I lose the ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| URS-F5-06 | URS | Change my password and my email (Phase 2: see where I am signed in and sign out another device) | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| URS-F5-07 | URS | (Phase 2) See the security events on my account: sign-ins, failed attempts, changes and actions by an administrator | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| URS-F5-08 | URS | Export all my data in a file I can keep | 0.1 (CHG-028) | Draft |
| URS-F5-09 | URS | (Phase 2) Delete my account and all my data, after a clear warning about the 7-year record rule, with time to change my ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| URS-F5-10 | URS | Use the app offline, and be safe if a device is shared, lost or kept offline for a long time | 0.1 (CHG-028) | Draft |
| URS-F5-11 | URS | Be sure that an administrator can never see my tax data or change my email or password | 0.1 (CHG-028) | Draft |
| URS-F5-12 | URS | (Admin) Invite people, see the status of accounts, disable or enable an account and send a password reset email, ... | 0.1 (CHG-028) | Draft |
| URS-F5-13 | URS | Find language, security, privacy, export and deletion in one Settings screen | 0.1 (CHG-028) | Draft |
| URS-F5-14 | URS | Be told when the records of a year are older than 7 years, and delete them myself when I choose | 0.2 (CHG-041) | Draft, new |
| SRS-F5-01 | SRS | Sign-up (by invitation) | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-02 | SRS | Password rules | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-03 | SRS | Email verification | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-04 | SRS | Consent | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-05 | SRS | Sign-in | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-06 | SRS | Two-factor login (admins and taxpayers) | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-07 | SRS | Recovery codes and a lost authenticator | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-08 | SRS | Sessions | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-09 | SRS | Offline use, expiry and sign-out | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-10 | SRS | Forgot password | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-040) |
| SRS-F5-11 | SRS | Change password and change email | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-12 | SRS | Security events | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-13 | SRS | Settings screen | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-14 | SRS | Data export (IF-19) | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-15 | SRS | Account deletion request | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-041) |
| SRS-F5-16 | SRS | Erase run (IF-20) | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-17 | SRS | Admin account tools (IF-21) | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SRS-F5-18 | SRS | Serving identity and events (IF-18, EV-07, EV-08) | 0.1 (CHG-028) | Draft |
| SRS-F5-19 | SRS | Transport, storage and logs | 0.1 (CHG-028) | Draft |
| SRS-F5-20 | SRS | Layout, language, accessibility, performance | 0.1 (CHG-028) | Draft |
| SRS-F5-21 | SRS | Records older than 7 years | 0.2 (CHG-041) | Draft, new |
| TC-F5-01 | TC | A valid invitation; email Aisyah@Example.com; password "correct horse battery 7"; ... | 0.1 (CHG-028) | Draft |
| TC-F5-02 | TC | (a) no code; (b) a used code; (c) a code made 8 days ago; (d) a valid code with an email ... | 0.1 (CHG-028) | Draft |
| TC-F5-03 | TC | Passwords: "short1"; "aisyah@example.com"; "password1234"; a 128-character password; a ... | 0.1 (CHG-028) | Draft |
| TC-F5-04 | TC | (Phase 2) Verification link opened at 23 h 59 min; another account's link at 24 h 01 min; ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| TC-F5-05 | TC | Consent version 1 accepted; version 2 is published; Aisyah signs in; (a) she accepts; (b) ... | 0.1 (CHG-028) | Draft |
| TC-F5-06 | TC | Settings, Privacy: try to withdraw the core consent | 0.1 (CHG-028) | Draft |
| TC-F5-07 | TC | Sign in with the right password; then with a wrong password; then with an unknown email | 0.1 (CHG-028) | Draft |
| TC-F5-08 | TC | (Phase 2) Five wrong passwords, the 5th at 10:00:00; the right password at 10:05; the ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| TC-F5-09 | TC | Two-factor is on. Right password, then (a) a wrong code, (b) the right code, (c) the same ... | 0.1 (CHG-028) | Draft |
| TC-F5-10 | TC | (Phase 2) Turn on two-factor: after 11 minutes since sign-in; then with a fresh sign-in; ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| TC-F5-11 | TC | (Phase 2) Turn off two-factor as Aisyah (password and a current code); then as an admin | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| TC-F5-12 | TC | (Phase 2) Sign in with a recovery code; use it again; use 8 codes in all; make new codes; ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| TC-F5-13 | TC | Own device: last server contact 13/11/2026 09:00; contact again 20/11/2026 09:00. Shared ... | 0.1 (CHG-028) | Draft |
| TC-F5-14 | TC | (Phase 2) Aisyah is signed in on a phone and a laptop; on the laptop she taps "Sign out ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| TC-F5-15 | TC | Phone offline 10 days (own device); then offline 15 days after the last contact; then she ... | 0.1 (CHG-028) | Draft |
| TC-F5-16 | TC | Sign out with 3 unsent changes; choose Wait; later sign out again and choose Sign out and ... | 0.1 (CHG-028) | Draft |
| TC-F5-17 | TC | (Phase 2) Forgot password for aisyah@example.com and for nobody@example.com; open the ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-040) |
| TC-F5-18 | TC | Change password: new equals old; then a new one. Change email to bilal@example.com. An ... | 0.1 (CHG-028) | Draft |
| TC-F5-19 | TC | (Phase 2) After TC-F5-07 and TC-F5-08, open Settings, Security events | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| TC-F5-20 | TC | Open Settings online, then offline; change the language to English | 0.1 (CHG-028) | Draft |
| TC-F5-21 | TC | Export: request after 11 minutes since sign-in; a second request while the first is ... | 0.1 (CHG-028) | Draft |
| TC-F5-22 | TC | Export of Aisyah's data (three YAs, the F3 data of TC-F3-23) | 0.1 (CHG-028) | Draft |
| TC-F5-23 | TC | (Phase 2) Delete account: on 13/11/2026 Aisyah taps Delete my account; on 05/01/2035 she ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-041) |
| TC-F5-24 | TC | (Phase 2) Due date 19/01/2035 reached. Case 1: F0, F1 and F3 all confirm. Case 2: F3 does ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-041) |
| TC-F5-25 | TC | An admin (two-factor on) opens Accounts; creates an invitation; disables Aisyah with the ... | 0.1 (CHG-028) | Draft |
| TC-F5-26 | TC | An admin tries: setting a password; changing an email; turning two-factor off; reading ... | 0.1 (CHG-028) | Draft |
| TC-F5-27 | TC | Run sign-in, add an expense of RM 120.00 at "Klinik Sihat", request an export; then ... | 0.1 (CHG-028) | Draft |
| TC-F5-28 | TC | 360 px screen, Bahasa Malaysia; sign-in screen on a mid-range phone over 4G | 0.1 (CHG-028) | Draft |
| TC-F5-29 | TC | Aisyah's data as in B3.4. Today is 05/01/2033. She opens the app offline, then online; ... | 0.2 (CHG-041) | Draft, new |
| SD-F5-01 | SD | In R1, sign-up needs a single-use invitation code made by an admin (valid 7 days). Public sign-up opens after the ... | 0.1 (CHG-028) | Needs owner decision |
| SD-F5-02 | SD | Passwords are 12 to 128 characters, any characters, checked against a list of common passwords; no composition rules, ... | 0.1 (CHG-028) | Needs owner decision |
| SD-F5-03 | SD | (Phase 2) The email must be verified before first use of the app (link valid 24 hours); an account not verified in 7 ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SD-F5-04 | SD | (Phase 2, except the 1-hour life of the admin-sent link, which is Phase 1) 5 failed sign-ins in 15 minutes lock the ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SD-F5-05 | SD | (Phase 2) Two-factor uses an authenticator app only (no SMS). It is optional for taxpayers and required for admins. Ten ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SD-F5-06 | SD | A session lasts 14 days after the last server contact for a taxpayer and 30 minutes for an admin (Phase 1). Phase 2 ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SD-F5-07 | SD | (Phase 2) A lost authenticator is recovered by an emailed link, a 24-hour wait, notices at both ends and a Cancel link. ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SD-F5-08 | SD | (The grace period is Phase 2; the 35-day backup purge is Phase 1) Deletion has a 14-day grace period that a sign-in ... | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SD-F5-09 | SD | The user can delete the records of a YA, or the account, only after the 7-year period has ended: 31 December of the YA ... | 0.1 (CHG-028) | Approved by the owner 14/11/2026 (CHG-041) |
| SD-F5-10 | SD | Approved by the owner on 14/11/2026 ("for admin only; as taxpayer they can change the email"; the admin helps with a ... | 0.1 (CHG-028) | Approved by the owner 14/11/2026 (CHG-040) |
| SD-F5-11 | SD | In R1 the owner sets the role in the data; there is no screen for roles. An admin account cannot be deleted in R1 | 0.1 (CHG-028) | Needs owner decision |
| SD-F5-12 | SD | R1 has one consent purpose, CORE. The text is a draft with the headings of B3.5 until the PDPA adviser writes the final ... | 0.1 (CHG-028) | Needs owner decision |
| SD-F5-13 | SD | F0 owns the name and the language; F5 owns the email, password, role and status. F5 creates the User row with the ... | 0.1 (CHG-028) | Needs owner decision |
| SD-F5-14 | SD | The export is a ZIP with CSV files, one JSON file and the original receipts; ready within 24 hours; the link works 7 ... | 0.1 (CHG-028) | Needs owner decision |
| SD-F5-15 | SD | (Phase 2) Security events are kept 12 months; IP addresses are kept 30 days; the user can read the last 50 | 0.1 (CHG-028) | Draft, changed in 0.2 (CHG-039) |
| SD-F5-16 | SD | Sign-out with unsent changes offers Wait or Sign out and discard; another user cannot sign in on a device that holds ... | 0.1 (CHG-028) | Needs owner decision |
| SD-F5-17 | SD | Phase 1 is the simple account: invitation-only sign-up, password sign-in, a simple session, consent, change of the own ... | 0.2 (CHG-039) | Approved by the owner 14/11/2026 (CHG-039) |
| SD-F5-18 | SD | In Phase 1 a taxpayer changes the own email in Settings with the current password and it takes effect at once; the ... | 0.2 (CHG-040) | Approved by the owner 14/11/2026 (CHG-040) |
| OI-F5-01 | OI | Where is the data hosted, and what is the basis for any transfer outside Malaysia (PRD decision on hosting)? | 0.1 (CHG-028) | Open |
| OI-F5-02 | OI | Who writes the final consent text and privacy notice? | 0.1 (CHG-028) | Open |
| OI-F5-03 | OI | How long may security events and IP addresses be kept? | 0.1 (CHG-028) | Open |
| OI-F5-04 | OI | What time limit applies to answering an export or deletion request, and to purging backups? | 0.1 (CHG-028) | Open |
| OI-F5-05 | OI | F2 and F4 get no SRS row of their own for the role check in IF-18. Is a short row needed there (F2 admin screens; F4 ... | 0.1 (CHG-028) | Open |
| OI-F5-06 | OI | Which service sends the emails (verification, reset, notices), and from which address? | 0.1 (CHG-028) | Open |
| OI-F5-07 | OI | Should two-factor become required for every taxpayer at public launch? | 0.1 (CHG-028) | Open |
