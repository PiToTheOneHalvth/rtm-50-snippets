"""
28 — An Annulus (Ring)
======================
What this does:
    A teal ring — a circle with a round hole — is drawn on screen.

Key ideas:
    - Annulus(inner_radius, outer_radius) is the region between two
      concentric circles, drawn as one mobject.
    - A translucent fill (0.4) shows the ring's interior as a band.
    - The hole is real geometry, not a white circle drawn on top.

Try changing:
    - inner_radius=1.0 -> 1.7 (a thin ring).
    - outer_radius=2.0 -> 3.0 and animate it with FadeIn.

Run:     python snippets/28_annulus_ring.py
Output:  outputs/28_annulus_ring.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class AnnulusRing(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        ring = Annulus(inner_radius=1.0, outer_radius=2.0)
        ring.set_fill(TEAL, 0.4).set_stroke(WHITE, 2)

        win.play(Create(ring), run_time=2.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(AnnulusRing, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
