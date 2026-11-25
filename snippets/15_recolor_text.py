"""
15 — Recolor Text
=================
What this does:
    A word smoothly changes color three times: white -> red -> yellow.

Key ideas:
    - .animate.set_color(c) interpolates the glyph colors.
    - Text colors come from the same color system as shapes, so you can
      match a shape and its label exactly.

Try changing:
    - Use t2c={"part": RED} in the Text() call to color substrings
      differently from the start (e.g. t2c={"this": RED}).

Run:     python snippets/15_recolor_text.py
Output:  outputs/15_recolor_text.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class RecolorText(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        text = Text("watch me change", font_size=72)
        self.add(text)

        win.play(text.animate.set_color(RED), run_time=1.0)
        win.play(text.animate.set_color(YELLOW), run_time=1.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(RecolorText, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
