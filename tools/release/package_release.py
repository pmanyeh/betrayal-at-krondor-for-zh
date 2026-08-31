"""Developer-side tool: assemble the complete end-user release package.

Builds `dist/release_v100_zh/`, containing:
    installer.py, bspatch_apply.py    -- the end-user installer (stdlib only)
    exe_patch/                        -- KRONDOR.EXE binary diff (via build_exe_patch)
    gam_patch/character_names.json    -- STARTUP.GAM hero-name field patch data
    resources/                        -- translated loose resource files
    README_安裝說明.txt                -- Traditional Chinese install instructions

Deliberately does NOT touch `dist/test_v100_zh/` beyond reading from it, and
never copies unmodified original game assets (krondor.001/.rmf, .wri manuals,
.drv sound drivers, etc.) -- see the RESOURCE_FAMILIES allowlist below, which
is sourced from this project's own *_BUILD_MANIFEST.json files (falling back
to a short explicit list only for the couple of older resource families that
predate the manifest convention).

Usage:
    python tools/release/build_exe_patch.py   # first, produces exe_patch/
    python tools/release/package_release.py
"""

from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "font"))
from build_font import encode_string  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DIST_TEST_DIR = REPO_ROOT / "dist" / "test_v100_zh"
RELEASE_DIR = REPO_ROOT / "dist" / "release_v100_zh"
TOOLS_RELEASE_DIR = Path(__file__).resolve().parent

# From docs/baseline/version-evidence.md -- the original, untouched STARTUP.GAM.
GAM_BASELINE_SHA256 = "b587c74b8a9f00a8b5bf5a382287319120c1958f26282dbc547bb199157bf8c2"
GAM_SLOT_WIDTH = 10
HERO_NAMES = [
    ("Locklear", "洛克利爾"),
    ("Gorath", "戈拉斯"),
    ("Owyn", "歐文"),
    ("Pug", "帕格"),
    ("James", "詹姆士"),
    ("Patrus", "派特魯斯"),
]

# Resource families that predate the *_BUILD_MANIFEST.json convention: just a
# filename, hash-logged at packaging time instead of verified against a prior
# expected value.
UNTRACKED_RESOURCE_FILES = ["KEYWORD.DAT", "OBJINFO.DAT", "fmap_twn.dat"]

FONT_FILES = ["ZH16.DAT", "ZHSTAT.DAT"]


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_manifest(name: str) -> dict:
    return json.loads((DIST_TEST_DIR / name).read_text(encoding="utf-8"))


def collect_ddx_files() -> list[tuple[str, str]]:
    m = _load_manifest("DDX_BUILD_MANIFEST.json")
    return [(f["output"], f["output_sha256"]) for f in m["files"]]


def collect_bok_files() -> list[tuple[str, str]]:
    m = _load_manifest("BOK_BUILD_MANIFEST.json")
    return [(f["output"], f["output_sha256"]) for f in m["files"]]


def collect_menupage_files() -> list[tuple[str, str]]:
    m = _load_manifest("MENUPAGE_BUILD_MANIFEST.json")
    return list(m["deployed_loose_sha256"].items())


def collect_spell_files() -> list[tuple[str, str]]:
    m = _load_manifest("SPELL_BUILD_MANIFEST.json")
    return [(f["output"], f["output_sha256"]) for f in m["files"]]


def collect_fmap_file() -> list[tuple[str, str]]:
    m = _load_manifest("FMAP_TWN_BUILD_MANIFEST.json")
    return [(m["output"], m["output_sha256"])]


def collect_mnames_file() -> list[tuple[str, str]]:
    m = _load_manifest("MNAMES_BUILD_MANIFEST.json")
    return [(m["output"], m["output_sha256"])]


def collect_resource_files() -> dict[str, str | None]:
    """Returns {filename: expected_sha256_or_None}."""
    files: dict[str, str | None] = {}
    for name, expected_hash in (
        collect_ddx_files()
        + collect_bok_files()
        + collect_menupage_files()
        + collect_spell_files()
        + collect_fmap_file()
        + collect_mnames_file()
    ):
        files[name] = expected_hash
    for name in UNTRACKED_RESOURCE_FILES:
        files.setdefault(name, None)
    for name in FONT_FILES:
        files.setdefault(name, None)
    return files


