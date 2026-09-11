# StudioZIO Release & Announcement Checklist

## 1. Rule 17 Capability Inspection Gate
Before any public metadata, sites, or third-party listings are updated, the following mandatory steps must be completed:
- [ ] Final artifact frozen
- [ ] SHA computed
- [ ] Public artifact downloaded and reverified
- [ ] Package expanded (read-only)
- [ ] AU presence and architecture verified via `lipo`/`file`
- [ ] VST3 presence and architecture verified via `lipo`/`file`
- [ ] AAX presence and architecture verified via `lipo`/`file`
- [ ] Standalone presence and architecture verified via `lipo`/`file`
- [ ] 12-question capability gate PASS
- [ ] Release Truth Manifest created in `release-truth/`

## 2. Source & Metadata Updates
Only after the Capability Gate passes:
- [ ] Update StudioZIO-Web source
- [ ] Update Mastering Site source
- [ ] Update Tempo Site source
- [ ] Update Release repository tables
- [ ] Update Support documents

## 3. Pre-Announcement Publication Gate
Global announcements are blocked until:
- [ ] Release Truth Manifest is committed and valid
- [ ] Source synchronization is complete
- [ ] Generated output verification is complete
- [ ] Rendered DOM verification is complete
- [ ] Live public-surface verification is complete
- [ ] Homebrew casks reconciled (URL/SHA and accurate uninstall receipts)
- [ ] Third-party (KVR) verification is complete

## 4. Final Cutover
- [ ] Announce release globally

## 5. Canonical Pipeline Architecture

To ensure immutable reproducibility, the release process follows a strict canonical pipeline:

- **Canonical Build Entrypoint:** Local `cmake` configuration followed by `cmake --build build-release --config Release`. (e.g. `cmake -S . -B build-release -DCMAKE_BUILD_TYPE=Release`).
- **Canonical Packaging Entrypoint:** The automated distribution scripting inside the source repository (e.g. CPack/Distribution scripts executed via CMake).
- **Mandatory Verifier:** `tools/verify_release_package.py` must be executed against the final `.pkg`.
- **Rule 17 Location:** Rule 17 occurs immediately after the final artifact is generated and before any metadata or external source is updated.
- **Release Truth Record:** Recorded exclusively in `release-truth/<product>-<version>.yaml` in this repository.
- **Homebrew Reconciliation:** Must happen during the Pre-Announcement Publication Gate (Stage 3), after the Release Truth Manifest is valid but before global announcement.
- **Third-Party Listings:** Checked at the very end of Stage 3 (Pre-Announcement Publication Gate) to ensure perfect alignment with the artifact truth.

## 6. Manual Packaging Prohibition

**PRODUCTION RELEASE PKGS MUST NOT BE MANUALLY ASSEMBLED.**

Forbidden actions:
- manual component copying
- ad-hoc `pkgbuild`/`productbuild` execution
- combining components from separate builds
- inserting a new format (e.g. AAX) into an older package
- modifying expanded PKG payloads
- building around a broken canonical pipeline

If canonical packaging fails: **fix the canonical pipeline**. Do not create a workaround package.

## 7. Format-Addition Governance

When a new format is added, the following must be verified:
1. build target
2. canonical package component
3. install destination
4. final package verification
5. Rule 17
6. Release Truth Manifest
7. web download metadata
8. download verifier
9. Homebrew cask URL/SHA
10. Homebrew uninstall receipts from PackageInfo IDs
11. Support if applicable
12. third-party listings such as KVR
