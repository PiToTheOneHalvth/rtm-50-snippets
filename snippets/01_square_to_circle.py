"""
01 — Square to Circle Morph
===========================
What this does:
    A blue square smoothly morphs into a yellow circle.

Key ideas:
    - Transform() interpolates the points of one shape into the points of another.
    - Only ONE object is ever on stage: the square *becomes* the circle.

Try changing:
    - run_time=2.0 -> 5.0 for a slower morph.
    - Morph a triangle into a pentagon instead (see snippet 27).

Run:     python snippets/01_square_to_circle.py
Output:  outputs/01_square_to_circle.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class SquareToCircle(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(BLUE, 0.6).set_stroke(WHITE, 3)
        circle = Circle(radius=1.8).set_fill(YELLOW, 0.6).set_stroke(WHITE, 3)

        self.add(square)                              # put the square on stage
        win.play(Transform(square, circle), run_time=2.0)  # morph square -> circle
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(SquareToCircle, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
