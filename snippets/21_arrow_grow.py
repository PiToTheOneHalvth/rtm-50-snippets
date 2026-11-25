"""
21 — Grow an Arrow
==================
What this does:
    An arrow grows out of its tail point, like it's being shot.

Key ideas:
    - Arrow(start, end) builds an arrow between two points.
    - GrowArrow() stretches the arrow from its start point to full length,
      including the tip.
    - The arrow head is part of the same mobject, not a separate shape.

Try changing:
    - The endpoints: Arrow(UP * 2, DOWN * 2) for a vertical arrow.
    - Add .set_color(RED) and .set_stroke(width=8) for a bold red arrow.

Run:     python snippets/21_arrow_grow.py
Output:  outputs/21_arrow_grow.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class ArrowGrow(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        arrow = Arrow(LEFT * 3, RIGHT * 3).set_color(YELLOW)

        win.play(GrowArrow(arrow), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(ArrowGrow, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
