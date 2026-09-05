# Data Center PCIe Cards

The deployment option that is not an SXM baseboard. What separates these cards is power and form factor, not peak FLOPS - a 70 W single-slot card drops into any server, a 600 W dual-slot card needs a chassis built for it.

| Parameter | T4 | A10 | L4 | L40S | H100 NVL | H200 NVL |
|---|---|---|---|---|---|---|
| Architecture | Turing | Ampere | Ada Lovelace | Ada Lovelace | Hopper | Hopper |
| Memory | 16 GB GDDR6 | 24 GB GDDR6 | 24 GB GDDR6 | 48 GB GDDR6 with ECC | 94 GB HBM3 | 141 GB HBM3e |
| Memory bandwidth | 300 GB/s | 600 GB/s | 300 GB/s | 864 GB/s | 3,938 GB/s | 4.8 TB/s |
| FP16 Tensor | 65 TFLOPS (dense - Turing has no sparsity) | 125 / 250 TFLOPS (dense / sparse) | 242 TFLOPS (sparse) | 733 TFLOPS (sparse) | 1,671 TFLOPS (sparse) | 1,671 TFLOPS (sparse) |
| FP8 Tensor | not supported | not supported | 485 TFLOPS (sparse) | 1,466 TFLOPS (sparse) | 3,341 TFLOPS (sparse) | 3,341 TFLOPS (sparse) |
| Form factor | low-profile, single slot | full-height full-length, single slot | low-profile, single slot | full-height full-length, dual slot | full-height full-length, dual slot | dual slot, air cooled |
| PCIe | Gen3 x16, 32 GB/s | Gen4 x16, 64 GB/s | Gen4 x16, 64 GB/s | Gen4 x16, 64 GB/s | Gen5 x16, 128 GB/s | Gen5 x16, 128 GB/s |
| NVLink | none | none | none | none | bridge, pairs of cards | 2- or 4-way bridge, 900 GB/s per GPU |
| MIG | not supported | not supported | not supported | not supported | up to 7 instances | up to 7 instances at 16.5 GB |
| Max power | 70 W | 150 W | 72 W | 350 W | 400 W | up to 600 W (configurable) |
| Launch | 2018 | 2021 | 2023 | 2023 | 2023 | 2024 |

> - Power is the real axis. A 70 W L4 or T4 fits a standard server with no changes; an L40S at 350 W needs airflow planning; an H200 NVL at up to 600 W needs a chassis designed for it. That constraint, not FLOPS, is usually what decides which card a fleet standardises on.
> - Only the HBM cards get MIG and an NVLink bridge. On GDDR6 cards, multi-card work goes over PCIe and each card's memory stays its own; the H100 NVL and H200 NVL can pair or quad up over a bridge instead.
> - H100 NVL and H200 NVL are the same Hopper die in the same PCIe power bin, which is why their FP8 and FP16 figures match. The difference is memory: 94 GB HBM3 versus 141 GB HBM3e.
> - For the Blackwell generation in a PCIe slot, see the RTX PRO 6000 Blackwell row in the consumer and workstation table - 96 GB GDDR7 with ECC, dual slot, 600 W. It is listed there rather than duplicated here.


## Sources

- [T4](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-t4/t4-tensor-core-datasheet-951643.pdf)
- [A10](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a10/pdf/datasheet-new/nvidia-a10-datasheet.pdf)
- [L4](https://www.nvidia.com/en-us/data-center/l4/)
- [L40S](https://www.nvidia.com/en-us/data-center/l40s/)
- [H100 NVL](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/h100/PB-11773-001_v01.pdf)
- [H100 NVL](https://www.nvidia.com/en-us/data-center/h100/)
- [H200 NVL](https://www.nvidia.com/en-us/data-center/h200/)

---

[Back to index](../README.zh-CN.md)
