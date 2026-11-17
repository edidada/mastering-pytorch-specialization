# Course 3 — Production Deployment

专项第 3 门课，最特殊的一门：除了 notebook，还包含**可运行的部署产物**。
TorchServe 配置、Flask 服务示例放 `serving/`，与 notebook 分开，便于直接复制到实际项目。

## 模块与规划

| 模块 | 位置 | 状态 |
|---|---|---|
| TorchScript / ONNX 导出 | `notebooks/torchscript-onnx-export.ipynb` | 未开始 |
| fastai / PyTorch Lightning | `notebooks/fastai-lightning.ipynb` | 未开始 |
| TorchServe 配置 | `serving/torchserve-config/` | 未开始 |
| Flask 服务示例 | `serving/flask-server-example/` | 未开始 |

覆盖 TorchServe、ONNX、TorchScript 导出、移动端部署，以及 fastai / PyTorch Lightning 加速。

## 模型文件不入库

导出后的 `*.onnx`、`*.pt`、`*.pth`、`*.ckpt` 体积不小，已在 `.gitignore` 中忽略，
`serving/` 只提交最小可运行的代码与配置。

## 依赖

见根目录 `requirements.txt` 的「Course 3 部署与加速」分组：`fastai`、`pytorch-lightning`、
`torchserve`、`onnx`。

## 笔记

- `notes/export-and-serving.md`
