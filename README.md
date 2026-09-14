# StudioZIO Releases

Official public release downloads for StudioZIO software.

This repository is a binary-release registry, not a product source-code repository. StudioZIO product source repositories may be private. Installers are provided as GitHub Release assets and are not committed to this Git history.

Where stated for an individual release, macOS installers are Developer ID signed and Apple notarized.

## Current releases

### StudioZIO Mastering Suite 2.1.1

- Platform: macOS 11 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: AU / VST3 / AAX / Standalone
- Installer: `StudioZIO-Mastering-Suite-2.1.1.pkg`
- SHA256: `b054098c4f6565e5e469efd41554425d468830a001c9d4c531e72ab8c50f4cf1`
- Release: [`mastering-suite-v2.1.1-install-fix-2026.09.11`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/mastering-suite-v2.1.1-install-fix-2026.09.11)
- Status: AAX validated in Pro Tools
- Product site: <https://studioziomasteringsuite.vercel.app/>

This release republishes the same 2.1.1 build with corrected installer
packaging. In the previous release the AU, VST3 and Standalone components
each stored their payload as a folder rather than an archive, so the macOS
Installer had nothing to unpack and installed none of them while still
reporting success. Only the AAX component installed. The plug-in code is
unchanged.

**Historical 2.1.1 releases:**
- The `aax` release (`StudioZIO-Mastering-Suite-v2.1.1-macOS-arm64.pkg`, SHA-256 `7ac80cb1...`) published on 10 September remains available. Do not install it: its AU, VST3 and Standalone components do not install.
- The `flicker-hold` release (`StudioZIO-Mastering-Suite-2.1.1.pkg`, SHA-256 `2345deeb...`) published on 8/9 September remains available.
- The `signed` release (`StudioZIO-Mastering-Suite-2.1.1.pkg`, SHA-256 `68e7abb8...`) published on 7 September remains available.

### StudioZIO Maximizer 1.0.2

- Platform: macOS 11 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: AU / VST3 / AAX / Standalone
- Installer: `StudioZIO-Maximizer-1.0.2.pkg`
- SHA256: `673da7c759b0cac3741ee816920a5ff2c199d01b975a1c6ffe7a48f65bcb3db6`
- Release: [`maximizer-v1.0.2`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/maximizer-v1.0.2)
- Status: Developer ID signed and Apple notarized; AAX PACE signing verified (Signing Only)

This maintenance release stabilizes the public metering path, prevents startup true-peak display transients, and updates the standalone GUI version label to `v1.0.2`. The audio/DSP path is unchanged. Pro Tools host validation is not claimed for this release.

### StudioZIO Inflator 1.0.0

- Platform: macOS 11.0 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: AU / VST3 / AAX / Standalone
- Installer: `StudioZIO-Inflator-1.0.0.pkg`
- SHA256: `c138a979cb80bd04b755ab4c308a1b0dc8ccad518d6483076e2b8a3ba05fabde`
- Release: [`inflator-v1.0.0`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/inflator-v1.0.0)
- Status: Developer ID signed and Apple notarized

Pro Tools host validation is not claimed for this release.

### StudioZIO Tempo Delay 4.0.1

- Platform: macOS 12 or later
- Architecture: Apple Silicon (arm64) only — there is no Intel build
- Formats: Standalone, Audio Unit (AU), VST3, AAX
- Installer: `StudioZIOTempoDelay-v4.0.1-macOS-arm64-AAX.pkg`
- SHA256: `4e919c509cca196e178a0a991d24c02eb7e1ba81c5890e0f4fce16aba94ec055`
- Release: [`tempo-delay-v4.0.1-aax-2026.09.10`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/tempo-delay-v4.0.1-aax-2026.09.10)
- Status: AAX validated in Pro Tools
- Product site: <https://www.tempodelay.tech/>

**Historical 4.0.1 releases:**
- The initial `tempo-delay-v4.0.1` release (`StudioZIOTempoDelay-v4.0.1-macOS-arm64.pkg`, SHA-256 `adae5102...`) remains available.

Both products are free. All StudioZIO products are listed on the hub:
<https://studiozio.vercel.app/>

## Release artifact immutability

Once a release artifact is public:

same version + same tag + same filename

must always refer to the same bytes.

Future rebuilds, repacks, installer changes, signing changes, or binary replacements MUST use a new release identity/tag. Do not silently replace release assets under an existing published identity. The purpose is checksum traceability and reproducibility.

## Verifying a download

Download the installer from the [Releases](https://github.com/StudioZIO/StudioZIO-Releases/releases) page, then in Terminal:

```sh
shasum -a 256 ~/Downloads/StudioZIO-Mastering-Suite-2.1.1.pkg
```

The output must match the SHA256 listed above for that exact file. If it does not, do not install it — delete the file and download it again.

**A checksum belongs to one release, not to one version number.** Every release is a different file, so an installer from an earlier release will not match the value above — check it against the release you actually downloaded from, and each release on the Releases page carries its own assets and notes.

Earlier versions stay published so that existing links keep working. The versions listed above are the current ones.

## Release Truth & Publication Governance

Current public format and architecture truth is strictly governed by the [StudioZIO Format Truth Publication Contract](FORMAT_TRUTH_PUBLICATION_CONTRACT.md).

- Every finalized release must map to a formal [Release Truth Manifest](release-truth/) established directly from artifact binaries.
- Release filenames (e.g. `-macOS-arm64`) are not a valid source of architecture truth.
- Final artifact inspection outranks all filenames, assumptions, and legacy documentation.
