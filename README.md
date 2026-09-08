# StudioZIO Releases

Official public release downloads for StudioZIO software.

This repository is a binary-release registry, not a product source-code repository. StudioZIO product source repositories may be private. Installers are provided as GitHub Release assets and are not committed to this Git history.

Where stated for an individual release, macOS installers are Developer ID signed and Apple notarized.

## Current releases

### StudioZIO Mastering Suite 2.1.1

- Platform: macOS 11 or later
- Architecture: Universal — Apple Silicon and Intel
- Formats: Standalone, Audio Unit (AU), VST3
- Installer: `StudioZIO-Mastering-Suite-2.1.1.pkg`
- SHA256: `97dcd2f55e317054fd15dbbee098a755623838345fc37cb89b114864d1e3da5d`
- Release: [`mastering-suite-v2.1.1-flicker-hold-2026.09.08`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/mastering-suite-v2.1.1-flicker-hold-2026.09.08)
- Product site: <https://studioziomasteringsuite.vercel.app/>

**2.1.1 shipped twice.** The 8 September build above is the current one. An
earlier 2.1.1, tagged `mastering-suite-v2.1.1-signed-2026.09.07`, is still
published and still downloadable, and it is a different file — 15,551,052 bytes
with SHA-256 `68e7abb8…`, against 15,564,737 bytes and `97dcd2f5…` here. The
version number is the same on both, so the checksum is the only thing that
tells them apart. If yours reads `68e7abb8…` you have the older build: it is
genuine and correctly signed, but download the one above instead.

### StudioZIO Tempo Delay 4.0.1

- Platform: macOS 12 or later
- Architecture: Apple Silicon (arm64) only — there is no Intel build
- Formats: Standalone, Audio Unit (AU), VST3
- Installer: `StudioZIOTempoDelay-v4.0.1-macOS-arm64.pkg`
- SHA256: `adae51020ee920d607f04e15c8db3c044c8dadd7bf3e01762dd56cc1c70072c7`
- Release: [`tempo-delay-v4.0.1`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/tempo-delay-v4.0.1)
- Product site: <https://www.tempodelay.tech/>

Both products are free. All StudioZIO products are listed on the hub:
<https://studiozio.vercel.app/>

## Verifying a download

Download the installer from the [Releases](https://github.com/StudioZIO/StudioZIO-Releases/releases) page, then in Terminal:

```sh
shasum -a 256 ~/Downloads/StudioZIO-Mastering-Suite-2.1.1.pkg
```

The output must match the SHA256 listed above for that exact file. If it does not, do not install it — delete the file and download it again.

**A checksum belongs to one release, not to one version number.** Every release is a different file, so an installer from an earlier release will not match the value above — check it against the release you actually downloaded from, and each release on the Releases page carries its own assets and notes.

That distinction matters for Mastering Suite 2.1.1 in particular, because two releases carry that version number. A mismatch there does not mean the download was tampered with; it means you have the other 2.1.1. The note above says which is which.

Earlier versions stay published so that existing links keep working. The versions listed above are the current ones.
