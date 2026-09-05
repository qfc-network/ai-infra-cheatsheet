# Cloud-Only Accelerators

Google TPU and AWS Trainium are the two largest accelerator fleets you cannot buy. Everything else in this repo has a price and a purchase order; these have an hourly rate and a region. That is the structural difference, not the specs.

| Parameter | TPU v5e | TPU v5p | TPU v6e (Trillium) | TPU7x (Ironwood) | Trainium2 | Trainium3 |
|---|---|---|---|---|---|---|
| Vendor | Google | Google | Google | Google | AWS | AWS |
| Memory per chip | 16 GB HBM | 95 GiB HBM | 32 GB HBM | 192 GiB HBM | 96 GiB | 144 GB HBM3e |
| Memory bandwidth | 800 GB/s | 2,765 GB/s | 1,638 GB/s | 7,380 GB/s | 2.9 TB/s | 4.9 TB/s |
| Low-precision compute | 393 TOPS (INT8) | 459 TFLOPS (FP8) | 1,836 TOPS (INT8) | 4,614 TFLOPS (FP8) | 1,299 TFLOPS FP8 dense, 2,563 sparse | about 2x Trainium2 on MXFP8 |
| BF16 compute | 197 TFLOPS | 459 TFLOPS | 918 TFLOPS | 2,307 TFLOPS | 667 TFLOPS (dense) | not separately published |
| Interconnect per chip | 400 GB/s ICI | 1,200 GB/s ICI | 800 GB/s ICI | 1,200 GB/s ICI, 3D torus | 1.28 TB/s NeuronLink | NeuronSwitch, about 2x Trainium2 |
| Max domain | 256 chips per pod | 8,960 chips per pod | 256 chips per pod | 9,216 chips per pod | 64 chips per Trn2 UltraServer | 144 chips per UltraServer, 20.7 TB HBM3e, 362 MXFP8 PFLOPS |
| Software | JAX and XLA first; PyTorch via PyTorch/XLA | JAX and XLA first; PyTorch via PyTorch/XLA | JAX and XLA first; PyTorch via PyTorch/XLA | JAX and XLA first; PyTorch via PyTorch/XLA | AWS Neuron SDK; PyTorch via torch-neuronx | AWS Neuron SDK; PyTorch via torch-neuronx |
| How you get it | Google Cloud only | Google Cloud only | Google Cloud only | Google Cloud only | AWS only | AWS only |
| Availability | 2023 | 2023 | 2024 | 2025-2026 | 2024 | 2025-2026 |

> - Neither runs CUDA, and neither is a drop-in for a GPU fleet. TPU is XLA territory - JAX natively, PyTorch through PyTorch/XLA. Trainium needs the Neuron SDK and torch-neuronx. Porting effort, not peak FLOPS, is what usually decides whether either is worth it.
> - Pod scale is where TPU has always been unusual. A TPU7x pod puts 9,216 chips on one ICI fabric, against 72 GPUs in a GB300 NVL72 rack and 8,192 accelerators in a Huawei Atlas 950. Compare domains, not chips.
> - Trainium3 quotes MXFP8, the OCP microscaling format AMD also uses, while TPU quotes plain FP8 and INT8 and NVIDIA quotes NVFP4. Four vendors, three incompatible low-precision families.
> - AWS does not publish a BF16 figure for Trainium3 or a per-chip compute number, only UltraServer totals and multipliers against Trainium2. Those cells are left as published rather than divided out.
> - Inferentia2 is not tabled here for lack of a current spec page; it is the inference-only sibling of the Trainium line.


## Sources

- [TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e)
- [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p)
- [TPU v6e (Trillium)](https://docs.cloud.google.com/tpu/docs/v6e)
- [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)
- [Trainium2](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/trainium2.html)
- [Trainium3](https://aws.amazon.com/ai/machine-learning/trainium/)

---

[Back to index](../README.zh-CN.md)
