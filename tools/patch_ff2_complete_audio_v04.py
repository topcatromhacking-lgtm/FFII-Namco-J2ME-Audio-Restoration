#!/usr/bin/env python3
"""FFII Namco J2ME v0.4: preserve Complete/Music/SFX/Off while allowing
layered SFX. Requires the exact v0.3 experimental JAR. No game files included.
Only two branch bytes in f.class change; a working MMAPI mixer is also needed.
"""
import argparse
import hashlib
import io
from pathlib import Path
import struct
import zipfile

EXPECTED_SHA256 = "60649c8ddf06d95140bd701550dd977305e9d0fef0fee107894b85d319c3b1b8"

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def locate_code(b, method, desc):
    def u2(p): return struct.unpack_from(">H", b, p)[0]
    def u4(p): return struct.unpack_from(">I", b, p)[0]
    assert b[:4] == bytes.fromhex("cafebabe"), "Not a Java class"
    names = {}
    p = 10
    i = 1
    while i < u2(8):
        t = b[p]
        p += 1
        if t == 1:
            n = u2(p); p += 2
            names[i] = b[p:p+n].decode("utf8", "replace")
            p += n
        elif t in (3,4,9,10,11,12,17,18): p += 4
        elif t in (5,6): p += 8; i += 1
        elif t in (7,8,16,19,20): p += 2
        elif t == 15: p += 3
        else: raise ValueError("Unexpected constant-pool tag %d" % t)
        i += 1
    p += 6
    n = u2(p); p += 2 + n*2
    n = u2(p); p += 2
    for _ in range(n):
        p += 6
        for __ in range(u2(p)):
            p += 2
            length = u4(p); p += 4 + length
        p += 2
    n = u2(p); p += 2
    for _ in range(n):
        nam, sig = names.get(u2(p+2)), names.get(u2(p+4))
        p += 6
        count = u2(p); p += 2
        for __ in range(count):
            attr_name, size = names.get(u2(p)), u4(p+2)
            body = p + 6
            if nam == method and sig == desc and attr_name == "Code":
                return body + 8, u4(body+4)
            p = body + size
    raise RuntimeError("Cannot locate f.b(II)V")

def patch(source_path, output_path):
    source = Path(source_path).read_bytes()
    if sha256(source) != EXPECTED_SHA256:
        raise ValueError("v0.3 source SHA-256 mismatch; refusing to patch")
    with zipfile.ZipFile(io.BytesIO(source)) as z:
        infos = z.infolist()
        files = {info.filename: z.read(info.filename) for info in infos}
    original = files["f.class"]
    patched = bytearray(original)
    offset, size = locate_code(patched, "b", "(II)V")
    code = bytes(patched[offset:offset+size])
    assert size == 303
    assert code[185:195] == bytes.fromhex("1d 10 0c 9f 00 36 1c 99 00 17")
    assert code[242:246] == bytes.fromhex("1a b8 01 58")
    patched[offset+193:offset+195] = bytes.fromhex("00 32")
    assert len(patched) == len(original)
    assert patched[offset+191:offset+195] == bytes.fromhex("1c 99 00 32")
    with zipfile.ZipFile(output_path, "w") as z:
        for info in infos:
            z.writestr(info, bytes(patched) if info.filename=="f.class" else files[info.filename])
    with zipfile.ZipFile(output_path) as z:
        assert z.testzip() is None
        changed = [name for name in files if z.read(name) != files[name]]
        assert changed == ["f.class"], changed
    result = Path(output_path).read_bytes()
    print("source sha256:", sha256(source))
    print("result sha256:", sha256(result))
    print("Static patch verified; real J2ME Loader audio mixing requires on-device validation.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("v03_jar")
    parser.add_argument("v04_jar")
    args = parser.parse_args()
    patch(args.v03_jar, args.v04_jar)
