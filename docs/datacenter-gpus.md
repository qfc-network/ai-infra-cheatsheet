# Flagship Data Center GPUs (SXM)

Chip-level comparison of the SXM parts that go into HGX baseboards and DGX nodes. Numbers are per single GPU.

| Parameter | A100 SXM4 | H100 SXM5 | H200 SXM5 | B200 SXM | B300 SXM |
|---|---|---|---|---|---|
| Architecture | Ampere (GA100) | Hopper (GH100) | Hopper (GH100) | Blackwell | Blackwell Ultra |
| Process | TSMC N7 | TSMC 4N | TSMC 4N | TSMC 4NP | TSMC 4NP |
| Transistors | 54.2 B | 80 B | 80 B | 208 B | 208 B |
| Dies per package | 1 | 1 | 1 | 2 (chip-to-chip 10 TB/s) | 2 (chip-to-chip 10 TB/s) |
| Memory | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180-192 GB HBM3e | 288 GB HBM3e |
| Memory bandwidth | 2,039 GB/s | 3,350 GB/s | 4,800 GB/s | 7.7-8 TB/s | 8 TB/s |
| FP64 / FP64 Tensor | 9.7 / 19.5 TFLOPS | 34 / 67 TFLOPS | 34 / 67 TFLOPS | 40 TFLOPS (FP64 Tensor) | de-emphasized vs B200 |
| TF32 Tensor (dense) | 156 TFLOPS | 495 TFLOPS | 495 TFLOPS | 1.1 PFLOPS | 1.1 PFLOPS |
| FP16/BF16 Tensor (dense) | 312 TFLOPS | 989 TFLOPS | 989 TFLOPS | 2.2 PFLOPS | 2.2 PFLOPS |
| FP8 Tensor (dense) | not supported | 1,979 TFLOPS | 1,979 TFLOPS | 4.5 PFLOPS | 4.5 PFLOPS |
| FP4 Tensor (dense) | not supported | not supported | not supported | 9 PFLOPS | 13.5 PFLOPS (15 PFLOPS in GB300) |
| NVLink | NVLink 3, 600 GB/s | NVLink 4, 900 GB/s | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s | NVLink 5, 1.8 TB/s |
| TDP | 400 W (up to 500 W) | up to 700 W | up to 700 W | 1,000 W (1,200 W in GB200) | ~1,400 W |
| MIG instances | up to 7 | up to 7 | up to 7 | up to 7 | up to 7 |
| Launch | 2020 | 2022 | 2023 | 2024 | 2025 |

> - Multiply the dense numbers by 2 for the sparse (2:4 structured sparsity) figures NVIDIA quotes in marketing material.
> - The same die ships in different power/memory bins: HGX/DGX air-cooled parts are clocked lower than the liquid-cooled superchip variants.


## Sources

- [A100 SXM4](https://www.nvidia.com/en-us/data-center/a100/)
- [H100 SXM5](https://www.nvidia.com/en-us/data-center/h100/)
- [H100 SXM5](https://resources.nvidia.com/en-us-hopper-architecture)
- [H200 SXM5](https://www.nvidia.com/en-us/data-center/h200/)
- [B200 SXM](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)
- [B200 SXM](https://resources.nvidia.com/en-us-blackwell-architecture)
- [B300 SXM](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)

---

[Back to index](../README.zh-CN.md)
