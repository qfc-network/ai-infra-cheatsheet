# Quantization vs VRAM (weights)

Weight memory = parameters x bytes per parameter. Sizes below are in GiB (2^30 bytes), the same unit a card's "24 GB" label uses.

| Name | Bits/param | Per 1B params | 7B model | 13B model | 32B model | 70B model | Native support | Typical use |
|---|---|---|---|---|---|---|---|---|
| FP32 | 32 | 3.7 GiB | 26 GiB | 48 GiB | 119 GiB | 261 GiB | everything | training master weights; rarely used for inference |
| FP16 / BF16 | 16 | 1.9 GiB | 13 GiB | 24 GiB | 60 GiB | 130 GiB | FP16 from V100; BF16 from A100 / RTX 30 | the accuracy baseline everything else is measured against |
| FP8 (E4M3) | 8 | 0.93 GiB | 6.5 GiB | 12 GiB | 30 GiB | 65 GiB | H100 / H200 / Ada (RTX 40) / Blackwell | near-lossless; no dequantization step on supported hardware |
| INT8 | 8 | 0.93 GiB | 6.5 GiB | 12 GiB | 30 GiB | 65 GiB | Turing (RTX 20) onward | the 8-bit option on pre-Hopper hardware |
| INT4 / NF4 / GPTQ / AWQ | 4 | 0.47 GiB | 3.3 GiB | 6.1 GiB | 15 GiB | 33 GiB | any GPU (dequantized in software) | the workhorse for running a big model on one consumer card |
| NVFP4 | 4 | 0.47 GiB | 3.3 GiB | 6.1 GiB | 15 GiB | 33 GiB | NVIDIA Blackwell (RTX 50, B200, B300) | 4-bit with tensor core support; no dequantization |
| MXFP4 | 4 | 0.47 GiB | 3.3 GiB | 6.1 GiB | 15 GiB | 33 GiB | AMD CDNA 4 (MI350X, MI355X); Huawei Ascend 950 series | the OCP microscaling 4-bit format; also tensor-core native |

> - NVFP4 and MXFP4 are not interchangeable. Both are 4 bits per weight and occupy the same memory, but they use different scaling-block layouts, so a checkpoint quantized for one must be requantized for the other.
> - Add 10-15% to the 4-bit rows in practice: quantized formats store scales and zero-points alongside the weights, so "4-bit" is closer to 4.5 bits/param.
> - Weights are only part of it. Add the KV cache (next table), activations, the CUDA context (~0.5-1 GiB) and fragmentation before deciding a model fits.
> - Native hardware support buys speed, not capacity. INT4 on a 3090 takes the same VRAM as FP4 on a 5090, but the 3090 dequantizes to FP16 inside the kernel while the 5090 multiplies in 4-bit directly.


---

[Back to index](../README.zh-CN.md)
