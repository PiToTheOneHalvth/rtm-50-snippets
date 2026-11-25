"""
24 — A Decimal Readout
======================
What this does:
    A corner readout tweens from 0.0000 to 3.1416 — pi to four decimals.

Key ideas:
    - DecimalNumber(0, num_decimal_places=4) renders a fixed-precision
      number with a system font (no LaTeX needed).
    - The updater pattern is the same as the integer counter: the
      ValueTracker owns the number, the label just displays it.
    - Separating state (tracker) from display (label) is the manim idiom.

Try changing:
    - 3.14159 -> 2.71828 (e), or a number of your own.
    - num_decimal_places=4 -> 8 for more digits.

Run:     python snippets/24_decimal_readout.py
Output:  outputs/24_decimal_readout.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class DecimalReadout(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        tracker = ValueTracker(0)
        readout = DecimalNumber(0, num_decimal_places=4).scale(1.5).to_corner(UL, buff=0.6)

        readout.add_updater(lambda m: m.set_value(tracker.get_value()))

        self.add(readout)
        win.play(tracker.animate.set_value(3.14159), run_time=3.0)  # tween to pi
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(DecimalReadout, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
