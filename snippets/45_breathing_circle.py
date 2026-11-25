"""
45 — A Breathing Circle
=======================
What this does:
    A circle inhales and exhales: its radius oscillates ±20% four times.

Key ideas:
    - An updater receives (mobject, dt) every frame while a play runs;
      dt is the seconds since the previous frame.
    - phase += 2*PI*dt advances exactly one cycle per second.
    - m.become(new_circle) rebuilds the geometry each frame — the radius
      is set absolutely (1.5 * (1 + 0.2*sin(phase))), so nothing drifts.
    - win.play(Wait(4.0)) keeps the clock running so the updater can work.

Try changing:
    - 0.2 -> 0.5 (deep breaths), 2*PI*dt -> 4*PI*dt (twice the tempo).
    - Rebuild with a different color inside become() to cycle colors too.

Run:     python snippets/45_breathing_circle.py
Output:  outputs/45_breathing_circle.mp4
"""
import os

import numpy as np

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class BreathingCircle(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        circle = Circle(radius=1.5).set_stroke(TEAL, 6)
        phase = [0.0]  # mutable box so the updater can accumulate time

        def breathe(m, dt):
            phase[0] += 2 * np.pi * dt                      # one cycle per second
            r = 1.5 * (1 + 0.2 * np.sin(phase[0]))          # 1.2 .. 1.8
            m.become(Circle(radius=r).set_stroke(TEAL, 6))  # rebuild the ring

        self.add(circle)
        circle.add_updater(breathe)
        win.play(Wait(4.0))  # the play keeps the updater clock running
        circle.clear_updaters()
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(BreathingCircle, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
