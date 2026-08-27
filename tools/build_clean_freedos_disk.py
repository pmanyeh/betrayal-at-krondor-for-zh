"""Build canonical bootable FreeDOS disk image for EVG Native CJK Gate A with X=TEST for Video 7."""

import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
from pathlib import Path

ROOT = Path("/mnt/d/git/betrayal-at-krondor-for-zh")
FREEDOS_SRC = Path("/home/pmanyeh/bak-toolchain/freedos/freedos.img")
TEMP_IMG = Path("/tmp/krondor_gate_a_temp.img")
FINAL_IMG = ROOT / "scratchpad" / "evg-native-cjk-poc" / "vm" / "krondor_evg_gate_a.img"
DIST_DIR = ROOT / "dist" / "test_v100_zh"
POC_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc"
LOG_PATH = POC_DIR / "gate-a-disk-build.log"
VALIDATION_PATH = POC_DIR / "gate-a-disk-validation.json"

EXPECTED_HASHES = {
    "KRONDOR.EXE": "4b71c99013732ed63561680689d7483325f498a7e2268dbdff8f0b59d6ff57ac",
    "VMCODE.OVL": "a1d138e069553fc45c235a3647009602fa5e5d07ed7e4482ceeba5c542f64e1a",
    "SX.OVL": "d73d92d8ff1a698ad64df9b108a04bc1ee7221bc4c336b4a6073191e5f4dabdb",
    "ZH16.DAT": "0a36619ba5dc257da820147ba38bcddedc3aa6686b8ddfe45037cb851420598d",
}

MENV = os.environ.copy()
MENV["MTOOLS_SKIP_CHECK"] = "1"

log_lines = []


def log(msg: str) -> None:
    print(msg)
    log_lines.append(msg)


def run_cmd(*args: str) -> subprocess.CompletedProcess:
    cmd_str = " ".join(args)
    log(f"+ {cmd_str}")
    res = subprocess.run(args, env=MENV, capture_output=True, text=True)
    if res.stdout:
        log(f"[stdout]\n{res.stdout}")
    if res.stderr:
        log(f"[stderr]\n{res.stderr}")
    if res.returncode != 0:
        log(f"ERROR: Command failed with exit code {res.returncode}: {cmd_str}")
        raise RuntimeError(f"Command failed: {cmd_str}\n{res.stderr}")
    return res


def compute_sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_mdir_filenames(mdir_output: str) -> set[str]:
    files = set()
    for line in mdir_output.splitlines():
        line = line.strip()
        if not line or line.startswith("Volume") or line.startswith("Directory") or "files" in line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            base = parts[0].upper()
            ext = parts[1].upper() if len(parts[1]) <= 3 and not parts[1].isdigit() and parts[1] != "<DIR>" else ""
            if ext:
                files.add(f"{base}.{ext}")
            else:
                files.add(base)
    return files


