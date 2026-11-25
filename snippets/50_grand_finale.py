"""
50 — The Grand Finale
======================
What this does:
    One big square dissolves into four smaller squares, then a closing
    line fades in underneath. Everything from the last 49 snippets in one
    shot: groups, fades, and text.

Key ideas:
    - FadeOut() removes the big square while FadeIn() brings the group of
      four on stage — a clean swap between two unrelated mobjects.
    - Each quadrant gets its own fill color for free contrast.
    - Text + FadeIn closes the show.

Try changing:
    - The four colors, or split into 9 squares in a 3x3 grid.
    - Put your own name in the closing text.

Run:     python snippets/50_grand_finale.py
Output:  outputs/50_grand_finale.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class GrandFinale(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        big = Square(side_length=3.0).set_fill(BLUE, 0.5).set_stroke(WHITE, 3)

        quadrants = [
            (RED, [0.75, 0.75, 0.0]),     # top right
            (GOLD, [-0.75, 0.75, 0.0]),   # top left
            (TEAL, [0.75, -0.75, 0.0]),   # bottom right
            (GREEN, [-0.75, -0.75, 0.0]),  # bottom left
        ]
        small = VGroup(*[
            Square(side_length=1.5).set_fill(color, 0.6).set_stroke(WHITE, 2).move_to(pos)
            for color, pos in quadrants
        ])

        self.add(big)
        win.play(FadeOut(big), run_time=0.8)   # the big square leaves...
        win.play(FadeIn(small), run_time=1.2)  # ...and the four arrive
        win.play(Wait(0.5))

        closing = Text("50 snippets — go make something!", font_size=48).to_edge(DOWN)
        win.play(FadeIn(closing), run_time=1.5)
        win.play(Wait(1.5))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(GrandFinale, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
