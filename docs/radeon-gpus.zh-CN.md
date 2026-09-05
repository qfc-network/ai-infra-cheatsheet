# AMD Radeon 本地 AI 显卡

Radeon 在本地推理上的卖点是"每块钱能买到多少显存"：W7900 有 48 GB、R9700 有 32 GB， 而 NVIDIA 消费级的天花板是 32 GB。代价是 ROCm 到底支持哪些卡。

| 参数 | RX 7900 XTX | RX 9070 XT | Radeon AI PRO R9700 | Radeon PRO W7900 |
|---|---|---|---|---|
| 架构 | RDNA 3 | RDNA 4 | RDNA 4 | RDNA 3 |
| 计算单元 | 96 | 64 | 64 | 96 |
| 显存 | 24 GB GDDR6 | 16 GB GDDR6 | 32 GB GDDR6 | 48 GB GDDR6 |
| 显存带宽 | 960 GB/s | 645 GB/s | 645 GB/s | 864 GB/s |
| 最低矩阵精度 | FP16 / INT8 / INT4 (WMMA) | FP8（RDNA 4 新增 FP8 WMMA） | FP8 | FP16 / INT8 / INT4 (WMMA) |
| ROCm 支持 | 官方支持 | ROCm 7.0 起支持 | 官方支持，面向 AI 的型号 | 官方支持 |
| 卡间互联 | 仅 PCIe | 仅 PCIe | 仅 PCIe | 仅 PCIe |
| 整卡功耗 | 355 W | 304 W | 300 W | 295 W |
| 本地 LLM 大致可跑 | 约 30B 四位量化 | 14B 四位量化 | 约 30B 四位量化，70B 很勉强 | 单卡 70B 四位量化 |
| 上市时间 | 2022 | 2025 | 2025 | 2023 |

> - 买之前查 ROCm 兼容性矩阵，别看营销页。AMD 官方支持的消费卡名单很短， 而且和 ROCm 版本绑定，不在名单里的卡往往只能靠社区编译版本跑。
> - 别把 AMD 给 7900 XTX 标的 "5.3 TB/s" 当带宽。那是 Infinity Cache 的带宽， 真正决定出词速度的 GDDR6 带宽是 960 GB/s。
> - RDNA 3 没有 FP8 矩阵通路，整条 Radeon 线都没有 FP4，所以这里每一张卡跑 4bit 模型都要软件反量化。只有 RDNA 4（9070 XT、R9700）加了 FP8 WMMA。
> - Radeon 在任何档位都没有 NVLink 的对应物，多卡只能走 PCIe—— 和 RTX 4090/5090 主机是同一个限制。


## 资料来源

- [RX 7900 XTX](https://www.amd.com/en/products/graphics/desktops/radeon/7000-series/amd-radeon-rx-7900xtx.html)
- [RX 7900 XTX](https://rocm.docs.amd.com/en/latest/reference/gpu-specs.html)
- [RX 9070 XT](https://www.amd.com/en/products/graphics/desktops/radeon/9000-series/amd-radeon-rx-9070xt.html)
- [RX 9070 XT](https://rocm.docs.amd.com/en/latest/reference/gpu-specs.html)
- [Radeon AI PRO R9700](https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html)
- [Radeon PRO W7900](https://rocm.docs.amd.com/en/latest/reference/gpu-specs.html)

---

[返回目录](../README.md)