def main():
    POC_DIR.mkdir(parents=True, exist_ok=True)
    FINAL_IMG.parent.mkdir(parents=True, exist_ok=True)

    errors = []

    try:
        log("=== 1. Checking Base FreeDOS Image ===")
        if not FREEDOS_SRC.exists():
            raise FileNotFoundError(f"FreeDOS source image not found: {FREEDOS_SRC}")

        base_bytes = FREEDOS_SRC.read_bytes()
        base_size = len(base_bytes)
        log(f"Base size: {base_size} bytes")
        if base_size != 33554432:
            raise ValueError(f"Unexpected base size: {base_size} (expected 33554432)")

        base_sha = compute_sha256(base_bytes)
        log(f"Base SHA256: {base_sha}")

        log("=== 2. Copying to Temporary Image ===")
        if TEMP_IMG.exists():
            TEMP_IMG.unlink()
        shutil.copy2(FREEDOS_SRC, TEMP_IMG)

        target = f"{TEMP_IMG}@@32256"

        log("=== 3. Cleaning Packages and Setup from Base Image ===")
        run_cmd("mdel", "-i", target, "::SETUP.BAT")
        run_cmd("mdeltree", "-i", target, "::PACKAGES")

        log("=== 4. Writing FDCONFIG.SYS and FDAUTO.BAT ===")
        fdconfig_content = (
            "!LASTDRIVE=Z\r\n"
            "!BUFFERS=20\r\n"
            "!FILES=40\r\n"
            "\r\n"
            "DOS=HIGH\r\n"
            "DOS=UMB\r\n"
            "DOSDATA=UMB\r\n"
            "\r\n"
            "DEVICE=\\FREEDOS\\BIN\\HIMEMX.EXE\r\n"
            "DEVICE=\\FREEDOS\\BIN\\JEMM386.EXE X=TEST\r\n"
            "\r\n"
            "SHELLHIGH=\\FREEDOS\\BIN\\COMMAND.COM \\FREEDOS\\BIN /E:2048 /P=\\FDAUTO.BAT\r\n"
        )
        fdconfig_tmp = Path("/tmp/FDCONFIG.SYS")
        fdconfig_tmp.write_text(fdconfig_content, encoding="ascii")
        run_cmd("mcopy", "-o", "-i", target, str(fdconfig_tmp), "::FDCONFIG.SYS")

        fdauto_content = (
            "@echo off\r\n"
            "SET DOSDIR=\\FREEDOS\r\n"
            "SET PATH=%DOSDIR%\\BIN\r\n"
            "SET LANG=\r\n"
            "SET TZ=\r\n"
            "CD \\\r\n"
            "echo EVG Native CJK Gate A\r\n"
            "MEM /C\r\n"
            "KRONDOR.EXE\r\n"
            "echo KRONDOR returned ERRORLEVEL %ERRORLEVEL%\r\n"
            "pause\r\n"
        )
        fdauto_tmp = Path("/tmp/FDAUTO.BAT")
        fdauto_tmp.write_text(fdauto_content, encoding="ascii")
        run_cmd("mcopy", "-o", "-i", target, str(fdauto_tmp), "::FDAUTO.BAT")

        log("=== 5. Copying Filtered Game Data ===")
        skip_exts = {".wri", ".bmp", ".sol", ".hlp", ".txt", ".doc"}
        files_to_copy = []
        for f in DIST_DIR.iterdir():
            if f.is_file():
                if f.suffix.lower() in skip_exts:
                    continue
                if ".pre-" in f.name or ".new." in f.name or "ZH_MAP" in f.name or "DDX_BUILD" in f.name:
                    continue
                if f.name.upper() in ["KRONDOR.EXE", "VMCODE.OVL", "SX.OVL", "ZH16.DAT"]:
                    continue
                files_to_copy.append(str(f))

        log(f"Copying {len(files_to_copy)} game data files...")
        run_cmd("mcopy", "-o", "-i", target, *files_to_copy, "::")

        log("=== 6. Copying Verified POC Binaries ===")
        poc_files = [
            (POC_DIR / "KRONDOR-EVG-NATIVE-POC.EXE", "::KRONDOR.EXE"),
            (POC_DIR / "VMCODE-EVG-NATIVE-POC.OVL", "::VMCODE.OVL"),
            (POC_DIR / "SX.OVL", "::SX.OVL"),
            (ROOT / "localization" / "generated" / "ZH16.DAT", "::ZH16.DAT"),
        ]
        for src_path, dst_name in poc_files:
            if not src_path.exists():
                raise FileNotFoundError(f"POC binary not found: {src_path}")
            log(f"Copying {src_path.name} -> {dst_name}")
            run_cmd("mcopy", "-o", "-i", target, str(src_path), dst_name)

        log("=== 7. Static Image Validation ===")
        img_bytes = TEMP_IMG.read_bytes()
        img_size = len(img_bytes)
        if img_size != 33554432:
            errors.append(f"Image size mismatch: {img_size} != 33554432")

        mbr_sig = img_bytes[510:512].hex()
        if mbr_sig != "55aa":
            errors.append(f"MBR signature invalid: {mbr_sig} != 55aa")

        part1 = img_bytes[446:462]
        boot_flag, start_h, start_s, start_c, part_type, end_h, end_s, end_c, start_lba, num_sec = struct.unpack(
            "<BBBBBBBBII", part1
        )
        is_active = (boot_flag == 0x80)
        if not is_active:
            errors.append(f"Partition 1 is not active (boot_flag=0x{boot_flag:02x})")
        if part_type != 0x04:
            errors.append(f"Partition type mismatch: 0x{part_type:02x} != 0x04")
        if start_lba != 63:
            errors.append(f"Start LBA mismatch: {start_lba} != 63")

        vbr_offset = 63 * 512
        vbr_sig = img_bytes[vbr_offset + 510 : vbr_offset + 512].hex()
        if vbr_sig != "55aa":
            errors.append(f"VBR signature invalid: {vbr_sig} != 55aa")

        vbr_jump = img_bytes[vbr_offset]
        vbr_jump_valid = (vbr_jump in (0xEB, 0xE9))
        if not vbr_jump_valid:
            errors.append(f"VBR jump byte invalid: 0x{vbr_jump:02x}")

        log("=== 8. Validating Filesystem Contents ===")
        mdir_res = run_cmd("mdir", "-i", target, "::")
        dir_files = parse_mdir_filenames(mdir_res.stdout)
        log(f"Found {len(dir_files)} files in root directory: {sorted(dir_files)}")

        required_files_list = [
            "KERNEL.SYS",
            "FDCONFIG.SYS",
            "FDAUTO.BAT",
            "KRONDOR.EXE",
            "VMCODE.OVL",
            "SX.OVL",
            "ZH16.DAT",
            "STARTUP.GAM",
        ]
        files_found = {}
        for req in required_files_list:
            found = (req in dir_files)
            files_found[req] = found
            if not found:
                errors.append(f"Required file missing in image: {req}")

        log("=== 9. Validating Startup Files Content ===")
        mtype_cfg = run_cmd("mtype", "-i", target, "::FDCONFIG.SYS").stdout
        mtype_auto = run_cmd("mtype", "-i", target, "::FDAUTO.BAT").stdout

        ems_configured = (
            "HIMEMX.EXE" in mtype_cfg and "JEMM386.EXE" in mtype_cfg and "KRONDOR.EXE" in mtype_auto
        )
        if not ems_configured:
            errors.append("FDCONFIG.SYS or FDAUTO.BAT missing HIMEMX / JEMM386 / KRONDOR.EXE")

        log("=== 10. Extracting and Verifying Embedded Binaries SHA256 ===")
        embedded_hashes = {}
        for fn, expected_h in EXPECTED_HASHES.items():
            tmp_out = Path(f"/tmp/verify_{fn}")
            if tmp_out.exists():
                tmp_out.unlink()
            run_cmd("mcopy", "-o", "-i", target, f"::{fn}", str(tmp_out))
            got_h = compute_sha256(tmp_out.read_bytes())
            embedded_hashes[fn] = got_h
            if got_h != expected_h:
                errors.append(f"Embedded {fn} hash mismatch: {got_h} != {expected_h}")
            else:
                log(f"  Verified {fn}: {got_h} (MATCH)")

        validation_result = {
            "schema_version": 1,
            "result": "PASS" if not errors else "FAIL",
            "image": "vm/krondor_evg_gate_a.img",
            "size_bytes": img_size,
            "geometry": {
                "cylinders": 65,
                "heads": 16,
                "sectors": 63,
            },
            "mbr": {
                "signature": mbr_sig,
                "active": is_active,
                "partition_type": part_type,
                "start_lba": start_lba,
            },
            "vbr": {
                "lba": 63,
                "jump_valid": vbr_jump_valid,
                "signature": vbr_sig,
            },
            "ems_configured": ems_configured,
            "required_files": files_found,
            "embedded_sha256": embedded_hashes,
            "errors": errors,
        }

        VALIDATION_PATH.write_text(json.dumps(validation_result, indent=2, ensure_ascii=False), encoding="utf-8")
        log(f"Wrote {VALIDATION_PATH}")

        if errors:
            raise RuntimeError(f"Static validation failed with {len(errors)} error(s): {errors}")

        log("=== 11. Finalizing Canonical Image ===")
        shutil.copy2(TEMP_IMG, FINAL_IMG)
        log(f"SUCCESS: Built canonical image at {FINAL_IMG} ({FINAL_IMG.stat().st_size} bytes)")

    except Exception as e:
        log(f"BUILD FAILED: {e}")
        if not VALIDATION_PATH.exists():
            validation_result = {
                "schema_version": 1,
                "result": "FAIL",
                "image": "vm/krondor_evg_gate_a.img",
                "errors": [str(e)],
            }
            VALIDATION_PATH.write_text(json.dumps(validation_result, indent=2, ensure_ascii=False), encoding="utf-8")
        sys.exit(1)
    finally:
        LOG_PATH.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        log(f"Wrote log to {LOG_PATH}")


if __name__ == "__main__":
    main()
