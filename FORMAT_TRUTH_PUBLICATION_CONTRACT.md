# StudioZIO Format Truth Publication Contract
Version 1.0

## Non-Negotiable Rule
No StudioZIO format or architecture claim may be published or changed until the final shipped artifact has been inspected for AU, VST3, AAX, Standalone, arm64 and x86_64 presence.

## 1. Purpose
This contract establishes the permanent governance infrastructure for publishing product capabilities, formats, and architecture truth. It ensures strict artifact-based verification before any downstream surfaces (websites, documentation, KVR) are updated.

## 2. Authority Order
The supreme authority for publication truth is the **FINAL IMMUTABLE ARTIFACT**. This supersedes build documentation, filenames, assumptions, and third-party listings. 

## 3. Format Existence Rule
A format is considered present only when the final immutable artifact contains the corresponding payload (.component, .vst3, .aaxplugin, .app).

## 4. Architecture Rule
Architecture truth must be extracted by binary analysis (`lipo -archs`, `file`) of the final contained executables, not inferred from package naming conventions (e.g., `-macOS-arm64.pkg`).

## 5. Package Inventory Gate
The final package must be expanded (without installation) to determine exactly which payloads are included.

## 6. Immutable Artifact Rule
Once published, artifacts are immutable. Artifacts must not be repackaged or renamed to fix cosmetic filename mismatch if the binary payload is otherwise correct. Release immutability outranks cosmetic filename accuracy.

## 7. Current vs Historical Truth
Current product specifications describe the latest available product state. Historical notes (e.g., SDK transitions, previous architecture limitations) must preserve chronological integrity and not be globally replaced.

## 8. Format List Semantics
- **PLUGIN FORMATS:** Refers exclusively to `AU / VST3 / AAX`.
- **PRODUCT OUTPUTS:** Must encompass all endpoints, e.g., `AU / VST3 / AAX / Standalone`.
Standalone must not be mislabeled as a plug-in API.

## 9. Host Support Rule
Host claims (e.g., "AAX validated in Pro Tools", "StudioZIO Verified" in REAPER/Logic) must be backed by testing and must not be altered based on broad architecture assumptions. Standalone must never be classified as a DAW host.

## 10. Publication Matrix
Every final capability fact (AU, VST3, AAX, Standalone, arm64, x86_64, validation) maps strictly from the artifact to the generated `Release Truth Manifest`.

## 11. Source → Render → Live Rule
Publication mandates an unbroken chain of truth propagation: Release Truth Manifest → Source Code → Generated Output → Rendered DOM → Live Public Surface.

## 12. Contradiction Rule
If any downstream surface contradicts the Release Truth Manifest, publication must halt, and the stale claim must be immediately corrected.

## 13. Test Contract
Tests and validators must enforce Release Truth Manifest compliance structurally but must not statically hardcode dynamic truths unless enforcing structural parity. Validators must not weaken checks to appease failing tests; stale test data must be fixed to match artifact evidence.

## 14. Change Authorization Rule
No agent or human may authorize a format/architecture update without referencing the finalized `Release Truth Manifest` mapped to the precise artifact.

## 15. Third-Party Listing Rule
Sites like KVR must be updated last in the chain and verified to align perfectly with the exact capability truth derived from the artifact.

## 16. Announcement Gate
Global announcements are blocked until:
1. The Release Truth Manifest is complete.
2. All source surfaces are synchronized.
3. Generated outputs are verified.
4. Rendered DOM is verified.
5. Live public surfaces are verified.
6. Third-party properties are verified.

## 17. Artifact Capability Inspection Gate
Before ANY StudioZIO public format, architecture, host-support, or platform claim is updated, the FINAL IMMUTABLE RELEASE ARTIFACT must be inspected directly.
The mandatory chain:
**FINAL IMMUTABLE ARTIFACT → EXPANDED PACKAGE MANIFEST → CONTAINED BINARY INSPECTION → RELEASE TRUTH MANIFEST → RELEASE METADATA → SOURCE → GENERATED OUTPUT → RENDERED DOM → LIVE PUBLIC SURFACE → THIRD-PARTY LISTINGS**

No stage may be skipped.

### The 12-Question Capability Gate
Publication cannot proceed until all 12 questions are answered from the final artifact:
1. AU PRESENT?
2. AU arm64?
3. AU x86_64?
4. VST3 PRESENT?
5. VST3 arm64?
6. VST3 x86_64?
7. AAX PRESENT?
8. AAX arm64?
9. AAX x86_64?
10. STANDALONE PRESENT?
11. STANDALONE arm64?
12. STANDALONE x86_64?

## Mixed-Architecture Rule
Collapsing mixed format architectures into a false global shorthand is strictly forbidden. If AU/VST3/Standalone are Universal but AAX is arm64 only, DO NOT publish product-wide `Universal` or `arm64 only`. Instead, publish format-specific architecture truth.

## Agent Consumption Rule
Before any AI agent modifies current StudioZIO public release information, it MUST:
1. Locate the matching Release Truth Manifest.
2. Confirm `capability_gate_passed = true`.
3. Derive format/architecture claims only from that manifest.
4. Stop if the manifest is missing, incomplete, or conflicts with the artifact.
No agent inference allowed.

## Communication Source-of-Truth Rule
Added 2026-09-11.

No release communication — including LinkedIn posts, Reddit threads, forum announcements,
press emails, KVR updates, YouTube descriptions, or Instagram captions — may state
product truth independently of the Release Truth Manifest.

The authorised derivation chain is:

```
FINAL ARTIFACT
  → RELEASE TRUTH MANIFEST (release-truth/*.yaml)
    → RELEASE METADATA (catalog.mjs, product site HTML)
      → PUBLIC COMMUNICATION (every external statement)
```

### What this means in practice
- Format lists (AU / VST3 / AAX / Standalone) must be copied from the manifest, not recalled from memory.
- Architecture claims (Universal / arm64-only) must come from the manifest `architecture.safe_product_wide_claim` field.
- SHA-256 checksums must be copied verbatim from the manifest `artifact.sha256` field.
- Version numbers must come from the manifest `product.version` field.
- Installer filenames must come from the manifest `artifact.filename` field.
- Pricing ("Free permanently") is stable and may be stated without manifest reference, but product format and architecture claims may not.

### Scope
This rule applies to both human authors and AI agents acting on behalf of StudioZIO.
The Agent Consumption Rule already requires AI agents to locate and
verify the manifest before modifying product information. This rule extends that
requirement to all downstream communication, not just source-code changes.

### Enforcement
Any external communication that contradicts the Release Truth Manifest must be
corrected immediately. The Contradiction Rule (Section 12) applies to all public
surfaces, including third-party platforms.
