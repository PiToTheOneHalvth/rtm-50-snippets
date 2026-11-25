"""
10 — A Staggered Row of Squares
===============================
What this does:
    Eight squares fade in one after another, left to right, like dominoes.

Key ideas:
    - VGroup(*squares) bundles mobjects into one container you can treat as one.
    - .arrange(RIGHT, buff=0.3) lines the children up with 0.3 units of gap.
    - LaggedStart(anim1, anim2, ..., lag_ratio=0.15) starts each animation a
      fraction of a second after the previous one.

Try changing:
    - lag_ratio=0.15 -> 0.5 (bigger gaps between starts).
    - FadeIn -> Create in the list comprehension for a drawing wave.

Run:     python snippets/10_staggered_row.py
Output:  outputs/10_staggered_row.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class StaggeredRow(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        squares = VGroup(*[Square(side_length=0.9) for _ in range(8)])
        squares.arrange(RIGHT, buff=0.3).set_fill(BLUE, 0.6).set_stroke(WHITE, 2)

        # One FadeIn per square, started with a small delay each.
        win.play(
            LaggedStart(*[FadeIn(sq) for sq in squares], lag_ratio=0.15),
            run_time=2.0,
        )
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(StaggeredRow, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
