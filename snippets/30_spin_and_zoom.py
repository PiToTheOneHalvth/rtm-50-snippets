"""
30 — Spin and Zoom
==================
What this does:
    A square grows by 50% and rotates 45° in one smooth motion.

Key ideas:
    - Chaining .animate builders does both at once:
      square.animate.scale(1.5).rotate(PI/4).
    - The builder records the *end state*; manim tweens every point there.
    - One play = one parallel timeline. Two motions, one clock.

Try changing:
    - PI/4 -> TAU/3 (120°), or add .shift(UP).
    - Remove .scale(1.5) to isolate the rotation.

Run:     python snippets/30_spin_and_zoom.py
Output:  outputs/30_spin_and_zoom.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class SpinAndZoom(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.0).set_fill(PURPLE, 0.6).set_stroke(WHITE, 3)
        self.add(square)

        # One play: grow by 50% and turn 45 degrees simultaneously.
        win.play(square.animate.scale(1.5).rotate(PI / 4), run_time=2.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(SpinAndZoom, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
