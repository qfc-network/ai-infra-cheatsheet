# 桌面与本地 AI 主机

能摆在桌上直接跑模型的机器，分两条路线：统一内存（容量大、带宽中等） 和独立显卡（容量小、带宽极高）。能装下多大模型看容量，出词多快看带宽。

| 参数 | NVIDIA DGX Spark | GB10 OEM boxes | Ryzen AI Max+ 395 box | Mac mini (M5 Pro) | Mac Studio (M5 Max) | Mac Studio (M5 Ultra) | RTX 5090 desktop |
|---|---|---|---|---|---|---|---|
| 芯片 | GB10 Grace Blackwell（20 核 Arm） | GB10 Grace Blackwell（同一颗芯片） | AMD Ryzen AI Max+ 395（16 核 Zen 5 + Radeon 8060S） | Apple M5 Pro | Apple M5 Max | Apple M5 Ultra | GB202 独立显卡 |
| 可用于模型的内存 | 128 GB LPDDR5X 统一内存 | 128 GB LPDDR5X 统一内存 | 最高 128 GB 统一内存，其中最多 96 GB 可划为显存 | 24 / 48 / 64 GB 统一内存 | 36 / 48 / 64 / 128 GB 统一内存 | 96 / 256 / 512 GB 统一内存 | 32 GB GDDR7（仅显存） |
| 内存带宽 | 273 GB/s | 273 GB/s | 256 GB/s | 307 GB/s | 460-614 GB/s | 1.2 TB/s | 1,792 GB/s |
| 厂商标称算力 | 1 PFLOP FP4（稀疏） | 1 PFLOP FP4（稀疏） | NPU 50+ TOPS（INT8）；GPU 侧无可比的 FLOPS 口径 | 官方未给出可比口径 | 官方未给出可比口径 | 官方未给出可比口径 | 3,352 AI TOPS FP4（稀疏） |
| 低精度支持 | 原生 FP4 / FP8（Blackwell 张量核） | 原生 FP4 / FP8 | FP16 / INT8（RDNA 3.5，无 FP8 与 FP4） | 无 FP4/FP8 张量通路，走 GPU + 神经引擎 | 无 FP4/FP8 张量通路 | 无 FP4/FP8 张量通路 | 原生 FP4 / FP8 |
| 网络 | ConnectX-7 200 GbE + 10 GbE | ConnectX-7 200 GbE + 10 GbE | 2.5~10 GbE，视机型而定 | 10 GbE, Thunderbolt 5 | 10 GbE, Thunderbolt 5 | 10 GbE, Thunderbolt 5 | 取决于主板 |
| 多机互联 | 最多 4 台互联，约 700B 参数 | 与 DGX Spark 相同 | 无 | 只有雷雳，算不上互联网络 | 只有雷雳 | 只有雷雳 | 只有 PCIe，无 NVLink |
| 整机功耗 | 240 W 电源（芯片 TDP 140 W） | ~240 W | 芯片约 120 W，整机视机型 | 最大持续 155 W | 最大持续 480 W | 最大持续 480 W | 显卡 575 W，整机约 1 kW |
| 大致能跑到多大 | 单机 70B 四位量化 | 单机 70B 四位量化 | 在 96 GB 显存划分内可跑 70B 四位量化 | 64 GB 版可跑 32B 四位量化 | 128 GB 版可跑 70B 四位量化 | 512 GB 版可跑 400B+ 四位量化 | 30B 四位量化，32 GB 是硬上限 |
| 上市时间 | 2025 | 2025 | 2025 | 2026 | 2026 | 2026 | 2025 |

> - Ryzen AI Max+ 395 用在 Framework Desktop、GMKtec EVO-X2、HP ZBook Ultra G1a 以及 AMD 自己的 Ryzen AI Halo 开发平台上。它是 AMD 对标 DGX Spark 和 Mac Studio 的方案：统一内存、无 FP4、无集群网络。
> - "GB10 OEM 机型" 就是同一颗 GB10 换了个壳：华硕 Ascent GX10、戴尔 Pro Max with GB10、 惠普 ZGX Nano、联想和微星都有。差别在存储、机箱和价格，算力与带宽完全一样。
> - 看出词速度就看带宽。5090 的带宽是 DGX Spark 的 6.6 倍，但内存只有四分之一： Spark 能跑 5090 根本装不下的模型，而装得下的模型 5090 快得多。
> - 苹果没有公布可与 NVIDIA AI TOPS 对比的算力口径，且 Apple Silicon 没有 FP4/FP8 张量通路，4bit 模型要靠软件反量化。容量和带宽才是能诚实对比的两项。
> - 这些都不是集群硬件。这里只有 DGX Spark 的 ConnectX-7 算真正的互联网络，且最多 4 台； Mac 之间的雷雳连接和 NVLink、InfiniBand 不是一个量级。


## 资料来源

- [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
- [Ryzen AI Max+ 395 box](https://www.amd.com/en/products/processors/desktops/ryzen/ryzen-ai-halo/ryzen-ai-max-plus-395.html)
- [Mac mini (M5 Pro)](https://www.apple.com/mac-mini/specs/)
- [Mac Studio (M5 Max)](https://www.apple.com/mac-studio/specs/)
- [Mac Studio (M5 Ultra)](https://www.apple.com/mac-studio/specs/)
- [RTX 5090 desktop](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)

---

[返回目录](../README.md)
