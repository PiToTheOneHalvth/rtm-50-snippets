"""
07 — Recolor a Square
=====================
What this does:
    A square cycles through three fill colors: red -> gold -> teal.

Key ideas:
    - .animate.set_fill(color, opacity) smoothly interpolates the fill.
    - Successive play() calls run one after another — a simple timeline.

Try changing:
    - The colors (any name like BLUE, PINK, GREY or a hex "#FF8800").
    - .set_fill -> .set_stroke to recolor the outline instead.

Run:     python snippets/07_recolor_square.py
Output:  outputs/07_recolor_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class RecolorSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(RED, 0.7).set_stroke(WHITE, 3)
        self.add(square)

        win.play(square.animate.set_fill(GOLD, 0.7), run_time=0.8)
        win.play(square.animate.set_fill(TEAL, 0.7), run_time=0.8)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(RecolorSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
