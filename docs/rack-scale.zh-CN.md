# 机柜级 NVLink 系统

整机柜当作一块大 GPU 使用：柜内所有 GPU 处于同一个 NVLink 域内，卡间通信不走网络。

| 参数 | GB200 NVL72 | GB300 NVL72 | Vera Rubin NVL144 (announced) |
|---|---|---|---|
| GPU 数量 | 72 x B200 | 72 x B300 | 144 Rubin dies (72 packages) |
| CPU 数量 | 36 x Grace | 36 x Grace | 36 x Vera |
| NVLink 域 | 72 GPUs | 72 GPUs | 144 GPU dies |
| NVLink 总带宽 | 130 TB/s | 130 TB/s | NVLink 6 交换 |
| HBM 容量 | 13.4 TB HBM3e | 20 TB HBM3e | ~21 TB HBM4 |
| 快速内存（HBM+LPDDR） | ~30 TB | 40 TB | ~75 TB |
| FP4 推理算力 | 1.4 EFLOPS（稀疏） | 1.1 EFLOPS（稠密） | 3.6 EFLOPS |
| FP8 训练算力 | 720 PFLOPS（稀疏） | 0.36 EFLOPS（稠密） | 1.2 EFLOPS |
| 横向扩展网卡 | ConnectX-7 400 Gb/s / BlueField-3 | ConnectX-8 800 Gb/s / BlueField-3 | ConnectX-9 / Spectrum-X |
| 机柜功耗 | ~120 kW | ~130-140 kW | 未公布 |
| 散热 | 液冷 | 液冷 | 液冷 |
| 上市时间 | 2024-2025 | 2025 | 2026（路线图） |

> - "GPU 数量" 沿用 NVIDIA 的口径：NVL72 按封装计数，NVL144 按 die 计数， 两者机柜内都是 72 个 GPU 封装。


## 资料来源

- [GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)
- [GB300 NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)
- [Vera Rubin NVL144 (announced)](https://nvidianews.nvidia.com/news/nvidia-blackwell-ultra-ai-factory-platform-paves-way-for-age-of-ai-reasoning)

---

[返回目录](../README.md)
