# Grace-based Superchips

CPU+GPU packages joined by NVLink-C2C, giving the GPU cache-coherent access to the CPU's LPDDR5X as a second memory tier.

| Parameter | GH200 Grace Hopper | GB200 Grace Blackwell | GB300 Grace Blackwell Ultra | VR200 Vera Rubin (announced) |
|---|---|---|---|---|
| Composition | 1 x Grace + 1 x H100/H200 | 1 x Grace + 2 x B200 | 1 x Grace + 2 x B300 | 1 x Vera + 2 x Rubin |
| CPU cores | 72 Arm Neoverse V2 | 72 Arm Neoverse V2 | 72 Arm Neoverse V2 | 88 custom Arm cores / 176 threads |
| HBM | 96 GB HBM3 or 144 GB HBM3e | 384 GB HBM3e | 576 GB HBM3e | 288 GB HBM4 per GPU |
| CPU memory | 480 GB LPDDR5X, ~500 GB/s | 480 GB LPDDR5X | up to 800 GB LPDDR5X | LPDDR5X (TBA) |
| NVLink-C2C | 900 GB/s | 900 GB/s | 900 GB/s | NVLink-C2C (next gen) |
| External NVLink | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s per GPU | NVLink 5, 1.8 TB/s per GPU | NVLink 6 |
| Module power | up to 1,000 W | up to ~2,700 W | ~3 kW class | TBA |
| Used in | GH200 NVL2, MGX servers | GB200 NVL72, GB200 NVL2 | GB300 NVL72 | Vera Rubin NVL144 |
| Availability | 2023-2024 | 2024-2025 | 2025 | 2026 (roadmap) |

> - Roadmap parts are listed from public announcements and may change before shipping.


## Sources

- [GH200 Grace Hopper](https://www.nvidia.com/en-us/data-center/grace-hopper-superchip/)
- [GB200 Grace Blackwell](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)
- [GB300 Grace Blackwell Ultra](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)
- [VR200 Vera Rubin (announced)](https://nvidianews.nvidia.com/news/nvidia-blackwell-ultra-ai-factory-platform-paves-way-for-age-of-ai-reasoning)

---

[Back to index](../README.zh-CN.md)
