"""
39 — A Passing Flash
====================
What this does:
    A band of light sweeps across a square, left to right.

Key ideas:
    - ShowPassingFlash(mobject, time_width=0.2) highlights a moving slice
      of the mobject, like light sweeping over it.
    - time_width controls how wide the lit band is (as a fraction of the
      whole animation time).
    - The square itself never changes — the flash is a separate effect.

Try changing:
    - time_width=0.2 -> 0.5 (a wider beam).
    - Use it on Text or MathTex for a "scan" effect.

Run:     python snippets/39_passing_flash.py
Output:  outputs/39_passing_flash.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class PassingFlash(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(BLUE, 0.6).set_stroke(WHITE, 3)
        self.add(square)

        win.play(ShowPassingFlash(square, time_width=0.2), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(PassingFlash, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
