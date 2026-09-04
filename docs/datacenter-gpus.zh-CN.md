# 数据中心旗舰 GPU（SXM）

用于 HGX 基板与 DGX 整机的 SXM 芯片级对比，所有数字均为单卡值。

| 参数 | A100 SXM4 | H100 SXM5 | H200 SXM5 | B200 SXM | B300 SXM |
|---|---|---|---|---|---|
| 架构 | Ampere (GA100) | Hopper (GH100) | Hopper (GH100) | Blackwell | Blackwell Ultra |
| 制程 | TSMC N7 | TSMC 4N | TSMC 4N | TSMC 4NP | TSMC 4NP |
| 晶体管数 | 54.2 B | 80 B | 80 B | 208 B | 208 B |
| 封装内 die 数 | 1 | 1 | 1 | 2（片间 10 TB/s） | 2（片间 10 TB/s） |
| 显存 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180-192 GB HBM3e | 288 GB HBM3e |
| 显存带宽 | 2,039 GB/s | 3,350 GB/s | 4,800 GB/s | 7.7-8 TB/s | 8 TB/s |
| FP64 / FP64 张量 | 9.7 / 19.5 TFLOPS | 34 / 67 TFLOPS | 34 / 67 TFLOPS | 40 TFLOPS (FP64 Tensor) | 相对 B200 大幅弱化 |
| TF32 张量（稠密） | 156 TFLOPS | 495 TFLOPS | 495 TFLOPS | 1.1 PFLOPS | 1.1 PFLOPS |
| FP16/BF16 张量（稠密） | 312 TFLOPS | 989 TFLOPS | 989 TFLOPS | 2.2 PFLOPS | 2.2 PFLOPS |
| FP8 张量（稠密） | 不支持 | 1,979 TFLOPS | 1,979 TFLOPS | 4.5 PFLOPS | 4.5 PFLOPS |
| FP4 张量（稠密） | 不支持 | 不支持 | 不支持 | 9 PFLOPS | 13.5 PFLOPS（GB300 中为 15 PFLOPS） |
| NVLink | NVLink 3, 600 GB/s | NVLink 4, 900 GB/s | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s | NVLink 5, 1.8 TB/s |
| 功耗 | 400 W (up to 500 W) | up to 700 W | up to 700 W | 1,000 W (1,200 W in GB200) | ~1,400 W |
| MIG 实例 | up to 7 | up to 7 | up to 7 | up to 7 | up to 7 |
| 上市时间 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - 稠密算力 x2 即为 NVIDIA 宣传常用的稀疏（2:4 结构化稀疏）算力。
> - 同一颗 die 会按功耗/显存分档：风冷 HGX/DGX 版本频率低于液冷超级芯片版本。


## 资料来源

- [A100 SXM4](https://www.nvidia.com/en-us/data-center/a100/)
- [H100 SXM5](https://www.nvidia.com/en-us/data-center/h100/)
- [H100 SXM5](https://resources.nvidia.com/en-us-hopper-architecture)
- [H200 SXM5](https://www.nvidia.com/en-us/data-center/h200/)
- [B200 SXM](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)
- [B200 SXM](https://resources.nvidia.com/en-us-blackwell-architecture)
- [B300 SXM](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)

---

[返回目录](../README.md)
