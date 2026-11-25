"""
18 — Axes and a Parabola
========================
What this does:
    Coordinate axes appear with a parabola y = 0.3x² drawn on them.

Key ideas:
    - Axes(x_range, y_range, x_length, y_length) builds the frame with
      tick numbers.
    - axes.plot(function, color=...) returns the graph as one mobject —
      animate it with Create() like any other shape.
    - self.add() puts the axes on stage instantly; only the curve animates.

Try changing:
    - The function: lambda x: np.sin(x) (need `import numpy as np`).
    - The ranges: x_range=[-5, 5] for a wider view.

Run:     python snippets/18_axes_parabola.py
Output:  outputs/18_axes_parabola.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class AxesParabola(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        axes = Axes(x_range=[-3, 3], y_range=[-1, 3], x_length=7, y_length=5)
        graph = axes.plot(lambda x: 0.3 * x**2, color=YELLOW)

        self.add(axes)                      # axes appear instantly...
        win.play(Create(graph), run_time=3.0)  # ...then the curve draws itself
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(AxesParabola, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
