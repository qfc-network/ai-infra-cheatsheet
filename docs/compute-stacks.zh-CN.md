# GPU 计算栈

CUDA 在各家的对应物。值得注意的是每一家都做了一条 CUDA 转换路径—— 这件事本身最能说明：生态是写给 CUDA 的，不是写给硬件的。

| 参数 | CUDA | ROCm | oneAPI / SYCL | Metal | CANN | MUSA |
|---|---|---|---|---|---|---|
| 厂商 | NVIDIA | AMD | Intel | Apple | 华为 | 摩尔线程 |
| 支持硬件 | 仅 NVIDIA GPU | Instinct MI 系列，部分 Radeon 与 Radeon PRO | Arc、Arc Pro、数据中心 GPU、至强 CPU | Apple Silicon | 昇腾 NPU | MTT 系列 GPU |
| 编程模型 | CUDA C++, PTX | HIP（刻意做成 CUDA 的样子） | SYCL / DPC++（Khronos 开放标准） | Metal Shading Language | Ascend C、AscendCL | MUSA C++（对标 CUDA） |
| CUDA 迁移路径 | 不适用——它就是别人要迁过来的目标 | HIPIFY 源码转换 | SYCLomatic 源码转换 | 没有，只能手工移植 | 无官方路径，需手工移植 | musify 源码转换 |
| 核心库 | cuBLAS, cuDNN, CUTLASS | rocBLAS, MIOpen, Composable Kernel | oneDNN, oneMKL | MPS, MPSGraph | 厂商自有算子库 | 对标 cuBLAS/cuDNN 的自有库 |
| 集合通信 | NCCL | RCCL | oneCCL | 无多机方案 | HCCL | MCCL |
| PyTorch 支持 | 一等公民，参考实现 | 已上游，有官方 ROCm wheel | 已上游的 XPU 后端 | MPS 后端，算子覆盖比 CUDA 窄 | torch_npu 插件，另有 vLLM / SGLang 后端 | torch_musa 插件 |
| 是否开源 | 否 | 是 | 是 | 否 | 部分开源 | 部分开源 |
| 起始年份 | 2007 | 2016 | 2020 | 2014 | 2018 | 2022 |

> - 这张表是编程模型层，也就是 CUDA 所在的那一层。框架在它上面： PyTorch、JAX、Apple 的 MLX 三者互为同类，而不是 CUDA 的同类。 MLX 特殊在它连算子层一起自己做了——PyTorch 把矩阵乘丢给 cuBLAS， MLX 自己写 Metal kernel——所以它横跨框架层和算子库层，但不在这一层。
> - 源码转换不等于二进制兼容。HIPIFY、SYCLomatic、musify 改的是你的源码， 跑不了现成的 CUDA 二进制；手写 PTX 或基于 CUTLASS 的算子通常还得真动手改。
> - 大多数人根本不用碰这一层。只要模型跑在 vLLM、SGLang 或 llama.cpp 上， 移植问题已经被引擎吃掉了——所以对多数读者来说，推理引擎那张表比这张更有用。
> - 差距体现在边缘地带：全新的注意力变体、自定义融合算子、论文的参考实现。 这些都先落在 CUDA 上，几个月后才到别的栈，甚至永远不到。
> - 集合通信是容易被忽略的依赖。多卡训练要快且正确就得靠 NCCL 或其对应物； RCCL 和 HCCL 是真实存在的，但整个生态的调优假设是围绕 NCCL 写的。


---

[返回目录](../README.md)
