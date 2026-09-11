# Release Truth Manifests

This directory contains Release Truth Manifests for StudioZIO products.

## Purpose
A Release Truth Manifest is the canonical source of truth for a finalized software release's capabilities (formats, architecture, binaries, installation destinations). 
These manifests enforce the **StudioZIO Format Truth Publication Contract**.

## Consumers
- Human engineers publishing updates to the StudioZIO ecosystem.
- Automated CI pipelines validating structural changes.
- AI agents reading repository state to ensure accurate propagation of release capabilities.

## Generation
Manifests are generated ONLY through direct, read-only binary inspection of the final, immutable `.pkg` artifacts (e.g., using `pkgutil --expand`, `lipo`, `file`). 
Filenames are deliberately excluded as a source of truth to prevent cosmetic naming assumptions (like `-macOS-arm64.pkg` overriding internal Universal binaries).

## Immutability
Once an artifact is frozen and `capability_gate_passed: true` is committed, the manifest becomes historical release evidence. It must never be silently rewritten. Factually wrong manifests require explicit, documented correction.

## Superseded releases
A manifest whose artifact has been replaced carries a root-level `superseded` block naming the release that replaced it, the date, and why. Where the artifact should not be installed at all it also carries `install_status: does_not_install` and `do_not_install: true`.

**Read that block before treating any other field as current truth.** The recorded capability facts stay exactly as they were inspected — they are evidence about that artifact, not a recommendation to ship it. A manifest can be entirely accurate about what is inside a package that nonetheless fails to install; `mastering-suite-2.1.1.yaml` is the worked example.

The propagation gates (`source_surfaces_synchronized`, `live_surfaces_verified`, `third_party_verified`) go false once a release stops being current, because no download surface points at it any more. `capability_gate_passed` stays as recorded: it describes an inspection that happened, not the release's standing.
