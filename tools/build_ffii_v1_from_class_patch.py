#!/usr/bin/env python3
"""Reconstruct the byte-exact, user-tested FFII Namco J2ME Complete Audio v1.0.
Requires the user's exact original JAR and the accompanying Git binary class patch.
Only f.class and j.class are patched; no game assets are distributed.
"""
import argparse
import hashlib
import subprocess
import tempfile
from pathlib import Path
from zipfile import ZipFile

ORIGINAL_SHA256 = 'ca62464edd07f17572a3e1949d68bb40ab2715b94b9ca7b1d8c41e793f74debb'
TARGET_SHA256 = '8f9d2ab4b8794a66a13d75549dff0db04f8bc42feaee525cf06b8af9d777e421'

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def build(original, patch, output):
    if sha256(original) != ORIGINAL_SHA256:
        raise ValueError('Original JAR mismatch: expected exact Namco FFII build')
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(original) as src, tempfile.TemporaryDirectory() as tmp:
        assert src.testzip() is None
        work = Path(tmp)
        for name in ('f.class', 'j.class'):
            (work/name).write_bytes(src.read(name))
        subprocess.run(['git','apply','--binary',str(Path(patch).resolve())],cwd=work,check=True)
        altered = {n:(work/n).read_bytes() for n in ('f.class','j.class')}
        with ZipFile(output, 'w') as dest:
            for info in src.infolist():
                dest.writestr(info, altered.get(info.filename,src.read(info.filename)))
    with ZipFile(original) as src, ZipFile(output) as built:
        assert built.testzip() is None
        assert src.namelist() == built.namelist()
        changed = [n for n in src.namelist() if src.read(n) != built.read(n)]
        assert changed == ['f.class','j.class'], changed
    actual=sha256(output)
    if actual != TARGET_SHA256:
        raise ValueError('Unexpected target SHA-256: '+actual)
    print('Byte-exact user-tested v1.0 reconstructed:',actual)

if __name__ == '__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('original_jar'); ap.add_argument('output_jar')
    ap.add_argument('--patch',default=str(Path(__file__).resolve().parent.parent/'patches'/'v1.0'/'ffii_audio_v1_classes_git_binary.patch'))
    a=ap.parse_args()
    build(a.original_jar,a.patch,a.output_jar)
