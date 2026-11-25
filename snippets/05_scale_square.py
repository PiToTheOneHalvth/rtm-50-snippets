"""
05 — Scale a Square
===================
What this does:
    A square smoothly doubles in size, keeping its center fixed.

Key ideas:
    - mobject.animate.method(...) is a *builder*: it records the method call
      and plays it as a smooth animation between now and the target state.
    - .scale(2) multiplies all distances from the mobject's center by 2.

Try changing:
    - .scale(2) -> .scale(0.3) (shrink).
    - .scale([2, 1, 1]) to stretch only horizontally.

Run:     python snippets/05_scale_square.py
Output:  outputs/05_scale_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class ScaleSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=1.5).set_fill(GREEN, 0.6).set_stroke(WHITE, 3)
        self.add(square)

        win.play(square.animate.scale(2), run_time=1.5)  # double the size
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(ScaleSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
