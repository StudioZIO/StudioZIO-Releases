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
- [ ] Third-party (KVR) verification is complete

## 4. Final Cutover
- [ ] Announce release globally
