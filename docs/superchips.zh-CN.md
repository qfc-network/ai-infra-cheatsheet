# Grace 系列超级芯片

通过 NVLink-C2C 把 CPU 与 GPU 封装在一起，GPU 可缓存一致地访问 CPU 侧 LPDDR5X， 形成第二级大容量内存。

| 参数 | GH200 Grace Hopper | GB200 Grace Blackwell | GB300 Grace Blackwell Ultra | VR200 Vera Rubin (announced) |
|---|---|---|---|---|
| 组成 | 1 x Grace + 1 x H100/H200 | 1 x Grace + 2 x B200 | 1 x Grace + 2 x B300 | 1 x Vera + 2 x Rubin |
| CPU 核心 | 72 Arm Neoverse V2 | 72 Arm Neoverse V2 | 72 Arm Neoverse V2 | 88 custom Arm cores / 176 threads |
| HBM 显存 | 96 GB HBM3 or 144 GB HBM3e | 384 GB HBM3e | 576 GB HBM3e | 288 GB HBM4 per GPU |
| CPU 内存 | 480 GB LPDDR5X, ~500 GB/s | 480 GB LPDDR5X | up to 800 GB LPDDR5X | LPDDR5X（未公布） |
| NVLink-C2C | 900 GB/s | 900 GB/s | 900 GB/s | NVLink-C2C (next gen) |
| 对外 NVLink | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s per GPU | NVLink 5, 1.8 TB/s per GPU | NVLink 6 |
| 模组功耗 | up to 1,000 W | up to ~2,700 W | 约 3 kW 级 | 未公布 |
| 用于 | GH200 NVL2, MGX servers | GB200 NVL72, GB200 NVL2 | GB300 NVL72 | Vera Rubin NVL144 |
| 上市时间 | 2023-2024 | 2024-2025 | 2025 | 2026（路线图） |

> - 路线图产品来自公开发布信息，量产前规格可能变化。


## 资料来源

- [GH200 Grace Hopper](https://www.nvidia.com/en-us/data-center/grace-hopper-superchip/)
- [GB200 Grace Blackwell](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)
- [GB300 Grace Blackwell Ultra](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)
- [VR200 Vera Rubin (announced)](https://nvidianews.nvidia.com/news/nvidia-blackwell-ultra-ai-factory-platform-paves-way-for-age-of-ai-reasoning)

---

[返回目录](../README.md)
