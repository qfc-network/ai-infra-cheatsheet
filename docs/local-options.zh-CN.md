# 按显存档位看本地选择

实际选型的顺序：先按模型定容量，再看谁家有货。48 GB 以上带宽会断崖式下跌， 因为再往上都是统一内存，不是独立显存。

| 名称 | NVIDIA | AMD | Apple | Intel | 典型带宽 | 能从容跑 |
|---|---|---|---|---|---|---|
| 16 GB | RTX 5060 Ti / 4060 Ti 16 GB | RX 9070 XT | Mac mini M6 | Arc Pro B50 | 200-650 GB/s | 14B 四位量化 |
| 24 GB | RTX 3090 / RTX 4090 | RX 7900 XTX | Mac mini M5 Pro | Arc Pro B60 | 300-1,000 GB/s | 约 30B 四位量化 |
| 32 GB | RTX 5090 | Radeon AI PRO R9700 | Mac mini M6 (32 GB) | Arc Pro B70 | 170-1,792 GB/s | 30B 四位量化且能带像样的上下文 |
| 48 GB | RTX 6000 Ada | Radeon PRO W7900 | Mac Studio M5 Max (48 GB) | 该档位无产品 | 460-960 GB/s | 70B 四位量化 |
| 96-128 GB | RTX PRO 6000（96 GB 显存）、DGX Spark（128 GB 统一内存） | Ryzen AI Max+ 395（128 GB 统一内存） | Mac Studio M5 Max 128 GB / M5 Ultra 96 GB | 该档位无产品 | 统一内存 256 GB/s，RTX PRO 卡 1,792 GB/s | 70B 八位量化，120B+ 四位量化 |
| 256-512 GB | 该档位无产品 | 该档位无产品 | Mac Studio M5 Ultra | 该档位无产品 | 1.2 TB/s | 400B+ 四位量化 |

> - 48 GB 以上，容量和带宽就不再同步增长了。96 GB 的 RTX PRO 6000 有 1,792 GB/s， 而 128 GB 的 DGX Spark 或 Strix Halo 只有 256~273 GB/s。纸面上同一档， 出词速度差约 7 倍。
> - 只有苹果卖单机 256~512 GB，而且 M5 Ultra 在这个容量下还有 1.2 TB/s—— 代价是没有 FP4 通路，也没有集群网络。
> - Intel 到 32 GB 为止。再往上它的答案是多张 B60 或 B70 走 PCIe，而不是更大的单卡。
> - 表中提到但本仓库没有独立条目的型号（RTX 5060 Ti、RTX 6000 Ada）仅用于定位， 除显存档位外不对其规格作任何声明。


---

[返回目录](../README.md)
