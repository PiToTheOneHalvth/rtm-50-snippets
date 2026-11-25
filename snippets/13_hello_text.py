"""
13 — Hello, RTM!
================
What this does:
    Big yellow text "Hello, RTM!" fades in at the center of the screen.

Key ideas:
    - Text() renders a string with a system font (no LaTeX needed).
    - font_size is in manim units; 96 is large on the 14.2-unit-wide frame.
    - FadeIn works for text exactly like it works for shapes.

Try changing:
    - The string itself, and the color (RED, TEAL, "#FF8800").
    - .to_edge(UP) to pin the text to the top of the frame.

Run:     python snippets/13_hello_text.py
Output:  outputs/13_hello_text.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class HelloText(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        text = Text("Hello, RTM!", font_size=96).set_color(YELLOW)

        win.play(FadeIn(text), run_time=1.5)
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(HelloText, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
