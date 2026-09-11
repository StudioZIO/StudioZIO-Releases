# StudioZIO Communication Browser Actions
Version 1.1 · 2026-09-11

This document lists every action that requires authenticated browser interaction
or external account access and has not yet been completed. Coding-agent work is
complete. A browser agent executes this document in order.

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

## Action 2 — LinkedIn product announcement

| Field | Value |
|---|---|
| **Platform** | LinkedIn |
| **Objective** | Post an announcement for Mastering Suite 2.1.1 (corrected installer) and Tempo Delay 4.0.1 AAX availability |
| **Exact destination** | StudioZIO LinkedIn company page or Mert Erkan personal profile, depending on which property is active |
| **Required material** | Short announcement copy (max 1300 chars, professional tone). Suggested headline: "StudioZIO Mastering Suite 2.1.1 and Tempo Delay 4.0.1 — now with AAX for Pro Tools." Body: state Universal architecture for Mastering Suite, arm64-only for Tempo Delay, Free, link to studiozio.vercel.app. Claims must not exceed what the Release Truth Manifest states |
| **Success criteria** | Post is live, links correctly to the Hub, formats and architecture stated accurately, no content contradicts the Release Truth Manifest |
| **Dependency** | None — KVR is already complete |
| **Status** | PENDING |

---

## Action 3 — Reddit / forum community announcement

| Field | Value |
|---|---|
| **Platform** | Reddit — suggested: r/audioproduction, r/reaper, VI-Control audio dev thread |
| **Objective** | Announce AAX availability and Mastering Suite 2.1.1 corrected installer to relevant audio communities |
| **Exact destination** | r/audioproduction (post) · REAPER forum or r/reaper (post) · VI-Control "Free plug-ins" thread if appropriate |
| **Required material** | Same factual copy as LinkedIn, adapted to community tone. Must include: what shipped, that it is free, no registration required, link to Hub. Acknowledge the installer fix transparently if posting in technical communities |
| **Success criteria** | Post is live, no factual errors, community moderation rules complied with |
| **Dependency** | None — KVR is already complete |
| **Status** | PENDING |

---

## Completed — no further action required

The following channels have already been updated and must not be re-actioned:

| Channel | Status |
|---|---|
| KVR — Mastering Suite listing | COMPLETE |
| KVR — Tempo Delay listing | COMPLETE |
| YouTube | COMPLETE |
| Instagram | COMPLETE |
| GitHub Releases | COMPLETE — live at correct URLs, verified via Release Truth Manifests |
| Homebrew | Governed by RELEASE_CHECKLIST.md Section 3 |

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
