r"""
16 — Pythagoras in TeX
======================
What this does:
    The formula a² + b² = c² is typeset with real math layout and faded in.

Key ideas:
    - MathTex() renders LaTeX-style source. With the [typst] extra installed
      it uses Typst in-process — no LaTeX distribution required.
    - Write the TeX as a raw string (r"...") so backslashes survive.
    - .scale(n) makes math bigger; the frame is 14.2 units wide.

Try changing:
    - The formula: r"\int_0^1 x^2\,dx = \frac{1}{3}" (an integral).
    - Use tex_to_color_map={"a": BLUE, "b": GREEN} to color the letters.

Run:     python snippets/16_pythagoras_tex.py
Output:  outputs/16_pythagoras_tex.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class PythagorasTex(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        formula = MathTex(r"a^2 + b^2 = c^2").scale(2.0)

        win.play(FadeIn(formula), run_time=2.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(PythagorasTex, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
