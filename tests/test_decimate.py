# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import decimate as mod  # noqa: E402


def test_simplify_reaches_target():
    m = decimate.load_mesh("data/mesh.txt")
    out = decimate.simplify(m, 12, 0.05)
    assert len(out.faces) <= 12


def test_hausdorff_non_negative():
    m = decimate.load_mesh("data/mesh.txt")
    d = decimate.hausdorff(m, m)
    assert d["max"] >= 0
