"""
12 — A Grid of Squares
======================
What this does:
    A 4x4 grid of teal squares is drawn all at once.

Key ideas:
    - VGroup(*[Square() for _ in range(16)]) builds 16 identical squares.
    - .arrange_in_grid(rows, cols, buff=gap) lays the children out in a grid.
    - The group can be animated as ONE object: a single Create() draws all 16.

Try changing:
    - 4x4 -> 5x7 for a wider wall.
    - Color each square differently by cycling a list of colors.

Run:     python snippets/12_grid_of_squares.py
Output:  outputs/12_grid_of_squares.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class GridOfSquares(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        grid = VGroup(*[Square(side_length=0.9) for _ in range(16)])
        grid.arrange_in_grid(4, 4, buff=0.25).set_fill(TEAL, 0.5).set_stroke(WHITE, 2)

        win.play(Create(grid), run_time=3.0)  # the whole grid is one mobject
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(GridOfSquares, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
