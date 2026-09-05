# 只能租用的云端加速器

Google TPU 和 AWS Trainium 是两支买不到的大规模加速器集群。 本仓库其他所有硬件都有报价单和采购流程，这两家只有按小时计费和可用区。 真正的差异在这里，不在规格。

| 参数 | TPU v5e | TPU v5p | TPU v6e (Trillium) | TPU7x (Ironwood) | Trainium2 | Trainium3 |
|---|---|---|---|---|---|---|
| 厂商 | Google | Google | Google | Google | AWS | AWS |
| 单芯片内存 | 16 GB HBM | 95 GiB HBM | 32 GB HBM | 192 GiB HBM | 96 GiB | 144 GB HBM3e |
| 内存带宽 | 800 GB/s | 2,765 GB/s | 1,638 GB/s | 7,380 GB/s | 2.9 TB/s | 4.9 TB/s |
| 低精度算力 | 393 TOPS (INT8) | 459 TFLOPS (FP8) | 1,836 TOPS (INT8) | 4,614 TFLOPS (FP8) | FP8 稠密 1,299 TFLOPS，稀疏 2,563 | MXFP8 约为 Trainium2 的 2 倍 |
| BF16 算力 | 197 TFLOPS | 459 TFLOPS | 918 TFLOPS | 2,307 TFLOPS | 667 TFLOPS（稠密） | 未单独公布 |
| 单芯片互联 | 400 GB/s ICI | 1,200 GB/s ICI | 800 GB/s ICI | ICI 1,200 GB/s，3D 环面 | 1.28 TB/s NeuronLink | NeuronSwitch，约为 Trainium2 的 2 倍 |
| 最大互联规模 | 单 pod 256 芯片 | 单 pod 8,960 芯片 | 单 pod 256 芯片 | 单 pod 9,216 芯片 | 单 Trn2 UltraServer 64 芯片 | 单 UltraServer 144 芯片，20.7 TB HBM3e，362 MXFP8 PFLOPS |
| 软件栈 | 首选 JAX + XLA；PyTorch 需经 PyTorch/XLA | 首选 JAX + XLA；PyTorch 需经 PyTorch/XLA | 首选 JAX + XLA；PyTorch 需经 PyTorch/XLA | 首选 JAX + XLA；PyTorch 需经 PyTorch/XLA | AWS Neuron SDK；PyTorch 需经 torch-neuronx | AWS Neuron SDK；PyTorch 需经 torch-neuronx |
| 获取方式 | 仅 Google Cloud | 仅 Google Cloud | 仅 Google Cloud | 仅 Google Cloud | 仅 AWS | 仅 AWS |
| 上市时间 | 2023 | 2023 | 2024 | 2025-2026 | 2024 | 2025-2026 |

> - 两家都不跑 CUDA，也都不是 GPU 机群的即插即用替代。TPU 是 XLA 的地盘—— JAX 原生，PyTorch 要经 PyTorch/XLA。Trainium 要用 Neuron SDK 和 torch-neuronx。 决定值不值得上的通常是移植工作量，不是峰值算力。
> - pod 规模一直是 TPU 最特别的地方。一个 TPU7x pod 把 9,216 颗芯片挂在同一套 ICI 上， 对比 GB300 NVL72 一柜 72 卡、华为 Atlas 950 的 8,192 卡。要比互联域，不是比芯片。
> - Trainium3 标的是 MXFP8（AMD 也在用的 OCP microscaling 格式）， TPU 标普通 FP8 和 INT8，NVIDIA 标 NVFP4。四家厂商，三套互不兼容的低精度格式。
> - AWS 没有公布 Trainium3 的 BF16 数字，也没有单芯片算力，只给了 UltraServer 总量 和相对 Trainium2 的倍数。这些单元格按公布口径原样保留，没有反推单芯片值。
> - Inferentia2 因为找不到现行规格页没有收录；它是 Trainium 线上只做推理的兄弟型号。


## 资料来源

- [TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e)
- [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p)
- [TPU v6e (Trillium)](https://docs.cloud.google.com/tpu/docs/v6e)
- [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)
- [Trainium2](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/trainium2.html)
- [Trainium3](https://aws.amazon.com/ai/machine-learning/trainium/)

---

[返回目录](../README.md)
