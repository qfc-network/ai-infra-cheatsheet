# 数据中心 - NVIDIA / AMD / Intel 对位

谁和谁对位，以及真正拉开差距的是什么。AMD 的杠杆是显存容量， Intel 的是片上以太网和价格，NVIDIA 的是互联域规模和软件。 这张表没有苹果，因为它不卖数据中心加速卡。

| 名称 | 时期 | NVIDIA | NVIDIA 显存 | AMD | AMD 显存 | Intel | Intel 显存 | 决定因素 |
|---|---|---|---|---|---|---|---|---|
| Hopper vs CDNA 3 | 2023 | H100 SXM | 80 GB | MI300X | 192 GB | Gaudi 2 | 96 GB | AMD 装得下 H100 装不下的模型；NVIDIA 赢在软件成熟度和 256 卡 NVLink 域 |
| Hopper refresh vs CDNA 3 refresh | 2024 | H200 SXM | 141 GB | MI325X | 256 GB | Gaudi 3 | 128 GB | 同一组对位，双方都加了 HBM；AMD 容量仍约为 1.8 倍 |
| Blackwell vs CDNA 4 | 2025 | B200 SXM | 180 GB | MI355X | 288 GB | Gaudi 3（无后继在售） | 128 GB | 双方第一次都有原生 4bit，但格式互不兼容（NVFP4 与 MXFP4）；Gaudi 3 完全没有 FP4 |
| Blackwell Ultra vs CDNA 4 | 2025 | B300 SXM | 288 GB | MI355X | 288 GB | Gaudi 3（无后继在售） | 128 GB | 显存首次持平，差距完全转移到机柜级（NVL72 对 8 卡节点） |
| Rubin vs MI400 | 2026（路线图） | Rubin / VR200 NVL144 | 288 GB HBM4 | MI400 series / Helios | 未公布 | 路线图未定 | 未公布 | 双方都上机柜级；AMD 押注开放的 UALink + Ultra Ethernet 对抗 NVLink |

> - Gaudi 3 没有 FP4，也没有后继型号在售，所以它是拿 FP8 在 Hopper 这一档比价格、 比"不需要 InfiniBand"，而不是拿峰值去和 Blackwell 硬碰。
> - 显存容量决定"能不能跑"，而在 B300 之前 AMD 每一代都领先。 如果一个模型单张 MI300X 装得下、却要两张 H100，那还没跑分 AMD 就已经赢了这一局。
> - scale-up 域的规模决定"怎么切模型"。NVIDIA 把 NVLink 扩到了单柜 72 卡， 而 Helios 之前 AMD 的一致性域是 8 卡。超过 8 卡做张量并行时， 这是结构性差异，不是调优能解决的问题。
> - 软件是规格表里看不到的那部分。CUDA 在算子、库和框架默认路径上领先十年以上。 ROCm 在主流模型的推理和训练上已经追上不少，但一旦涉及自定义或全新的东西差距依然明显。
> - 两家的 4bit 格式不通用。NVIDIA 的 NVFP4 和 AMD 的 MXFP4 缩放块布局不同， 为其一量化好的权重要重新量化才能给另一边用。


---

[返回目录](../README.md)
