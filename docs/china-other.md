# Other Chinese AI Accelerators

Cambricon, Moore Threads, Hygon, Biren and Kunlunxin all ship or have shipped training and inference silicon. None of them publish datasheets at the level the rest of this repo relies on, so this table is deliberately coarse.

| Name | Vendor | Memory | Status | Note |
|---|---|---|---|---|
| MLU590 (思元590) | Cambricon 寒武纪 | reported 64 GB | in volume production | the most widely deployed non-Huawei domestic training chip |
| MTT S5000 | Moore Threads 摩尔线程 | reported 64 GB | shipping | full-function GPU line with its own CUDA-compatible stack (MUSA) |
| Hygon DCU (深算系列) | Hygon 海光 | varies by generation | shipping | derived from an AMD GCN license; ROCm-like software stack |
| BR100 | Biren 壁仞 | reported 64 GB | never reached volume | strong 2022 paper specs; blocked by export controls on its foundry |
| Kunlun P800 | Baidu Kunlunxin 昆仑芯 | reported 64 GB | deployed internally at scale | mostly consumed inside Baidu rather than sold broadly |

> - Read this table as a map of who exists, not as specifications. Every value marked "reported" traces to Chinese-language secondary sources and industry aggregators, not vendor datasheets, which is below the sourcing bar the rest of this repo holds to.
> - Pull requests replacing any row with vendor-published figures and a citation are very welcome - that is exactly the gap here.
> - Software is the harder problem than silicon for all of these. Each ships its own stack (MUSA, Cambricon Neuware, Hygon's ROCm fork), and porting effort rather than peak FLOPS usually decides whether a chip is usable.


---

[Back to index](../README.zh-CN.md)
