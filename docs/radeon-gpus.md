# AMD Radeon for Local AI

Radeon's pitch for local inference is VRAM per dollar: a W7900 carries 48 GB and an R9700 32 GB where NVIDIA's consumer ceiling is 32 GB. The catch is which cards ROCm actually supports.

| Parameter | RX 7900 XTX | RX 9070 XT | Radeon AI PRO R9700 | Radeon PRO W7900 |
|---|---|---|---|---|
| Architecture | RDNA 3 | RDNA 4 | RDNA 4 | RDNA 3 |
| Compute units | 96 | 64 | 64 | 96 |
| VRAM | 24 GB GDDR6 | 16 GB GDDR6 | 32 GB GDDR6 | 48 GB GDDR6 |
| Memory bandwidth | 960 GB/s | 645 GB/s | 645 GB/s | 864 GB/s |
| Lowest matrix precision | FP16 / INT8 / INT4 (WMMA) | FP8 (RDNA 4 adds FP8 WMMA) | FP8 | FP16 / INT8 / INT4 (WMMA) |
| ROCm support | officially supported | supported from ROCm 7.0 | officially supported, AI-targeted SKU | officially supported |
| GPU-to-GPU link | PCIe only | PCIe only | PCIe only | PCIe only |
| Board power | 355 W | 304 W | 300 W | 295 W |
| Rough local LLM fit | ~30B at 4-bit | 14B at 4-bit | ~30B at 4-bit, 70B is tight | 70B at 4-bit on one card |
| Launch | 2022 | 2025 | 2025 | 2023 |

> - Check the ROCm compatibility matrix before buying, not the marketing page. AMD's officially supported consumer list is short and version-dependent, and unsupported cards often work only through community builds.
> - Ignore AMD's "5.3 TB/s" figure for the 7900 XTX. That is Infinity Cache bandwidth, not memory bandwidth; the GDDR6 number that governs decode speed is 960 GB/s.
> - RDNA 3 has no FP8 matrix path and no FP4 anywhere in the Radeon line, so 4-bit models are dequantized in software on every card here. Only RDNA 4 (9070 XT, R9700) adds FP8 WMMA.
> - Radeon has no NVLink equivalent at any tier. Multi-card is PCIe only, which is the same constraint as an RTX 4090/5090 box.


## Sources

- [RX 7900 XTX](https://www.amd.com/en/products/graphics/desktops/radeon/7000-series/amd-radeon-rx-7900xtx.html)
- [RX 7900 XTX](https://rocm.docs.amd.com/en/latest/reference/gpu-specs.html)
- [RX 9070 XT](https://www.amd.com/en/products/graphics/desktops/radeon/9000-series/amd-radeon-rx-9070xt.html)
- [RX 9070 XT](https://rocm.docs.amd.com/en/latest/reference/gpu-specs.html)
- [Radeon AI PRO R9700](https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html)
- [Radeon PRO W7900](https://rocm.docs.amd.com/en/latest/reference/gpu-specs.html)

---

[Back to index](../README.zh-CN.md)
