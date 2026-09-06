#!/usr/bin/env python3
"""
Cross-language conformance run for the MLG v1 message-log container.

Why this exists
---------------
Two Python models agreeing with each other proves nothing about the format the
game will actually write. This driver closes the loop in both directions:

  C  -> Python   `MLGTEST GEN` (Borland C++ 3.1, medium model, linking the game's
                 own bak/SRC/DIALOG/MSGLOG.C) writes a scripted timeline inside
                 FreeDOS; the bytes are pulled out and compared, byte for byte,
                 against tools.text.message_log.build_scripted_fixture().

  Python -> C    Fixtures this repo generates — a valid timeline, a >64 KiB one,
                 a bound snapshot and deliberately damaged files — are fed
                 to the DOS core, and its per-event listing and per-file result
                 codes are checked against the Python model's expectations.

Where to run it
---------------
Inside the WSL build clone, which is where the vendored Borland toolchain and the
``bakbuild`` VM driver live::

    wsl -e bash -lc "cd ~/krondor-build-msglog \\
      && export BAK_TOOLCHAIN=/home/pmanyeh/bak-toolchain \\
      && export PATH=\\$HOME/.local/bin:\\$PATH \\
      && uv run python /mnt/d/git/betrayal-at-krondor-for-zh/tools/text/mlg_dos_check.py"

It builds only ``OUT\\MLGTEST.EXE`` (the ``mlgtest`` MAKE target) and writes only
fixtures and logs in the build image root — it never touches KRONDOR.EXE or the OVLs.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from tools.text.message_log import (  # noqa: E402
    MLG_HEADER_SIZE,
    SCRIPTED_CREATED,
    MlgFile,
    build_corrupt_snapshot_fixture,
    build_invalid_fixtures,
    build_large_fixture,
    build_python_fixture,
    build_scripted_fixture,
    build_snapshot_fixture,
    crc32,
)

try:
    from bakbuild import freedos, paths, vm  # type: ignore
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "bakbuild not importable — run this from the WSL build clone with `uv run python`"
    ) from exc


GAM_LENGTH = 123456
GAM_CRC = 0xA1B2C3D4

# 8.3 names for the Python-generated inputs.
INVALID_NAMES = {
    "EMPTY": "EMPTY.MLG",
    "SHORTHDR": "SHORTHDR.MLG",
    "BADMAGIC": "BADMAGIC.MLG",
    "BADVER": "BADVER.MLG",
    "BADFP": "BADFP.MLG",
    "BADHCRC": "BADHCRC.MLG",
    "BADECRC": "BADECRC.MLG",
    "TRUNCEV": "TRUNCEV.MLG",
    "BADLEN": "BADLEN.MLG",
    "BIGOFF": "BIGOFF.MLG",
    "TOOBIG": "TOOBIG.MLG",
}


def _stage(tmp: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {
        "PGEN.MLG": build_python_fixture(),
        "BIG.MLG": build_large_fixture(),
        "SNAP.MLG": build_snapshot_fixture(GAM_LENGTH, GAM_CRC),
        "BADLENS.MLG": build_corrupt_snapshot_fixture(),
    }
    for key, (blob, _) in build_invalid_fixtures().items():
        files[INVALID_NAMES[key]] = blob
    tmp.mkdir(parents=True, exist_ok=True)
    for name, blob in files.items():
        (tmp / name).write_bytes(blob)
    return files


def _batch() -> str:
    """The FreeDOS batch. Everything lives in the image root so the run needs no
    `mmd` — mtools' mkdir prompts on an existing directory and blocks forever."""
    exe = "OUT\\MLGTEST"
    crc = f"{GAM_CRC:X}"
    runs = [
        f"{exe} SPLIT",
        f"{exe} STATE",
        f"{exe} GEN \\CGEN.MLG",
        f"{exe} DUMP \\CGEN.MLG",
        f"{exe} DUMP \\PGEN.MLG",
        f"{exe} OPEN \\BIG.MLG",
        f"{exe} CAND \\SNAP.MLG {GAM_LENGTH} {crc}",
        f"{exe} CAND \\SNAP.MLG {GAM_LENGTH + 1} {crc}",
        f"{exe} CAND \\PGEN.MLG 0 0",
        f"{exe} ACT \\SNAP.MLG \\ACTWORK.MLG",
        f"{exe} SNAP \\CGEN.MLG \\CSNAP.MLG {GAM_LENGTH} {crc}",
        f"{exe} CAND \\CSNAP.MLG {GAM_LENGTH} {crc}",
        f"{exe} CAND \\BADLENS.MLG 1 2",
    ]
    runs += [f"{exe} OPEN \\{name}" for name in INVALID_NAMES.values()]
    body = "\r\n".join(f"{ln} >> C:\\MLG.LOG" for ln in runs)
    return "@echo off\r\nc:\r\ncd \\\r\n" + body + "\r\nc:\\EXIT.COM\r\n"


