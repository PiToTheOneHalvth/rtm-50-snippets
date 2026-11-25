"""
38 — Point at the Square
========================
What this does:
    A square sits on stage, then pulses once with a bright ring around it.

Key ideas:
    - Indicate(mobject, scale_factor, color) draws attention: the mobject
      swells by scale_factor while a colored echo of it fades out.
    - The square itself is not changed afterwards — Indicate is a
      spotlight, not a transform.
    - Use it for "this is the thing we're talking about" moments.

Try changing:
    - scale_factor=1.3 -> 2.0 (an aggressive pulse).
    - color=WHITE -> color=RED for an alarm-style flash.

Run:     python snippets/38_indicate_square.py
Output:  outputs/38_indicate_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class IndicateSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(BLUE, 0.6).set_stroke(WHITE, 3)
        self.add(square)

        win.play(Indicate(square, scale_factor=1.3), run_time=2.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(IndicateSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
