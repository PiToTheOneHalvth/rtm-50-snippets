"""
32 — A Shining Star
===================
What this does:
    A gold five-pointed star is drawn, then pulses with a highlight ring.

Key ideas:
    - Star(n=5, outer_radius=2, inner_radius=0.8) alternates between the
      outer and inner radii to make the points.
    - Indicate(scale_factor=...) briefly scales the star up and back while
      fading a colored copy — a "look here" effect.

Try changing:
    - n=5 -> n=7 for a heptagram.
    - Indicate's color (WHITE -> RED) and scale_factor (1.25 -> 1.6).

Run:     python snippets/32_shining_star.py
Output:  outputs/32_shining_star.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class ShiningStar(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        star = Star(5, outer_radius=2.0, inner_radius=0.8)
        star.set_fill(GOLD, 0.7).set_stroke(WHITE, 2)

        win.play(Create(star), run_time=2.0)
        win.play(Indicate(star, scale_factor=1.25, color=WHITE), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(ShiningStar, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
