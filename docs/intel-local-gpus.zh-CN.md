# Intel Arc Pro 本地 AI 显卡

Intel 的打法是低功耗下的显存与多卡性价比——B50 用 70 W 就给到 16 GB。 代价是软件栈（oneAPI / OpenVINO / IPEX-LLM）覆盖面远不如 CUDA，且实际精度下限是 INT8。

| 参数 | Arc Pro B50 | Arc Pro B60 | Arc Pro B70 |
|---|---|---|---|
| 架构 | Xe2 (Battlemage) | Xe2 (Battlemage) | Xe2-HPG |
| Xe 核心 / XMX 引擎 | 16 个 Xe 核心 / 128 EU | 20 个 Xe 核心 / 160 EU | 32 个 Xe 核心 / 256 个 XMX |
| 显存 | 16 GB | 24 GB | 32 GB |
| 显存位宽 | 128-bit | 192-bit | 256-bit |
| 显存带宽 | 224 GB/s | 456 GB/s | 608 GB/s |
| INT8 峰值（稠密） | 170 TOPS | 197 TOPS | 367 TOPS |
| 多卡 | 仅 PCIe | PCIe，有合作伙伴双芯卡（2 x 24 GB） | PCIe Gen5 x16，Linux 下经 oneAPI 多卡 |
| 软件栈 | oneAPI / OpenVINO / IPEX-LLM | oneAPI / OpenVINO / IPEX-LLM | oneAPI / OpenVINO / IPEX-LLM |
| 整卡功耗 | 70 W | 120-200 W | 由板卡厂商决定 |
| 本地 LLM 大致可跑 | 14B 四位量化 | 约 30B 四位量化 | 约 30B 四位量化 |
| 上市时间 | 2025 | 2025 | 2026 |

> - Intel 标的是 INT8 TOPS，不是 FP8 或 FP4 的 FLOPS。Arc 有 XMX 矩阵引擎但没有 FP4 通路，4bit 权重要靠软件反量化——和 Radeon 处境相同。
> - Intel 没有公布 B70 的 TDP，规格书上功耗、供电接口和形态都写"由板卡厂商决定"。 另有 Arc Pro B65，因为查不到公开规格书这里没收录。
> - 真正要问的是软件栈。OpenVINO 和 IPEX-LLM 对主流模型覆盖不错，llama.cpp 也有 SYCL 后端，但凡是依赖自定义 CUDA 算子的东西都得重新移植。


## 资料来源

- [Arc Pro B50](https://www.intel.com/content/www/us/en/products/sku/242615/intel-arc-pro-b50-graphics/specifications.html)
- [Arc Pro B60](https://www.intel.com/content/www/us/en/products/sku/243916/intel-arc-pro-b60-graphics/specifications.html)
- [Arc Pro B70](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b70-gpu.pdf)

---

[返回目录](../README.md)
