"""Create synthetic 1/5/10 MiB histories and optionally build the DOS probe.

Windows: python tools/text/mlg_capacity_check.py scratchpad/mlg-capacity
WSL build clone: uv run python <repo>/tools/text/mlg_capacity_check.py <out> --build
Mount the output directory in DOSBox-X at the release CPU settings and run RUN.BAT.
BENCH.LOG measures standalone core I/O; it is not a game UI performance claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from tools.text.message_log import (MlgEvent, MlgFile, MlgHeader, MlgTime,
                                    load_mapping, mapping_fingerprint)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out", type=Path)
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    manifest = []
    fp = mapping_fingerprint(load_mapping(REPO / "localization/generated/zh_mapping.json"))
    for size in (1, 5, 10):
        template = MlgEvent(body=b"Synthetic message. " * 26, speaker=b"NPC", location=b"Zone 9",
                            timestamp=MlgTime(2026, 9, 7, 12, 0, 0))
        count = (size * 1024 * 1024 - 64 + len(template.pack()) - 1) // len(template.pack())
        events = [MlgEvent(body=template.body, speaker=template.speaker,
                          location=template.location, timestamp=template.timestamp)
                  for _ in range(count)]
        path = args.out / f"SIZE{size}.MLG"
        MlgFile(MlgHeader(mapping_fingerprint=fp), events).write(path)
        data = path.read_bytes()
        MlgFile.read(path, expect_mapping=fp)
        manifest.append(dict(file=path.name, bytes=len(data), events=count,
                             sha256=hashlib.sha256(data).hexdigest()))
    (args.out / "fixtures.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (args.out / "RUN.BAT").write_bytes(
        b"@echo off\r\nMLGBENCH SIZE1.MLG > BENCH.LOG\r\n"
        b"MLGBENCH SIZE5.MLG >> BENCH.LOG\r\n"
        b"MLGBENCH SIZE10.MLG >> BENCH.LOG\r\necho DONE >> BENCH.LOG\r\n")
    if args.build:
        from bakbuild import vm, freedos, paths
        vm.sync_files(["TOOLS/TOOLS.MAK", "TOOLS/MLGBENCH.C", "SRC/DIALOG/MSGLOG.C", "SRC/DIALOG/MSGLOG.H"])
        # A tiny target file avoids shell-escaping the DOS backslash in MAKE's target.
        freedos.write_in(paths.IMG, "/BENCH.MAK", "!include MAKEFILE\nbench: OUT\\MLGBENCH.EXE\n", paths.WORK)
        print(vm.run_make("-fBENCH.MAK bench", "kvm", 200, "BENCHC.LOG")[-1800:])
        freedos.mcopy_out(paths.IMG, "/OUT/MLGBENCH.EXE", args.out)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
