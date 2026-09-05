# Flagship Data Center GPUs (SXM)

Chip-level comparison of the SXM parts that go into HGX baseboards and DGX nodes. Numbers are per single GPU.

| Parameter | P100 SXM | V100 SXM2 | A100 SXM4 | H100 SXM5 | H200 SXM5 | B200 SXM | B300 SXM |
|---|---|---|---|---|---|---|---|
| Architecture | Pascal (GP100) | Volta (GV100) | Ampere (GA100) | Hopper (GH100) | Hopper (GH100) | Blackwell | Blackwell Ultra |
| Process | TSMC 16nm FinFET | TSMC 12nm FFN | TSMC N7 | TSMC 4N | TSMC 4N | TSMC 4NP | TSMC 4NP |
| Transistors | 15.3 B | 21.1 B | 54.2 B | 80 B | 80 B | 208 B | 208 B |
| Dies per package | 1 | 1 | 1 | 1 | 1 | 2 (chip-to-chip 10 TB/s) | 2 (chip-to-chip 10 TB/s) |
| Memory | 16 GB HBM2 | 16 or 32 GB HBM2 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180-192 GB HBM3e | 288 GB HBM3e |
| Memory bandwidth | 732 GB/s | 900 GB/s | 2,039 GB/s | 3,350 GB/s | 4,800 GB/s | 7.7-8 TB/s | 8 TB/s |
| FP64 / FP64 Tensor | 5.3 TFLOPS / no FP64 Tensor | 7.8 TFLOPS / no FP64 Tensor | 9.7 / 19.5 TFLOPS | 34 / 67 TFLOPS | 34 / 67 TFLOPS | 40 TFLOPS (FP64 Tensor) | de-emphasized vs B200 |
| TF32 Tensor (dense) | not supported | not supported | 156 TFLOPS | 495 TFLOPS | 495 TFLOPS | 1.1 PFLOPS | 1.1 PFLOPS |
| FP16/BF16 Tensor (dense) | no Tensor Cores (21.2 TFLOPS FP16 vector) | 125 TFLOPS (FP16 only, no BF16) | 312 TFLOPS | 989 TFLOPS | 989 TFLOPS | 2.2 PFLOPS | 2.2 PFLOPS |
| FP8 Tensor (dense) | not supported | not supported | not supported | 1,979 TFLOPS | 1,979 TFLOPS | 4.5 PFLOPS | 4.5 PFLOPS |
| FP4 Tensor (dense) | not supported | not supported | not supported | not supported | not supported | 9 PFLOPS | 13.5 PFLOPS (15 PFLOPS in GB300) |
| NVLink | NVLink 1, 160 GB/s | NVLink 2, 300 GB/s | NVLink 3, 600 GB/s | NVLink 4, 900 GB/s | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s | NVLink 5, 1.8 TB/s |
| TDP | 300 W | 300 W (350 W SXM3) | 400 W (up to 500 W) | up to 700 W | up to 700 W | 1,000 W (1,200 W in GB200) | ~1,400 W |
| MIG instances | not supported | not supported | up to 7 | up to 7 | up to 7 | up to 7 | up to 7 |
| Launch | 2016 | 2017 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - Volta and Pascal predate structured sparsity, TF32, BF16 and MIG; V100 Tensor Cores are FP16-only.
> - Multiply the dense numbers by 2 for the sparse (2:4 structured sparsity) figures NVIDIA quotes in marketing material.
> - The same die ships in different power/memory bins: HGX/DGX air-cooled parts are clocked lower than the liquid-cooled superchip variants.


## Sources

- [P100 SXM](https://www.nvidia.com/en-us/data-center/tesla-p100/)
- [V100 SXM2](https://www.nvidia.com/en-us/data-center/v100/)
- [A100 SXM4](https://www.nvidia.com/en-us/data-center/a100/)
- [H100 SXM5](https://www.nvidia.com/en-us/data-center/h100/)
- [H100 SXM5](https://resources.nvidia.com/en-us-hopper-architecture)
- [H200 SXM5](https://www.nvidia.com/en-us/data-center/h200/)
- [B200 SXM](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)
- [B200 SXM](https://resources.nvidia.com/en-us-blackwell-architecture)
- [B300 SXM](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)

---

[Back to index](../README.zh-CN.md)
