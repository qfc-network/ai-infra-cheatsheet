# DGX Systems (8-GPU nodes)

NVIDIA's own 8-GPU appliance line. One node = 8 SXM GPUs on a single NVSwitch fabric, dual x86 CPUs, and 8-10 network ports for scale-out.

| Parameter | DGX A100 | DGX H100 | DGX H200 | DGX B200 | DGX B300 |
|---|---|---|---|---|---|
| Architecture | Ampere | Hopper | Hopper | Blackwell | Blackwell Ultra |
| GPU | 8 x A100 SXM4 | 8 x H100 SXM5 | 8 x H200 SXM5 | 8 x B200 SXM | 8 x B300 SXM |
| Memory per GPU | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180 GB HBM3e | 288 GB HBM3e |
| Total GPU memory | 640 GB | 640 GB | 1,128 GB | 1,440 GB | 2.1 TB (NVIDIA spec) |
| Memory bandwidth/GPU | 2.0 TB/s | 3.35 TB/s | 4.8 TB/s | 8 TB/s (64 TB/s per node) | 8 TB/s |
| FP4 (sparse/dense) | not supported | no native FP4 | no native FP4 | 144 / 72 PFLOPS | 144 / 108 PFLOPS |
| FP8 (sparse/dense) | not supported | ~32 / 16 PFLOPS | ~32 / 16 PFLOPS | 72 / 36 PFLOPS | 72 / 36 PFLOPS |
| FP16/BF16 (sparse) | 5 PFLOPS | ~16 PFLOPS | ~16 PFLOPS | 36 PFLOPS | 36 PFLOPS |
| GPU interconnect | NVLink 3 / NVSwitch 2 | NVLink 4 / NVSwitch 3 | NVLink 4 / NVSwitch 3 | NVLink 5 / NVSwitch 4 | NVLink 5 / NVSwitch 4 |
| NVLink BW per GPU | 600 GB/s | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| Cluster network | up to 8 x 200 Gbit/s (HDR IB) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 800 Gbit/s (ConnectX-8) |
| CPU | 2 x AMD EPYC 7742 (64C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8570 (56C) | 2 x Intel Xeon 6776P |
| System memory | 1 TB, up to 2 TB | 2 TB | 2 TB | 2 TB, up to 4 TB | 2 TB, up to 4 TB |
| Internal NVMe | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB E1.S + 2 x 1.9 TB M.2 (OS) |
| Height | 6U | 8U | 8U | 10U | 10U |
| Max power | 6.5 kW | 10.2 kW | 10.2 kW | 14.3 kW | ~14 kW |
| Cooling | air | air | air | air | air |
| Announced | 2020 | 2022 | 2023 | 2024 | 2025 |

> - DGX B300 GPU memory is listed by NVIDIA as 2.1 TB per node; 8 x 288 GB of B300 chip capacity would be 2.3 TB, so the shipping configuration reserves part of it.
> - Peak FLOPS are dense unless a sparse/dense pair is given; NVIDIA marketing numbers usually quote the sparse (2:4 structured sparsity) figure.
> - B200 is documented as 192 GB HBM3e at the chip level; DGX B200 ships a 180 GB per-GPU configuration (1,440 GB per node).


## Sources

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