def run() -> int:
    tmp = paths.WORK / "mlgcheck"
    files = _stage(tmp)

    print("== syncing the msglog sources and building OUT\\MLGTEST.EXE ==")
    # Targeted sync, not vm.mirror(): mirror() re-copies the whole bak/ tree one
    # mtools process at a time and takes many minutes on a warm image.
    vm.sync_files(
        [
            "MAKEFILE",
            "TOOLS/TOOLS.MAK",
            "TOOLS/MLGTEST.C",
            "SRC/DIALOG/DIALOG.MAK",
            "SRC/DIALOG/MSGLOG.C",
            "SRC/DIALOG/MSGLOG.H",
        ]
    )
    log = vm.run_make("mlgtest", "kvm", 200, "MLGT.LOG")
    if "MLGTEST.EXE" not in log and "mlgtest" not in log.lower():
        print(log[-2000:])
    print(log[-1200:])

    freedos.mcopy_in(paths.IMG, "", *[tmp / n for n in files])

    # Fresh log file each run.
    freedos.write_in(paths.IMG, "/MLG.LOG", "", paths.WORK)
    vm._run(_batch(), "kvm", 200)

    out = paths.WORK / "mlgout"
    out.mkdir(parents=True, exist_ok=True)
    for stale in out.glob("*"):
        stale.unlink()
    freedos.mcopy_out(paths.IMG, "/MLG.LOG", out)
    freedos.mcopy_out(paths.IMG, "/*.MLG", out)
    text = (out / "MLG.LOG").read_text(errors="replace")
    print(text)

    return _assert(text, out)


