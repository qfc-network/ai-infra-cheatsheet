# CUDA Versions & Compute Capability

Which sm_ target belongs to which architecture, and which toolkit still supports it. The sm_-to-family mapping is quoted from the CUDA 13.3 nvcc documentation; the GPU column is added for orientation.

| Name | sm_ targets | Representative GPUs | Added in CUDA | Notable additions | In CUDA 13.3? |
|---|---|---|---|---|---|
| Maxwell | sm_50, sm_52, sm_53 | GTX 900 series, Tesla M40 | CUDA 6.5 | unified memory improvements | dropped |
| Pascal | sm_60, sm_61 | P100 (60), P40 and GTX 10 series (61) | CUDA 8 | first NVLink, FP16 on P100 | dropped |
| Volta | sm_70, sm_72 | V100, Titan V | CUDA 9 | first Tensor Cores, independent thread scheduling | dropped |
| Turing | sm_75 | T4, RTX 20 series, Quadro RTX | CUDA 10 | INT8 and INT4 tensor ops, RT cores | yes - the oldest still supported, and nvcc's default target |
| Ampere | sm_80, sm_86, sm_87, sm_88 | A100 (80), A40 and RTX 30 (86), Jetson Orin (87) | CUDA 11 | TF32, BF16, 2:4 structured sparsity, MIG | yes |
| Ada Lovelace | sm_89 | L40S, L4, RTX 40 series, RTX 6000 Ada | CUDA 11.8 | FP8 tensor cores | yes |
| Hopper | sm_90, sm_90a | H100, H200, GH200 | CUDA 12 | FP8 Transformer Engine, TMA, thread block clusters, DPX | yes |
| Blackwell | sm_100, sm_103, sm_110, sm_120, sm_121 (each with f and a variants) | B200 and GB200, B300 and GB300, RTX 50 series, RTX PRO 6000 | CUDA 12.8 | FP4 tensor cores, second-generation Transformer Engine | yes |

> - CUDA 13 dropped Maxwell, Pascal and Volta. nvcc 13.3 accepts nothing older than sm_75, so a V100 needs a CUDA 12.x toolchain - worth checking before planning around older hardware.
> - The suffixes matter. A bare sm_90 target is forward-compatible; sm_90a is architecture-specific and unlocks instructions that exist only on that architecture (the Hopper wgmma path CUTLASS and FlashAttention-3 use). CUDA 13 adds an f suffix for family-specific targets, which sit between the two.
> - Compute capability is not performance. sm_87 (Jetson Orin) and sm_80 (A100) are both Ampere; they share features and share nothing else.
> - NVIDIA does not publish a product for every sm_ value. sm_88 is documented as Ampere and sm_110 as Blackwell, but the docs name no GPU for either, so this table does not guess one.
> - Minor version compatibility: since CUDA 11, an application built against one minor version runs on any later driver in the same major series, so you do not need to match toolkit and driver exactly.


---

[Back to index](../README.zh-CN.md)
