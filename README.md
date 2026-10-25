# Final Fantasy II — Namco J2ME Audio Restoration

Restoration of independent background-music and sound-effect controls in Namco's **Final Fantasy II** J2ME edition.

**Status (25 October 2026): v1.0 Stable approved following user gameplay verification. IPS and BPS archives have both been independently verified against the original and tested output.**

## User-validated features

- **Complete:** music and sound effects simultaneously.
- **Music Only**.
- **SFX Only**.
- **Off**.
- Earlier development tests confirmed functioning audio modes and behavior after restarting the game.

A **v1.0 Stable** IPS/BPS package with checksums has been recovered and verified. See [v1.0 release notes](RELEASE_NOTES_v1.0.md). The compressed IPS/BPS package is available separately; this GitHub repository preserves the compact, reproducible class-level patch and build scripts.

## Release verification

The exact original, tested v0.4 JAR, IPS and BPS were recovered and independently validated. The user confirmed that FFII J2ME is tested and working, clearing v1.0 for release. The full public GitHub Release entry/tag is separate from the repository-held release notes and portable source patch.

## Preservation policy

Independent, non-commercial preservation research; not affiliated with Square Enix or Namco. **No complete copyrighted JARs or extracted proprietary assets** are distributed. Users provide their own legally obtained game files.

## Recovered release-candidate source (24 October 2026)

The [v1.0 candidate reproduction guide](releases/v1.0-candidate/README.md) and [hashes](releases/v1.0-candidate/HASHES.sha256) are now committed. The 1 KB [Git binary class patch](patches/v1.0/ffii_audio_v1_classes_git_binary.patch) and [`tools/build_ffii_v1_from_class_patch.py`](tools/build_ffii_v1_from_class_patch.py) reconstruct the **exact** user-tested v0.4/v1.0 JAR from the specific original Namco JAR. Source and target SHA-256 were verified independently against the recovered original and archived IPS/BPS patches. The user has confirmed the tested game works; v1.0 Stable is approved and [release notes](RELEASE_NOTES_v1.0.md) have been published.
