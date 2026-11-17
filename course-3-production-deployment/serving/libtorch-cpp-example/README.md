# LibTorch C++ 最小示例（Course 3）

`serving/` 下的可运行部署产物之一：用 **CMake + g++ 链接 LibTorch**，把一个 C++ 源文件
真正编译成可执行文件 `smoke_demo` 并运行。对应课程里「导出模型后由 libtorch (C++) 侧加载推理」这条链路。

## 文件

- `CMakeLists.txt` —— `find_package(Torch REQUIRED)`，链接 `${TORCH_LIBRARIES}`
- `src/smoke_demo.cpp` —— 构造张量与 `torch::nn::Linear`，跑一次前向并校验输出形状与数值

## CI 中的构建方式

CI 安装 CPU 版 PyTorch wheel，用 `torch.utils.cmake_prefix_path` 提供 `TorchConfig.cmake`：

```bash
# 在本目录内执行
TORCH_CMAKE_PREFIX="$(python -c 'import torch; print(torch.utils.cmake_prefix_path)')"
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH="$TORCH_CMAKE_PREFIX"
cmake --build build --parallel 2

TORCH_LIB="$(python -c 'import os, torch; print(os.path.join(os.path.dirname(torch.__file__), "lib"))')"
LD_LIBRARY_PATH="$TORCH_LIB:$LD_LIBRARY_PATH" ./build/smoke_demo
```

`LD_LIBRARY_PATH` 让可执行文件在运行时找到 `libtorch.so` / `libtorch_cpu.so`。
若改用官方预编译的 LibTorch zip，把 `CMAKE_PREFIX_PATH` 指向解压目录、
`LD_LIBRARY_PATH` 指向该目录的 `lib/` 即可，CMakeLists.txt 无需改动。

## 本地

> 本仓库约定：编译与运行全部由 GitHub Actions 完成，本地不执行编译。
> 上面的命令仅供把这个目录复制到实际项目时使用。
