# Mastering PyTorch Specialization

跟学 Coursera《Mastering PyTorch》专项（3 门系列课，定位中级，约 4 周）的个人仓库。
仓库目录直接映射专项的三门课程结构，学完哪门就填哪门的内容；原始设计说明保留在 `README.txt`。

- Course 1：高级架构 —— CNN / RNN / Transformer
- Course 2：生成模型 —— GPT 文本生成、神经风格迁移、DCGAN、扩散模型、DQN
- Course 3：生产部署 —— TorchScript / ONNX 导出、TorchServe、fastai / PyTorch Lightning

## 进度表

| 课程 | 模块 | 状态 | 关键产出 |
|---|---|---|---|
| Course 1 | CNN / RNN / Transformer | 进行中 | 形状计算工具、概念笔记 |
| Course 2 | GPT 文本生成 | 未开始 | |
| Course 2 | 扩散模型 | 未开始 | |
| Course 3 | ONNX 导出 | 未开始 | |
| Course 3 | TorchServe 部署 | 未开始 | |

## 目录

```
├── .github/workflows/ci.yml        # CI：编译 → 运行 → 测试
├── mastering_pytorch/              # 与框架无关的配套代码
├── scripts/demo.py                 # 运行入口
├── tests/                          # 单元测试
├── course-1-advanced-architectures/
├── course-2-generative-models/
└── course-3-production-deployment/
```

每门课的 `notebooks/` 在学到对应模块时再补充，规划清单见各课程的 README。

## 代码与 CI

`mastering_pytorch/` 存放与框架无关的配套代码（卷积/池化输出形状、学习率调度），
`scripts/demo.py` 是运行入口，`tests/` 是单元测试。

`.github/workflows/ci.yml` 在每次 push / PR 时依次执行：

1. `python -m compileall -q mastering_pytorch scripts tests` —— 把源码编译为字节码，同时完成语法校验
2. `python scripts/demo.py` —— 运行冒烟示例
3. `python -m unittest discover -s tests -v` —— 运行单元测试

CI 只覆盖纯 Python 核心代码，因此无需安装 PyTorch；`requirements.txt` 中的重型依赖
（torch / diffusers / torchserve 等）供 notebooks 与本地实验使用。

> 本仓库的编译与运行全部由 GitHub Actions 完成，本地不执行编译。
