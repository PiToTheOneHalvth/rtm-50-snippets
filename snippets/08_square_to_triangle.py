"""
08 — Square to Triangle Morph
=============================
What this does:
    A square morphs into a triangle. 4 points become 3.

Key ideas:
    - Transform() works even when the shapes have DIFFERENT point counts:
      manim matches the curve families as well as it can.
    - You build any polygon with Polygon(point1, point2, point3, ...).
      Each point is a list [x, y, z] of plain numbers.

Try changing:
    - Add more vertices to make a hexagon, an arrow head, anything.
    - Give the triangle a different fill than the square.

Run:     python snippets/08_square_to_triangle.py
Output:  outputs/08_square_to_triangle.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class SquareToTriangle(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(BLUE, 0.6).set_stroke(WHITE, 3)
        triangle = Polygon(
            [-1.5, -1.0, 0.0],
            [1.5, -1.0, 0.0],
            [0.0, 1.6, 0.0],
        ).set_fill(GREEN, 0.6).set_stroke(WHITE, 3)

        self.add(square)
        win.play(Transform(square, triangle), run_time=2.0)  # 4 points -> 3 points
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(SquareToTriangle, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
