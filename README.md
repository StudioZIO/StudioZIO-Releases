# StudioZIO Releases

Official public release downloads for StudioZIO software.

This repository is a binary-release registry, not a product source-code repository. StudioZIO product source repositories may be private. Installers are provided as GitHub Release assets and are not committed to this Git history.

Where stated for an individual release, macOS installers are Developer ID signed and Apple notarized.

## Current releases

### StudioZIO Mastering Suite 2.1.1

- Platform: macOS 11 or later
- Architecture: Apple Silicon / arm64
- Formats: AU / VST3 / AAX / Standalone
- Installer: `StudioZIO-Mastering-Suite-v2.1.1-macOS-arm64.pkg`
- SHA256: `7ac80cb1a340a92b1dc606254604b58b83907b0a1d594e29a77a39d807319ceb`
- Release: [`mastering-suite-v2.1.1-aax-2026.09.10`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/mastering-suite-v2.1.1-aax-2026.09.10)
- Status: AAX validated in Pro Tools
- Product site: <https://studioziomasteringsuite.vercel.app/>

**Historical 2.1.1 releases:**
- The `flicker-hold` release (`StudioZIO-Mastering-Suite-2.1.1.pkg`, SHA-256 `2345deeb...`) published on 8/9 September remains available.
- The `signed` release (`StudioZIO-Mastering-Suite-2.1.1.pkg`, SHA-256 `68e7abb8...`) published on 7 September remains available.

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
shasum -a 256 ~/Downloads/StudioZIO-Mastering-Suite-v2.1.1-macOS-arm64.pkg
```

The output must match the SHA256 listed above for that exact file. If it does not, do not install it — delete the file and download it again.

**A checksum belongs to one release, not to one version number.** Every release is a different file, so an installer from an earlier release will not match the value above — check it against the release you actually downloaded from, and each release on the Releases page carries its own assets and notes.

Earlier versions stay published so that existing links keep working. The versions listed above are the current ones.
