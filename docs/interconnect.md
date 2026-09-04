# NVLink & NVSwitch Generations

Per-GPU NVLink bandwidth is bidirectional aggregate across all links, which is how NVIDIA quotes it.

| Name | Generation | First GPU | Year | Per-link BW | Links per GPU | Total BW per GPU | Switch | Max GPUs in domain |
|---|---|---|---|---|---|---|---|---|
| NVLink 1 | 1 | P100 | 2016 | 40 GB/s | 4 | 160 GB/s | none | 8 (hybrid cube mesh) |
| NVLink 2 | 2 | V100 | 2017 | 50 GB/s | 6 | 300 GB/s | NVSwitch 1 | 16 (DGX-2) |
| NVLink 3 | 3 | A100 | 2020 | 50 GB/s | 12 | 600 GB/s | NVSwitch 2 | 8 per node, 16 via NVLink Switch |
| NVLink 4 | 4 | H100 | 2022 | 50 GB/s | 18 | 900 GB/s | NVSwitch 3 | 8 per node, up to 256 with NVLink Switch System |
| NVLink 5 | 5 | B200 / B300 | 2024 | 100 GB/s | 18 | 1.8 TB/s | NVLink Switch (7.2 TB/s per chip) | 72 in one rack (NVL72), 576 across racks |

> - NVLink-C2C is the 900 GB/s CPU-to-GPU link used inside Grace superchips; it is separate from GPU-to-GPU NVLink.


---

[Back to index](../README.zh-CN.md)
