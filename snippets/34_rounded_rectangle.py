"""
34 — A Rounded Rectangle
========================
What this does:
    A blue rectangle with rounded corners grows out of its center.

Key ideas:
    - RoundedRectangle(width, height, corner_radius) is a rectangle whose
      corners are arcs of the given radius.
    - GrowFromCenter() scales the shape up from its center point — the
      opposite feel of Create()'s pen-stroke drawing.

Try changing:
    - corner_radius=0.3 -> 1.0 (fully rounded capsule ends).
    - GrowFromCenter -> GrowFromEdge(edge=LEFT) to grow from the left side.

Run:     python snippets/34_rounded_rectangle.py
Output:  outputs/34_rounded_rectangle.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class RoundedRectangleDemo(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        card = RoundedRectangle(width=4.0, height=2.5, corner_radius=0.3)
        card.set_fill(BLUE, 0.5).set_stroke(WHITE, 2)

        win.play(GrowFromCenter(card), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(RoundedRectangleDemo, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