def build_resources(resources_dir: Path) -> dict[str, str]:
    resources_dir.mkdir(parents=True, exist_ok=True)
    files = collect_resource_files()
    shipped: dict[str, str] = {}
    for name, expected_hash in sorted(files.items()):
        src = DIST_TEST_DIR / name
        if not src.exists():
            raise SystemExit(f"預期的資源檔不存在：{src}（HANDOFF.md 記錄已部署，但 dist 裡找不到，先重新建置）")
        data = src.read_bytes()
        actual_hash = sha256_of(data)
        if expected_hash is not None and actual_hash != expected_hash:
            raise SystemExit(
                f"{name} 的雜湊值跟對應 manifest 記錄的不符（可能 dist 已過期，先重新跑對應的 build 工具）：\n"
                f"  manifest：{expected_hash}\n"
                f"  實際：    {actual_hash}"
            )
        shutil.copy2(src, resources_dir / name)
        shipped[name] = actual_hash
    (resources_dir / "RESOURCE_MANIFEST.json").write_text(
        json.dumps({"format": "bak-zh-resource-manifest", "version": 1, "files": shipped}, indent=2, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
    print(f"[OK] 已收錄 {len(shipped)} 個資源檔到 {resources_dir}")
    return shipped


def build_gam_patch(gam_patch_dir: Path) -> None:
    gam_patch_dir.mkdir(parents=True, exist_ok=True)
    mapping = json.loads((REPO_ROOT / "localization" / "generated" / "zh_mapping.json").read_text(encoding="utf-8"))
    char_to_id = mapping["char_to_id"]

    entries = []
    for eng, zh in HERO_NAMES:
        encoded = encode_string(zh, char_to_id)
        if len(encoded) + 1 > GAM_SLOT_WIDTH:
            raise SystemExit(f"{zh!r} ({len(encoded)} bytes + NUL) 塞不進 {GAM_SLOT_WIDTH}-byte 欄位")
        slot = encoded + bytes(GAM_SLOT_WIDTH - len(encoded))
        entries.append({"name_en": eng, "name_zh": zh, "encoded_slot_hex": slot.hex()})

    manifest = {
        "format": "bak-zh-gam-charnames",
        "version": 1,
        "slot_width": GAM_SLOT_WIDTH,
        "baseline_sha256": GAM_BASELINE_SHA256,
        "entries": entries,
    }
    (gam_patch_dir / "character_names.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"[OK] 已產生 {gam_patch_dir / 'character_names.json'}（{len(entries)} 位隊伍角色）")


def write_installer_files(release_dir: Path) -> None:
    for name in ("installer.py", "bspatch_apply.py"):
        shutil.copy2(TOOLS_RELEASE_DIR / name, release_dir / name)
    print("[OK] 已複製 installer.py / bspatch_apply.py")


README_TEXT = """\
Betrayal at Krondor 繁體中文化 -- 安裝說明
==========================================

這是一份「補丁」，不含任何原版遊戲檔案。你需要自備合法取得的
《Betrayal at Krondor》v1.00 Floppy 版（1993 年 6 月 16 日發行）。

目前只支援這個版本，不支援光碟版（v1.02）或其他數位重製版本 -- 安裝程式
會先檢查你的 KRONDOR.EXE 雜湊值，版本不符會直接中止，不會動到任何檔案。

安裝步驟
--------
1. 安裝 Python 3（https://www.python.org/），或確認電腦上已經有。
2. 打開命令列，切換到這個資料夾。
3. 執行：
       python installer.py --game-dir "你的遊戲安裝目錄"
   例如：
       python installer.py --game-dir "C:\\Games\\BetrayalAtKrondor"
4. 完成後，被改動的檔案都備份在遊戲目錄底下的 _zh_backup_<時間戳記> 資料夾。

解除安裝
--------
       python installer.py --game-dir "你的遊戲安裝目錄" --uninstall

免責聲明
--------
本補丁為非營利粉絲翻譯專案，與原開發商／發行商（Dynamix、Sierra
及其後續版權繼受者）無任何關係，亦未獲得其授權或背書。《Betrayal at
Krondor》的著作權歸原版權所有者所有。

補丁本身（安裝程式、翻譯文字、二進位差異檔）的授權條款請見本專案
GitHub repo 的 LICENSE 檔案。
"""


def write_readme(release_dir: Path) -> None:
    (release_dir / "README_安裝說明.txt").write_text(README_TEXT, encoding="utf-8")
    print("[OK] 已寫入 README_安裝說明.txt")


def make_zip(release_dir: Path) -> Path:
    zip_path = release_dir.parent / f"{release_dir.name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in release_dir.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(release_dir.parent))
    print(f"[OK] 已打包 {zip_path}")
    return zip_path


def main() -> None:
    if not (RELEASE_DIR / "exe_patch" / "manifest.json").exists():
        raise SystemExit(f"找不到 {RELEASE_DIR / 'exe_patch' / 'manifest.json'}，先跑 tools/release/build_exe_patch.py")

    build_resources(RELEASE_DIR / "resources")
    build_gam_patch(RELEASE_DIR / "gam_patch")
    write_installer_files(RELEASE_DIR)
    write_readme(RELEASE_DIR)
    make_zip(RELEASE_DIR)
    print(f"\n完成：{RELEASE_DIR}")


if __name__ == "__main__":
    main()
