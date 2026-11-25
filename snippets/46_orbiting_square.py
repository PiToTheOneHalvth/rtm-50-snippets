"""
46 — An Orbiting Square
=======================
What this does:
    A small square orbits the center of the screen, two full turns.

Key ideas:
    - .move_to(RIGHT*2.5) parks the square 2.5 units right of the center.
    - Rotate(square, angle=2*TAU, about_point=ORIGIN) spins it around the
      screen center — the square itself stays upright? No: it rotates
      with the orbit, like the Moon showing one face.
    - about_point is the pivot; without it the square would spin in place.

Try changing:
    - angle=2*TAU -> angle=TAU (one orbit).
    - Add a small circle at ORIGIN as the "sun" being orbited.

Run:     python snippets/46_orbiting_square.py
Output:  outputs/46_orbiting_square.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class OrbitingSquare(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        sun = Circle(radius=0.2).set_fill(GOLD, 1.0)
        square = Square(side_length=0.8).set_fill(BLUE, 0.7).set_stroke(WHITE, 2)
        square.move_to(RIGHT * 2.5)  # start on the right

        self.add(sun, square)
        # Two full turns around the screen center.
        win.play(Rotate(square, angle=2 * TAU, about_point=ORIGIN), run_time=4.0)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(OrbitingSquare, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
