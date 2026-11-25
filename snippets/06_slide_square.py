"""
06 — Slide a Square
===================
What this does:
    A square glides from the center of the screen to the right edge.

Key ideas:
    - .shift(vector) adds the vector to every point of the mobject.
    - RIGHT, LEFT, UP, DOWN are unit vectors; multiplying scales the distance
      (RIGHT * 4 = four units to the right).

Try changing:
    - RIGHT*4 -> UP*2.5 + RIGHT*2 (diagonal).
    - .shift -> .move_to(RIGHT*4) (jump instantly instead of animating).

Run:     python snippets/06_slide_square.py
Output:  outputs/06_slide_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class SlideSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=1.5).set_fill(MAROON, 0.6).set_stroke(WHITE, 3)
        self.add(square)

        win.play(square.animate.shift(RIGHT * 4), run_time=1.5)  # glide right
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(SlideSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
