"""
37 — Recolor a Matrix
=====================
What this does:
    A 3x3 grid of grey squares lights up teal, one square at a time.

Key ideas:
    - A plain Python for loop over the group's children schedules nine
      short plays back to back — each square recolors on its own beat.
    - .animate.set_fill(color, opacity) tweens the fill of one square.
    - Loops + play() = your first procedural animation timeline.

Try changing:
    - run_time=0.15 -> 0.4 for a slower wave.
    - Iterate reversed(grid) to light up the other way.

Run:     python snippets/37_recolor_matrix.py
Output:  outputs/37_recolor_matrix.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class RecolorMatrix(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        grid = VGroup(*[Square(side_length=1.2) for _ in range(9)])
        grid.arrange_in_grid(3, 3, buff=0.35)
        grid.set_fill(GREY, 0.3).set_stroke(WHITE, 2)
        self.add(grid)

        for square in grid:  # light up one square per play
            win.play(square.animate.set_fill(TEAL, 0.8), run_time=0.15)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(RecolorMatrix, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
