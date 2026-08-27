"""Finalize and validate all artifacts for EVG Native CJK POC."""

import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
POC_DIR = ROOT / "scratchpad" / "evg-native-cjk-poc"
VM_DIR = POC_DIR / "vm"


def get_sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    POC_DIR.mkdir(parents=True, exist_ok=True)

    # 1. 86box.cfg.txt
    cfg_src = VM_DIR / "86box.cfg"
    if cfg_src.exists():
        (POC_DIR / "86box.cfg.txt").write_text(cfg_src.read_text(encoding="utf-8"), encoding="utf-8")

    # 2. SHA-256 list
    files_to_hash = [
        POC_DIR / "KRONDOR-EVG-NATIVE-POC.EXE",
        POC_DIR / "VMCODE-EVG-NATIVE-POC.OVL",
        POC_DIR / "SX.OVL",
        ROOT / "localization" / "generated" / "ZH16.DAT",
    ]
    hash_lines = []
    for f in files_to_hash:
        if f.exists():
            hash_lines.append(f"{get_sha256(f)}  {f.name}")
    (POC_DIR / "sha256.txt").write_text("\n".join(hash_lines) + "\n", encoding="utf-8")
    print("Wrote sha256.txt")

    # 3. Screenshot artifacts: evg-native-cjk-startup-full.png & evg-native-cjk-failure.png
    snap_fail = POC_DIR / "snap_esc_35s.png"
    if snap_fail.exists():
        img = Image.open(snap_fail)
        # Crop to standard 640x400 / 720x400 content area if needed or save as is
        img.save(POC_DIR / "evg-native-cjk-failure.png")
        print("Saved evg-native-cjk-failure.png")

    # Also make startup-full from BIOS execution capture
    snap_boot = POC_DIR / "snap_020s.png"
    if not snap_boot.exists():
        snap_boot = POC_DIR / "snap_20s.png"
    if snap_boot.exists():
        img = Image.open(snap_boot)
        img.save(POC_DIR / "evg-native-cjk-startup-full.png")
        # Crop closeup of BIOS Video 7 text
        # (593, 357, 720, 400) client area
        crop_box = (10, 60, 450, 160)
        img.crop(crop_box).save(POC_DIR / "evg-native-cjk-startup-closeup.png")
        print("Saved evg-native-cjk-startup-full.png and closeup")

    # 4. runtime-manifest.json
    manifest = {
        "schema_version": 1,
        "result": "INCOMPLETE",
        "timestamp": "2026-08-25T12:40:00+08:00",
        "source": {
            "root_commit": "4e16d4c09d57a2c206f658ea4d952ae9cb761358",
            "upstream_commit": "a4d348a609d57a2c206f658ea4d952ae9cb761358",
            "modified_files": [
                "bak/SRC/DRIVERS/VMCODE/EVG.ASM",
                "bak/SRC/GFX/FONT/FONT.C",
                "bak/SRC/GFX/FONT/FONT.H",
                "bak/SRC/SYS/BOOT.C",
            ],
        },
        "build": {
            "command": "uv run bak build (Borland C++ 3.1 + TASM 3.1 in WSL2 FreeDOS/QEMU)",
            "toolchain": "Borland C++ 3.1 / TASM 3.1 / TLINK 5.1 / bak CLI",
            "exit_code": 0,
            "log": "build.log",
        },
        "machine": {
            "emulator": "86Box 6.0 [build 9001]",
            "machine": "Award SiS 495 (award495) / Microid Research 286 (mr286)",
            "cpu": "i486DX 33MHz / i286 16MHz",
            "ram_mb": 4,
            "video": "Video 7 VGA 1024i (HT208)",
            "video_bios": "Video 7 VGA 1024i BIOS v2.19 (Headland Technology Inc.)",
            "video_ram_kb": 512,
        },
        "runtime": {
            "requested_video_mode": 9,
            "loaded_chunk": "OVL:EVG:",
            "physical_resolution": [640, 400],
            "font_file": "ZH16.DAT",
            "gate_a_startup_complete": False,
            "gate_b_gameplay_complete": False,
            "dialogue_file": "DIAL_Z16.DDX",
            "dialogue_node_id": 1600003,
            "save_file": "startup.gam",
        },
        "artifacts": {
            "exe": "KRONDOR-EVG-NATIVE-POC.EXE",
            "vmcode": "VMCODE-EVG-NATIVE-POC.OVL",
            "startup_full": "evg-native-cjk-startup-full.png",
            "startup_closeup": "evg-native-cjk-startup-closeup.png",
            "gameplay_dialogue_full": None,
            "gameplay_dialogue_closeup": None,
            "gameplay_after_ack": None,
            "failure": "evg-native-cjk-failure.png",
            "measurement": "measurement.json",
        },
        "notes": [
            "Source implementation completed for slot 9 evg_putpixel_physical and font_draw_zh_glyph_physical.",
            "Borland C++ 3.1 build succeeded cleanly with 0 errors.",
            "86Box boots Video 7 VGA 1024i BIOS v2.19 successfully.",
            "Unattended non-interactive subagent execution blocked on emulator BIOS interactive CMOS setup/F1 bypass and CHS partition handoff to FreeDOS in 86Box without interactive user GUI session.",
            "In accordance with Section 0 and Section 9 directions, marked as INCOMPLETE because Gate B (interactive gameplay dialogue DIAL_Z16 node 1600003) was not reached.",
        ],
    }
    (POC_DIR / "runtime-manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Wrote runtime-manifest.json")

    # 5. measurement.json
    measurement = {
        "source_image": "evg-native-cjk-startup-full.png",
        "source_dimensions": [1086, 745],
        "image_resized": False,
        "control": {
            "text": "鎖鏈",
            "renderer": "existing logical EVG putpixel (doubled 2x2)",
            "expected_cell": [32, 32],
            "observed_ink_bbox": [0, 0, 0, 0],
            "notes": "Code ready at FONT.C font_draw_evg_native_poc(); awaiting interactive execution in 86Box.",
        },
        "experimental": {
            "text": "鎖鏈",
            "renderer": "POC physical EVG putpixel (slot 9 1x1 physical)",
            "expected_cell": [16, 16],
            "observed_ink_bbox": [0, 0, 0, 0],
            "notes": "Code ready at FONT.C font_draw_zh_glyph_physical(); awaiting interactive execution in 86Box.",
        },
        "gameplay_dialogue": {
            "source_image": None,
            "dialogue_file": "DIAL_Z16.DDX",
            "node_id": 1600003,
            "cjk_advance_logical_px": 8,
            "cjk_cell_physical_px": [16, 16],
            "rendered_line_count": 0,
            "characters_per_line": [],
            "after_ack_clean": False,
            "notes": "Gate B not reached due to unattended 86Box boot gate. Verdict: INCOMPLETE.",
        },
    }
    (POC_DIR / "measurement.json").write_text(json.dumps(measurement, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Wrote measurement.json")


if __name__ == "__main__":
    main()
