"""
41 — Grow from Center
=====================
What this does:
    A square expands out of its center point to full size.

Key ideas:
    - GrowFromCenter() scales the mobject from 0 at its center to 100%.
    - Compare with Create() (snippet 03): that one traces the outline,
      this one inflates the whole shape.
    - The growing square stays centered throughout.

Try changing:
    - The shape: a Circle, Star, or Text.
    - run_time=1.5 -> 3.0 for a slow inflate.

Run:     python snippets/41_grow_from_center.py
Output:  outputs/41_grow_from_center.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class GrowFromCenterDemo(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(GREEN, 0.6).set_stroke(WHITE, 3)

        win.play(GrowFromCenter(square), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(GrowFromCenterDemo, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
