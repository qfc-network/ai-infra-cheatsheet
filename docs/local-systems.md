# Desktop & Local AI Systems

Boxes you can put on a desk and run a model on. Two different bets: unified memory (lots of capacity, moderate bandwidth) versus a discrete GPU (little capacity, huge bandwidth). Decode speed tracks bandwidth; what fits at all tracks capacity.

| Parameter | NVIDIA DGX Spark | GB10 OEM boxes | Mac mini (M5 Pro) | Mac Studio (M5 Max) | Mac Studio (M5 Ultra) | RTX 5090 desktop |
|---|---|---|---|---|---|---|
| Chip | GB10 Grace Blackwell (20-core Arm) | GB10 Grace Blackwell (same silicon) | Apple M5 Pro | Apple M5 Max | Apple M5 Ultra | GB202 discrete GPU |
| Memory for the model | 128 GB LPDDR5X unified | 128 GB LPDDR5X unified | 24 / 48 / 64 GB unified | 36 / 48 / 64 / 128 GB unified | 96 / 256 / 512 GB unified | 32 GB GDDR7 (VRAM only) |
| Memory bandwidth | 273 GB/s | 273 GB/s | 307 GB/s | 460-614 GB/s | 1.2 TB/s | 1,792 GB/s |
| Vendor AI figure | 1 PFLOP FP4 (sparse) | 1 PFLOP FP4 (sparse) | not published in comparable terms | not published in comparable terms | not published in comparable terms | 3,352 AI TOPS FP4 (sparse) |
| Low precision support | FP4 / FP8 native (Blackwell tensor cores) | FP4 / FP8 native | no FP4/FP8 tensor path; GPU + Neural Engine | no FP4/FP8 tensor path | no FP4/FP8 tensor path | FP4 / FP8 native |
| Networking | ConnectX-7 200 GbE + 10 GbE | ConnectX-7 200 GbE + 10 GbE | 10 GbE, Thunderbolt 5 | 10 GbE, Thunderbolt 5 | 10 GbE, Thunderbolt 5 | whatever the motherboard has |
| Multi-box linking | up to 4 units, ~700B params | same as DGX Spark | Thunderbolt only, not a real fabric | Thunderbolt only | Thunderbolt only | PCIe only, no NVLink |
| System power | 240 W PSU (140 W chip TDP) | ~240 W | 155 W max continuous | 480 W max continuous | 480 W max continuous | 575 W card, ~1 kW system |
| Rough model ceiling | 70B at 4-bit on one box | 70B at 4-bit on one box | 32B at 4-bit on 64 GB | 70B at 4-bit on 128 GB | 400B+ at 4-bit on 512 GB | 30B at 4-bit, hard ceiling at 32 GB |
| Launch | 2025 | 2025 | 2026 | 2026 | 2026 | 2025 |

> - "GB10 OEM boxes" are the same GB10 superchip in someone else's case - ASUS Ascent GX10, Dell Pro Max with GB10, HP ZGX Nano, Lenovo and MSI all ship one. They differ in storage, chassis and price, not in compute or bandwidth.
> - Bandwidth is the number to watch for token generation. A 5090 has 6.6x the bandwidth of a DGX Spark but a quarter of the memory: the Spark runs models the 5090 cannot load at all, and the 5090 runs the models that fit far faster.
> - Apple does not publish FLOPS in a form comparable to NVIDIA's AI TOPS, and Apple Silicon has no FP4/FP8 tensor path, so 4-bit models are dequantized in software. Capacity and bandwidth are the honest comparison points.
> - None of these are cluster hardware. DGX Spark's ConnectX-7 is the only real fabric here, and it tops out at 4 boxes; Thunderbolt between Macs is not comparable to NVLink or InfiniBand.


## Sources

- [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
- [Mac mini (M5 Pro)](https://www.apple.com/mac-mini/specs/)
- [Mac Studio (M5 Max)](https://www.apple.com/mac-studio/specs/)
- [Mac Studio (M5 Ultra)](https://www.apple.com/mac-studio/specs/)
- [RTX 5090 desktop](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)

---

[Back to index](../README.zh-CN.md)
