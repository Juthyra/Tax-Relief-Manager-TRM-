# DES-000: Design system

| Item | Value |
| --- | --- |
| Document ID | DES-000 |
| Document type | DES (design: look, screens and how they behave) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.1 |
| Status | Proposed (direction A is chosen by the owner; this document waits for approval) |
| Date | 2026-11-23 (first written 2026-11-23) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7: NFR-11 (language), NFR-12 (accessibility), NFR-1 (PWA) |
| Source | Owner prompts P-80 to P-83; the ui-ux-pro-max design skill; URS-SRS-F0 SRS-F0-18 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md); detail in [REG-02](../registers/REG_02_URS_SRS_Change_Log.md) |
| Decided by | Owner chose direction A on 23/11/2026 (P-83); the rest waits for the owner |

## 1. Decision

The owner chose **direction A, "Navy Trust"**, on 23/11/2026 (P-83). Direction B, "Friendly Blue", is kept as a backup in `tokens/theme_b_backup.css`. It is not used.

| | A. Navy Trust (chosen) | B. Friendly Blue (backup) |
| --- | --- | --- |
| Style | Minimalism and Swiss: square corners (6 px), thin lines, no shadows | Flat and friendly: rounded corners (18 px), filled tiles, soft shadow |
| Fonts | Lexend (headings), Source Sans 3 (text) | Plus Jakarta Sans |
| Main colours | Navy `#0F172A` bar, blue `#1E3A8A` primary, gold `#A16207` accent | Blue `#1E40AF` bar and primary, green `#047857` accent |
| Why it was in the list | The skill's entry for banking and traditional finance | The skill's entry for a personal finance tracker, moved from a dark to a light background |

**"Can the two be mixed?"** Yes. Both use the same markup and the same variable names. A mix is a change to `tokens/tokens.css` (for example `--font-head` and `--font-body`) or to the shape rules at the end of `theme_b_backup.css`. No mix is applied. Direction A is used as it is.

The directions were compared on the same screen (the F0 profile screen) in `directions/`.

## 2. Design rules

| # | Rule | Reason |
| --- | --- | --- |
| D1 | **Fonts are self-hosted in the real app.** The mockups load them from Google Fonts for review only | A PWA must work offline, and a Google request sends the user's IP address to Google (PDPA) |
| D2 | **Every screen exists in English and Bahasa Malaysia.** Text must wrap: no fixed widths for text. Bahasa Malaysia is often longer | NFR-11 |
| D3 | The Bahasa Malaysia text in the mockups is a **draft**. A native speaker reviews it before the app uses it. "TT" stands for Tahun Taksiran | I wrote it; it is not reviewed |
| D4 | **WCAG 2.1 AA.** Text contrast at least 4.5:1, other parts at least 3:1, touch targets at least 44 px, visible focus ring, visible labels, errors beside the field | NFR-12, SRS-F0-18 |
| D5 | **A status is never shown by colour alone.** Draft, Active, Filed, Incomplete and Complete always have text. An open answer shows "!" and the words "Not answered" | SRS-F0-18 |
| D6 | **PWA shell.** Phone (up to 899 px): top bar and five tabs (Dashboard, Calculator, Reliefs, Spending, Profile). From 900 px: the tabs become a left rail. A status line shows offline use and the last sync | NFR-1, NFR-2 |
| D7 | Icons are SVG line icons. No emoji as icons | The skill's checklist |
| D8 | Motion is only a short colour change, and it is off when the user asks for reduced motion | The skill's checklist |
| D9 | Money is shown as "RM 1,449.00" and dates as DD/MM/YYYY | NFR-11 |
| D10 | Mockups use **test data only** (the test family Aisyah, Nur and Adam). No real tax or personal data | AGENTS.md section 1 |

## 3. Tokens (direction A)

The values are in `tokens/tokens.css`, named here by their variable. Contrast was computed by script on 23/11/2026.

