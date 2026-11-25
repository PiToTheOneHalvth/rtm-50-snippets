"""
35 — A Sine Wave
================
What this does:
    A sine curve is traced across the screen, left to right.

Key ideas:
    - ParametricFunction with f(t) = (t, sin(t)) turns the classic
      function graph into a curve mobject.
    - t_range=[-4, 4] gives a little more than one full period (2π ≈ 6.28).
    - Create() draws it exactly like a line — a curve is just points.

Try changing:
    - np.sin(t) -> np.cos(t) (shifted a quarter period).
    - 2*np.sin(0.5*t) for double amplitude, half frequency.

Run:     python snippets/35_sine_wave.py
Output:  outputs/35_sine_wave.mp4
"""
import os

import numpy as np

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class SineWave(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        wave = ParametricFunction(
            lambda t: [t, np.sin(t), 0],
            t_range=[-4, 4],
        ).set_stroke(TEAL, 4)

        win.play(Create(wave), run_time=3.0)  # trace the curve
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(SineWave, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
