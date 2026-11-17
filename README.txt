Coursera 上的《Mastering PyTorch》专项：这是一个由浅入深的 3 门系列课，明确覆盖了从基础网络（CNN/RNN/Transformer）到生成模型（GAN/扩散模型），再到生产部署（TorchServe/ONNX/Hugging Face）的全流程。它定位中级，建议有基础的学习者用 4 周左右完成，学完可获得职业证书。
针对 Coursera《Mastering PyTorch》专项，仓库组织应该**直接映射它的三门课程结构**，而不是像官方基础教程那样按知识点拆分。专项本身有明确的阶段划分，仓库目录跟课程走，学完哪门就填哪门的内容，进度一目了然。

### 仓库命名建议

推荐 `mastering-pytorch-specialization` 或 `pytorch-advanced-deploy`。前者最直白，一眼知道跟的是哪个专项；后者突出了后半程的生产部署重点，适合你日后求职时展示工程能力。

### 目录结构

专项的三门课程对应三个顶层文件夹，编号与 Coursera 课程顺序一致：

```text
mastering-pytorch-specialization/
├── README.md
├── requirements.txt
├── .gitignore
├── course-1-advanced-architectures/
│   ├── README.md
│   ├── notes/
│   │   └── (按模块整理的概念笔记)
│   └── notebooks/
│       ├── cnn.ipynb
│       ├── rnn.ipynb
│       └── transformer.ipynb
├── course-2-generative-models/
│   ├── README.md
│   ├── notes/
│   └── notebooks/
│       ├── text-generation-gpt.ipynb
│       ├── neural-style-transfer.ipynb
│       ├── dcgan.ipynb
│       ├── diffusion-unet.ipynb
│       └── deep-rl-dqn.ipynb
├── course-3-production-deployment/
│   ├── README.md
│   ├── notes/
│   ├── notebooks/
│   │   ├── torchscript-onnx-export.ipynb
│   │   └── fastai-lightning.ipynb
│   └── serving/
│       ├── torchserve-config/
│       └── flask-server-example/
└── assets/
    └── (架构图、输出截图)
```

### 每个课程文件夹的组织逻辑

**Course 1** 覆盖 CNN、RNN、Transformer 等高级架构。notebook 按架构分文件，每个文件里包含该架构的 PyTorch 实现和训练实验。`notes/` 放你自己的概念梳理，比如 “Transformer 的 attention 和 RNN 的 hidden state 到底差在哪”。

**Course 2** 是生成模型专题，包含 GPT 文本生成、神经风格迁移、DCGAN、扩散模型和深度强化学习。这个文件夹的 notebook 数量最多，建议按技术类型命名，方便日后查 “当时扩散模型是怎么搭 UNet 的”。

**Course 3** 最特殊，它不只包含 notebook，还涉及**可运行的部署产物**。TorchServe 配置、Flask 服务示例这类内容放 `serving/` 下，与 notebook 分开。这门课覆盖 TorchServe、ONNX、TorchScript 导出、移动端部署以及 fastai/PyTorch Lightning 加速。`serving/` 里的内容是你日后可以直接复制到实际项目里用的最小可运行示例。

### 根目录文件的作用

`README.md` 首页放一张**三门课进度表**，比按周记录更匹配专项的结构：

| 课程 | 模块 | 状态 | 关键产出 |
|---|---|---|---|
| Course 1 | CNN / RNN / Transformer | | |
| Course 2 | GPT 文本生成 | | |
| Course 2 | 扩散模型 | | |
| Course 3 | ONNX 导出 | | |
| Course 3 | TorchServe 部署 | | |

`requirements.txt` 需要比基础教程更丰富。除了 `torch` `torchvision`，Course 2 的扩散模型部分会用到 `diffusers`，Course 3 涉及 `fastai`、`pytorch-lightning`、`torchserve` 等。建议按课程分组注释，而不是一股脑堆在一起：

```text
# 基础
torch
torchvision

# Course 2 生成模型
diffusers
transformers

# Course 3 部署与加速
fastai
pytorch-lightning
torchserve
onnx
```

`.gitignore` 除了忽略 `data/`，还要加上 `*.onnx`、`*.pt`、`*.pth` 等模型权重文件。Course 3 导出后的模型文件体积不小，不适合提交到仓库。

### 为什么不按“周”分

专项建议 4 周完成，但 Coursera 是自定进度的，你很可能一周内连续看 Course 1 的多个模块，或者某天只折腾 TorchServe 配置。**按课程和模块分文件夹**，你的提交记录会自然形成一条 “先架构、再生成了、最后部署” 的成长轨迹，日后回顾时定位也快。