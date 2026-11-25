"""
40 — Blink Three Times
======================
What this does:
    A square vanishes and reappears three times, on a fixed rhythm.

Key ideas:
    - Blink(mobject, blinks=3) toggles visibility: on/off, on/off, on/off.
    - time_on=0.5 and time_off=0.5 set the rhythm (defaults here).
    - The square ends visible because hide_at_end defaults to False.

Try changing:
    - blinks=3 -> blinks=6, or time_off=0.5 -> 0.2 (frantic).
    - hide_at_end=True to leave it invisible.

Run:     python snippets/40_blink_square.py
Output:  outputs/40_blink_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class BlinkSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(GOLD, 0.6).set_stroke(WHITE, 3)
        self.add(square)

        win.play(Blink(square, blinks=3), run_time=3.0)  # 3 x (0.5 on + 0.5 off)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(BlinkSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
