"""
43 — Grow from a Point
======================
What this does:
    A square grows out of a single point at the bottom-left of the screen.

Key ideas:
    - GrowFromPoint(mobject, point=...) anchors the growth at ANY point
      you choose, not just the shape's own edges.
    - Here the anchor is DOWN + LEFT (one unit down and left from center).
    - The square inflates away from that corner like a thought balloon.

Try changing:
    - point=DOWN+LEFT -> point=UP*2 (grow from above the square).
    - Combine with a Dot at the anchor to show where growth starts.

Run:     python snippets/43_grow_from_point.py
Output:  outputs/43_grow_from_point.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class GrowFromPointDemo(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(PINK, 0.6).set_stroke(WHITE, 3)

        # Anchor the growth at an arbitrary point off to the side.
        win.play(GrowFromPoint(square, point=DOWN + LEFT), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(GrowFromPointDemo, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
