# Huawei Atlas SuperPoDs

Huawei's answer to NVL72 is not a better chip, it is a much larger coherent domain. Where a GB300 NVL72 rack holds 72 GPUs, an Atlas 950 puts 8,192 accelerators on one interconnect.

| Parameter | Atlas 900 A3 (CloudMatrix 384) | Atlas 950 SuperPoD | Atlas 960 SuperPoD |
|---|---|---|---|
| Accelerators | 384 x Ascend 910C | 8,192 x Ascend 950DT | 15,488 x Ascend 960 |
| Total memory | not officially published | 1,152 TB | 4,460 TB |
| Interconnect BW | Unified Bus, all-to-all non-blocking | 16 PB/s | 34 PB/s |
| FP8 compute | not officially published | 8 EFLOPS | 30 EFLOPS |
| FP4 compute | not supported | 16 EFLOPS | 60 EFLOPS |
| Cabinets | 16 | 160 (128 compute + 32 comms) | 220 (176 compute + 44 comms) |
| NVIDIA counterpart | GB200 NVL72 | beyond NVL72 scale - compare at cluster level | beyond NVL72 scale - compare at cluster level |
| Availability | March 2025, 300+ deployed | Q4 2026 | Q4 2027 |

> - Compare like with like. A GB300 NVL72 is one rack; an Atlas 950 is 160 cabinets. Huawei is trading power and floor space for domain size because per-chip it cannot match Blackwell on process node.
> - Everything here is from Huawei's own Huawei Connect 2025 keynote. Widely quoted CloudMatrix figures such as "48 TB HBM" and "300 PFLOPS dense BF16" come from analyst teardowns, not Huawei, and are left out.
> - Power draw is the number Huawei does not headline and NVIDIA does. Treat any performance-per-watt comparison against NVL72 with suspicion until someone publishes measured rack power.


## Sources

- [Atlas 900 A3 (CloudMatrix 384)](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- [Atlas 950 SuperPoD](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- [Atlas 960 SuperPoD](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)

---

[Back to index](../README.zh-CN.md)
