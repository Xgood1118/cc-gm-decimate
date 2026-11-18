# -*- coding: utf-8 -*-
"""网格简化与误差控制"""

from dataclasses import dataclass


@dataclass
class Mesh:
    """三角网格。"""
    verts: list
    faces: list




def quadric(mesh, vertex):
    """算顶点二次误差"""
    raise NotImplementedError("quadric 尚未实现")


def simplify(mesh, target_faces, tolerance):
    """简化"""
    raise NotImplementedError("simplify 尚未实现")


def hausdorff(a, b):
    """双向偏差"""
    raise NotImplementedError("hausdorff 尚未实现")


def load_mesh(path):
    """读入与落盘辅助"""
    raise NotImplementedError("load_mesh 尚未实现")

