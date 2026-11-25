"""
42 — Grow from an Edge
======================
What this does:
    A square grows out of its left edge, expanding to the right.

Key ideas:
    - GrowFromEdge(mobject, edge=LEFT) anchors the LEFT side and grows
      away from it — like a bar chart filling up.
    - Any edge works: UP, DOWN, LEFT, RIGHT (and diagonal combos).
    - Same animation family as GrowFromCenter, different anchor.

Try changing:
    - edge=LEFT -> edge=DOWN (grows upward, like a tower).
    - The shape to a Rectangle for a proper bar.

Run:     python snippets/42_grow_from_edge.py
Output:  outputs/42_grow_from_edge.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class GrowFromEdgeDemo(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(ORANGE, 0.6).set_stroke(WHITE, 3)

        win.play(GrowFromEdge(square, edge=LEFT), run_time=1.5)  # anchored left
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(GrowFromEdgeDemo, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
