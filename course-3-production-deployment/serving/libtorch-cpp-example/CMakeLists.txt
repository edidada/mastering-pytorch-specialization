cmake_minimum_required(VERSION 3.18)
project(mastering_pytorch_libtorch LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Locates TorchConfig.cmake via CMAKE_PREFIX_PATH (see the workflow / README).
find_package(Torch REQUIRED)

add_executable(smoke_demo src/smoke_demo.cpp)
target_link_libraries(smoke_demo PRIVATE "${TORCH_LIBRARIES}")
target_compile_options(smoke_demo PRIVATE ${TORCH_CXX_FLAGS})
