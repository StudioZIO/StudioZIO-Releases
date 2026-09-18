# StudioZIO Releases

Official public release downloads for StudioZIO software.

This repository is a binary-release registry, not a product source-code repository. StudioZIO product source repositories may be private. Installers are provided as GitHub Release assets and are not committed to this Git history.

Where stated for an individual release, macOS installers are Developer ID signed and Apple notarized.

## Current releases

### StudioZIO Everything 1.0.2

- Platform: macOS 11.0 or later (Tempo Delay requires Apple Silicon and macOS 12.0 or later)
- Architecture: Universal — Apple Silicon and Intel, except Tempo Delay, which is Apple Silicon only
- Formats: AU / VST3 / AAX / Standalone for every included product
- Installer: [`StudioZIO-Everything-1.0.2.pkg`](https://github.com/StudioZIO/StudioZIO-Releases/releases/download/everything-v1.0.2/StudioZIO-Everything-1.0.2.pkg)
- SHA256: `9a51e7768f5bc8530c368b98bc79811144def1dfdcbb3f94143e1cbc13a43952`
- Release: [`everything-v1.0.2`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/everything-v1.0.2)
- Release truth: [`release-truth/everything-1.0.2.yaml`](https://github.com/StudioZIO/StudioZIO-Releases/blob/main/release-truth/everything-1.0.2.yaml)
- Status: Developer ID signed, Apple notarized and stapled

One installer for all seven StudioZIO products: Mastering Suite 2.1.1, Tempo Delay 4.0.1, MixRack 1.0.0, Inflator 1.0.0, Maximizer 1.0.3, Compressor 1.0.0 and De-Esser 1.0.0. Every component package is the qualified individual installer's, byte for byte. Products are selectable in the installer's Customize panel and selected by default; on Intel Macs and on macOS 11 the installer disables Tempo Delay automatically, and the other six products install and run.

**Earlier releases:**
- [`everything-v1.0.0`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/everything-v1.0.0) (`StudioZIO-Everything-1.0.0.pkg`, SHA-256 `0f148ecd...`) remains available. It includes Maximizer 1.0.2; on Intel Macs and macOS 11, deselect Tempo Delay in its Customize panel.

### StudioZIO De-Esser 1.0.0

- Platform: macOS 11.0 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: AU / VST3 / AAX / Standalone
- Installer: [`StudioZIO-De-Esser-1.0.0.pkg`](https://github.com/StudioZIO/StudioZIO-Releases/releases/download/deesser-v1.0.0/StudioZIO-De-Esser-1.0.0.pkg)
- SHA256: `698a5c45dc530b97bd4fc3c9f6e401bf4cbb414a435ff1d4235f6afa66e661f2`
- Release: [`deesser-v1.0.0`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/deesser-v1.0.0)
- Release truth: [`release-truth/deesser-1.0.0.yaml`](https://github.com/StudioZIO/StudioZIO-Releases/blob/main/release-truth/deesser-1.0.0.yaml)
- Status: Developer ID signed, Apple notarized and stapled; AAX validated in Pro Tools

### StudioZIO Compressor 1.0.0

- Platform: macOS 11.0 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: AU / VST3 / AAX / Standalone
- Installer: [`StudioZIO-Compressor-1.0.0.pkg`](https://github.com/StudioZIO/StudioZIO-Releases/releases/download/compressor-v1.0.0-clean-packaging-2026.09.16/StudioZIO-Compressor-1.0.0.pkg)
- SHA256: `96c9d4cccefc918ffef47b094464da901be742778b4fc6e97145ddcfa11d37bc`
- Release: [`compressor-v1.0.0-clean-packaging-2026.09.16`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/compressor-v1.0.0-clean-packaging-2026.09.16)
- Release truth: [`release-truth/compressor-1.0.0-clean-packaging-2026.09.16.yaml`](https://github.com/StudioZIO/StudioZIO-Releases/blob/main/release-truth/compressor-1.0.0-clean-packaging-2026.09.16.yaml)
- Status: Developer ID signed, Apple notarized and stapled

Same 1.0.0 plug-in code as the first release, repackaged by the canonical pipeline as four component packages with clean payload metadata.

**Historical 1.0.0 release:**
- [`compressor-v1.0.0`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/compressor-v1.0.0) (`StudioZIO-Compressor-1.0.0.pkg`, SHA-256 `49db1ddd...`) remains available. Single-component package with AppleDouble metadata records in its payload; superseded packaging.

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

### StudioZIO Maximizer 1.0.3

- Platform: macOS 11.0 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: AU / VST3 / AAX / Standalone
- Installer: [`StudioZIO-Maximizer-1.0.3.pkg`](https://github.com/StudioZIO/StudioZIO-Releases/releases/download/maximizer-v1.0.3/StudioZIO-Maximizer-1.0.3.pkg)
- SHA256: `d589be77a2d72355a86a2bd2b7d5ea70dcd9d2b5871ec61c6960e5754abecc50`
- Release: [`maximizer-v1.0.3`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/maximizer-v1.0.3)
- Release truth: [`release-truth/maximizer-1.0.3.yaml`](https://github.com/StudioZIO/StudioZIO-Releases/blob/main/release-truth/maximizer-1.0.3.yaml)
- Status: Developer ID signed, Apple notarized and stapled

Fixes Standalone microphone/live-input permission on macOS; the Standalone now uses the StudioZIO Maximizer name and icon. No DSP, sound, parameter or GUI design changes.

**Earlier 1.0.2 releases:**
- [`maximizer-v1.0.2-clean-packaging-2026.09.16`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/maximizer-v1.0.2-clean-packaging-2026.09.16) (`StudioZIO-Maximizer-1.0.2.pkg`, SHA-256 `69510b08...`) remains available. Its Standalone cannot open audio input.
- [`maximizer-v1.0.2`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/maximizer-v1.0.2) (`StudioZIO-Maximizer-1.0.2.pkg`, SHA-256 `673da7c7...`) remains available. AppleDouble metadata records in its payload; superseded packaging.

### StudioZIO Inflator 1.0.0

- Platform: macOS 11.0 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: AU / VST3 / AAX / Standalone
- Installer: `StudioZIO-Inflator-1.0.0.pkg`
- SHA256: `c138a979cb80bd04b755ab4c308a1b0dc8ccad518d6483076e2b8a3ba05fabde`
- Release: [`inflator-v1.0.0`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/inflator-v1.0.0)
- Status: Developer ID signed and Apple notarized

Pro Tools host validation is not claimed for this release.

### StudioZIO MixRack 1.0.0

- Platform: macOS 11.0 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: AU / VST3 / AAX / Standalone
- Installer: [`StudioZIO-Mixrack-1.0.0.pkg`](https://github.com/StudioZIO/StudioZIO-Releases/releases/download/mixrack-v1.0.0/StudioZIO-Mixrack-1.0.0.pkg)
- SHA256: `9452403bf1150bd4188cbfe550f1ad0840087c68fe0b56f5036f08e17b4a4fda`
- Release: [`mixrack-v1.0.0`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/mixrack-v1.0.0)
- Release truth: [`release-truth/mixrack-1.0.0.yaml`](https://github.com/StudioZIO/StudioZIO-Releases/blob/main/release-truth/mixrack-1.0.0.yaml)
- Status: Developer ID signed, Apple notarized and stapled

### StudioZIO Tempo Delay 4.0.1 (clean installer 2026-09-16)

- Platform: macOS 12.0 or later
- Architecture: Apple Silicon (arm64) only — no Intel build
- Formats: AU / VST3 / AAX / Standalone
- Installer: [`StudioZIOTempoDelay-v4.1.0-macOS-arm64.pkg`](https://github.com/StudioZIO/StudioZIO-Releases/releases/download/tempo-delay-v4.1.0-clean-packaging-2026.09.16/StudioZIOTempoDelay-v4.1.0-macOS-arm64.pkg)
- SHA256: `fa16f0c9f04f5f56e446ae06074a0f3b0a8e193fa21089e0bf92c486d197910d`
- Release: [`tempo-delay-v4.1.0-clean-packaging-2026.09.16`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/tempo-delay-v4.1.0-clean-packaging-2026.09.16)
- Release truth: [`release-truth/tempo-delay-4.1.0-clean-packaging-2026.09.16.yaml`](https://github.com/StudioZIO/StudioZIO-Releases/blob/main/release-truth/tempo-delay-4.1.0-clean-packaging-2026.09.16.yaml)
- Status: Developer ID signed, Apple notarized and stapled

The product is 4.0.1: the plug-ins report 4.0.1 in every host. The installer file and its four component receipts carry 4.1.0, the version the four-component package topology uses; that number is an installer detail, not a plug-in version.

**Historical 4.0.1 releases:**
- [`tempo-delay-v4.0.1-aax-2026.09.10`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/tempo-delay-v4.0.1-aax-2026.09.10) (`StudioZIOTempoDelay-v4.0.1-macOS-arm64-AAX.pkg`, SHA-256 `4e919c50...`) remains available; same plug-ins, superseded packaging.
- [`tempo-delay-v4.0.1`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/tempo-delay-v4.0.1) (`StudioZIOTempoDelay-v4.0.1-macOS-arm64.pkg`, SHA-256 `adae5102...`) remains available.

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
