# Consumer & Workstation GPUs

What people actually run local LLMs on. For inference the binding constraint is VRAM first and memory bandwidth second — peak FLOPS rarely decides anything.

| Parameter | RTX 2080 Ti | RTX 3090 | RTX 4090 | RTX 5090 | RTX PRO 6000 Blackwell |
|---|---|---|---|---|---|
| Architecture | Turing (TU102) | Ampere (GA102) | Ada Lovelace (AD102) | Blackwell (GB202) | Blackwell (GB202) |
| VRAM | 11 GB GDDR6 | 24 GB GDDR6X | 24 GB GDDR6X | 32 GB GDDR7 | 96 GB GDDR7 |
| Memory bandwidth | 616 GB/s | 936 GB/s | 1,008 GB/s | 1,792 GB/s | 1,792 GB/s |
| Lowest native precision | FP16 / INT8 (no BF16) | BF16 / INT8 | FP8 | FP4 | FP4 |
| NVIDIA tensor figure | ~108 TFLOPS FP16 (FP16 accumulate) | 285 TFLOPS FP16 (sparse) | 1,321 AI TOPS (FP8, sparse) | 3,352 AI TOPS (FP4, sparse) | 4,000 AI TOPS (FP4, sparse) |
| GPU-to-GPU link | NVLink 2 bridge, 100 GB/s (2 GPUs) | NVLink 3 bridge, 112.5 GB/s (2 GPUs) | PCIe 4.0 x16 only - no NVLink | PCIe 5.0 x16 only - no NVLink | PCIe 5.0 x16 only - no NVLink |
| ECC memory | no | no | no | no | yes |
| Board power | 250-260 W | 350 W | 450 W | 575 W | 600 W |
| Rough local LLM fit | 7-8B at 4-bit | ~30B at 4-bit, 14B at 8-bit | ~30B at 4-bit, 14B at 8-bit | ~30B at 4-bit with long context, 32B comfortable | 70B at 8-bit, 120B+ at 4-bit |
| Launch | 2018 | 2020 | 2022 | 2025 | 2025 |

> - The "NVIDIA tensor figure" row is NOT comparable across generations: NVIDIA quotes FP16 for Turing/Ampere, FP8 for Ada and FP4 for Blackwell, all with sparsity from Ampere on. A 5090 is not 2.5x a 4090 at the same precision.
> - NVLink is gone from GeForce after the RTX 3090. On a 4090/5090 box, multi-GPU tensor parallelism runs over PCIe, which is roughly an order of magnitude slower than the 1.8 TB/s NVLink inside a DGX node — fine for pipeline-parallel or per-GPU replicas, painful for tensor parallelism.
> - GeForce cards have no ECC and no MIG, and NVIDIA's GeForce driver licence restricts data center deployment. Read the licence yourself before renting them out; this is the main reason hosting providers buy RTX PRO or data center SKUs.
> - "Rough local LLM fit" assumes weights plus a modest KV cache. Long context, batching, or unquantized weights all move the ceiling down sharply.


## Sources

- [RTX 2080 Ti](https://www.nvidia.com/content/geforce-gtx/GEFORCE_RTX_2080Ti_User_Guide.pdf)
- [RTX 2080 Ti](https://developer.nvidia.com/blog/nvidia-turing-architecture-in-depth/)
- [RTX 3090](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/)
- [RTX 3090](https://www.nvidia.com/content/PDF/nvidia-ampere-ga-102-gpu-architecture-whitepaper-v2.1.pdf)
- [RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
- [RTX 5090](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)
- [RTX PRO 6000 Blackwell](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/)

---

[Back to index](../README.zh-CN.md)
