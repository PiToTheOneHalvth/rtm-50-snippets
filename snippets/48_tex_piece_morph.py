"""
48 — TeX Piece Morph
====================
What this does:
    "a + b" rearranges piece by piece into "b + a" — addition commutes.

Key ideas:
    - MathTex(*three_strings) builds ONE formula from three submobjects.
    - FadeTransformPieces(src, dst) matches the pieces by position and
      fades each one into its counterpart — a controlled morph.
    - The pieces must decompose the same way on both sides (same number
      of glyph families per slot), otherwise manim cannot pair them.
      Single symbols like "a", "+", "b" are the safe choice.

Try changing:
    - The pieces: "x", "=", "y" on both sides, in different orders.
    - Scale each piece differently (lhs[0].scale(1.5)) to see which is which.

Run:     python snippets/48_tex_piece_morph.py
Output:  outputs/48_tex_piece_morph.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class TexPieceMorph(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        lhs = MathTex("a", "+", "b").scale(2.0)
        rhs = MathTex("b", "+", "a").scale(2.0)

        self.add(lhs)
        # Three pieces -> three pieces: the terms swap places.
        win.play(FadeTransformPieces(lhs, rhs), run_time=3.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(TexPieceMorph, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
