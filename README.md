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
- SHA256: `68e7abb87458bcf8e331f435c7bec7792d33e67fe5c9a5e834195676c11bad7b`
- Release: [`mastering-suite-v2.1.1-signed-2026.09.07`](https://github.com/StudioZIO/StudioZIO-Releases/releases/tag/mastering-suite-v2.1.1-signed-2026.09.07)
- Product site: <https://studioziomasteringsuite.vercel.app/>

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

**A checksum is only valid for the one version it is listed under.** Every release is a different file, so an installer from an earlier release will not match the value above and that mismatch means nothing is wrong — check the value against the version you actually downloaded. Each release on the Releases page carries its own assets and notes.

Earlier versions stay published so that existing links keep working. The versions listed above are the current ones.
