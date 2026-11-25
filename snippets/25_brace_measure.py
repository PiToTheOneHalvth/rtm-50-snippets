"""
25 — Measure a Row with a Brace
===============================
What this does:
    Three squares line up and a brace appears underneath, labeled
    "3 squares wide".

Key ideas:
    - Brace(group, direction) stretches to span the group's bounding box.
    - .next_to(brace, DOWN, buff=0.15) places a label just below the brace.
    - FadeIn can introduce several mobjects at once: FadeIn(brace, label).

Try changing:
    - direction=DOWN -> direction=UP for an over-brace.
    - The label text, or the number of squares.

Run:     python snippets/25_brace_measure.py
Output:  outputs/25_brace_measure.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class BraceMeasure(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        squares = VGroup(*[Square(side_length=1.0) for _ in range(3)])
        squares.arrange(RIGHT, buff=0.5).set_fill(BLUE, 0.6).set_stroke(WHITE, 2)

        brace = Brace(squares, direction=DOWN)
        label = Text("3 squares wide", font_size=36).next_to(brace, DOWN, buff=0.15)

        self.add(squares)
        win.play(FadeIn(brace, label), run_time=1.5)  # brace + label together
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(BraceMeasure, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
