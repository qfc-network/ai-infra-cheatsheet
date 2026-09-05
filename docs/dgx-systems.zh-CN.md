# DGX 整机

NVIDIA 官方整机产品线，从 2017 年的 DGX-1 到今天的 Blackwell Ultra 节点。 DGX-2 之后每一代都把机内 GPU 挂在同一个 NVSwitch 全互联域上， 只有 DGX-1 用的是 NVLink 直连网格。

| 参数 | DGX-1 (V100) | DGX-2 | DGX A100 | DGX H100 | DGX H200 | DGX B200 | DGX B300 |
|---|---|---|---|---|---|---|---|
| 架构 | Volta | Volta | Ampere | Hopper | Hopper | Blackwell | Blackwell Ultra |
| GPU | 8 x V100 SXM2 | 16 x V100 SXM3 | 8 x A100 SXM4 | 8 x H100 SXM5 | 8 x H200 SXM5 | 8 x B200 SXM | 8 x B300 SXM |
| 单卡显存 | 16 GB，后期 32 GB HBM2 | 32 GB HBM2 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180 GB HBM3e | 288 GB HBM3e |
| 整机显存 | 128 GB（32 GB 版 V100 为 256 GB） | 512 GB | 640 GB | 640 GB | 1,128 GB | 1,440 GB | 2.1 TB (NVIDIA spec) |
| 单卡显存带宽 | 900 GB/s | 900 GB/s | 2.0 TB/s | 3.35 TB/s | 4.8 TB/s | 8 TB/s (64 TB/s per node) | 8 TB/s |
| FP4（稀疏/稠密） | 不支持 | 不支持 | 不支持 | 无原生 FP4 | 无原生 FP4 | 144 / 72 PFLOPS | 144 / 108 PFLOPS |
| FP8（稀疏/稠密） | 不支持 | 不支持 | 不支持 | ~32 / 16 PFLOPS | ~32 / 16 PFLOPS | 72 / 36 PFLOPS | 72 / 36 PFLOPS |
| FP16/BF16 张量 | 1 PFLOPS（稠密） | 2 PFLOPS（稠密） | 5 PFLOPS（稀疏） | 约 16 PFLOPS（稀疏） | 约 16 PFLOPS（稀疏） | 36 PFLOPS（稀疏） | 36 PFLOPS（稀疏） |
| GPU 互联 | NVLink 2 立方网格直连（无 NVSwitch） | NVLink 2 / NVSwitch 1（12 颗） | NVLink 3 / NVSwitch 2 | NVLink 4 / NVSwitch 3 | NVLink 4 / NVSwitch 3 | NVLink 5 / NVSwitch 4 | NVLink 5 / NVSwitch 4 |
| 单卡 NVLink 带宽 | 300 GB/s | 300 GB/s | 600 GB/s | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| 集群网络 | 4 x 100 Gbit/s (EDR IB) + 2 x 10 GbE | 8 x 100 Gbit/s (EDR IB) | up to 8 x 200 Gbit/s (HDR IB) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 800 Gbit/s (ConnectX-8) |
| CPU | 2 x Intel Xeon E5-2698 v4 (20C) | 2 x Intel Xeon Platinum 8168 (24C) | 2 x AMD EPYC 7742 (64C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8570 (56C) | 2 x Intel Xeon 6776P |
| 系统内存 | 512 GB DDR4 | 1.5 TB DDR4 | 1 TB, up to 2 TB | 2 TB | 2 TB | 2 TB, up to 4 TB | 2 TB, up to 4 TB |
| 内置 NVMe | 4 x 1.92 TB SSD (RAID 0) | 8 x 3.84 TB NVMe + 2 x 960 GB (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB E1.S + 2 x 1.9 TB M.2 (OS) |
| 高度 | 3U | 10U | 6U | 8U | 8U | 10U | 10U |
| 最大功耗 | 3.5 kW | 10 kW | 6.5 kW | 10.2 kW | 10.2 kW | 14.3 kW | ~14 kW |
| 散热 | 风冷 | 风冷 | 风冷 | 风冷 | 风冷 | 风冷 | 风冷 |
| 发布时间 | 2017 | 2018 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - DGX-2 是唯一的 16 卡机型，其余 DGX 节点都是 8 卡；它也是 NVSwitch 的首发平台。
> - NVIDIA 官方页面标注 DGX B300 整机显存为 2.1 TB；按 B300 芯片 8 x 288 GB 计算应为 2.3 TB，说明出厂配置保留了一部分。
> - 未特别标注时算力为稠密值；NVIDIA 官方宣传数字通常是稀疏（2:4 结构化稀疏）值。
> - B200 芯片规格为 192 GB HBM3e，但 DGX B200 整机按每卡 180 GB 配置（整机 1,440 GB）。


## 资料来源

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

[返回目录](../README.md)
