"""
17 — Expand a Binomial
======================
What this does:
    (a+b)² dissolves into its expansion a² + 2ab + b².

Key ideas:
    - FadeTransform(src, dst) is Transform plus a fade: the old formula
      dims out while the new one fades in at the same spot.
    - This is the standard "algebra move" animation: identity on the left,
      expansion on the right.

Try changing:
    - The two formulas (e.g. sin²x + cos²x -> 1).
    - Run it backwards: swap which formula is first.

Run:     python snippets/17_expand_binomial.py
Output:  outputs/17_expand_binomial.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class ExpandBinomial(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        lhs = MathTex(r"(a+b)^2").scale(1.8)
        rhs = MathTex(r"a^2 + 2ab + b^2").scale(1.8)

        self.add(lhs)
        win.play(FadeTransform(lhs, rhs), run_time=3.0)  # one formula becomes the other
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(ExpandBinomial, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
