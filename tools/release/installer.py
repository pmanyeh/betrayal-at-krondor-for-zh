#!/usr/bin/env python3
"""Betrayal at Krondor 繁體中文化 -- 安裝／解除安裝程式

只依賴標準函式庫（不需要 pip install 任何套件）。使用者必須自備合法取得的
v1.00 Floppy 版（1993-06-16）遊戲檔案；本安裝程式不包含、也不會下載任何
原版遊戲資產 -- 只會：

  1. 對使用者自己的 KRONDOR.EXE 套用二進位差異補丁（bspatch_apply.py）。
  2. 對使用者自己的 STARTUP.GAM 做隊伍角色英文名 -> 中文名的原地欄位替換。
  3. 把中文化資源檔（DDX/BOK/DAT/字型等 loose 覆蓋檔）複製進遊戲目錄。

執行前會先驗證 KRONDOR.EXE 的雜湊是否符合已知的 v1.00 基準版本，不符合就
直接中止、不改動任何檔案。所有被覆蓋的檔案都會先備份，可用 --uninstall
還原。

用法：
    python installer.py --game-dir "C:\\Games\\BetrayalAtKrondor"
    python installer.py --game-dir "C:\\Games\\BetrayalAtKrondor" --uninstall
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bspatch_apply import apply_patch  # noqa: E402

INSTALL_MANIFEST_NAME = "zh_install_manifest.json"


def sha256_of_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_ci(directory: Path, filename: str) -> Path | None:
    """Case-insensitive file lookup (DOS-era filenames are often upper/lowercase mixed)."""
    target = filename.lower()
    for p in directory.iterdir():
        if p.is_file() and p.name.lower() == target:
            return p
    return None


def backup_file(path: Path, backup_dir: Path) -> str:
    backup_dir.mkdir(parents=True, exist_ok=True)
    dest = backup_dir / path.name
    shutil.copy2(path, dest)
    return dest.name


# ---------------------------------------------------------------------------
# EXE patch
# ---------------------------------------------------------------------------


def install_exe_patch(game_dir: Path, release_dir: Path, backup_dir: Path) -> str:
    manifest = json.loads((release_dir / "exe_patch" / "manifest.json").read_text(encoding="utf-8"))
    baseline = manifest["baseline"]
    target = manifest["target"]

    exe_path = find_ci(game_dir, "krondor.exe")
    if exe_path is None:
        raise SystemExit(f"找不到 {game_dir} 底下的 KRONDOR.EXE，請確認 --game-dir 指向正確的遊戲目錄。")

    exe_bytes = exe_path.read_bytes()
    actual_hash = hashlib.sha256(exe_bytes).hexdigest()
    if len(exe_bytes) != baseline["size"] or actual_hash != baseline["sha256"]:
        raise SystemExit(
            f"偵測到的 KRONDOR.EXE 不是本補丁支援的 {baseline['version_label']}。\n"
            f"  預期：{baseline['size']} bytes, sha256 {baseline['sha256']}\n"
            f"  實際：{len(exe_bytes)} bytes, sha256 {actual_hash}\n"
            "本補丁目前只支援 1993 年 6 月 16 日的 v1.00 Floppy 版，不支援 CD/GOG 等其他版本。\n"
            "沒有任何檔案被改動。"
        )

    backed_up_name = backup_file(exe_path, backup_dir)

    patch_bytes = (release_dir / "exe_patch" / manifest["patch_file"]).read_bytes()
    patched = apply_patch(exe_bytes, patch_bytes)

    patched_hash = hashlib.sha256(patched).hexdigest()
    if len(patched) != target["size"] or patched_hash != target["sha256"]:
        raise SystemExit(
            "套用 EXE 補丁後的雜湊值與預期不符，安裝已中止、原始檔案保持不變。\n"
            f"  預期：{target['size']} bytes, sha256 {target['sha256']}\n"
            f"  實際：{len(patched)} bytes, sha256 {patched_hash}"
        )

    exe_path.write_bytes(patched)
    print(f"[OK] {exe_path.name}：已套用中文化補丁（備份於 {backed_up_name}）")
    return exe_path.name


def restore_exe(game_dir: Path, backup_dir: Path) -> None:
    backed_up = backup_dir / "krondor.exe"
    if not backed_up.exists():
        return
    exe_path = find_ci(game_dir, "krondor.exe")
    if exe_path is not None:
        shutil.copy2(backed_up, exe_path)
        print(f"[OK] {exe_path.name}：已還原成安裝前的版本")


# ---------------------------------------------------------------------------
# STARTUP.GAM character-name patch
# ---------------------------------------------------------------------------


def install_gam_patch(game_dir: Path, release_dir: Path, backup_dir: Path) -> str | None:
    gam_manifest_path = release_dir / "gam_patch" / "character_names.json"
    if not gam_manifest_path.exists():
        return None
    manifest = json.loads(gam_manifest_path.read_text(encoding="utf-8"))

    gam_path = find_ci(game_dir, "startup.gam")
    if gam_path is None:
        print("[跳過] 找不到 STARTUP.GAM，隊伍角色名字維持英文。")
        return None

    data = gam_path.read_bytes()
    actual_hash = hashlib.sha256(data).hexdigest()
    if actual_hash != manifest["baseline_sha256"]:
        print(
            "[跳過] STARTUP.GAM 內容跟已知的原版基準不符（可能是不同版本或已被修改過），"
            "隊伍角色名字維持英文，不強行修改以避免弄壞存檔。"
        )
        return None

    data = bytearray(data)
    slot_width = manifest["slot_width"]
    for entry in manifest["entries"]:
        needle = entry["name_en"].encode("ascii") + b"\x00"
        idx = data.find(needle)
        if idx == -1:
            print(f"[警告] 找不到角色名 {entry['name_en']!r}，跳過這一位。")
            continue
        slot = bytes(data[idx : idx + slot_width])
        expected_prefix = entry["name_en"].encode("ascii")
        if slot[: len(expected_prefix)] != expected_prefix or any(b != 0 for b in slot[len(expected_prefix) :]):
            print(f"[警告] {entry['name_en']!r} 欄位內容跟預期不符，跳過這一位。")
            continue
        new_slot = bytes.fromhex(entry["encoded_slot_hex"])
        data[idx : idx + slot_width] = new_slot

    backed_up_name = backup_file(gam_path, backup_dir)
    gam_path.write_bytes(bytes(data))
    print(f"[OK] {gam_path.name}：隊伍角色名字已中文化（備份於 {backed_up_name}）")
    return gam_path.name


def restore_gam(game_dir: Path, backup_dir: Path) -> None:
    backed_up = backup_dir / "startup.gam"
    if not backed_up.exists():
        return
    gam_path = find_ci(game_dir, "startup.gam")
    if gam_path is not None:
        shutil.copy2(backed_up, gam_path)
        print(f"[OK] {gam_path.name}：已還原成安裝前的版本")


# ---------------------------------------------------------------------------
# Loose resource files
# ---------------------------------------------------------------------------


def install_resources(game_dir: Path, release_dir: Path, backup_dir: Path) -> list[str]:
    resources_dir = release_dir / "resources"
    installed: list[str] = []
    for src in sorted(resources_dir.iterdir()):
        if not src.is_file() or src.name == "RESOURCE_MANIFEST.json":
            continue
        existing = find_ci(game_dir, src.name)
        if existing is not None:
            backup_file(existing, backup_dir)
            dest = existing
        else:
            dest = game_dir / src.name
        shutil.copy2(src, dest)
        installed.append(dest.name)
    print(f"[OK] 已複製 {len(installed)} 個中文化資源檔進遊戲目錄")
    return installed


def remove_resources(game_dir: Path, filenames: list[str], backup_dir: Path) -> None:
    for name in filenames:
        target = find_ci(game_dir, name)
        backed_up = backup_dir / name
        if backed_up.exists():
            if target is not None:
                shutil.copy2(backed_up, target)
        elif target is not None:
            target.unlink()
    print(f"[OK] 已移除／還原 {len(filenames)} 個資源檔")


# ---------------------------------------------------------------------------
# Top-level install / uninstall
# ---------------------------------------------------------------------------


def do_install(game_dir: Path, release_dir: Path) -> None:
    exe_path = find_ci(game_dir, "krondor.exe")
    if exe_path is None:
        raise SystemExit(f"{game_dir} 底下找不到 KRONDOR.EXE，請確認這是合法的遊戲安裝目錄。")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = game_dir / f"_zh_backup_{timestamp}"

    print(f"遊戲目錄：{game_dir}")
    print(f"備份目錄：{backup_dir}\n")

    exe_installed = install_exe_patch(game_dir, release_dir, backup_dir)
    gam_installed = install_gam_patch(game_dir, release_dir, backup_dir)
    resource_files = install_resources(game_dir, release_dir, backup_dir)

    install_manifest = {
        "format": "bak-zh-install-manifest",
        "version": 1,
        "installed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "backup_dir": backup_dir.name,
        "exe_patched": exe_installed,
        "gam_patched": gam_installed,
        "resource_files": resource_files,
    }
    (game_dir / INSTALL_MANIFEST_NAME).write_text(
        json.dumps(install_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"\n安裝完成。若要解除安裝，執行：\n  python installer.py --game-dir \"{game_dir}\" --uninstall")


def do_uninstall(game_dir: Path) -> None:
    manifest_path = game_dir / INSTALL_MANIFEST_NAME
    if not manifest_path.exists():
        raise SystemExit(f"{game_dir} 底下找不到 {INSTALL_MANIFEST_NAME}，看起來這個目錄沒有安裝過中文化補丁。")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    backup_dir = game_dir / manifest["backup_dir"]
    if not backup_dir.exists():
        raise SystemExit(f"找不到備份目錄 {backup_dir}，無法自動還原，請手動處理。")

    restore_exe(game_dir, backup_dir)
    restore_gam(game_dir, backup_dir)
    remove_resources(game_dir, manifest["resource_files"], backup_dir)

    manifest_path.unlink()
    print(f"\n解除安裝完成。備份目錄 {backup_dir.name} 保留未刪除，可自行清理。")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--game-dir", required=True, type=Path, help="遊戲安裝目錄（含 KRONDOR.EXE 的那個資料夾）")
    parser.add_argument("--uninstall", action="store_true", help="還原成安裝前的狀態")
    args = parser.parse_args()

    game_dir = args.game_dir.resolve()
    if not game_dir.is_dir():
        raise SystemExit(f"找不到目錄：{game_dir}")

    if args.uninstall:
        do_uninstall(game_dir)
    else:
        release_dir = Path(__file__).resolve().parent
        do_install(game_dir, release_dir)


if __name__ == "__main__":
    main()
