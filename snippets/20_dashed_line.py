"""
20 — A Dashed Line
==================
What this does:
    A dashed blue line is drawn across the screen.

Key ideas:
    - DashedLine(start, end, dash_length=...) is a Line with a dash pattern.
    - Longer dash_length gives longer dashes and bigger gaps.

Try changing:
    - dash_length=0.5 -> 0.15 (finer dashes, like a perforation).
    - Turn it into a dashed circle with DashedVMobject(Circle(...)).

Run:     python snippets/20_dashed_line.py
Output:  outputs/20_dashed_line.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class DashedLineDemo(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        line = DashedLine(LEFT * 4, RIGHT * 4, dash_length=0.5).set_stroke(BLUE, 4)

        win.play(Create(line), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(DashedLineDemo, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
