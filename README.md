# RTM — 50 Snippets

50 tiny, self-contained [**real-time-manim**](https://github.com/axioviva/real-time-manim) scenes.
Each file is one idea, ~35 lines, fully commented, and renders a short MP4 on its own —
no project structure, no shared helpers, nothing to configure. Open any file, read the
header, change one number, run it.

> **real-time-manim (RTM)** is a Vulkan-accelerated renderer that drives the ManimCE
> object/animation model. One `import real_time_manim` gives you the whole ManimCE
> namespace (shapes, colors, text, math, axes) *plus* the real-time window and a fast
> offline MP4 recorder. It is a library, not a CLI — you write a `Scene`, then record it
> with `fast_record_scene`. Every render is **1920×1080 @ 60 fps**.

## Setup (macOS)

```bash
brew install molten-vk ffmpeg           # Vulkan driver + encoder (ffmpeg must be on PATH)
python3.12 -m venv .venv && source .venv/bin/activate
pip install "real-time-manim[typst]"    # [typst] makes MathTex render without a LaTeX install
```

Linux: a working Vulkan driver + `ffmpeg`. Windows: the wheel ships the Vulkan runtime;
install ffmpeg and put it on `PATH`.

## Run one snippet

```bash
python snippets/01_square_to_circle.py     # -> outputs/01_square_to_circle.mp4
```

Every snippet writes its MP4 into `outputs/`. Want the window **visible** while it plays?
Swap the last line's `fast_record_scene` for `record_scene` (same signature, same import) —
the scene then renders to a real window at wall-clock speed. There is no `manim` CLI and
`Scene.render()` is never called; `fast_record_scene` / `record_scene` are the two entry points.

## Run them all

```bash
python render_all.py            # all 50, reports failures
python render_all.py 01 05 18   # just those three
```

~3 minutes for the whole set at 60 fps.

## The shape of every snippet

```python
class SquareToCircle(Scene):            # 1. one Scene class
    def construct(self):
        win = MLWindow(1920, 1080)      # 2. open the Vulkan window
        win.scene = self                # 3. bind it (REQUIRED)
        square = Square(...)
        win.play(Transform(square, circle), run_time=2.0)   # 4. animate
        win.close()                     # 5. flush + finish the MP4 (REQUIRED)
```

The two rules that bite beginners: **`win.scene = self` before any `play()`**, and
**`win.close()` at the end** — without it nothing is written.

## The 50 snippets

| # | File | What it does | Key API |
|---|------|--------------|---------|
| 01 | [square_to_circle.py](snippets/01_square_to_circle.py) | Square morphs into a circle | `Transform` |
| 02 | [fade_in_square.py](snippets/02_fade_in_square.py) | Square fades in while drifting down | `FadeIn(shift=)` |
| 03 | [draw_square.py](snippets/03_draw_square.py) | Square outline traced like a pen | `Create` |
| 04 | [rotate_square.py](snippets/04_rotate_square.py) | Quarter turn about its center | `Rotate(angle=PI/2)` |
| 05 | [scale_square.py](snippets/05_scale_square.py) | Doubles in size | `.animate.scale` |
| 06 | [slide_square.py](snippets/06_slide_square.py) | Glides to the right | `.animate.shift` |
| 07 | [recolor_square.py](snippets/07_recolor_square.py) | Cycles red → gold → teal | `.animate.set_fill` |
| 08 | [square_to_triangle.py](snippets/08_square_to_triangle.py) | 4 points morph into 3 | `Polygon` + `Transform` |
| 09 | [filled_circle.py](snippets/09_filled_circle.py) | Translucent filled disk | `set_fill(color, opacity)` |
| 10 | [staggered_row.py](snippets/10_staggered_row.py) | Eight squares pop in as a wave | `VGroup` + `LaggedStart` |
| 11 | [story_sequence.py](snippets/11_story_sequence.py) | Draw → rotate → fade in one play | `Succession` |
| 12 | [grid_of_squares.py](snippets/12_grid_of_squares.py) | 4×4 grid drawn as one object | `arrange_in_grid` |
| 13 | [hello_text.py](snippets/13_hello_text.py) | Big "Hello, RTM!" fades in | `Text` + `FadeIn` |
| 14 | [typewriter_text.py](snippets/14_typewriter_text.py) | Sentence written stroke by stroke | `Write` |
| 15 | [recolor_text.py](snippets/15_recolor_text.py) | Word changes color twice | `.animate.set_color` |
| 16 | [pythagoras_tex.py](snippets/16_pythagoras_tex.py) | a² + b² = c², typeset by Typst | `MathTex` |
| 17 | [expand_binomial.py](snippets/17_expand_binomial.py) | (a+b)² dissolves into its expansion | `FadeTransform` |
| 18 | [axes_parabola.py](snippets/18_axes_parabola.py) | Axes appear, parabola draws itself | `Axes.plot` + `Create` |
| 19 | [straight_line.py](snippets/19_straight_line.py) | Thick yellow line | `Line` + `set_stroke` |
| 20 | [dashed_line.py](snippets/20_dashed_line.py) | Dashed line across the frame | `DashedLine` |
| 21 | [arrow_grow.py](snippets/21_arrow_grow.py) | Arrow shoots out of its tail | `GrowArrow` |
| 22 | [dot_ride.py](snippets/22_dot_ride.py) | Dot travels a full circle | `MoveAlongPath` |
| 23 | [count_to_100.py](snippets/23_count_to_100.py) | Live counter 0 → 100 | `ValueTracker` + updater |
| 24 | [decimal_readout.py](snippets/24_decimal_readout.py) | Tweens to π = 3.1416 | `DecimalNumber` |
| 25 | [brace_measure.py](snippets/25_brace_measure.py) | Brace + label under a row | `Brace` + `next_to` |
| 26 | [draw_arc.py](snippets/26_draw_arc.py) | 300° arc traced out | `Arc` + `Create` |
| 27 | [triangle_pentagon.py](snippets/27_triangle_pentagon.py) | 3-gon → 5-gon → back | vertices from cos/sin |
| 28 | [annulus_ring.py](snippets/28_annulus_ring.py) | Ring with a real hole | `Annulus` |
| 29 | [arrange_grid.py](snippets/29_arrange_grid.py) | Row of shapes glides into a 3×3 grid | `.animate.arrange_in_grid` |
| 30 | [spin_and_zoom.py](snippets/30_spin_and_zoom.py) | Grow + rotate in one motion | chained `.animate` |
| 31 | [logarithmic_spiral.py](snippets/31_logarithmic_spiral.py) | Spiral from an equation | `ParametricFunction` |
| 32 | [shining_star.py](snippets/32_shining_star.py) | Gold star, then a pulse | `Star` + `Indicate` |
| 33 | [ellipse.py](snippets/33_ellipse.py) | Squashed circle | `Ellipse` |
| 34 | [rounded_rectangle.py](snippets/34_rounded_rectangle.py) | Card grows from its center | `RoundedRectangle` + `GrowFromCenter` |
| 35 | [sine_wave.py](snippets/35_sine_wave.py) | Sine curve traced across the frame | `ParametricFunction` |
| 36 | [unit_circle_ride.py](snippets/36_unit_circle_ride.py) | Radius hand sweeps one turn | `Rotate(about_point=)` |
| 37 | [recolor_matrix.py](snippets/37_recolor_matrix.py) | 3×3 grid lights up square by square | loop of plays |
| 38 | [indicate_square.py](snippets/38_indicate_square.py) | Attention pulse around a square | `Indicate` |
| 39 | [passing_flash.py](snippets/39_passing_flash.py) | Light band sweeps across | `ShowPassingFlash` |
| 40 | [blink_square.py](snippets/40_blink_square.py) | Three on/off blinks | `Blink` |
| 41 | [grow_from_center.py](snippets/41_grow_from_center.py) | Inflates from its center | `GrowFromCenter` |
| 42 | [grow_from_edge.py](snippets/42_grow_from_edge.py) | Bar-chart growth from the left | `GrowFromEdge` |
| 43 | [grow_from_point.py](snippets/43_grow_from_point.py) | Grows from an arbitrary anchor | `GrowFromPoint` |
| 44 | [uncreate_square.py](snippets/44_uncreate_square.py) | Outline erased backwards | `Uncreate` |
| 45 | [breathing_circle.py](snippets/45_breathing_circle.py) | Radius oscillates via an updater | updaters + `become` |
| 46 | [orbiting_square.py](snippets/46_orbiting_square.py) | Square orbits the screen center | `Rotate` + `about_point` |
| 47 | [arc_between_points.py](snippets/47_arc_between_points.py) | Curved arc bridges two dots | `ArcBetweenPoints` |
| 48 | [tex_piece_morph.py](snippets/48_tex_piece_morph.py) | a + b swaps into b + a, piece by piece | `FadeTransformPieces` |
| 49 | [perpetual_spin.py](snippets/49_perpetual_spin.py) | Steady full-turn spin | `Rotating` |
| 50 | [grand_finale.py](snippets/50_grand_finale.py) | One square dissolves into four + closing text | `FadeOut`/`FadeIn` swap |

## License

MIT — see [LICENSE](LICENSE).
