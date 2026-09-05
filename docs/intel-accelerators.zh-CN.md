# Intel Gaudi 加速卡

Gaudi 的特点不在算力，而在于横向扩展网络做进了芯片： 每张卡 24 个以太网口，不需要另买网卡，也没有私有互联要买。

| 参数 | Gaudi 2 | Gaudi 3 |
|---|---|---|
| 代次 | Gaudi 2 | Gaudi 3 |
| 显存 | 96 GB HBM2e | 128 GB HBM2e |
| 显存带宽 | 2.45 TB/s | 3.7 TB/s |
| BF16 矩阵 | ~432 TFLOPS | 1,678 TFLOPS |
| FP8 矩阵 | 支持 | 1,678 TFLOPS |
| FP4 | 不支持 | 不支持 |
| 片上网络 | 24 x 100 GbE RoCE | 24 x 200 GbE RoCE |
| scale-up 域 | 单机 8 卡，走片上以太网 | 单机 8 卡，走片上以太网 |
| 功耗 | 600 W | OAM 900 W，PCIe 卡 600 W |
| 形态 | OAM | OAM 夹层卡或 PCIe 卡 |
| 软件栈 | SynapseAI, PyTorch, vLLM | SynapseAI, PyTorch, vLLM |
| 上市时间 | 2022 | 2024 |

> - Gaudi 3 没有 FP4。跟标 FP4 的 B200 或 MI355X 比时要统一到 FP8，否则对比没有意义。
> - Intel 宣传口径是 "FP8 与 BF16 各 1.8 PFLOPS"，而白皮书表格里两者都是 1,678 TFLOPS。 本表采用白皮书数字。
> - 片上以太网是它的架构赌注：横向扩展走标准 RoCE 交换机而不是 InfiniBand 或 NVLink， 更便宜也更通用，但放弃了 GB300 NVL72 那种 72 卡一致性域。
> - Intel 在 Gaudi 3 之后的路线图改过不止一次，围绕任何后续型号做规划前请先确认它真的在出货。


## 资料来源

- [Gaudi 2](https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html)
- [Gaudi 3](https://cdrdv2-public.intel.com/817486/gaudi-3-ai-accelerator-white-paper.pdf)
- [Gaudi 3](https://newsroom.intel.com/artificial-intelligence/vision-2024-gaudi-3-ai-accelerator)

---

[返回目录](../README.md)
