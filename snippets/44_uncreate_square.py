"""
44 — Un-draw a Square
=====================
What this does:
    A square disappears by having its outline erased, stroke by stroke.

Key ideas:
    - Uncreate() is Create() played backwards: the pen retraces the
      outline in reverse until nothing is left.
    - The mobject must already be on stage (self.add first).
    - After Uncreate the square is removed from the scene entirely.

Try changing:
    - Use Uncreate on Text for an eraser effect.
    - Compare with FadeOut() — same result, very different feel.

Run:     python snippets/44_uncreate_square.py
Output:  outputs/44_uncreate_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class UncreateSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=3.0).set_stroke(YELLOW, 6)
        self.add(square)          # fully drawn first...

        win.play(Uncreate(square), run_time=2.0)  # ...then erased backwards
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(UncreateSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
