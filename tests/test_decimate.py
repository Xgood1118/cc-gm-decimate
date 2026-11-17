# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import decimate as mod  # noqa: E402
decimate = mod

def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_hex(path):
    with open(path, encoding="utf-8") as f:
        return f.read().strip()


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def test_simplify_reaches_target():
    m = decimate.load_mesh("data/mesh.txt")
    out = decimate.simplify(m, 12, 0.05)
    assert len(out.faces) <= 12


def test_hausdorff_non_negative():
    m = decimate.load_mesh("data/mesh.txt")
    d = decimate.hausdorff(m, m)
    assert d["max"] >= 0
