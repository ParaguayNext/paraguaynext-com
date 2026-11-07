# ParaguayNext ALTERNATIVE set: Lapacho Forward logo + Ñandutí lace pattern

**Status: drafts only.** Nothing has been published, uploaded or set as an avatar. This set exists so Roger can compare it with `/workspace/brand/logo-final/` (Ñandutí logo + Lapacho pattern), which this round did not touch.
Side-by-side comparison: `/workspace/brand/logo-compare-2026-11-06.png`. Overview: `contact-sheet.png`.
Rebuild: `/workspace/.brandvenv/bin/python src/run.py && /workspace/.brandvenv/bin/python src/sheet.py && /workspace/.brandvenv/bin/python src/compare.py`

## The mark: v3 02 Lapacho Forward, with Critiquito's v3 fixes
- **Forward petal:** it now has the same round base as the other four petals (same inner and body circles), and its sides curve slightly **outward** into a sharp tip at the same length as v3 (262 units from the centre). The point is kept; there's no hat or leaf shape. The sides are quadratic curves that meet the body circle tangentially, so the petal has no corners.
- **Equal gaps:** all five petals sit on exact 72° slots around one centre, and the forward petal's body matches the others, so all five gaps are the same width at the centre.
- **One plain centre hole everywhere:** the dark-green dot and cream ring are gone. In the full mark the open centre is the hole. In the 32 px master, a ring joins the petal bases around a round hole. The 16 px master has a 1 px hole.
- `symbol/` holds the full mark (transparent) in light (lapacho pink), dark (cream), black, white, lapacho and on-green (#F07AA0) versions, as SVG plus PNG at 512 and 1024.
- `favicon/lapacho-32-master-*.svg` is a separate 32 px drawing: bolder petals, a joining ring and a 2 px hole.
- `favicon/lapacho-16-master-*.svg` is a pixel master: thresholded from a 16-unit drawing, then hand-fixed (1 px hole and ring pixels).
- `favicon.ico` (pink) and `favicon-dark.ico` (cream) each hold 16 and 32 px. `favicon.svg` uses the 16 px master and switches to cream in dark mode. `apple-touch-icon-180` is included.

## Colours (and why)
| Name | Hex | Use |
|---|---|---|
| Lapacho pink | #D2386C | The mark on light grounds |
| Pink on dark | #F07AA0 | The mark on yerba green (Critiquito's locked pink-on-dark) |
| Red earth | #B4442A | "Next" on light, the same as logo-final |
| Red earth on dark | #E07A55 | "Next" on dark, the same as logo-final (Roger's pick) |
| Black ground | #16181A | Dark lockup and dark avatar ground |
| Cream | #FAF4EA | Light ground, the mark and "Paraguay" on dark |
| Ink | #1E1A17 | "Paraguay" on light |
| Yerba green | #1F4E36 | Pattern ground (yerba colourway) and the cover |
| Lace, cream colourway | #F4E1E4 | Pattern motifs on cream (same as the Lapacho pattern) |
| Lace, yerba colourway | #2A6447 | Pattern motifs on yerba (same as the Lapacho pattern) |

**Light lockup choice:** a lapacho-pink mark, ink "Paraguay" and red-earth "Next" on cream. The wordmark is identical to logo-final's light lockup, and the dark lockup is identical too (cream mark, cream "Paraguay", #E07A55 "Next" on #16181A). Between the two sets, only the mark and the pattern change, so the comparison is fair. Pink is the lapacho's own colour and the reason to choose this set. I didn't use a red-earth mark because it makes the flower look like a rust-coloured clone of the Ñandutí set, and I didn't use a pink "Next" because it can't carry over to dark grounds (pink on dark is 2.6:1). Weakness: pink next to red earth is close in hue (1.19:1 against each other). It reads as warm and deliberate at lockup size, but some may find it a little sweet.

## Contrast (WCAG 2.x)
| Pair | Ratio |
|---|---|
| #D2386C pink on #FAF4EA cream | 4.24:1 (fine for a graphic, 3:1 needed) |
| #D2386C on #FFFFFF | 4.64:1 |
| #FAF4EA cream on #D2386C (light avatar) | 4.24:1 |
| #FAF4EA on #16181A (dark lockup and avatar) | 16.27:1 |
| #E07A55 "Next" on #16181A | 6.01:1 |
| #B4442A "Next" on cream | 5.05:1 |
| #1E1A17 ink on cream | 15.79:1 |
| #D2386C on #35363A dark tab | 2.60:1 (too low, so the dark favicon is cream: 11.03:1) |
| #F07AA0 on #1F4E36 yerba | 3.63:1 |
| #EFA184 "Next" on yerba (cover) | 4.59:1 |
| Pattern motifs on their grounds | 1.15:1 (cream) and 1.37:1 (yerba): faint on purpose |

## Avatars
- Primary light: `avatar-cream-on-pink` (cream flower on a lapacho-pink circle).
- Primary dark: `avatar-cream-on-black` (cream flower on #16181A), the same style as logo-final.
- Alternate: `avatar-pink-on-yerba` (#F07AA0 on #1F4E36), Critiquito's v3 favourite for social.
- Each comes as an X 400 PNG, a Skool 512 PNG, and a 48 and 32 px PNG drawn from the 32 px master. The flower reaches 68% of the circle radius, inside a 10% safe margin, and is nudged about 3% down-left for optical centring.

## Ñandutí lace pattern
- The motif is the v3 ñandutí lace (10 scallops, 10 threads, centre hole) **without the needle**. In this set the needle would be a second pointer competing with the forward petal, and a field of needles reads as arrows.
- A 240 px tile holds 5 motifs at different sizes and slight rotations. Wrapped copies make it seamless. **Seam check:** a 2×2 grid of rendered tiles matches an SVG `<pattern>` fill with a maximum difference of 0 at the seams (12 to 13/255 elsewhere, from anti-aliasing only). Motifs never touch; the closest gap is 15 px at tile scale.
- Colourways: cream (#F4E1E4 on #FAF4EA) and yerba (#2A6447 on #1F4E36), the same colour rules as the Lapacho pattern in logo-final.
- **Skool cover 1084×576** (`samples/`): yerba colourway with the stacked on-green lockup (#F07AA0 mark, cream "Paraguay", #EFA184 "Next"). Any motif that would touch the lockup's ink box (plus a 22 px margin) **or cross the image edge** is dropped whole, so no motif is clipped anywhere: 28 kept, 23 dropped.

## Weaknesses
- At 16 px it reads as a five-lobed pink flower with a nick on the upper right. The forward point survives only as a 1 px tip. The Ñandutí 16 px (scalloped disc with a plus) is a stronger silhouette in a tab.
- The 32 px master merges the petal bases into a ring, so it's a little heavier and rounder than the open full mark.
- Pink on dark tabs is 2.6:1, so all dark-UI uses switch to cream and lose the pink identity.
- The pattern is a more regular grid than the Lapacho pattern (round motifs), and at cover scale the empty band at the top and bottom edges (from dropping edge motifs) is visible.
- The caps lockups and the one-colour lockups were generated too (same build), but they weren't art-directed for this set.
- Real X and Skool upload tests are still needed before anything goes live.

## SVG file sizes
| File | Size |
|---|---|
| avatar/avatar-cream-on-black-small-master.svg | 0.71 KB |
| avatar/avatar-cream-on-black.svg | 0.64 KB |
| avatar/avatar-cream-on-pink-small-master.svg | 0.71 KB |
| avatar/avatar-cream-on-pink.svg | 0.64 KB |
| avatar/avatar-pink-on-yerba-small-master.svg | 0.71 KB |
| avatar/avatar-pink-on-yerba.svg | 0.64 KB |
| favicon/apple-touch-icon-180.svg | 0.70 KB |
| favicon/favicon.svg | 0.54 KB |
| favicon/lapacho-16-master-black.svg | 0.44 KB |
| favicon/lapacho-16-master-dark.svg | 0.44 KB |
| favicon/lapacho-16-master-light.svg | 0.44 KB |
| favicon/lapacho-16-master-white.svg | 0.44 KB |
| favicon/lapacho-32-master-black.svg | 0.65 KB |
| favicon/lapacho-32-master-dark.svg | 0.65 KB |
| favicon/lapacho-32-master-light.svg | 0.65 KB |
| favicon/lapacho-32-master-white.svg | 0.65 KB |
| lockup/lockup-caps-horizontal-black.svg | 4.61 KB |
| lockup/lockup-caps-horizontal-dark.svg | 4.61 KB |
| lockup/lockup-caps-horizontal-lapacho.svg | 4.61 KB |
| lockup/lockup-caps-horizontal-light.svg | 4.61 KB |
| lockup/lockup-caps-horizontal-on-green.svg | 4.61 KB |
| lockup/lockup-caps-horizontal-white.svg | 4.61 KB |
| lockup/lockup-caps-stacked-black.svg | 4.61 KB |
| lockup/lockup-caps-stacked-dark.svg | 4.61 KB |
| lockup/lockup-caps-stacked-lapacho.svg | 4.61 KB |
| lockup/lockup-caps-stacked-light.svg | 4.61 KB |
| lockup/lockup-caps-stacked-on-green.svg | 4.61 KB |
| lockup/lockup-caps-stacked-white.svg | 4.61 KB |
| lockup/lockup-serif-horizontal-black.svg | 6.14 KB |
| lockup/lockup-serif-horizontal-dark.svg | 6.14 KB |
| lockup/lockup-serif-horizontal-lapacho.svg | 6.14 KB |
| lockup/lockup-serif-horizontal-light.svg | 6.14 KB |
| lockup/lockup-serif-horizontal-on-green.svg | 6.14 KB |
| lockup/lockup-serif-horizontal-white.svg | 6.14 KB |
| lockup/lockup-serif-stacked-black.svg | 6.14 KB |
| lockup/lockup-serif-stacked-dark.svg | 6.14 KB |
| lockup/lockup-serif-stacked-lapacho.svg | 6.14 KB |
| lockup/lockup-serif-stacked-light.svg | 6.14 KB |
| lockup/lockup-serif-stacked-on-green.svg | 6.14 KB |
| lockup/lockup-serif-stacked-white.svg | 6.14 KB |
| pattern/nanduti-pattern-cream-swatch.svg | 5.82 KB |
| pattern/nanduti-pattern-cream-tile.svg | 5.70 KB |
| pattern/nanduti-pattern-yerba-swatch.svg | 5.82 KB |
| pattern/nanduti-pattern-yerba-tile.svg | 5.70 KB |
| samples/skool-cover-1084x576.svg | 37.94 KB |
| symbol/lapacho-symbol-black.svg | 0.58 KB |
| symbol/lapacho-symbol-dark.svg | 0.58 KB |
| symbol/lapacho-symbol-lapacho.svg | 0.58 KB |
| symbol/lapacho-symbol-light.svg | 0.58 KB |
| symbol/lapacho-symbol-on-green.svg | 0.58 KB |
| symbol/lapacho-symbol-white.svg | 0.58 KB |

## All files (excluding `src/`)
- `build-report.json`
- `contact-sheet.png`
- `avatar/avatar-cream-on-black-32.png`
- `avatar/avatar-cream-on-black-48.png`
- `avatar/avatar-cream-on-black-skool-512.png`
- `avatar/avatar-cream-on-black-small-master.svg`
- `avatar/avatar-cream-on-black-x-400.png`
- `avatar/avatar-cream-on-black.svg`
- `avatar/avatar-cream-on-pink-32.png`
- `avatar/avatar-cream-on-pink-48.png`
- `avatar/avatar-cream-on-pink-skool-512.png`
- `avatar/avatar-cream-on-pink-small-master.svg`
- `avatar/avatar-cream-on-pink-x-400.png`
- `avatar/avatar-cream-on-pink.svg`
- `avatar/avatar-pink-on-yerba-32.png`
- `avatar/avatar-pink-on-yerba-48.png`
- `avatar/avatar-pink-on-yerba-skool-512.png`
- `avatar/avatar-pink-on-yerba-small-master.svg`
- `avatar/avatar-pink-on-yerba-x-400.png`
- `avatar/avatar-pink-on-yerba.svg`
- `favicon/apple-touch-icon-180.png`
- `favicon/apple-touch-icon-180.svg`
- `favicon/favicon-dark.ico`
- `favicon/favicon.ico`
- `favicon/favicon.svg`
- `favicon/lapacho-16-black.png`
- `favicon/lapacho-16-dark.png`
- `favicon/lapacho-16-light.png`
- `favicon/lapacho-16-master-black.svg`
- `favicon/lapacho-16-master-dark.svg`
- `favicon/lapacho-16-master-light.svg`
- `favicon/lapacho-16-master-white.svg`
- `favicon/lapacho-16-white.png`
- `favicon/lapacho-32-black.png`
- `favicon/lapacho-32-dark.png`
- `favicon/lapacho-32-light.png`
- `favicon/lapacho-32-master-black.svg`
- `favicon/lapacho-32-master-dark.svg`
- `favicon/lapacho-32-master-light.svg`
- `favicon/lapacho-32-master-white.svg`
- `favicon/lapacho-32-white.png`
- `lockup/lockup-caps-horizontal-black.png`
- `lockup/lockup-caps-horizontal-black.svg`
- `lockup/lockup-caps-horizontal-dark.png`
- `lockup/lockup-caps-horizontal-dark.svg`
- `lockup/lockup-caps-horizontal-lapacho.png`
- `lockup/lockup-caps-horizontal-lapacho.svg`
- `lockup/lockup-caps-horizontal-light.png`
- `lockup/lockup-caps-horizontal-light.svg`
- `lockup/lockup-caps-horizontal-on-green.png`
- `lockup/lockup-caps-horizontal-on-green.svg`
- `lockup/lockup-caps-horizontal-white.png`
- `lockup/lockup-caps-horizontal-white.svg`
- `lockup/lockup-caps-stacked-black.png`
- `lockup/lockup-caps-stacked-black.svg`
- `lockup/lockup-caps-stacked-dark.png`
- `lockup/lockup-caps-stacked-dark.svg`
- `lockup/lockup-caps-stacked-lapacho.png`
- `lockup/lockup-caps-stacked-lapacho.svg`
- `lockup/lockup-caps-stacked-light.png`
- `lockup/lockup-caps-stacked-light.svg`
- `lockup/lockup-caps-stacked-on-green.png`
- `lockup/lockup-caps-stacked-on-green.svg`
- `lockup/lockup-caps-stacked-white.png`
- `lockup/lockup-caps-stacked-white.svg`
- `lockup/lockup-serif-horizontal-black.png`
- `lockup/lockup-serif-horizontal-black.svg`
- `lockup/lockup-serif-horizontal-dark.png`
- `lockup/lockup-serif-horizontal-dark.svg`
- `lockup/lockup-serif-horizontal-lapacho.png`
- `lockup/lockup-serif-horizontal-lapacho.svg`
- `lockup/lockup-serif-horizontal-light.png`
- `lockup/lockup-serif-horizontal-light.svg`
- `lockup/lockup-serif-horizontal-on-green.png`
- `lockup/lockup-serif-horizontal-on-green.svg`
- `lockup/lockup-serif-horizontal-white.png`
- `lockup/lockup-serif-horizontal-white.svg`
- `lockup/lockup-serif-stacked-black.png`
- `lockup/lockup-serif-stacked-black.svg`
- `lockup/lockup-serif-stacked-dark.png`
- `lockup/lockup-serif-stacked-dark.svg`
- `lockup/lockup-serif-stacked-lapacho.png`
- `lockup/lockup-serif-stacked-lapacho.svg`
- `lockup/lockup-serif-stacked-light.png`
- `lockup/lockup-serif-stacked-light.svg`
- `lockup/lockup-serif-stacked-on-green.png`
- `lockup/lockup-serif-stacked-on-green.svg`
- `lockup/lockup-serif-stacked-white.png`
- `lockup/lockup-serif-stacked-white.svg`
- `pattern/nanduti-pattern-cream-swatch-1600x900.png`
- `pattern/nanduti-pattern-cream-swatch.svg`
- `pattern/nanduti-pattern-cream-tile-480.png`
- `pattern/nanduti-pattern-cream-tile.svg`
- `pattern/nanduti-pattern-yerba-swatch-1600x900.png`
- `pattern/nanduti-pattern-yerba-swatch.svg`
- `pattern/nanduti-pattern-yerba-tile-480.png`
- `pattern/nanduti-pattern-yerba-tile.svg`
- `samples/skool-cover-1084x576.png`
- `samples/skool-cover-1084x576.svg`
- `symbol/lapacho-symbol-black-1024.png`
- `symbol/lapacho-symbol-black-512.png`
- `symbol/lapacho-symbol-black.svg`
- `symbol/lapacho-symbol-dark-1024.png`
- `symbol/lapacho-symbol-dark-512.png`
- `symbol/lapacho-symbol-dark.svg`
- `symbol/lapacho-symbol-lapacho-1024.png`
- `symbol/lapacho-symbol-lapacho-512.png`
- `symbol/lapacho-symbol-lapacho.svg`
- `symbol/lapacho-symbol-light-1024.png`
- `symbol/lapacho-symbol-light-512.png`
- `symbol/lapacho-symbol-light.svg`
- `symbol/lapacho-symbol-on-green-1024.png`
- `symbol/lapacho-symbol-on-green-512.png`
- `symbol/lapacho-symbol-on-green.svg`
- `symbol/lapacho-symbol-white-1024.png`
- `symbol/lapacho-symbol-white-512.png`
- `symbol/lapacho-symbol-white.svg`
- `../logo-compare-2026-11-06.png` (comparison)

Source: `src/` (mark.py geometry, build.py lockups/avatars/pattern, run.py exports, sheet.py contact sheet, compare.py comparison).
