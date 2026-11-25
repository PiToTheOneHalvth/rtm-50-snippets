"""
11 — A Short Story in One Line
==============================
What this does:
    One Succession() call chains three animations: a square is drawn,
    rotates 45°, then fades away.

Key ideas:
    - Succession(anim1, anim2, ...) plays its animations strictly one after
      another, inside a SINGLE play() call.
    - Each inner animation carries its own run_time; the play's run_time is
      the sum of the parts.
    - FadeOut() removes the mobject from the scene when it finishes.

Try changing:
    - Insert another step, like Rotate(square, angle=-PI/4) before the fade.
    - Add lag_ratio=0.5 to Succession so each step overlaps the next.

Run:     python snippets/11_story_sequence.py
Output:  outputs/11_story_sequence.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class StorySequence(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        square = Square(side_length=2.5).set_fill(BLUE, 0.6).set_stroke(WHITE, 3)

        # Draw it, spin it, let it go — three acts, one play.
        win.play(
            Succession(
                Create(square, run_time=1.2),
                Rotate(square, angle=PI / 4, run_time=1.0),
                FadeOut(square, run_time=0.8),
            ),
            run_time=3.0,
        )

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(StorySequence, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
