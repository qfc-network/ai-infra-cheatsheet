# DGX 整机（8 卡节点）

NVIDIA 官方的 8 卡整机产品线。一台 = 8 张 SXM GPU + 单机内 NVSwitch 全互联 + 双路 x86 CPU + 8~10 个横向扩展网口。

| 参数 | DGX A100 | DGX H100 | DGX H200 | DGX B200 | DGX B300 |
|---|---|---|---|---|---|
| 架构 | Ampere | Hopper | Hopper | Blackwell | Blackwell Ultra |
| GPU | 8 x A100 SXM4 | 8 x H100 SXM5 | 8 x H200 SXM5 | 8 x B200 SXM | 8 x B300 SXM |
| 单卡显存 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180 GB HBM3e | 288 GB HBM3e |
| 整机显存 | 640 GB | 640 GB | 1,128 GB | 1,440 GB | 2,304 GB |
| 单卡显存带宽 | 2.0 TB/s | 3.35 TB/s | 4.8 TB/s | 7.7 TB/s | 8 TB/s |
| FP4（稀疏/稠密） | 不支持 | 无原生 FP4 | 无原生 FP4 | 144 / 72 PFLOPS | 144 / 108 PFLOPS |
| FP8（稀疏/稠密） | 不支持 | ~32 / 16 PFLOPS | ~32 / 16 PFLOPS | 72 / 36 PFLOPS | 72 / 36 PFLOPS |
| FP16/BF16（稀疏） | 5 PFLOPS | ~16 PFLOPS | ~16 PFLOPS | 36 PFLOPS | 36 PFLOPS |
| GPU 互联 | NVLink 3 / NVSwitch 2 | NVLink 4 / NVSwitch 3 | NVLink 4 / NVSwitch 3 | NVLink 5 / NVSwitch 4 | NVLink 5 / NVSwitch 4 |
| 单卡 NVLink 带宽 | 600 GB/s | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| 集群网络 | up to 8 x 200 Gbit/s (HDR IB) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 800 Gbit/s (ConnectX-8) |
| CPU | 2 x AMD EPYC 7742 (64C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8570 (56C) | 2 x Intel Xeon 6 (6776P class) |
| 系统内存 | 1 TB, up to 2 TB | 2 TB | 2 TB | 2 TB, up to 4 TB | 2 TB, up to 4 TB |
| 内置 NVMe | 30 TB U.2 NVMe | 30 TB U.2 NVMe | 30 TB U.2 NVMe | 30 TB U.2 NVMe | 30 TB U.2 NVMe |
| 高度 | 6U | 8U | 8U | 10U | 10U |
| 最大功耗 | 6.5 kW | 10.2 kW | 10.2 kW | 14.3 kW | ~14-15 kW |
| 散热 | 风冷 | 风冷 | 风冷 | 风冷 | 风冷 |
| 发布时间 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - 未特别标注时算力为稠密值；NVIDIA 官方宣传数字通常是稀疏（2:4 结构化稀疏）值。
> - B200 芯片规格为 192 GB HBM3e，但 DGX B200 整机按每卡 180 GB 配置（整机 1,440 GB）。


## 资料来源

- [DGX A100](https://www.nvidia.com/en-us/data-center/dgx-a100/)
- [DGX H100](https://www.nvidia.com/en-us/data-center/dgx-h100/)
- [DGX H100](https://resources.nvidia.com/en-us-dgx-systems/ai-enterprise-dgx)
- [DGX H200](https://www.nvidia.com/en-us/data-center/dgx-platform/)
- [DGX H200](https://www.nvidia.com/en-us/data-center/h200/)
- [DGX B200](https://www.nvidia.com/en-us/data-center/dgx-b200/)
- [DGX B200](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)
- [DGX B300](https://www.nvidia.com/en-us/data-center/dgx-b300/)

---

[返回目录](../README.md)