def _assert(text: str, out: Path) -> int:
    fails: list[str] = []

    def check(cond: bool, what: str) -> None:
        print(("  ok   " if cond else "  FAIL ") + what)
        if not cond:
            fails.append(what)

    lines = [ln.rstrip() for ln in text.splitlines()]
    joined = "\n".join(lines)

    print("\n== C -> Python: the DOS-written fixture ==")
    cgen = out / "CGEN.MLG"
    check(cgen.exists(), "MLGTEST GEN produced CGEN.MLG")
    if cgen.exists():
        got, want = cgen.read_bytes(), build_scripted_fixture()
        check(len(got) == len(want), f"CGEN.MLG length {len(got)} == {len(want)}")
        if got != want:
            for i, (a, b) in enumerate(zip(got, want)):
                if a != b:
                    fails.append(f"first byte difference at 0x{i:X}: DOS {a:02X} != model {b:02X}")
                    print(f"  FAIL first byte difference at 0x{i:X}: {a:02X} != {b:02X}")
                    break
        else:
            print("  ok   CGEN.MLG is byte-identical to build_scripted_fixture()")
        try:
            mlg = MlgFile.parse(got)
            check(mlg.header.event_count == 7, "Python parses the DOS file: 7 events")
            check(
                [e.sequence for e in mlg.events] == [1, 2, 3, 4, 5, 6, 7],
                "sequence numbers 1..7",
            )
            check(len(mlg.events[3].body) == 511, "long span split at 511 (glyph-safe)")
        except Exception as exc:  # noqa: BLE001
            check(False, f"Python parse of the DOS file: {exc}")

    print("\n== Python -> C: the DOS core reading our fixtures ==")
    pgen = MlgFile.parse(build_python_fixture())
    for ev in pgen.events:
        want = (
            f"EV off={ev.offset} len={ev.record_length} kind={ev.kind} "
            f"flags={ev.flags:04X} seq={ev.sequence} conv={ev.conversation} "
            f"prev={ev.prev_offset}"
        )
        check(want in joined, f"DOS listed PGEN event seq={ev.sequence}")
        check(f"BOD {ev.body.hex().upper()}" in joined, f"DOS read body of seq={ev.sequence} byte-exact")
        check(
            f"SPK {ev.speaker.hex().upper()}" in joined or (not ev.speaker and "SPK \n" in text),
            f"DOS read speaker of seq={ev.sequence}",
        )

    big = MlgFile.parse(build_large_fixture())
    check(
        f"OPEN rc=0 committed_events={big.header.event_count}" in joined,
        f">64 KiB file: DOS recovered all {big.header.event_count} events",
    )

    print("\n== candidate validation ==")
    candidates = [ln for ln in lines if ln.startswith("CAND rc=")]
    check(
        candidates == ["CAND rc=0", "CAND rc=-13", "CAND rc=-8", "CAND rc=0", "CAND rc=-12"],
        "candidate results in batch order: matching, wrong binding, working file, "
        "DOS snapshot, structurally corrupt snapshot",
    )
    check("ACT activate=0 state=1" in joined, "candidate activated -> ACTIVE")
    check("SNAP prepare=0" in joined, "snapshot written from the working timeline")
    csnap = out / "CSNAP.MLG"
    if csnap.exists():
        try:
            snap = MlgFile.parse(
                csnap.read_bytes(), expect_gam=(GAM_LENGTH, GAM_CRC)
            )
            check(snap.header.event_count == 7, "DOS-written snapshot validates in Python")
            check(
                snap.header.created_time == SCRIPTED_CREATED,
                "reopening a timeline preserves its creation stamp",
            )
            check(
                csnap.read_bytes()[MLG_HEADER_SIZE:] == build_scripted_fixture()[MLG_HEADER_SIZE:],
                "snapshot data region equals the working timeline's",
            )
            check(
                snap.header.data_crc32 == crc32(
                    csnap.read_bytes()[MLG_HEADER_SIZE : snap.header.committed_length]
                ),
                "snapshot data CRC32 covers the committed data region",
            )
        except Exception as exc:  # noqa: BLE001
            check(False, f"Python validation of the DOS snapshot: {exc}")
    else:
        check(False, "CSNAP.MLG produced")

    print("\n== damaged files: one distinguishable outcome each ==")
    opens = [ln for ln in lines if ln.startswith("OPEN rc=")]
    expectations = build_invalid_fixtures()
    # The OPEN lines appear in INVALID_NAMES order, after the BIG.MLG one.
    idx = 1
    for key in INVALID_NAMES:
        _, expectation = expectations[key]
        if idx >= len(opens):
            check(False, f"{key}: no OPEN line")
            idx += 1
            continue
        line = opens[idx]
        if expectation.startswith("reject:"):
            want = f"OPEN rc={expectation.split(':')[1]} committed_events=0"
            check(line == want, f"{key}: {line!r} == {want!r}")
        else:
            n = expectation.split(":")[1]
            want = f"OPEN rc=0 committed_events={n}"
            check(line == want, f"{key}: {line!r} == {want!r}")
        idx += 1

    print("\n== split point and state machine ==")
    for limit, cut in enumerate([0, 1, 2, 2, 4, 4, 6, 7, 8]):
        check(f"SPLIT limit={limit} cut={cut}" in joined, f"split_point(limit={limit}) == {cut}")
    check("SPLIT lead_only cut=0" in joined, "a lone lead byte yields no safe cut")
    check("ST init base=0 state=0 rec=0" in joined, "starts INACTIVE, not recording")
    check("ST transition state=2 rec=0" in joined, "transition suppresses recording")
    check("ST viewer state=3 rec=0" in joined, "viewer suppresses recording")
    check("ST restored base=0 state=0" in joined, "leaving both restores the base state")
    check("ST bad_new=-4" in joined, "unopenable path -> MSGLOG_E_OPEN")
    check("ST failed base=4 state=4 rec=0" in joined, "a failed create latches recording-failed")
    check("ST failed_in_viewer state=4 rec=0" in joined, "viewer does not mask the failure")
    check(
        "ST failed_after_viewer base=4 state=4 rec=0" in joined,
        "leaving the viewer does NOT turn recording-failed back into active",
    )
    check("ST gap_when_failed=-1" in joined, "appends stay refused while failed")

    print()
    if fails:
        print(f"FAILED: {len(fails)} check(s)")
        for f in fails:
            print("  - " + f)
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