| Use | Pair | Contrast | Needed |
| --- | --- | --- | --- |
| Main text on the page | `--color-fg` on `--color-bg` | 19.28:1 | text |
| Muted text on a card | `--color-muted` on `--color-card` | 7.58:1 | text |
| Muted text on the page | `--color-muted` on `--color-bg` | 7.24:1 | text |
| Button text on primary | `--color-on-primary` on `--color-primary` | 10.36:1 | text |
| Top bar and rail text | `--color-on-bar` on `--color-bar` | 17.85:1 | text |
| Primary link on a card | `--color-primary` on `--color-card` | 10.36:1 | text |
| Warning text on warning background | `--color-warn` on `--color-warn-bg` | 6.37:1 | text |
| Chip text | `--color-on-chip` on `--color-chip` | 12.33:1 | text |
| Error text on error background | `--color-danger` on `--color-danger-bg` | 5.91:1 | text |
| Disabled button text | `--color-disabled-fg` on `--color-disabled-bg` | 6.15:1 | text |
| Complete pill text | `--color-on-ok` on `--color-ok-bg` | 8.30:1 | text |
| White text on the gold banner | `--color-card` on `--color-accent` | 4.92:1 | text |
| Gold progress bar on its track | `--color-accent` on `--color-track` | 3.99:1 | graphic (3:1) |

The skill's own personal-finance palette uses a green `#059669`, which gives only 3.77:1 on white. Direction B uses `#047857` instead (5.48:1).

## 4. Components

All are in `components.css`.

| Component | Used for |
| --- | --- |
| App shell: top bar, status line, tab bar, left rail | Every screen |
| Card, completeness card, progress bar with ARIA values | Profile and gate screens |
| Group list and row with chips and an edit button | Profile answers |
| Chips (relief codes), pills and badges (Draft, Active, Incomplete, Complete) | Profile, history |
| Buttons: primary, secondary, disabled | All forms |
| Field with label, help text, error beside the field | Dependant form |
| Segmented Yes and No, with no preselected answer | Dependant form |
| Choice cards (one question per screen) and the step bar | Guided creation |
| To-do list | Gate screen |
| Dialog (bottom sheet on a phone, centred on desktop) and tick box | Apply to later years |
| Year cards (phone) and table (desktop) | Tax-year history |
| Banner and lock flag | Admin support mode, filed years |

## 5. Where the files are

```
docs/design/
  README.md                          a map for developers
  DES_000_Design_System.md           this document
  components.css                     the components
  tokens/tokens.css                  direction A, in use
  tokens/theme_b_backup.css          direction B, backup
  directions/                        the A and B comparison pages and screenshots
  tools/build_f0_mockups.py          builds the F0 mockup pages
  phase-1_R1/F0_User_Profile/        DES-F0 and its mockups and screenshots
```

A new feature or phase gets its own folder in the same way, for example `phase-1_R1/F1_Tax_Calculator/` and `phase-2_R2/F0_User_Profile/`.

## 6. How to rebuild and photograph the mockups

1. `python3 docs/design/tools/build_f0_mockups.py` writes the pages in `mockups/en` and `mockups/ms`. It reads no real data.
2. Open each page in Chrome and capture it with the device-metrics override: 360 px wide at scale 2 for the phone, 1280 px wide at scale 1 for the desktop. The page height is the height of the `.app` element, and 800 px for the dialog page. The pages need an internet connection once for the fonts.
3. Save the images in `screenshots/<mobile or desktop>/<en or ms>/`, named like the page.

## 7. Open points

- How the tokens enter the Vue application (CSS variables as they are, or a Tailwind theme) is decided when the project is created ([ADR-001](../decisions/ADR_001_Language_And_Framework.md)). The Laravel starter kit for Vue may bring its own component library; this is not checked yet.
- The font files, with their licences, are added to the repository when the project is created.
- The design of screens for features F1 to F5 and for later phases is not done.
- A review of the Bahasa Malaysia text by a native speaker (D3).
