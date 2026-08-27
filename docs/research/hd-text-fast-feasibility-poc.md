# High-Resolution CJK Text: Fast Feasibility POC

## Purpose

Decide in no more than half a day whether Krondor's 320x200 logical graphics
combined with native-resolution CJK text is visually valuable enough to justify
further work.

This is a decision gate, not a VESA driver implementation. Stop after producing
and reviewing the comparison images unless the improvement is compelling.

## Hypothesis

Keep the game at 320x200 logical coordinates, expand ordinary graphics to
640x400, but render the existing 16x16 `ZH16.DAT` glyphs as 16x16 *physical*
pixels instead of expanding them to 32x32.

```text
ordinary graphics: 1 logical pixel -> 2x2 physical pixels
CJK text:          1 glyph pixel   -> 1x1 physical pixel
glyph advance:     8 logical       -> 16 physical pixels
```

This should approximately double the amount of Chinese text that fits in the
same logical rectangle without reducing the glyph bitmap to 8x8.

## Hard Timebox

- Visual gate: 30 minutes to 4 hours.
- Optional original-EVG gate in 86Box: 30 minutes to 4 hours.
- Do **not** modify `VMCODE.OVL`, write a VESA driver, or change production game
  files during this experiment.

## Existing Inputs

### Font

- `localization/generated/ZH16.DAT`
- `localization/generated/zh_mapping.json`

`ZH16.DAT` layout:

```text
16-byte header
glyph_count * 32-byte CJK bitmaps (16x16, 1bpp)
256 * 16-byte ETen ASCII bitmaps (8x16, 1bpp)
```

### Captures

The debugger PNGs are 640x400 but use a split capture layout:

```text
x=0..319: valid complete game frame with doubled scanlines
x=320..639: planar/debug artefact
```

For the proposed output, crop the valid left half and expand only X from 320 to
640 with nearest-neighbor sampling. This yields the same 640x400 physical model
that an EVG-style 2x driver would produce.

Recommended cases:

1. `scratchpad/stage2.png` (clean cutscene parchment background) with
   `scratchpad/frame7.png` as the current-text reference.
2. `scratchpad/corpse-loot-hang.png` (ordinary multi-line dialogue).
3. `scratchpad/corpse-loot-bug-20260823/current-pagination-screen.png`
   (compact stats UI).
4. `scratchpad/ems-debug-menu.png` (chapter/objective banner).

## Reproducible Visual Gate

The repository includes `tools/visual/mock_hd_text.py`. It reads the real font,
does no antialiasing, and makes no generative or artistic substitutions.

Run from the repository root:

```powershell
python tools/visual/mock_hd_text.py `
  --background scratchpad/stage2.png `
  --reference scratchpad/frame7.png `
  --spec tools/visual/hd-text-cutscene-spec.json `
  --output scratchpad/hd-text-cutscene-comparison.png
```

The output is 1280x400:

```text
left:  reconstructed current capture
right: proposed 640x400 background + native 16x16 text
```

Coordinates in the JSON spec are physical 640x400 coordinates. Add runs or
change `max_width`, `line_height`, `align`, and `color` to explore layout without
editing the script.

## Visual Acceptance Criteria

PASS only if all are true:

- 16x16 physical Chinese remains comfortably readable at the intended window
  size and 4:3 presentation.
- The text no longer dominates the parchment/UI artwork.
- Typical dialogue line capacity improves by at least 70 percent.
- A 16-19 physical-pixel line height looks coherent with the original art.
- Dense UI and chapter-banner tests do not look conspicuously undersized.

FAIL/STOP if any are true:

- The glyphs are readable only when the user enlarges the window beyond the
  intended size.
- The mixed-resolution text looks visually detached from the pixel art.
- The gain is modest enough that editorial shortening or the existing 10x10
  small-font mode would solve the same problem.
- Different surfaces require incompatible scale policies.

## Optional Hardware Gate: Original EVG in 86Box

Current 86Box includes an exact `Video 7 VGA 1024i (HT208)` device and emulates
the Video Seven registers used by `EVG.ASM`, including Sequencer `0xF6`.

Krondor does not auto-select it: `BOOT.C` currently calls `video_init(8, ...)`,
where mode 8 is VGA; mode 9 maps to `OVL:EVG:`. A disposable experimental build
may change only startup mode 8 to 9. Keep `VMCODE.OVL` unchanged.

Suggested configuration:

```text
86Box: latest stable release and matching ROM set
Machine: generic 386/486 ISA
RAM: 4-8 MB
Video: Video 7 VGA 1024i (HT208)
Video BIOS: v2.19 first
Video RAM: 512 KB
```

Expected effort:

- Existing 86Box/DOS environment: 30-90 minutes.
- From scratch: 2-4 hours.

PASS means the stock EVG driver returns adapter 9 and the game displays and
interacts at physical 640x400. This proves the original 2x graphics path only;
the offline comparison remains the test of native-size CJK.

Useful upstream references:

- <https://github.com/86Box/86Box/blob/master/src/video/vid_ht216.c>
- <https://github.com/86Box/roms/releases>
- <https://github.com/86Box/docs/blob/master/usage/roms.rst>

## Decision

After the visual gate, record exactly one result:

```text
GO: mixed-resolution CJK is a large, obvious improvement; schedule an in-game POC.
NO-GO: retain the current 320x200 renderer and spend no more project time here.
```

Do not interpret a visual PASS as evidence that a publishable VESA driver is
cheap. It proves only that the destination is worth considering.
