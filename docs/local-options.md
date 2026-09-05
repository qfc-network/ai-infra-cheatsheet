# Local Options by Memory Tier

The practical way to shop: pick the capacity your model needs, then see who sells it. Above 48 GB the field splits in two - dedicated VRAM on a card keeps its bandwidth but stops at 96 GB, while unified-memory boxes go far higher at roughly a quarter of the bandwidth.

| Name | NVIDIA | AMD | Apple | Intel | Typical bandwidth | Runs comfortably |
|---|---|---|---|---|---|---|
| 16 GB | RTX 5060 Ti / 4060 Ti 16 GB | RX 9070 XT | Mac mini M6 | Arc Pro B50 | 200-650 GB/s | 14B at 4-bit |
| 24 GB | RTX 3090 / RTX 4090 | RX 7900 XTX | Mac mini M5 Pro | Arc Pro B60 | 300-1,000 GB/s | ~30B at 4-bit |
| 32 GB | RTX 5090 | Radeon AI PRO R9700 | Mac mini M6 (32 GB) | Arc Pro B70 | 170-1,792 GB/s | 30B at 4-bit with real context |
| 48 GB | RTX 6000 Ada | Radeon PRO W7900 | Mac Studio M5 Max (48 GB) | nothing at this tier | 460-960 GB/s | 70B at 4-bit |
| 96-128 GB | RTX PRO 6000 (96 GB VRAM), DGX Spark (128 GB unified) | Ryzen AI Max+ 395 (128 GB unified) | Mac Studio M5 Max 128 GB / M5 Ultra 96 GB | nothing at this tier | 256 GB/s unified, 1,792 GB/s on the RTX PRO card | 70B at 8-bit, 120B+ at 4-bit |
| 256-512 GB | nothing at this tier | nothing at this tier | Mac Studio M5 Ultra | nothing at this tier | 1.2 TB/s | 400B+ at 4-bit |

> - Read the 96-128 GB row as two different products, not one tier. The 96 GB RTX PRO 6000 is dedicated VRAM at 1,792 GB/s; a 128 GB DGX Spark or Strix Halo box is unified memory at 256-273 GB/s. Same tier on paper, roughly 7x apart on decode speed.
> - Apple is the only vendor selling 256-512 GB to one machine, and the M5 Ultra holds 1.2 TB/s while doing it - but with no FP4 path and no cluster fabric.
> - Intel stops at 32 GB. Above that tier its answer is multiple B60 or B70 cards over PCIe, not a bigger card.
> - Parts named here that have no row of their own elsewhere in this repo (RTX 5060 Ti, RTX 6000 Ada) are listed for orientation only; no specs are claimed for them beyond the memory tier.


---

[Back to index](../README.zh-CN.md)
