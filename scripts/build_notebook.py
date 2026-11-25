"""
Build one .ipynb notebook per snippet, written to notebooks/<name>.ipynb.

Every notebook has two cells:
  - a markdown cell with the snippet's docstring (what it does, key ideas,
    what to change), and
  - a code cell that renders the MP4 and embeds it inline.

Usage:
    python scripts/build_notebook.py          # writes notebooks/01_*.ipynb ... 50_*.ipynb

Pure stdlib — no notebook packages required to GENERATE the notebooks
(you only need a Jupyter kernel to run them).
"""
import ast
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS_DIR = os.path.join(ROOT, "notebooks")


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
            out.append("# " + line)
        elif re.match(r"^(What this does|Key ideas|Try changing):$", line):
            out.append("**" + line + "**")
        else:
            out.append(line)
    out.append("")
    out.append("Run the code cell below to render this scene "
               "and play it back inline.")
    return "\n".join(out).strip()


def snippet_to_notebook(path):
    """Build the two-cell notebook dict for one snippet file."""
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
        "cells": [markdown, code],
    }
    return notebook


def main():
    snippets = sorted(glob.glob(os.path.join(ROOT, "snippets", "*.py")))
    os.makedirs(NOTEBOOKS_DIR, exist_ok=True)
    written = 0
    for path in snippets:
        stem = os.path.splitext(os.path.basename(path))[0]
        out = os.path.join(NOTEBOOKS_DIR, f"{stem}.ipynb")
        with open(out, "w") as f:
            json.dump(snippet_to_notebook(path), f, indent=1, ensure_ascii=False)
        written += 1
    print(f"wrote {written} notebooks to notebooks/")


if __name__ == "__main__":
    main()
