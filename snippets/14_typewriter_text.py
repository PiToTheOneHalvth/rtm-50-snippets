"""
14 — Typewriter Text
====================
What this does:
    A sentence is written out character by character, like a typewriter.

Key ideas:
    - Write() reveals a text mobject progressively along its glyphs.
    - Unlike FadeIn, Write feels like pen strokes, not a dissolve.
    - Unwrite() (snippet 44's sibling) erases text the same way, backwards.

Try changing:
    - The string to something longer and watch it keep up.
    - Write -> Unwrite to see the eraser version.

Run:     python snippets/14_typewriter_text.py
Output:  outputs/14_typewriter_text.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class TypewriterText(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        text = Text("RTM types this out...", font_size=56).set_color(TEAL)

        win.play(Write(text), run_time=3.0)  # stroke by stroke
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(TypewriterText, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
