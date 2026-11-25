"""
47 — An Arc Between Two Dots
============================
What this does:
    Two dots appear, then a curved arc bridges the gap between them.

Key ideas:
    - ArcBetweenPoints(point_a, point_b) draws the (upward-bowing) arc
      that connects exactly those two points.
    - Dot(point=...) places a dot at any coordinate.
    - You don't compute angles yourself — the mobject does the geometry.

Try changing:
    - The dot positions (further apart = a taller arc).
    - Add .set_color(RED) to the arc, or angle=-PI/2 to bow it downward.

Run:     python snippets/47_arc_between_points.py
Output:  outputs/47_arc_between_points.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class ArcBetweenPointsDemo(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        a = Dot(point=LEFT * 2.5).set_color(YELLOW)
        b = Dot(point=RIGHT * 2.5).set_color(YELLOW)
        arc = ArcBetweenPoints(a.get_center(), b.get_center()).set_stroke(TEAL, 4)

        self.add(a, b)
        win.play(Create(arc), run_time=1.5)  # bridge the two dots
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(ArcBetweenPointsDemo, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
