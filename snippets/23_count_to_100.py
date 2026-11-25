"""
23 — Count to 100
=================
What this does:
    A number in the corner counts up from 0 to 100 in four seconds.

Key ideas:
    - ValueTracker(value) is a mobject that holds one number and can be
      animated: tracker.animate.set_value(100) tweens from 0 to 100.
    - An updater is a function re-run every frame: here it copies the
      tracker's value into the displayed Integer.
    - Updaters only run during a play() — the play drives the clock.

Try changing:
    - 100 -> 10000, or run_time=4.0 -> 10.0.
    - Replace Integer(0) with DecimalNumber(0) to show decimals.

Run:     python snippets/23_count_to_100.py
Output:  outputs/23_count_to_100.mp4
"""
import os

from real_time_manim import *  # Vulkan renderer + full ManimCE namespace
from real_time_manim.record import fast_record_scene  # hidden-window MP4 recorder

OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")
os.makedirs("outputs", exist_ok=True)


class CountToHundred(Scene):
    def construct(self):
        win = MLWindow(1920, 1080)  # the real-time Vulkan window (fixed 1080p60)
        win.scene = self            # REQUIRED: bind this scene to the window

        tracker = ValueTracker(0)
        counter = Integer(0).scale(1.5).to_corner(UL, buff=0.6)

        # Every frame: copy the tracker's value into the visible number.
        counter.add_updater(lambda m: m.set_value(int(round(tracker.get_value()))))

        self.add(counter)
        win.play(tracker.animate.set_value(100), run_time=4.0)  # tweens 0 -> 100
        win.play(Wait(1.0))

        win.close()  # REQUIRED: flush frames and finish the MP4


if __name__ == "__main__":
    result = fast_record_scene(CountToHundred, OUTPUT, overwrite=True)
    print("wrote:", result["files"])
