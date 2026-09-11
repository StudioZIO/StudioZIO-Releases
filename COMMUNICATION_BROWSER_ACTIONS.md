# StudioZIO Communication Browser Actions
Version 1.0 · 2026-09-11

This document lists every action that requires authenticated browser interaction
or external account access. Coding-agent work is complete. A browser agent
executes this document in order.

**Prerequisite for all entries below:**
The Pre-Announcement Publication Gate (Section 3 of RELEASE_CHECKLIST.md) must
be fully complete before any external communication is sent.

No communication may invent product truth independently. Every claim must derive
from the Release Truth Manifest in `release-truth/`.

---

## Action 1 — Formspree email routing verification

| Field | Value |
|---|---|
| **Platform** | Formspree |
| **Objective** | Confirm that the mrpzbbzp endpoint routes correctly: (a) MixRack notify signups land in the correct inbox, (b) Hub contact form submissions land in the correct inbox |
| **Exact destination** | https://formspree.io/f/mrpzbbzp — log in at formspree.io |
| **Required material** | Formspree account credentials |
| **Success criteria** | mrpzbbzp shows correct destination email; both form types (notify intent = mixrack-notify, support intent = Hub support) reach the right inbox; submissions since the last release are accounted for |
| **Dependency** | None — this is an always-on operational check |
| **Status** | PENDING |

---

## Action 2 — KVR listing update: Mastering Suite 2.1.1

| Field | Value |
|---|---|
| **Platform** | KVR Audio |
| **Objective** | Update the StudioZIO Mastering Suite KVR listing to reflect 2.1.1, corrected installer, Universal architecture, and AU / VST3 / AAX / Standalone formats |
| **Exact destination** | https://www.kvraudio.com/product/studiozio-mastering-suite-by-studiozio — log in as developer |
| **Required material** | Current installer filename: `StudioZIO-Mastering-Suite-2.1.1.pkg` · SHA-256: `b054098c4f6565e5e469efd41554425d468830a001c9d4c531e72ab8c50f4cf1` · Release tag: `mastering-suite-v2.1.1-install-fix-2026.09.11` · Download URL: `https://github.com/StudioZIO/StudioZIO-Releases/releases/download/mastering-suite-v2.1.1-install-fix-2026.09.11/StudioZIO-Mastering-Suite-2.1.1.pkg` |
| **Success criteria** | KVR listing shows version 2.1.1, formats AU / VST3 / AAX / Standalone, architecture Universal (Apple Silicon and Intel), price Free, download link pointing to the correct release asset |
| **Dependency** | Release Truth Manifest `release-truth/mastering-suite-2.1.1-install-fix-2026.09.11.yaml` must have `capability_gate_passed: true` (it does — verified 2026-09-11) |
| **Status** | PENDING |

---

## Action 3 — KVR listing update: Tempo Delay 4.0.1

| Field | Value |
|---|---|
| **Platform** | KVR Audio |
| **Objective** | Verify that the Tempo Delay KVR listing reflects 4.0.1, AAX format, and arm64-only architecture. Update if any field is stale |
| **Exact destination** | https://www.kvraudio.com/product/studiozio-tempo-delay-by-studiozio — log in as developer |
| **Required material** | Version: 4.0.1 · Installer: `StudioZIOTempoDelay-v4.0.1-macOS-arm64-AAX.pkg` · SHA-256: `4e919c509cca196e178a0a991d24c02eb7e1ba81c5890e0f4fce16aba94ec055` · Formats: AU / VST3 / AAX / Standalone · Architecture: Apple Silicon (arm64) only |
| **Success criteria** | KVR listing shows 4.0.1, formats AU / VST3 / AAX / Standalone, architecture Apple Silicon only, price Free, correct download link |
| **Dependency** | Release Truth Manifest `release-truth/tempo-delay-4.0.1.yaml` verified |
| **Status** | PENDING |

---

## Action 4 — LinkedIn product announcement

