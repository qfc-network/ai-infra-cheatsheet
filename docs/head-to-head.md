# NVIDIA vs AMD, Generation by Generation

Which AMD part competes with which NVIDIA part, and what actually separates them. Memory capacity has been AMD's lever; domain size and software have been NVIDIA's.

| Name | Era | NVIDIA | NVIDIA HBM | AMD | AMD HBM | What decides it |
|---|---|---|---|---|---|---|
| Hopper vs CDNA 3 | 2023 | H100 SXM | 80 GB | MI300X | 192 GB | AMD fits models H100 cannot; NVIDIA wins on software maturity and a 256-GPU NVLink domain |
| Hopper refresh vs CDNA 3 refresh | 2024 | H200 SXM | 141 GB | MI325X | 256 GB | same matchup, both sides added HBM; AMD still ~1.8x the capacity |
| Blackwell vs CDNA 4 | 2025 | B200 SXM | 180 GB | MI355X | 288 GB | first generation where both have native 4-bit, but in incompatible formats (NVFP4 vs MXFP4) |
| Blackwell Ultra vs CDNA 4 | 2025 | B300 SXM | 288 GB | MI355X | 288 GB | memory parity for the first time; the gap moves entirely to rack scale (NVL72 vs 8-GPU nodes) |
| Rubin vs MI400 | 2026 (roadmap) | Rubin / VR200 NVL144 | 288 GB HBM4 | MI400 series / Helios | TBA | both go rack-scale; AMD bets on open UALink + Ultra Ethernet against NVLink |

> - Memory capacity decides what you can run at all, and AMD has led on it every generation until B300. If a model fits on one MI300X but needs two H100s, AMD wins that comparison before any benchmark runs.
> - Scale-up domain size decides how you shard. NVIDIA extended NVLink to 72 GPUs in one rack; AMD's coherent domain is 8 GPUs until Helios ships. For tensor parallelism across more than 8 GPUs that difference is structural, not a tuning problem.
> - Software is the part no spec table shows. CUDA has a decade-plus lead in kernels, libraries and framework defaults. ROCm has closed much of the gap for mainstream inference and training on popular models, and much less of it for anything custom or new.
> - The 4-bit formats are not interchangeable. NVIDIA's NVFP4 and AMD's MXFP4 use different scaling-block layouts, so a checkpoint quantized for one needs requantizing for the other.


---

[Back to index](../README.zh-CN.md)
