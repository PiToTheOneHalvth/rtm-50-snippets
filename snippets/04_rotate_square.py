"""
04 — Rotate a Square 90°
========================
What this does:
    A square turns a quarter of a turn (PI/2 radians = 90°) about its center.

Key ideas:
    - Rotate() spins a mobject about its own center by default.
    - Angles are in radians: PI/2 = 90°, PI = 180°, TAU = a full turn.

Try changing:
    - angle=PI/2 -> angle=TAU (one full turn).
    - Add about_point=ORIGIN to spin it around the screen center instead.

Run:     python snippets/04_rotate_square.py
Output:  outputs/04_rotate_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class RotateSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(PURPLE, 0.6).set_stroke(WHITE, 3)
        self.add(square)

        win.play(Rotate(square, angle=PI / 2), run_time=1.5)  # 90 degrees
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(RotateSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
