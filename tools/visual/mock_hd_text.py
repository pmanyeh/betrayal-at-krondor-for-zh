"""Build deterministic mixed-resolution Krondor text mocks and comparison suites.

The saved debugger captures in this repository are 640x400 images whose left
320x400 half is the complete 320x200 game frame with doubled scanlines. The
right half is a planar/debug artefact. This tool reconstructs the proposed
EVG-style output by stretching the valid left half to 640x400 horizontally,
clears optional rectangular areas if specified, then draws glyphs from the real
ZH16.DAT at native physical resolution (16x16 for CJK, 8x16 for ASCII).

JSON Spec format:
{
  "name": "Optional Scenario Name",
  "clear_rects": [
    {"x": 38, "y": 24, "w": 564, "h": 194, "color": "#926534"}
  ],
  "runs": [
    {"text": "戈拉斯", "x": 208, "y": 240, "max_width": 224, "align": "center", "color": "#e8d176"},
    {"text": "中文內容", "x": 72, "y": 298, "max_width": 496, "line_height": 19, "color": "#e8d176"}
  ]
}

All x/y/width values are physical 640x400 coordinates.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw


HEADER_SIZE = 16
CJK_GLYPH_BYTES = 32
ASCII_GLYPH_BYTES = 16


def reconstruct_mixed_resolution_background(image: Image.Image) -> Image.Image:
    """Recover the valid frame and expand logical X from 320 to 640."""
    if image.size != (640, 400):
        raise ValueError(f"expected a 640x400 debugger capture, got {image.size}")
    valid_half = image.crop((0, 0, 320, 400))
    return valid_half.resize((640, 400), Image.Resampling.NEAREST).convert("RGB")


class Zh16Font:
    def __init__(self, font_path: Path, mapping_path: Path) -> None:
        self.data = font_path.read_bytes()
        self.mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        self.count = int(self.mapping["glyph_count"])
        self.char_to_id = {
            ch: int(glyph_id) for ch, glyph_id in self.mapping["char_to_id"].items()
        }
        expected = HEADER_SIZE + self.count * CJK_GLYPH_BYTES + 256 * ASCII_GLYPH_BYTES
        if len(self.data) != expected:
            raise ValueError(
                f"ZH16 size mismatch: expected {expected} bytes for {self.count} slots, "
                f"got {len(self.data)}"
            )

    def advance(self, ch: str) -> int:
        return 8 if ord(ch) < 0x80 else 16

    def bitmap(self, ch: str) -> tuple[int, int, bytes]:
        code = ord(ch)
        if code < 0x100:
            offset = HEADER_SIZE + self.count * CJK_GLYPH_BYTES + code * ASCII_GLYPH_BYTES
            return 8, 16, self.data[offset : offset + ASCII_GLYPH_BYTES]

        glyph_id = self.char_to_id.get(ch)
        if glyph_id is None:
            raise KeyError(f"{ch!r} is not present in {self.mapping.get('format', 'ZH16')} mapping")
        offset = HEADER_SIZE + glyph_id * CJK_GLYPH_BYTES
        return 16, 16, self.data[offset : offset + CJK_GLYPH_BYTES]


def wrap_text(text: str, font: Zh16Font, max_width: int | None) -> list[str]:
    if not max_width:
        return text.split("\n")
    lines: list[str] = []
    current: list[str] = []
    width = 0
    for ch in text:
        if ch == "\n":
            lines.append("".join(current))
            current = []
            width = 0
            continue
        advance = font.advance(ch)
        if current and width + advance > max_width:
            lines.append("".join(current))
            current = []
            width = 0
        current.append(ch)
        width += advance
    lines.append("".join(current))
    return lines


def draw_glyph(draw: ImageDraw.ImageDraw, font: Zh16Font, ch: str, x: int, y: int, color: str | tuple[int, ...]) -> None:
    width, height, bitmap = font.bitmap(ch)
    stride = (width + 7) // 8
    for row in range(height):
        for col in range(width):
            if bitmap[row * stride + col // 8] & (0x80 >> (col & 7)):
                draw.point((x + col, y + row), fill=color)


def apply_clear_rects(image: Image.Image, clear_rects: list[dict[str, object]]) -> None:
    draw = ImageDraw.Draw(image)
    for rect in clear_rects:
        x = int(rect["x"])
        y = int(rect["y"])
        w = int(rect["w"])
        h = int(rect["h"])
        color = ImageColor.getrgb(str(rect.get("color", "#000000")))
        draw.rectangle([x, y, x + w, y + h], fill=color)


def draw_run(image: Image.Image, font: Zh16Font, run: dict[str, object]) -> None:
    text = str(run["text"])
    x = int(run["x"])
    y = int(run["y"])
    max_width = int(run["max_width"]) if run.get("max_width") else None
    line_height = int(run.get("line_height", 18))
    color = ImageColor.getrgb(str(run.get("color", "#000000")))
    align = str(run.get("align", "left"))
    draw = ImageDraw.Draw(image)

    for line in wrap_text(text, font, max_width):
        line_width = sum(font.advance(ch) for ch in line)
        line_x = x
        if align == "center":
            if max_width is None:
                raise ValueError("center alignment requires max_width")
            line_x += (max_width - line_width) // 2
        elif align == "right":
            if max_width is None:
                raise ValueError("right alignment requires max_width")
            line_x += max_width - line_width
        elif align != "left":
            raise ValueError(f"unsupported alignment: {align}")

        cursor_x = line_x
        for ch in line:
            draw_glyph(draw, font, ch, cursor_x, y, color)
            cursor_x += font.advance(ch)
        y += line_height


@dataclass
class CapacityMetric:
    scenario: str
    max_width_px: int
    cjk_capacity_320x200: int  # 32px per glyph advance in 640x400 physical space
    cjk_capacity_640x400: int  # 16px per glyph advance in 640x400 physical space
    capacity_increase_pct: float
    rendered_lines: int


def render_mock(
    background_path: Path,
    spec_data: dict[str, object],
    font: Zh16Font,
    reference_path: Path | None = None,
) -> tuple[Image.Image, list[CapacityMetric]]:
    background = reconstruct_mixed_resolution_background(Image.open(background_path))

    if "clear_rects" in spec_data:
        apply_clear_rects(background, spec_data["clear_rects"])  # type: ignore[arg-type]

    metrics: list[CapacityMetric] = []
    runs = spec_data.get("runs", [])
    scenario_name = str(spec_data.get("name", background_path.stem))

    for run in runs:  # type: ignore[union-attr]
        draw_run(background, font, run)
        max_w = int(run.get("max_width", 640))
        text = str(run["text"])
        lines = wrap_text(text, font, max_w)
        # In 320x200 logical space, each CJK glyph is 16 logical px -> 32 physical px
        cap_320 = max(1, max_w // 32)
        # In 640x400 native space, each CJK glyph is 16 physical px
        cap_640 = max(1, max_w // 16)
        increase = ((cap_640 - cap_320) / cap_320) * 100.0
        metrics.append(
            CapacityMetric(
                scenario=scenario_name,
                max_width_px=max_w,
                cjk_capacity_320x200=cap_320,
                cjk_capacity_640x400=cap_640,
                capacity_increase_pct=increase,
                rendered_lines=len(lines),
            )
        )

    output = background
    if reference_path:
        reference = reconstruct_mixed_resolution_background(Image.open(reference_path))
        comparison = Image.new("RGB", (1280, 400))
        comparison.paste(reference, (0, 0))
        comparison.paste(background, (640, 0))
        output = comparison

    return output, metrics


SUITE_CASES = [
    {
        "id": "cutscene",
        "name": "1. Cutscene Parchment Dialogue",
        "background": Path("scratchpad/stage2.png"),
        "reference": Path("scratchpad/frame7.png"),
        "spec": Path("tools/visual/hd-text-cutscene-spec.json"),
        "output": Path("scratchpad/hd_poc_cutscene_comparison.png"),
    },
    {
        "id": "dialogue",
        "name": "2. In-Game World Multi-Line Dialogue",
        "background": Path("scratchpad/corpse-loot-hang.png"),
        "reference": Path("scratchpad/corpse-loot-hang.png"),
        "spec": Path("tools/visual/hd-text-dialogue-spec.json"),
        "output": Path("scratchpad/hd_poc_dialogue_comparison.png"),
    },
    {
        "id": "stats",
        "name": "3. Compact Character Stats UI",
        "background": Path("scratchpad/corpse-loot-bug-20260823/current-pagination-screen.png"),
        "reference": Path("scratchpad/corpse-loot-bug-20260823/current-pagination-screen.png"),
        "spec": Path("tools/visual/hd-text-stats-spec.json"),
        "output": Path("scratchpad/hd_poc_stats_comparison.png"),
    },
    {
        "id": "banner",
        "name": "4. Map Chapter / Objective Banner",
        "background": Path("scratchpad/ems-debug-menu.png"),
        "reference": Path("scratchpad/ems-debug-menu.png"),
        "spec": Path("tools/visual/hd-text-banner-spec.json"),
        "output": Path("scratchpad/hd_poc_banner_comparison.png"),
    },
]


def run_suite(
    font_path: Path,
    mapping_path: Path,
    out_dir: Path | None = None,
) -> list[tuple[str, Path, list[CapacityMetric]]]:
    font = Zh16Font(font_path, mapping_path)
    results = []
    print("=" * 80)
    print("HIGH-RESOLUTION CJK TEXT POC: BENCHMARK SUITE EXECUTION")
    print("=" * 80)
    for case in SUITE_CASES:
        out_path = case["output"] if out_dir is None else out_dir / case["output"].name  # type: ignore[union-attr]
        spec_data = json.loads(case["spec"].read_text(encoding="utf-8"))  # type: ignore[union-attr]
        img, metrics = render_mock(
            background_path=case["background"],  # type: ignore[arg-type]
            spec_data=spec_data,
            font=font,
            reference_path=case["reference"],  # type: ignore[arg-type]
        )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(out_path)
        results.append((case["name"], out_path, metrics))  # type: ignore[arg-type]
        print(f"[{case['id']}] Generated: {out_path} ({img.width}x{img.height})")
        for m in metrics:
            print(
                f"       - Width: {m.max_width_px}px | 320x200 capacity: {m.cjk_capacity_320x200} chars/line "
                f"-> 640x400 capacity: {m.cjk_capacity_640x400} chars/line (+{m.capacity_increase_pct:.0f}%) | "
                f"Rendered lines: {m.rendered_lines}"
            )
    print("=" * 80)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", action="store_true", help="Run all 4 canonical benchmark cases")
    parser.add_argument("--background", type=Path, help="Background image (640x400 capture)")
    parser.add_argument("--spec", type=Path, help="JSON spec file for text runs and clear rects")
    parser.add_argument("--output", type=Path, help="Output PNG path")
    parser.add_argument("--reference", type=Path, help="Optional capture for a side-by-side comparison")
    parser.add_argument("--font", type=Path, default=Path("localization/generated/ZH16.DAT"))
    parser.add_argument("--mapping", type=Path, default=Path("localization/generated/zh_mapping.json"))
    args = parser.parse_args()

    if args.suite:
        run_suite(args.font, args.mapping)
        return

    if not args.background or not args.spec or not args.output:
        parser.error("--background, --spec, and --output are required when not running with --suite")

    font = Zh16Font(args.font, args.mapping)
    spec_data = json.loads(args.spec.read_text(encoding="utf-8"))
    img, metrics = render_mock(args.background, spec_data, font, args.reference)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    img.save(args.output)
    print(f"Wrote {args.output} ({img.width}x{img.height})")
    for m in metrics:
        print(
            f"Metrics: max_width={m.max_width_px}px | 320x200={m.cjk_capacity_320x200} chars "
            f"-> 640x400={m.cjk_capacity_640x400} chars (+{m.capacity_increase_pct:.0f}%)"
        )


if __name__ == "__main__":
    main()
