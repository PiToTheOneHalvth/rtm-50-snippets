"""
19 — A Straight Line
====================
What this does:
    A thick yellow line is drawn from the left edge to the right edge.

Key ideas:
    - Line(start, end) takes two points; LEFT and RIGHT are built-in
      points at the frame edges scaled to frame width, so multiplying
      them controls the length.
    - set_stroke(color, width) sets outline color and thickness.

Try changing:
    - The endpoints: Line(ORIGIN, UR) (center to the top-right corner).
    - Add a second line with a different color to cross it.

Run:     python snippets/19_straight_line.py
Output:  outputs/19_straight_line.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class StraightLine(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        line = Line(LEFT * 4, RIGHT * 4).set_stroke(YELLOW, 6)

        win.play(Create(line), run_time=1.5)  # draw left -> right
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(StraightLine, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
