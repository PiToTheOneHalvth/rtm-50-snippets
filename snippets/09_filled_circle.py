"""
09 — A Filled Circle
====================
What this does:
    A circle is drawn, then filled with translucent blue.

Key ideas:
    - set_fill(color, opacity) controls the interior; opacity 0.4 is translucent.
    - set_stroke(color, width) controls the outline; width 0 removes it.
    - With a fill already authored, Create() draws stroke AND fill together.

Try changing:
    - opacity 0.4 -> 1.0 for a solid disk, or 0.0 for an empty ring.
    - radius=2.0 -> radius=3.5 for a big disc.

Run:     python snippets/09_filled_circle.py
Output:  outputs/09_filled_circle.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class FilledCircle(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        circle = Circle(radius=2.0).set_fill(BLUE, 0.4).set_stroke(WHITE, 3)

        win.play(Create(circle), run_time=2.0)  # stroke and translucent fill
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(FilledCircle, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
