# NVLink / NVSwitch 各代对比

单卡 NVLink 带宽为所有链路的双向合计值（与 NVIDIA 官方口径一致）。

| 名称 | 代次 | 首发 GPU | 年份 | 单链路带宽 | 单卡链路数 | 单卡总带宽 | 配套交换 | 最大互联规模 |
|---|---|---|---|---|---|---|---|---|
| NVLink 1 | 1 | P100 | 2016 | 40 GB/s | 4 | 160 GB/s | 无 | 8（立方网格） |
| NVLink 2 | 2 | V100 | 2017 | 50 GB/s | 6 | 300 GB/s | NVSwitch 1 | 16 (DGX-2) |
| NVLink 3 | 3 | A100 | 2020 | 50 GB/s | 12 | 600 GB/s | NVSwitch 2 | 单机 8 卡，经 NVLink Switch 可 16 卡 |
| NVLink 4 | 4 | H100 | 2022 | 50 GB/s | 18 | 900 GB/s | NVSwitch 3 | 单机 8 卡，NVLink Switch System 最多 256 卡 |
| NVLink 5 | 5 | B200 / B300 | 2024 | 100 GB/s | 18 | 1.8 TB/s | NVLink Switch（单芯片 7.2 TB/s） | 单柜 72 卡（NVL72），跨柜可达 576 卡 |

> - NVLink-C2C 是 Grace 超级芯片内部 900 GB/s 的 CPU-GPU 互联，与 GPU 间 NVLink 不是同一条链路。


---

[返回目录](../README.md)
