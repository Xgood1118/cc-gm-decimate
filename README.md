# 网格简化与误差控制

一个按二次误差简化网格、并把几何偏差压在容差内的简化器

## 保留签名

- `Mesh`
- `quadric(mesh, vertex)`
- `simplify(mesh, target_faces, tolerance)`
- `hausdorff(a, b)`

## 自测

```
python -m pytest tests -q
python -m decimate.cli data/mesh.txt --target 12 --out simplified.txt
```
