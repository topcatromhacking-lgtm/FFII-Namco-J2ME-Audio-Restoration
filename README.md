# Final Fantasy II — Namco J2ME Audio Restoration

Restoration of independent background-music and sound-effect controls in Namco's **Final Fantasy II** J2ME edition.

**Status (24 October 2026): tested audio restoration, candidate for first stable public release. No GitHub release published yet.**

## User-validated features

- **Complete:** music and sound effects simultaneously.
- **Music Only**.
- **SFX Only**.
- **Off**.
- Earlier development tests confirmed functioning audio modes and behavior after restarting the game.

An internal **v1.0 candidate** with IPS/BPS patches and checksums was packaged during development; that does **not** mean it has been uploaded to this repository or retested from a clean install.

## Release checklist

1. Recover and validate the exact original Namco JAR supported by the patch.
2. Reconstruct the candidate with IPS and BPS; verify identical output and SHA-256.
3. Publish reproducible patch tools, source/target checksums, instructions and change log.
4. Confirm settings and audio after fresh install and game restart.
5. Publish a stable version tag only after the above checks pass.

## Preservation policy

Independent, non-commercial preservation research; not affiliated with Square Enix or Namco. **No complete copyrighted JARs or extracted proprietary assets** are distributed. Users provide their own legally obtained game files.

## Recovered release-candidate source (24 October 2026)

The [v1.0 candidate reproduction guide](releases/v1.0-candidate/README.md) and [hashes](releases/v1.0-candidate/HASHES.sha256) are now committed. The 1 KB [Git binary class patch](patches/v1.0/ffii_audio_v1_classes_git_binary.patch) and [`tools/build_ffii_v1_from_class_patch.py`](tools/build_ffii_v1_from_class_patch.py) reconstruct the **exact** user-tested v0.4/v1.0 JAR from the specific original Namco JAR. Source and target SHA-256 were verified independently against the recovered original and archived IPS/BPS patches. The initial public release tag remains unpublished until clean-install regression testing is complete.
