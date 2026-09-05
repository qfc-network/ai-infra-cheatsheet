# Intel Gaudi Accelerators

Gaudi's distinguishing feature is not the compute, it is that the scale-out network is on the die: 24 Ethernet ports per accelerator, no separate NIC and no proprietary fabric to buy.

| Parameter | Gaudi 2 | Gaudi 3 |
|---|---|---|
| Generation | Gaudi 2 | Gaudi 3 |
| Memory | 96 GB HBM2e | 128 GB HBM2e |
| Memory bandwidth | 2.45 TB/s | 3.7 TB/s |
| BF16 matrix | ~432 TFLOPS | 1,678 TFLOPS |
| FP8 matrix | supported | 1,678 TFLOPS |
| FP4 | not supported | not supported |
| On-die networking | 24 x 100 GbE RoCE | 24 x 200 GbE RoCE |
| Scale-up domain | 8 accelerators per node over on-die Ethernet | 8 accelerators per node over on-die Ethernet |
| TDP | 600 W | 900 W (OAM), 600 W PCIe card |
| Form factor | OAM | OAM mezzanine or PCIe card |
| Software | SynapseAI, PyTorch, vLLM | SynapseAI, PyTorch, vLLM |
| Launch | 2022 | 2024 |

> - Gaudi 3 has no FP4. Against a B200 or MI355X quoting FP4 numbers, compare at FP8 or the comparison is meaningless.
> - Intel markets Gaudi 3 as "1.8 PFLOPS FP8 and BF16" while the whitepaper tables list 1,678 TFLOPS for both. The table uses the whitepaper figure.
> - On-die Ethernet is the architectural bet: scale-out runs on standard RoCE switches instead of InfiniBand or NVLink, which is cheaper and more portable but gives up the coherent 72-GPU domain a GB300 NVL72 rack provides.
> - Intel's post-Gaudi-3 roadmap has changed more than once. Verify what is actually shipping before planning around any successor part.


## Sources

- [Gaudi 2](https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html)
- [Gaudi 3](https://cdrdv2-public.intel.com/817486/gaudi-3-ai-accelerator-white-paper.pdf)
- [Gaudi 3](https://newsroom.intel.com/artificial-intelligence/vision-2024-gaudi-3-ai-accelerator)

---

[Back to index](../README.zh-CN.md)
