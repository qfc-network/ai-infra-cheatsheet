# Intel Arc Pro for Local AI

Intel's angle is VRAM and multi-GPU per dollar at low power - a B50 does 16 GB in 70 W. The trade is a software stack (oneAPI / OpenVINO / IPEX-LLM) with far less coverage than CUDA, and INT8 as the practical floor.

| Parameter | Arc Pro B50 | Arc Pro B60 | Arc Pro B70 |
|---|---|---|---|
| Architecture | Xe2 (Battlemage) | Xe2 (Battlemage) | Xe2-HPG |
| Xe cores / XMX engines | 16 Xe cores / 128 EU | 20 Xe cores / 160 EU | 32 Xe cores / 256 XMX |
| VRAM | 16 GB | 24 GB | 32 GB |
| Memory interface | 128-bit | 192-bit | 256-bit |
| Memory bandwidth | 224 GB/s | 456 GB/s | 608 GB/s |
| Peak INT8 (dense) | 170 TOPS | 197 TOPS | 367 TOPS |
| Multi-GPU | PCIe only | PCIe, dual-GPU partner boards exist (2 x 24 GB) | PCIe Gen5 x16, Linux multi-GPU via oneAPI |
| Software | oneAPI / OpenVINO / IPEX-LLM | oneAPI / OpenVINO / IPEX-LLM | oneAPI / OpenVINO / IPEX-LLM |
| Board power | 70 W | 120-200 W | varies by board partner |
| Rough local LLM fit | 14B at 4-bit | ~30B at 4-bit | ~30B at 4-bit |
| Launch | 2025 | 2025 | 2026 |

> - Intel quotes INT8 TOPS, not FP8 or FP4 FLOPS. Arc has XMX matrix engines but no FP4 path, so 4-bit weights are dequantized in software - the same situation as Radeon.
> - Intel does not publish a TDP for the B70; the datasheet lists power, connector and form factor as "varies by partner". An Arc Pro B65 also exists but is not listed here for lack of a published spec sheet.
> - The software stack is the real question. OpenVINO and IPEX-LLM cover popular models well and llama.cpp has a SYCL backend, but anything depending on a custom CUDA kernel needs porting.


## Sources

- [Arc Pro B50](https://www.intel.com/content/www/us/en/products/sku/242615/intel-arc-pro-b50-graphics/specifications.html)
- [Arc Pro B60](https://www.intel.com/content/www/us/en/products/sku/243916/intel-arc-pro-b60-graphics/specifications.html)
- [Arc Pro B70](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b70-gpu.pdf)

---

[Back to index](../README.zh-CN.md)
