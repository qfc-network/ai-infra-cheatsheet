# Huawei Ascend Accelerators

Huawei publishes compute and interconnect figures for the 950 series and later but never released per-chip datasheets for the 910B or 910C, so the older rows are marked as unpublished rather than filled with analyst estimates.

| Parameter | Ascend 910B | Ascend 910C | Ascend 950PR | Ascend 950DT | Ascend 960 | Ascend 970 |
|---|---|---|---|---|---|---|
| FP8 | not officially published | not officially published | 1 PFLOPS | 1 PFLOPS | 2 PFLOPS | 4 PFLOPS |
| FP4 / MXFP4 | not supported | not supported | 2 PFLOPS (MXFP4) | 2 PFLOPS (MXFP4) | 4 PFLOPS | 8 PFLOPS |
| Memory | not officially published | not officially published | not stated in the keynote | not stated in the keynote | not stated in the keynote | not stated in the keynote |
| Interconnect per chip | not officially published | Unified Bus (UB) | 2 TB/s | 2 TB/s | not stated | 4 TB/s |
| Used in | Atlas 800 servers | Atlas 900 A3 SuperPoD | Atlas 950 SuperPoD | Atlas 950 SuperPoD | Atlas 960 SuperPoD | TBA |
| Availability | shipping since 2023 | shipping since 2025 | Q1 2026 | Q4 2026 | Q4 2027 | Q4 2028 |
| Spec source | no public datasheet | no public datasheet | Huawei Connect 2025 keynote | Huawei Connect 2025 keynote | Huawei Connect 2025 keynote | Huawei Connect 2025 keynote |

> - For scale: an Ascend 950 at 1 PFLOPS FP8 sits near a B200 (4.5 PFLOPS FP8 dense) per chip. Huawei's strategy is not per-chip parity - it is putting far more chips in one interconnect domain, which the SuperPoD table shows.
> - Widely circulated 910B and 910C figures (64/128 GB HBM, 376/780 TFLOPS) come from analysts and secondary reporting, not Huawei. They are omitted here rather than presented as specifications.


## Sources

- [Ascend 950PR](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- [Ascend 950DT](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- [Ascend 960](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- [Ascend 970](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)

---

[Back to index](../README.zh-CN.md)
