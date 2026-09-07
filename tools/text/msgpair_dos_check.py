#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from bakbuild import freedos, paths, vm  # type: ignore  # noqa: E402
from tools.text.message_log import MlgFile  # noqa: E402


def run() -> int:
    vm.sync_files(
        [
            "MAKEFILE",
            "TOOLS/TOOLS.MAK",
            "TOOLS/MSGPTEST.C",
            "SRC/DIALOG/MSGLOG.C",
            "SRC/DIALOG/MSGLOG.H",
            "SRC/DIALOG/MSGSAVE.C",
            "SRC/DIALOG/MSGSAVE.H",
        ]
    )
    print(vm.run_make("msgptest", "kvm", 200, "MSGP.LOG")[-1600:])
    freedos.write_in(paths.IMG, "/PAIR.LOG", "", paths.WORK)
    vm._run("@echo off\r\nc:\r\ncd \\\r\nOUT\\MSGPTEST > C:\\PAIR.LOG\r\nc:\\EXIT.COM\r\n", "kvm", 200)
    out = paths.WORK / "msgpairout"
    out.mkdir(parents=True, exist_ok=True)
    freedos.mcopy_out(paths.IMG, "/PAIR.LOG", out)
    text = (out / "PAIR.LOG").read_text(errors="replace")
    print(text)
    expected = [
        "NEW 0",
        "AAPP 0",
        "ASAVE 1",
        "BAPP 0",
        "BSAVE 1",
        "ALOAD prep=1 finish=1 count=1",
        "CAPP 0",
        "CSAVE 1 count=2 err=12 newg=-1 newm=-1 txn=-1",
        "AOVER 1",
        "CRASH step=7 save=0 recover=1 again=1 count=2 expect=2",
        "CRASH step=8 save=0 recover=1 again=1 count=2 expect=2",
        "CRASH step=9 save=0 recover=1 again=1 count=2 expect=2",
        "CRASH step=10 save=0 recover=1 again=1 count=2 expect=2",
        "CRASH step=11 save=0 recover=1 again=1 count=3 expect=3",
        "MISS prep=0 finish=0 count=1 flags=2",
        "GAMONLY save=0 recover=1 gam=0 mlg=-1",
        "BADMARK recover=0 gam=0 mark=0",
        "RECOVERY_RETRY failures=0",
        "FAULT_MATRIX failures=0",
    ]
    missing = [line for line in expected if line not in text.splitlines()]
    if missing:
        for line in missing:
            print("MISSING " + line)
        return 1
    work = out / "MSGWORK.MLG"
    if work.exists():
        work.unlink()
    freedos.mcopy_out(paths.IMG, "/MSGWORK.MLG", out)
    stamp = MlgFile.read(work).header.created_time
    dos_time = datetime(stamp.year, stamp.month, stamp.day, stamp.hour, stamp.minute, stamp.second)
    delta = abs((datetime.now() - dos_time).total_seconds())
    if delta > 120:
        print(f"DOS TIME OUT OF RANGE: {dos_time.isoformat()} delta={delta:.0f}s")
        return 1
    print(f"DOS getdate/gettime round trip: {dos_time.isoformat()} delta={delta:.0f}s")
    print("ALL PAIR CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
