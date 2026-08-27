"""Generate FONT8X16.DAT binary with CP437 standard 8x16 font bitmaps."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.load_default()
raw = bytearray()

for ascii_code in range(32, 128):
    im = Image.new("1", (8, 16), 0)
    draw = ImageDraw.Draw(im)
    draw.text((0, 1), chr(ascii_code), font=font, fill=1)

    for y in range(16):
        b = 0
        for x in range(8):
            if im.getpixel((x, y)):
                b |= (0x80 >> x)
        raw.append(b)

target_src = Path("scratchpad/vesa-640x400-cjk-poc/src/FONT8X16.DAT")
target_rt = Path("scratchpad/vesa-640x400-cjk-poc/runtime/FONT8X16.DAT")
target_src.write_bytes(raw)
target_rt.write_bytes(raw)
print(f"Generated FONT8X16.DAT ({len(raw)} bytes)")
