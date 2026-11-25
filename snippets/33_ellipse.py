"""
33 — An Ellipse
===============
What this does:
    A purple ellipse — a stretched circle — is drawn on screen.

Key ideas:
    - Ellipse(width=5, height=2.5) is a circle squashed in one direction.
    - width and height are the full extents, not the radii.
    - It's the same point-interpolation machinery as Circle, so every
      animation (morphs, rotations) applies to it unchanged.

Try changing:
    - width=5, height=2.5 -> width=7, height=1 (a very flat pancake).
    - Rotate it with .animate.rotate(PI/3).

Run:     python snippets/33_ellipse.py
Output:  outputs/33_ellipse.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class EllipseDemo(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        ellipse = Ellipse(width=5.0, height=2.5).set_fill(PURPLE, 0.5).set_stroke(WHITE, 2)

        win.play(Create(ellipse), run_time=2.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(EllipseDemo, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
