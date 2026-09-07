#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from tools.text.message_log import MlgFile

try:
    from bakbuild import freedos, paths, vm  # type: ignore
except ImportError as exc:
    raise SystemExit("run from the WSL build clone with uv run python") from exc


def check(value: bool, label: str, failures: list[str]) -> None:
    print(("  ok   " if value else "  FAIL ") + label)
    if not value:
        failures.append(label)


def run() -> int:
    vm.sync_files(
        [
            "MAKEFILE",
            "TOOLS/TOOLS.MAK",
            "TOOLS/CAPTEST.C",
            "SRC/DIALOG/DIALOG.MAK",
            "SRC/DIALOG/MSGLOG.C",
            "SRC/DIALOG/MSGLOG.H",
            "SRC/DIALOG/MSGCAP.C",
            "SRC/DIALOG/MSGCAP.H",
            "SRC/DIALOG/CAPCLASS.INC",
        ]
    )
    print(vm.run_make("msgcaptest", "kvm", 200, "MCAP.LOG")[-1600:])
    freedos.write_in(paths.IMG, "/CAP.LOG", "", paths.WORK)
    batch = (
        "@echo off\r\nc:\r\ncd \\\r\ndel CAP.MLG\r\n"
        "OUT\\CAPTEST > C:\\CAP.LOG\r\nC:\\EXIT.COM\r\n"
    )
    vm._run(batch, "kvm", 200)
    out = paths.WORK / "msgcapout"
    out.mkdir(parents=True, exist_ok=True)
    for path in out.glob("*"):
        path.unlink()
    freedos.mcopy_out(paths.IMG, "/CAP.LOG", out)
    freedos.mcopy_out(paths.IMG, "/CAP.MLG", out)
    freedos.mcopy_out(paths.IMG, "/CAPSPLIT.MLG", out)
    log = (out / "CAP.LOG").read_text(errors="replace")
    print(log)
    failures: list[str] = []
    check("NEW 0" in log and "BEGIN 0" in log, "timeline and conversation opened", failures)
    check("PAGE1 0" in log and "PAGE2 0" in log, "two visible pages appended", failures)
    check("DUP1 -16" in log and "BACK -16" in log, "redraw and back-page deduplicated", failures)
    check("CHOICE 0" in log, "confirmed choice appended", failures)
    check(
        "XBEGIN -16" in log and "XPAGE -16" in log and "XCHOICE -16" in log,
        "shop transaction source excluded",
        failures,
    )
    check(
        all(f"EX {key} -16 -16" in log for key in (254, 199, 11)),
        "combat, spell, and puzzle sources excluded by DOS classifier",
        failures,
    )
    check("SCENE 0" in log and "SDUP -16" in log, "scene caption recorded once", failures)
    check("COUNT 6" in log, "DOS core reports exactly six events", failures)
    mlg = MlgFile.read(out / "CAP.MLG")
    check([event.kind for event in mlg.events] == [1, 2, 2, 3, 4, 6], "event order is stable", failures)
    check([event.body for event in mlg.events if event.kind == 2] == [b"first", b"second"], "stored bodies match visible spans", failures)
    check(mlg.events[1].speaker == b"NPC" and mlg.events[1].location == b"Zone 9", "Who and fallback Where were snapshotted", failures)
    check(mlg.events[-1].scene_id == 0x1301 and mlg.events[-1].location == b"Inn", "scene identity and title were snapshotted", failures)
    split = MlgFile.read(out / "CAPSPLIT.MLG")
    names = [event.speaker for event in split.events if event.kind == 2]
    check(names == [b"A" * 63, b"A" * 62 + b"\x80\x40"],
          "long names truncate only at a complete Chinese glyph", failures)
    if failures:
        print(f"FAILED: {len(failures)} check(s)")
        return 1
    print("ALL CAPTURE CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
