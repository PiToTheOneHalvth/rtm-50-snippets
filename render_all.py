"""
Render every snippet in order and report which ones fail.

Usage:
    python render_all.py            # all 50 snippets
    python render_all.py 01 12 33   # only snippets 01, 12, 33

Requires: real-time-manim installed in this Python environment
          (pip install "real-time-manim[typst]") and ffmpeg on PATH.

Each snippet writes its MP4 into outputs/ next to this file.
"""
import glob
import os
import subprocess
import sys
import time

here = os.path.dirname(os.path.abspath(__file__))
snippets = sorted(glob.glob(os.path.join(here, "snippets", "*.py")))

if len(sys.argv) > 1:
    want = {f"{int(a):02d}" for a in sys.argv[1:]}
    snippets = [s for s in snippets if os.path.basename(s).split("_")[0] in want]
    if not snippets:
        sys.exit("no snippets matched; pass numbers like: python render_all.py 01 05")

# A stale PYTHONPATH (e.g. from an IDE/agent environment) can shadow
# real_time_manim with an external manim install. Drop it for the children.
env = os.environ.copy()
env.pop("PYTHONPATH", None)

failed = []
t0 = time.time()
for path in snippets:
    name = os.path.basename(path)
    print(f"--- {name}", flush=True)
    result = subprocess.run(
        [sys.executable, path],
        cwd=here, env=env,
        capture_output=True, text=True,
    )
    elapsed = time.time() - t0
    if result.returncode == 0:
        print(f"    OK   ({elapsed:6.1f}s total)")
    else:
        failed.append(name)
        print(f"    FAIL ({elapsed:6.1f}s total)")
        tail = (result.stdout + result.stderr).strip().splitlines()[-12:]
        print("\n".join("    " + line for line in tail))

print()
print(f"{len(snippets) - len(failed)}/{len(snippets)} rendered OK in {time.time() - t0:.1f}s")
if failed:
    print("failed:", ", ".join(failed))
    sys.exit(1)
