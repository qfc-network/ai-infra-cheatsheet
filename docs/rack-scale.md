# Rack-Scale NVLink Systems

One rack behaves as a single large GPU: every GPU in the rack sits inside one NVLink domain instead of talking over the network.

| Parameter | GB200 NVL72 | GB300 NVL72 | Vera Rubin NVL144 (announced) |
|---|---|---|---|
| GPUs | 72 x B200 | 72 x B300 | 144 Rubin dies (72 packages) |
| CPUs | 36 x Grace | 36 x Grace | 36 x Vera |
| NVLink domain | 72 GPUs | 72 GPUs | 144 GPU dies |
| Aggregate NVLink BW | 130 TB/s | 130 TB/s | NVLink 6 switch |
| HBM capacity | 13.4 TB HBM3e | 20 TB HBM3e | ~21 TB HBM4 |
| Fast memory (HBM+LPDDR) | ~30 TB | 40 TB | ~75 TB |
| FP4 inference | 1.4 EFLOPS (sparse) | 1.1 EFLOPS (dense) | 3.6 EFLOPS |
| FP8 training | 720 PFLOPS (sparse) | 0.36 EFLOPS (dense) | 1.2 EFLOPS |
| Scale-out NIC | ConnectX-7 400 Gb/s / BlueField-3 | ConnectX-8 800 Gb/s / BlueField-3 | ConnectX-9 / Spectrum-X |
| Rack power | ~120 kW | ~130-140 kW | TBA |
| Cooling | liquid | liquid | liquid |
| Availability | 2024-2025 | 2025 | 2026 (roadmap) |

> - "GPU count" follows NVIDIA's convention: NVL72 counts packages, NVL144 counts reticle-sized dies. Both racks hold 72 GPU packages.


## Sources

- [GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)
- [GB300 NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)
- [Vera Rubin NVL144 (announced)](https://nvidianews.nvidia.com/news/nvidia-blackwell-ultra-ai-factory-platform-paves-way-for-age-of-ai-reasoning)

---

[Back to index](../README.zh-CN.md)
