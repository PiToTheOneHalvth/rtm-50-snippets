"""
03 — Draw a Square
==================
What this does:
    The outline of a square is traced out stroke by stroke, like a pen.

Key ideas:
    - Create() draws the stroke progressively along its length (no fade).
    - For closed shapes it starts at one vertex and works around the outline.

Try changing:
    - run_time=2.0 -> 0.5 for a fast snap.
    - Remove the fill so you can watch the pure outline being drawn.

Run:     python snippets/03_draw_square.py
Output:  outputs/03_draw_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class DrawSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=3.0).set_stroke(YELLOW, 6)

        win.play(Create(square), run_time=2.0)  # trace the outline
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(DrawSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
