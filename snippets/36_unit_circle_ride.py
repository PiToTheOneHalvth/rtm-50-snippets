"""
36 — Ride the Unit Circle
=========================
What this does:
    A radius line with a dot at its end sweeps one full turn around a circle.

Key ideas:
    - The line and dot are grouped (VGroup), so one Rotate() moves both.
    - about_point=ORIGIN overrides the default pivot (the group's own
      center) and pins the rotation to the screen center.
    - TAU radians = one full turn.

Try changing:
    - angle=TAU -> angle=PI/2 (stop at the top).
    - about_point=ORIGIN -> about_point=UP (pivot above the circle).

Run:     python snippets/36_unit_circle_ride.py
Output:  outputs/36_unit_circle_ride.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class UnitCircleRide(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        circle = Circle(radius=1.8).set_stroke(GREY, 3)
        radius = Line(ORIGIN, RIGHT * 1.8).set_stroke(YELLOW, 5)
        tip = Dot(point=RIGHT * 1.8).set_color(GOLD)
        hand = VGroup(radius, tip)  # one mobject: line + dot move together

        self.add(circle, hand)
        # One full sweep about the center of the screen.
        win.play(Rotate(hand, angle=TAU, about_point=ORIGIN), run_time=4.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(UnitCircleRide, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
