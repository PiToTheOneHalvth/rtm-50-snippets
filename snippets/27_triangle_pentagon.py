"""
27 — Triangle to Pentagon and Back
==================================
What this does:
    A triangle morphs into a pentagon, holds, then morphs back.

Key ideas:
    - Regular polygons are built from points on a circle:
      cos(2*pi*k/n), sin(2*pi*k/n) for k = 0..n-1.
    - Polygon(*points) takes the list of vertices and closes the loop.
    - .copy() freezes a snapshot of a mobject — Transform(tri, tri_copy)
      morphs back to the exact original shape.
    - Transform works across different vertex counts (3 vs 5).

Try changing:
    - n=5 -> n=8 for an octagon, or n=100 for a near-circle.
    - Make the two polygons different colors.

Run:     python snippets/27_triangle_pentagon.py
Output:  outputs/27_triangle_pentagon.mp4
"""
import os

import numpy as np

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


def ngon(n, radius, color):
    """Build a regular n-gon from n evenly spaced points on a circle."""
    points = [
        np.array([radius * np.cos(2 * np.pi * k / n - np.pi / 2),
                  radius * np.sin(2 * np.pi * k / n - np.pi / 2), 0.0])
        for k in range(n)
    ]
    return Polygon(*points).set_fill(color, 0.5).set_stroke(WHITE, 2)


class TrianglePentagon(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        triangle = ngon(3, 1.6, BLUE)
        pentagon = ngon(5, 1.6, GOLD)
        triangle_copy = triangle.copy()  # snapshot for the return trip

        self.add(triangle)
        win.play(Transform(triangle, pentagon), run_time=2.0)      # 3 -> 5 sides
        win.play(Transform(triangle, triangle_copy), run_time=2.0)  # and back
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(TrianglePentagon, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
