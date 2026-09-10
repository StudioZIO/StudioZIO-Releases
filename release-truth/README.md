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
