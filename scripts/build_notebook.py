"""
Build rtm_50_snippets.ipynb from the snippet .py files.

Every snippet becomes two cells:
  - a markdown cell with the file's docstring (what it does, key ideas,
    what to change), and
  - a code cell that renders the MP4 and embeds it inline.

Usage:
    python scripts/build_notebook.py          # writes rtm_50_snippets.ipynb

Pure stdlib — no notebook packages required to GENERATE the notebook
(you only need a Jupyter kernel to run it).
"""
import ast
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOK = os.path.join(ROOT, "rtm_50_snippets.ipynb")

INTRO_MD = """\
# RTM — 50 Snippets (notebook edition)

One interactive notebook for trying [real-time-manim](https://github.com/axioviva/real-time-manim):
**each cell is one complete snippet** — it builds a `Scene`, renders it to
`outputs/<name>.mp4` (1920×1080 @ 60 fps), and embeds the video right below the cell.

## Setup

```bash
pip install "real-time-manim[typst]" jupyter   # + molten-vk and ffmpeg on macOS
jupyter notebook rtm_50_snippets.ipynb
```

Then run any cell — or all of them (≈2 minutes for all 50).

## How to read a cell

1. Read the markdown above it: what the scene does and what to change.
2. Run the code cell: an MP4 lands in `outputs/` and plays inline.
3. Change one number (a `run_time`, a color, an angle) and re-run.

Each cell is self-contained — imports, scene, render, display — so cells can
be run in any order. The canonical file format is still `snippets/*.py`
(see the README); regenerate this notebook anytime with
`python scripts/build_notebook.py`.
"""


def docstring_to_markdown(doc):
    """Turn a snippet docstring into a markdown cell body."""
    out = []
    for raw in doc.splitlines():
        line = raw.rstrip()
        if not line or line.startswith("=") or set(line) <= {"="}:
            continue
        if line.startswith("Run:") or line.startswith("Output:"):
            continue
        if re.match(r"^\d{2} — ", line):
            out.append("## " + line)
        elif re.match(r"^(What this does|Key ideas|Try changing):$", line):
            out.append("**" + line + "**")
        else:
            out.append(line)
    return "\n".join(out).strip()


def snippet_to_cells(path):
    """Return (markdown_cell, code_cell) for one snippet file."""
    src = open(path).read()
    tree = ast.parse(src)
    doc = ast.get_docstring(tree, clean=False) or ""
    class_name = next(n.name for n in tree.body if isinstance(n, ast.ClassDef))

    # Code cell = source minus the module docstring, with the __main__
    # guard replaced by a direct render + inline video embed.
    body = re.sub(r'^r?"""\n.*?"""\n', "", src, count=1, flags=re.DOTALL)
    # __file__ does not exist in a notebook -> bake in the literal name.
    stem = os.path.splitext(os.path.basename(path))[0]
    body = body.replace(
        'OUTPUT = os.path.join("outputs", f"{os.path.splitext(os.path.basename(__file__))[0]}.mp4")',
        f'OUTPUT = os.path.join("outputs", "{stem}.mp4")',
    )
    tail = (
        'from IPython.display import Video, display\n'
        '\n'
        'result = fast_record_scene(%s, OUTPUT, overwrite=True)\n'
        'display(Video(OUTPUT, width=854))\n'
    ) % class_name
    body = re.sub(
        r'\nif __name__ == "__main__":\n.*$', "\n" + tail, body, flags=re.DOTALL
    )
    body = body.rstrip() + "\n"

    markdown = {
        "cell_type": "markdown",
        "metadata": {},
        "source": docstring_to_markdown(doc).splitlines(keepends=True),
    }
    code = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": body.splitlines(keepends=True),
    }
    return markdown, code


def main():
    snippets = sorted(glob.glob(os.path.join(ROOT, "snippets", "*.py")))
    cells = [
        {"cell_type": "markdown", "metadata": {}, "source": INTRO_MD.splitlines(keepends=True)}
    ]
    for path in snippets:
        md, code = snippet_to_cells(path)
        cells.extend([md, code])

    notebook = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.12"},
        },
        "cells": cells,
    }
    with open(NOTEBOOK, "w") as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    print(f"wrote {NOTEBOOK} ({len(snippets)} snippets, {len(cells)} cells)")


if __name__ == "__main__":
    main()
