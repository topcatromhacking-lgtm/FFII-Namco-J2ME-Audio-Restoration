# Final Fantasy II — Namco J2ME Complete Audio Restoration

## v1.0 Stable — 25 October 2026

**Release status: tested and approved.** Both IPS and BPS patch transports reproduce byte-for-byte the same JAR as the user-tested v0.4 build. All four audio settings have been verified in J2ME Loader.

### Restoration

The sound configuration now offers **Complete** (simultaneous music and sound effects), **Music Only**, **SFX Only**, and **Off**. The working Complete mode removes the audio-player priority behavior that previously rejected overlapping effects. The implementation changes only `f.class` and `j.class` relative to the specific original Namco J2ME JAR; no music or game resources were changed.

### Supported original (not distributed)

- Filename: `finalfanta_bx36yx6t.jar`
- Size: 1,375,308 bytes
- SHA-256: `ca62464edd07f17572a3e1949d68bb40ab2715b94b9ca7b1d8c41e793f74debb`

### Rebuilt v1.0 output (not distributed)

- Size: 1,367,269 bytes
- SHA-256: `8f9d2ab4b8794a66a13d75549dff0db04f8bc42feaee525cf06b8af9d777e421`

### Patch formats

- `FFII_J2ME_Complete_Audio_v1.0.bps` — **recommended**, 50,678 bytes, SHA-256 `6aa8246f576c21d1c71cc1ee2a0da689dda09c227e2b06a87181e6bc44574a35`
- `FFII_J2ME_Complete_Audio_v1.0.ips` — 1,394,700 bytes, SHA-256 `d864629b180644e7e28e47514fa9d916197ef43c6ea43ba17f5a8b256b322c79`

The IPS is large because reconstructing the changed compressed JAR shifts substantial archive content. IPS and BPS round trips were independently verified against the original and tested JAR on 25 October 2026. The small, repository-hosted [class-level Git binary patch](patches/v1.0/ffii_audio_v1_classes_git_binary.patch) and [reproducible builder](tools/build_ffii_v1_from_class_patch.py) are an additional distribution method that does not store copyrighted game files.

### Installation

Obtain your own legal copy of the exact original. With Floating IPS or another compatible patcher apply **one** IPS or BPS patch to the complete original JAR and save as a new `.jar`. Check the output SHA-256 above. Run in J2ME Loader with `supports.mixing=true`, and back up saves/settings before replacing an existing installation.

### Project

Independent non-commercial preservation/restoration effort; not affiliated with Square Enix or Namco. No complete copyrighted JAR, music, art, or game audio is distributed.
