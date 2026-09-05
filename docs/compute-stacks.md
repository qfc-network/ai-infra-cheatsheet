# GPU Compute Stacks

CUDA's counterparts, one per vendor. Note that every one of them ships a CUDA translation path - that fact is the clearest measure of how much of the ecosystem is written against CUDA rather than against the hardware.

| Parameter | CUDA | ROCm | oneAPI / SYCL | Metal | CANN | MUSA |
|---|---|---|---|---|---|---|
| Vendor | NVIDIA | AMD | Intel | Apple | Huawei | Moore Threads |
| Runs on | NVIDIA GPUs only | Instinct MI series, some Radeon and Radeon PRO | Arc, Arc Pro, Data Center GPU, Xeon CPU | Apple Silicon | Ascend NPUs | MTT GPUs |
| Programming model | CUDA C++, PTX | HIP (deliberately CUDA-shaped C++) | SYCL / DPC++ (Khronos open standard) | Metal Shading Language | Ascend C, AscendCL | MUSA C++ (CUDA-shaped) |
| CUDA porting path | n/a - this is the target everyone ports to | HIPIFY source translation | SYCLomatic source translation | none - port by hand | none official - port by hand | musify source translation |
| Core libraries | cuBLAS, cuDNN, CUTLASS | rocBLAS, MIOpen, Composable Kernel | oneDNN, oneMKL | MPS, MPSGraph | vendor kernel libraries | vendor equivalents of cuBLAS/cuDNN |
| Collectives | NCCL | RCCL | oneCCL | none for multi-node | HCCL | MCCL |
| PyTorch support | first-class, the reference backend | upstream, ROCm wheels published | upstream XPU backend | MPS backend, narrower op coverage than CUDA | torch_npu plugin, plus vLLM and SGLang backends | torch_musa plugin |
| Open source | no | yes | yes | no | partially | partially |
| Since | 2007 | 2016 | 2020 | 2014 | 2018 | 2022 |

> - This table is the programming-model layer, the one CUDA occupies. Frameworks sit above it: PyTorch, JAX and Apple's MLX are peers of each other, not of CUDA. MLX is unusual in owning its kernel layer too - PyTorch hands matmuls to cuBLAS, while MLX writes its own Metal kernels - so it spans the framework and library rows but not this one.
> - Source translation is not binary compatibility. HIPIFY, SYCLomatic and musify rewrite your source; they do not run an existing CUDA binary, and hand-tuned PTX or a CUTLASS-derived kernel usually needs real work.
> - Most people never touch any of this. If your models run under vLLM, SGLang or llama.cpp, the engine has already absorbed the porting problem - which is why the inference engine table matters more than this one for most readers.
> - The gap shows up at the edges: a brand-new attention variant, a custom fused kernel, a paper's reference implementation. Those land on CUDA first and reach other stacks months later, if at all.
> - Collectives are the quiet dependency. Multi-GPU training needs NCCL or its equivalent to be fast and correct; RCCL and HCCL are real, but the ecosystem's tuning assumptions are written around NCCL.


---

[Back to index](../README.zh-CN.md)
