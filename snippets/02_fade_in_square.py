"""
02 — Fade a Square In
=====================
What this does:
    A filled square fades in from nothing while drifting down slightly.

Key ideas:
    - FadeIn() ramps opacity from 0 to the mobject's authored value.
    - The optional shift= makes the square slide in from an offset while fading.

Try changing:
    - shift=UP*0.5 -> shift=LEFT*2.0 (slide in from the left).
    - scale=0.3 inside FadeIn to also grow while fading.

Run:     python snippets/02_fade_in_square.py
Output:  outputs/02_fade_in_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class FadeInSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(TEAL, 0.6).set_stroke(WHITE, 3)

        # Not self.add() first: FadeIn *introduces* the mobject itself.
        win.play(FadeIn(square, shift=UP * 0.5), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(FadeInSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
