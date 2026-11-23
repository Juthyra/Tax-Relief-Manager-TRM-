# ADR-006: Email service and sending domain

| Item | Value |
| --- | --- |
| Document ID | ADR-006 |
| Document type | ADR (architecture decision record) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.1 |
| Status | Proposed (held by the owner on 23/11/2026; decided with the stack) |
| Date | 2026-11-23 (first written 2026-11-23) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (sign in, security, PDPA) and section 9.3 decision 8 (hosting) |
| Source | Owner prompts P-40 and P-41; F5 OI-F5-06 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md) |
| Decided by | Owner (not decided yet) |

## Question

Which service sends the emails of TRM, and from which domain and address?

## What has to be sent

| When | Email | Specification |
| --- | --- | --- |
| Basic account (R1) | Temporary password-reset link sent by an admin (1 hour, single use) | SRS-F5-10, SRS-F5-17 |
| Basic account (R1) | Notice that the password was changed | SRS-F5-11 item 1 |
| Launch account (before public launch) | Verification link, self-service reset link, email-change link and notices, two-factor notices, deletion notices | SRS-F5-03, SRS-F5-07, SRS-F5-10, SRS-F5-11, SRS-F5-15 |
| R2 | Reminders, only with the optional SERVICE_EMAILS consent | SRS-F5-04 |

No email ever carries tax data (F5 A6 item 6).

## What the decision needs

| Point | Why |
| --- | --- |
| A domain the owner controls, and a sending address such as `no-reply@` on it | The SPF, DKIM and DMARC records of the domain decide whether the mail reaches the inbox |
| The provider: a transactional email service or the SMTP of the domain host | The provider stores the recipient's email address, which is personal data |
| The provider's region and data terms | A transfer outside Malaysia needs a basis under the PDPA, the same question as hosting (ADR-005, OI-F5-01) |

## Options

| Option | For | Against |
| --- | --- | --- |
| To be filled when the stack is chosen. Prices, regions and terms are read from each provider's own pages at that time | | |

## Decision and reason

Not decided. On 23/11/2026 the owner held this decision: no domain yet, and the provider is chosen together with the stack (ADR-001 to ADR-005), after the YA 2026 and YA 2027 rules are firm.

## Effect on the specifications

Answers OI-F5-06 when decided. Until then the basic account cannot send the admin reset link, so it must be decided before the R1 build reaches F5.
