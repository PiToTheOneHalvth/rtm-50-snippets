"""
29 — Arrange into a Grid
========================
What this does:
    Nine shapes start in a horizontal row, then reorganize into a 3x3 grid.

Key ideas:
    - .animate.arrange_in_grid(3, 3, buff=0.4) is a builder: it records the
      target layout and animates each child gliding to its new spot.
    - One play call moves all nine shapes at once.
    - VGroup methods like arrange() apply to every child.

Try changing:
    - The shapes inside the group (Circle, Star, Triangle, ...).
    - The grid shape: arrange_in_grid(2, 4) or arrange(DOWN).

Run:     python snippets/29_arrange_grid.py
Output:  outputs/29_arrange_grid.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class ArrangeGrid(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        shapes = VGroup(
            *[Circle(radius=0.5).set_fill(c, 0.7).set_stroke(WHITE, 2)
              for c in (RED, GOLD, GREEN, TEAL, BLUE, PURPLE, PINK, ORANGE, GREY)]
        )
        shapes.arrange(RIGHT, buff=0.4)  # starting layout: a row
        self.add(shapes)

        # Glide every shape from the row into a 3x3 grid.
        win.play(shapes.animate.arrange_in_grid(3, 3, buff=0.6), run_time=2.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(ArrangeGrid, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
