# Mastering PyTorch Specialization

跟学 Coursera《Mastering PyTorch》专项（3 门系列课，定位中级，约 4 周）的个人仓库。
仓库目录直接映射专项的三门课程结构，学完哪门就填哪门的内容；原始设计说明保留在 `README.txt`。

- Course 1：高级架构 —— CNN / RNN / Transformer
- Course 2：生成模型 —— GPT 文本生成、神经风格迁移、DCGAN、扩散模型、DQN
- Course 3：生产部署 —— TorchScript / ONNX 导出、TorchServe、fastai / PyTorch Lightning、LibTorch C++

## 进度表

| 课程 | 模块 | 状态 | 关键产出 |
|---|---|---|---|
| Course 1 | CNN / RNN / Transformer | 进行中 | 形状计算工具、概念笔记 |
| Course 2 | GPT 文本生成 | 未开始 | |
| Course 2 | 扩散模型 | 未开始 | |
| Course 3 | ONNX 导出 | 未开始 | |
| Course 3 | TorchServe 部署 | 未开始 | |
| Course 3 | LibTorch C++ 部署 | 进行中 | CMake + smoke_demo 示例 |

## 目录

```
├── .github/workflows/ci.yml        # CI：C++ 真编译 + Python 校验
├── mastering_pytorch/              # 与框架无关的配套代码
├── scripts/demo.py                 # Python 运行入口
├── tests/                          # 单元测试
├── course-1-advanced-architectures/
├── course-2-generative-models/
└── course-3-production-deployment/
    └── serving/libtorch-cpp-example/   # CMakeLists.txt + C++ 源码
```

每门课的 `notebooks/` 在学到对应模块时再补充，规划清单见各课程的 README。

## 代码与 CI

**C++ / LibTorch（Course 3 部署链路）** —— `course-3-production-deployment/serving/libtorch-cpp-example/`
是一份最小可运行的 C++ 示例：`CMakeLists.txt` + `src/smoke_demo.cpp`。CI 装 CPU 版 LibTorch，
用 CMake 配置后由 g++ **真正编译、链接**成可执行文件 `smoke_demo` 并运行，验证张量与
`torch::nn::Linear` 的前向计算。

**Python 配套代码** —— `mastering_pytorch/`（卷积/池化输出形状、学习率调度）、`scripts/demo.py`、
`tests/`，纯标准库，CI 里做字节码编译与单元测试。

`.github/workflows/ci.yml` 在每次 push / PR 时跑两个 job：

| job | 步骤 |
|---|---|
| `cpp-build-and-run` | 装 LibTorch(CPU) → `cmake` 配置 → **`cmake --build`（真编译 + 链接）** → 运行可执行文件 |
| `python-core` | `compileall` → demo → unittest |

`requirements.txt` 中的重型依赖供 notebooks 与本地实验使用；CI 的 `python-core` 不需要它们，
`cpp-build-and-run` 只装 CPU 版 PyTorch wheel 来取得 `TorchConfig.cmake` 与 libtorch 动态库。

> 本仓库的编译与运行全部由 GitHub Actions 完成，本地不执行编译。
