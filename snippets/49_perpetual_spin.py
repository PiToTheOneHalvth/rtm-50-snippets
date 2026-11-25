"""
49 — A Perpetual Spin
=====================
What this does:
    A square spins a full turn, forever — well, for three seconds.

Key ideas:
    - Rotating(mobject, angle=TAU) is the looping cousin of Rotate():
      it keeps turning at a constant angular speed for the whole play.
    - Rotate() would ease in and out; Rotating() is a steady motor.
    - Perfect for wheels, fans, and loading spinners.

Try changing:
    - run_time=3.0 -> 10.0 for a long spin.
    - angle=2*TAU for twice the rpm, or about_point to change the axle.

Run:     python snippets/49_perpetual_spin.py
Output:  outputs/49_perpetual_spin.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class PerpetualSpin(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(PURPLE, 0.6).set_stroke(WHITE, 3)
        self.add(square)

        win.play(Rotating(square, angle=TAU), run_time=3.0)  # one steady turn
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(PerpetualSpin, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
