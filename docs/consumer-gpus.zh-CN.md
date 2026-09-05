# 消费级与工作站 GPU

大部分人本地跑 LLM 用的其实是这些卡。推理阶段的瓶颈依次是显存容量和显存带宽， 峰值算力基本不是决定因素。

| 参数 | RTX 2080 Ti | RTX 3090 | RTX 4090 | RTX 5090 | RTX PRO 6000 Blackwell |
|---|---|---|---|---|---|
| 架构 | Turing (TU102) | Ampere (GA102) | Ada Lovelace (AD102) | Blackwell (GB202) | Blackwell (GB202) |
| 显存 | 11 GB GDDR6 | 24 GB GDDR6X | 24 GB GDDR6X | 32 GB GDDR7 | 96 GB GDDR7 |
| 显存带宽 | 616 GB/s | 936 GB/s | 1,008 GB/s | 1,792 GB/s | 1,792 GB/s |
| 最低原生精度 | FP16 / INT8（无 BF16） | BF16 / INT8 | FP8 | FP4 | FP4 |
| NVIDIA 标称算力 | ~108 TFLOPS FP16 (FP16 accumulate) | 285 TFLOPS FP16（稀疏） | 1,321 AI TOPS（FP8，稀疏） | 3,352 AI TOPS（FP4，稀疏） | 4,000 AI TOPS（FP4，稀疏） |
| 卡间互联 | NVLink 2 桥接，100 GB/s（限 2 卡） | NVLink 3 桥接，112.5 GB/s（限 2 卡） | 仅 PCIe 4.0 x16，无 NVLink | 仅 PCIe 5.0 x16，无 NVLink | 仅 PCIe 5.0 x16，无 NVLink |
| ECC 显存 | 无 | 无 | 无 | 无 | 有 |
| 整卡功耗 | 250-260 W | 350 W | 450 W | 575 W | 600 W |
| 本地 LLM 大致可跑 | 7~8B 四位量化 | 约 30B 四位量化，14B 八位量化 | 约 30B 四位量化，14B 八位量化 | 约 30B 四位量化且能带长上下文 | 70B 八位量化，120B+ 四位量化 |
| 上市时间 | 2018 | 2020 | 2022 | 2025 | 2025 |

> - "NVIDIA 标称算力" 这一行跨代不可比：Turing/Ampere 报的是 FP16，Ada 报 FP8， Blackwell 报 FP4，且 Ampere 之后都是稀疏值。同精度下 5090 并不是 4090 的 2.5 倍。
> - RTX 3090 之后 GeForce 就没有 NVLink 了。4090/5090 多卡做张量并行只能走 PCIe， 比 DGX 机内 1.8 TB/s 的 NVLink 慢一个数量级左右——跑流水线并行或每卡一个副本没问题， 跑张量并行会很难受。
> - GeForce 没有 ECC、没有 MIG，而且 NVIDIA 的 GeForce 驱动许可协议对数据中心部署有限制。 要对外出租算力前请自己读一遍许可条款；这也是各家托管商买 RTX PRO 或数据中心卡的主要原因。
> - "本地 LLM 大致可跑" 按权重加少量 KV cache 估算。长上下文、批量推理或不量化都会显著拉低上限。


## 资料来源

- [RTX 2080 Ti](https://www.nvidia.com/content/geforce-gtx/GEFORCE_RTX_2080Ti_User_Guide.pdf)
- [RTX 2080 Ti](https://developer.nvidia.com/blog/nvidia-turing-architecture-in-depth/)
- [RTX 3090](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/)
- [RTX 3090](https://www.nvidia.com/content/PDF/nvidia-ampere-ga-102-gpu-architecture-whitepaper-v2.1.pdf)
- [RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
- [RTX 5090](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)
- [RTX PRO 6000 Blackwell](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/)

---

[返回目录](../README.md)
