# 导出与上线：TorchScript → ONNX → TorchServe

## 为什么要导出

训练时的 Python 模型依赖解释器、动态图和整套训练代码，既不好部署，也不好做图优化。
导出就是把它固化成一份与训练代码解耦、可被独立运行时加载的计算图。

## 两条路径

- **TorchScript**：用 `torch.jit.trace` 或 `torch.jit.script` 把模型变成可序列化的图，
  保存为 `.pt`，由 libtorch（C++）加载。trace 记录一次实际前向，控制流会被固化；
  script 直接解析源码，能保留分支/循环。
- **ONNX**：把模型导出为框架中立的算子图，交给 ONNX Runtime / TensorRT / 移动端运行时。
  好处是跨框架、跨硬件；代价是部分 PyTorch 算子没有对应 ONNX 算子，需要自定义算子或改写。

## 导出时注意

- 模型先 `eval()`，关掉 dropout / BN 的训练行为；
- 用固定 shape 的 dummy input，并明确 `dynamic_axes` 声明哪些维可变；
- 导出后必须用真实输入做一次数值比对（输出误差在容差内），别只看「导出成功」。

## 服务化

TorchServe 把模型包成 `.mar`，提供 HTTP/gRPC 推理接口、多模型版本管理、批处理与指标。
最小链路是：`handler` 负责预处理/推理/后处理 → `model-config` 配 batch size 与 worker 数 →
启动服务后用 REST 调 `predictions/<model_name>`。
`serving/flask-server-example/` 则保留一个不依赖 TorchServe 的最轻对照实现，便于理解 handler 边界。

## 验证顺序

本地数值比对 → 目标运行时加载 → 单请求延迟 → 并发压测 → 再谈上线。模型文件本身按约定不入库。
