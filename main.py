#!/usr/bin/env python3
"""The World Tonight - Friday 27 November 2026.

Copies the front-page image (front.png, drawn in this session) to
$MAKEFUN_OUTPUT_DIR/entry.png. Standard library only.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "front.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
DST = OUT

with open(SRC, "rb") as f:
    head = f.read(8)
if head != b"\x89PNG\r\n\x1a\n":
    sys.exit("front.png is not a PNG")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote", DST)
