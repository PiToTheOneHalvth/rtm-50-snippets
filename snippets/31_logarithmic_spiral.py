"""
31 — A Logarithmic Spiral
=========================
What this does:
    A golden spiral is drawn: the radius grows exponentially with the angle.

Key ideas:
    - ParametricFunction(f, t_range) samples f(t) for many t values and
      connects them into a curve — you describe shapes by equations.
    - Here x = 0.18·t·cos(t), y = 0.18·t·sin(t) for t in [0, 6π]:
      three turns, each turn further from the center.
    - Create() traces the curve exactly like it traces a square.

Try changing:
    - 0.18*t -> 0.05*t (a tight spiral).
    - t_range=[0, 6*PI] -> [0, 12*PI] (six turns).

Run:     python snippets/31_logarithmic_spiral.py
Output:  outputs/31_logarithmic_spiral.mp4
"""
import os

import numpy as np

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class LogarithmicSpiral(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        spiral = ParametricFunction(
            lambda t: [0.18 * t * np.cos(t), 0.18 * t * np.sin(t), 0],
            t_range=[0, 6 * PI],
        ).set_stroke(GOLD, 3)

        win.play(Create(spiral), run_time=4.0)  # draw the whole curve
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(LogarithmicSpiral, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
