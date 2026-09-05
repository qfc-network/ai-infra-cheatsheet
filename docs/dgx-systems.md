# DGX Systems

NVIDIA's own appliance line, from the 2017 DGX-1 to today's Blackwell Ultra nodes. Every generation since DGX-2 puts all GPUs in the box on one NVSwitch fabric; DGX-1 used a direct NVLink mesh instead.

| Parameter | DGX-1 (V100) | DGX-2 | DGX A100 | DGX H100 | DGX H200 | DGX B200 | DGX B300 |
|---|---|---|---|---|---|---|---|
| Architecture | Volta | Volta | Ampere | Hopper | Hopper | Blackwell | Blackwell Ultra |
| GPU | 8 x V100 SXM2 | 16 x V100 SXM3 | 8 x A100 SXM4 | 8 x H100 SXM5 | 8 x H200 SXM5 | 8 x B200 SXM | 8 x B300 SXM |
| Memory per GPU | 16 GB, later 32 GB HBM2 | 32 GB HBM2 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180 GB HBM3e | 288 GB HBM3e |
| Total GPU memory | 128 GB (256 GB with 32 GB V100) | 512 GB | 640 GB | 640 GB | 1,128 GB | 1,440 GB | 2.1 TB (NVIDIA spec) |
| Memory bandwidth/GPU | 900 GB/s | 900 GB/s | 2.0 TB/s | 3.35 TB/s | 4.8 TB/s | 8 TB/s (64 TB/s per node) | 8 TB/s |
| FP4 (sparse/dense) | not supported | not supported | not supported | no native FP4 | no native FP4 | 144 / 72 PFLOPS | 144 / 108 PFLOPS |
| FP8 (sparse/dense) | not supported | not supported | not supported | ~32 / 16 PFLOPS | ~32 / 16 PFLOPS | 72 / 36 PFLOPS | 72 / 36 PFLOPS |
| FP16/BF16 Tensor | 1 PFLOPS (dense) | 2 PFLOPS (dense) | 5 PFLOPS (sparse) | ~16 PFLOPS (sparse) | ~16 PFLOPS (sparse) | 36 PFLOPS (sparse) | 36 PFLOPS (sparse) |
| GPU interconnect | NVLink 2 hybrid cube mesh (no NVSwitch) | NVLink 2 / NVSwitch 1 (12 switches) | NVLink 3 / NVSwitch 2 | NVLink 4 / NVSwitch 3 | NVLink 4 / NVSwitch 3 | NVLink 5 / NVSwitch 4 | NVLink 5 / NVSwitch 4 |
| NVLink BW per GPU | 300 GB/s | 300 GB/s | 600 GB/s | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| Cluster network | 4 x 100 Gbit/s (EDR IB) + 2 x 10 GbE | 8 x 100 Gbit/s (EDR IB) | up to 8 x 200 Gbit/s (HDR IB) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 800 Gbit/s (ConnectX-8) |
| CPU | 2 x Intel Xeon E5-2698 v4 (20C) | 2 x Intel Xeon Platinum 8168 (24C) | 2 x AMD EPYC 7742 (64C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8570 (56C) | 2 x Intel Xeon 6776P |
| System memory | 512 GB DDR4 | 1.5 TB DDR4 | 1 TB, up to 2 TB | 2 TB | 2 TB | 2 TB, up to 4 TB | 2 TB, up to 4 TB |
| Internal NVMe | 4 x 1.92 TB SSD (RAID 0) | 8 x 3.84 TB NVMe + 2 x 960 GB (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB E1.S + 2 x 1.9 TB M.2 (OS) |
| Height | 3U | 10U | 6U | 8U | 8U | 10U | 10U |
| Max power | 3.5 kW | 10 kW | 6.5 kW | 10.2 kW | 10.2 kW | 14.3 kW | ~14 kW |
| Cooling | air | air | air | air | air | air | air |
| Announced | 2017 | 2018 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - DGX-2 is the odd one out at 16 GPUs; every other DGX node here is an 8-GPU system. It was also the debut of NVSwitch.
> - DGX B300 GPU memory is listed by NVIDIA as 2.1 TB per node; 8 x 288 GB of B300 chip capacity would be 2.3 TB, so the shipping configuration reserves part of it.
> - Peak FLOPS are dense unless a sparse/dense pair is given; NVIDIA marketing numbers usually quote the sparse (2:4 structured sparsity) figure.
> - B200 is documented as 192 GB HBM3e at the chip level; DGX B200 ships a 180 GB per-GPU configuration (1,440 GB per node).


## Sources

- [DGX-1 (V100)](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/dgx-1/NVIDIA-DGX-1-Volta-AI-Supercomputer-Datasheet.pdf)
- [DGX-1 (V100)](https://images.nvidia.com/content/pdf/dgx1-v100-system-architecture-whitepaper.pdf)
- [DGX-2](https://images.nvidia.com/content/pdf/dgx-2-datasheet-us-nvidia-848202-r3-web.pdf)
- [DGX A100](https://www.nvidia.com/en-us/data-center/dgx-a100/)
- [DGX H100](https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html)
- [DGX H100](https://resources.nvidia.com/en-us-dgx-systems/ai-enterprise-dgx)
- [DGX H200](https://www.nvidia.com/en-us/data-center/dgx-platform/)
- [DGX H200](https://www.nvidia.com/en-us/data-center/h200/)
- [DGX B200](https://www.nvidia.com/en-us/data-center/dgx-b200/)
- [DGX B200](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)
- [DGX B300](https://www.nvidia.com/en-us/data-center/dgx-b300/)

---

[Back to index](../README.zh-CN.md)
