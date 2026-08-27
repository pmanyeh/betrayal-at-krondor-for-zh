"""Unit tests for mock_hd_text tool."""

import json
from pathlib import Path
import unittest

from PIL import Image

from tools.visual.mock_hd_text import (
    Zh16Font,
    reconstruct_mixed_resolution_background,
    wrap_text,
    render_mock,
    CapacityMetric,
)


class TestMockHdText(unittest.TestCase):
    def setUp(self) -> None:
        self.font_path = Path("localization/generated/ZH16.DAT")
        self.mapping_path = Path("localization/generated/zh_mapping.json")
        self.font = Zh16Font(self.font_path, self.mapping_path)

    def test_font_advances_and_bitmaps(self) -> None:
        # ASCII should advance 8
        self.assertEqual(self.font.advance("A"), 8)
        self.assertEqual(self.font.advance("5"), 8)
        self.assertEqual(self.font.advance(":"), 8)

        # CJK should advance 16
        self.assertEqual(self.font.advance("克"), 16)
        self.assertEqual(self.font.advance("朗"), 16)
        self.assertEqual(self.font.advance("多"), 16)

        # Bitmaps
        w_asc, h_asc, data_asc = self.font.bitmap("A")
        self.assertEqual(w_asc, 8)
        self.assertEqual(h_asc, 16)
        self.assertEqual(len(data_asc), 16)

        w_cjk, h_cjk, data_cjk = self.font.bitmap("克")
        self.assertEqual(w_cjk, 16)
        self.assertEqual(h_cjk, 16)
        self.assertEqual(len(data_cjk), 32)

    def test_wrap_text(self) -> None:
        # 4 CJK chars = 64px width. If max_width = 48, wraps after 3 chars (48px)
        text = "克朗多之"
        lines = wrap_text(text, self.font, max_width=48)
        self.assertEqual(lines, ["克朗多", "之"])

        # Explicit newline preserves lines
        text_nl = "第一行\n第二行"
        lines_nl = wrap_text(text_nl, self.font, max_width=100)
        self.assertEqual(lines_nl, ["第一行", "第二行"])

    def test_reconstruct_background(self) -> None:
        # Create a dummy 640x400 image
        dummy = Image.new("RGB", (640, 400), color=(10, 20, 30))
        reconstructed = reconstruct_mixed_resolution_background(dummy)
        self.assertEqual(reconstructed.size, (640, 400))

        with self.assertRaises(ValueError):
            reconstruct_mixed_resolution_background(Image.new("RGB", (320, 200)))

    def test_render_mock_and_metrics(self) -> None:
        # Test cutscene mock rendering
        spec_data = {
            "name": "Test Mock",
            "clear_rects": [{"x": 10, "y": 10, "w": 100, "h": 50, "color": "#123456"}],
            "runs": [
                {
                    "text": "戈拉斯",
                    "x": 20,
                    "y": 20,
                    "max_width": 160,
                    "color": "#e8d176",
                }
            ],
        }
        bg_path = Path("scratchpad/stage2.png")
        if bg_path.exists():
            img, metrics = render_mock(
                background_path=bg_path,
                spec_data=spec_data,
                font=self.font,
                reference_path=Path("scratchpad/frame7.png"),
            )
            self.assertEqual(img.size, (1280, 400))
            self.assertEqual(len(metrics), 1)
            self.assertEqual(metrics[0].max_width_px, 160)
            self.assertEqual(metrics[0].cjk_capacity_320x200, 5)  # 160 // 32
            self.assertEqual(metrics[0].cjk_capacity_640x400, 10)  # 160 // 16
            self.assertEqual(metrics[0].capacity_increase_pct, 100.0)


if __name__ == "__main__":
    unittest.main()
