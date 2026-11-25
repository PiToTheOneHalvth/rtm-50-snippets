"""
22 — Ride the Circle
====================
What this does:
    A yellow dot travels all the way around a grey circle.

Key ideas:
    - MoveAlongPath(mobject, path) makes the mobject follow the path's
      points from start to finish.
    - The path is just a normal Circle with no fill — it stays on screen.
    - The dot and the path are separate mobjects, so they animate separately.

Try changing:
    - The path to a Line, a Square, or a ParametricFunction curve.
    - run_time=4.0 -> 1.0 for a fast lap.

Run:     python snippets/22_dot_ride.py
Output:  outputs/22_dot_ride.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class DotRide(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        path = Circle(radius=2.5).set_stroke(GREY, 3)
        dot = Dot(radius=0.15).set_color(YELLOW)

        self.add(path, dot)                       # path and dot on stage
        win.play(MoveAlongPath(dot, path), run_time=4.0)  # one lap
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(DotRide, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