| Field | Value |
|---|---|
| **Platform** | LinkedIn |
| **Objective** | Post an announcement for Mastering Suite 2.1.1 (corrected installer) and Tempo Delay 4.0.1 AAX availability |
| **Exact destination** | StudioZIO LinkedIn company page or Mert Erkan personal profile, depending on which property is active |
| **Required material** | Short announcement copy (max 1300 chars, professional tone). Suggested headline: "StudioZIO Mastering Suite 2.1.1 and Tempo Delay 4.0.1 — now with AAX for Pro Tools." Body: state Universal architecture for Mastering Suite, arm64-only for Tempo Delay, Free, link to studiozio.vercel.app. Do not invent claims not in the Release Truth Manifest |
| **Success criteria** | Post is live, links correctly to the Hub, formats and architecture stated accurately, no content that contradicts the Release Truth Manifest |
| **Dependency** | Actions 2 and 3 complete (KVR must be updated before LinkedIn directs traffic) |
| **Status** | PENDING |

---

## Action 5 — Reddit/forum community announcement

| Field | Value |
|---|---|
| **Platform** | Reddit — suggested: r/audioproduction, r/reaper, VI-Control audio dev thread |
| **Objective** | Announce AAX availability and Mastering Suite 2.1.1 corrected installer to relevant audio communities |
| **Exact destination** | r/audioproduction (post) · REAPER forum or r/reaper (post) · VI-Control "Free plug-ins" thread if appropriate |
| **Required material** | Same factual copy as LinkedIn, adapted to community tone. Must include: what shipped, that it is free, no registration required, link to Hub and to KVR. Acknowledge the installer fix transparently if posting in technical communities |
| **Success criteria** | Post is live, no factual errors, community moderation rules complied with |
| **Dependency** | Action 2 and 3 complete |
| **Status** | PENDING |

---

## Action 6 — Mastering Suite site local changes → PR

| Field | Value |
|---|---|
| **Platform** | GitHub — StudioZIO/StudioZIO-Mastering-Suite-Site repository |
| **Objective** | The local working tree at `/Users/mert/Projects/StudioZIO-Mastering-Suite-Site` has 8 staged modifications (footer-brand, Instagram/KVR social links, Notes and Community nav links, 404.html, styles.css, tools/README.md, tools/build_ms_docs.py). These improve navigation and brand consistency. They need to be committed and submitted as a PR to be deployed via Vercel |
| **Exact destination** | https://github.com/StudioZIO/StudioZIO-Mastering-Suite-Site — create PR from local branch targeting origin/main |
| **Required material** | The uncommitted local changes listed above. Note: local HEAD (e7c6775) is behind origin/main (3cc76b4) by 2 commits; rebase onto origin/main before creating the PR to avoid conflicts |
| **Success criteria** | PR created, CI/Vercel preview passes, changes merged, Vercel production deployment reflects updated nav and footer |
| **Dependency** | Must rebase local work onto origin/main (2 commits ahead: copy-audit-fixes, header-parity) |
| **Status** | PENDING — requires git rebase + push in a terminal session with GitHub credentials |

---

## Action 7 — Hub local pull and redeploy (informational)

| Field | Value |
|---|---|
| **Platform** | GitHub — StudioZIO/StudioZIO-Web |
| **Objective** | The local Hub repo at `/Users/mert/StudioZIO-Web` is 8 commits behind origin/main. Origin/main already has all correct product data (corrected installer SHA, filename, download URL). No new code changes are needed — this is a tracking update |
| **Exact destination** | Local: `cd /Users/mert/StudioZIO-Web && git pull origin main` |
| **Required material** | None — local repo is clean, pull is safe |
| **Success criteria** | Local HEAD matches origin/main (7a6f411); `npm run check` passes; dist/ is rebuilt with correct catalog data |
| **Dependency** | None |
| **Status** | PENDING — safe to run locally at any time |

---

## Excluded from this document

The following are already handled by existing owned infrastructure and require
no new browser action:

- **KVR developer page** — separate from product listings; no new update needed unless releasing a new product
- **YouTube** — no new video to post at this time; existing overview video is linked from the Hub press page
- **Instagram** — no new visual asset to post at this time; existing presence is linked from Hub footer and press page
- **GitHub Releases** — already live at correct URLs (verified via Release Truth Manifests)
- **Homebrew** — cask reconciliation is covered by Section 3 of RELEASE_CHECKLIST.md before announcement

---

## Communication source-of-truth rule (summary)

All external communication must trace back to:

```
FINAL ARTIFACT
  → RELEASE TRUTH MANIFEST (release-truth/*.yaml)
    → RELEASE METADATA
      → PUBLIC COMMUNICATION
```

Do not copy version, SHA, filename, format list, or architecture from memory,
prior posts, or other external sources. Read the manifest. See
`FORMAT_TRUTH_PUBLICATION_CONTRACT.md` for the full governance contract.
