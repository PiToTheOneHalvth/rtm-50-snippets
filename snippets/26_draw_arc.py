"""
26 — Draw an Arc
================
What this does:
    A 300° arc is traced out around the center of the screen.

Key ideas:
    - Arc(radius, start_angle, angle) spans from start_angle for angle
      radians, measured counterclockwise from the positive x-axis.
    - 5*PI/3 radians = 300°, so the arc is five-sixths of a full circle.
    - The arc is one mobject: a partial circle outline.

Try changing:
    - angle=5*PI/3 -> PI/2 (a quarter circle).
    - radius=2.0 -> 3.0, or color it with set_color(GREEN).

Run:     python snippets/26_draw_arc.py
Output:  outputs/26_draw_arc.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class DrawArc(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        arc = Arc(radius=2.0, start_angle=0, angle=5 * PI / 3).set_stroke(YELLOW, 6)

        win.play(Create(arc), run_time=2.0)  # trace 300 degrees
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(DrawArc, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
