# FFII Namco J2ME — Complete Audio v1.0 (verified candidate)

This restoration allows **Complete** (music and SFX simultaneously), **Music** only, **SFX** only, and **Off**. The four modes were user-validated in J2ME Loader; the reconstructed game matches the tested v0.4 build byte-for-byte. This repository does not distribute any copyrighted original or modified JAR.

## Exact supported game

Original file: `finalfanta_bx36yx6t.jar`; 1,375,308 bytes; SHA-256 `ca62464edd07f17572a3e1949d68bb40ab2715b94b9ca7b1d8c41e793f74debb`.

Expected output: 1,367,269 bytes; SHA-256 `8f9d2ab4b8794a66a13d75549dff0db04f8bc42feaee525cf06b8af9d777e421`.

## Reproduction using only owned original game + open patch

Install Python 3 and Git. From the repository root:

```bash
python tools/build_ffii_v1_from_class_patch.py /path/to/finalfanta_bx36yx6t.jar /path/to/FFII_Complete_Audio_v1.0.jar
```

The self-checking builder reads the original JAR, applies `patches/v1.0/ffii_audio_v1_classes_git_binary.patch` to only `f.class` and `j.class` (a 1 KB compressed Git binary diff), reconstructs the archive preserving original ZIP entry settings, and refuses success unless the output SHA-256 matches the archived user-tested JAR. It was independently exercised against the recovered original and tested JAR on October 24, 2026 and reproduced the exact SHA above.

An earlier archived distribution kit also contains a BPS (50,678 bytes) and IPS (1,394,700 bytes). Both were independently applied and confirmed to produce the same target. The class-level patch is the primary **repository-hosted** distribution: smaller and easier to audit.

## Test requirements

In J2ME Loader enable `supports.mixing=true`. Test a battle with BGM and attacks/spells playing simultaneously in Complete mode; confirm that Music only, SFX only and Off are distinct. Exit and restart the game, then test selected mode persistence; finally compare saves with a clean backup. A new clean-install regression pass has not yet been repeated since the original validation.

## Technical scope

v0.3 introduced the four-option audio menu. v0.4 prevented SFX from being rejected by an existing music-player priority gate. The final user-validated v1.0 candidate matches v0.4. Its functional ZIP-entry differences from the original are only `f.class` and `j.class`; all other entries match. This project is independent of Square Enix and Namco.
