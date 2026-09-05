# NVIDIA AI Infrastructure Cheat Sheet

Side-by-side spec tables for NVIDIA's AI data center stack — GPUs, DGX systems,
Grace superchips, rack-scale NVLink systems, and the networking that ties them
together. Every table is generated from the YAML files in [`data/`](data/), so
corrections are a one-line pull request.

[English](README.md) · [简体中文](README.zh-CN.md)

## Contents

- [DGX Systems](#dgx-systems)
- [Flagship Data Center GPUs (SXM)](#flagship-data-center-gpus-sxm)
- [Consumer & Workstation GPUs](#consumer--workstation-gpus)
- [Quantization vs VRAM (weights)](#quantization-vs-vram-weights)
- [KV Cache vs Context Length](#kv-cache-vs-context-length)
- [Grace-based Superchips](#grace-based-superchips)
- [Rack-Scale NVLink Systems](#rack-scale-nvlink-systems)
- [NVLink & NVSwitch Generations](#nvlink--nvswitch-generations)
- [Scale-Out Networking](#scale-out-networking)
- [Platform Roadmap](#platform-roadmap)

## DGX Systems

NVIDIA's own appliance line, from the 2017 DGX-1 to today's Blackwell Ultra nodes. Every generation since DGX-2 puts all GPUs in the box on one NVSwitch fabric; DGX-1 used a direct NVLink mesh instead.

| Parameter | DGX-1 (V100) | DGX-2 | DGX A100 | DGX H100 | DGX H200 | DGX B200 | DGX B300 |
|---|---|---|---|---|---|---|---|
| Architecture | Volta | Volta | Ampere | Hopper | Hopper | Blackwell | Blackwell Ultra |
| GPU | 8 x V100 SXM2 | 16 x V100 SXM3 | 8 x A100 SXM4 | 8 x H100 SXM5 | 8 x H200 SXM5 | 8 x B200 SXM | 8 x B300 SXM |
| Memory per GPU | 16 GB, later 32 GB HBM2 | 32 GB HBM2 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180 GB HBM3e | 288 GB HBM3e |
| Total GPU memory | 128 GB (256 GB with 32 GB V100) | 512 GB | 640 GB | 640 GB | 1,128 GB | 1,440 GB | 2.1 TB (NVIDIA spec) |
| Memory bandwidth/GPU | 900 GB/s | 900 GB/s | 2.0 TB/s | 3.35 TB/s | 4.8 TB/s | 8 TB/s (64 TB/s per node) | 8 TB/s |
| FP4 (sparse/dense) | not supported | not supported | not supported | no native FP4 | no native FP4 | 144 / 72 PFLOPS | 144 / 108 PFLOPS |
| FP8 (sparse/dense) | not supported | not supported | not supported | ~32 / 16 PFLOPS | ~32 / 16 PFLOPS | 72 / 36 PFLOPS | 72 / 36 PFLOPS |
| FP16/BF16 Tensor | 1 PFLOPS (dense) | 2 PFLOPS (dense) | 5 PFLOPS (sparse) | ~16 PFLOPS (sparse) | ~16 PFLOPS (sparse) | 36 PFLOPS (sparse) | 36 PFLOPS (sparse) |
| GPU interconnect | NVLink 2 hybrid cube mesh (no NVSwitch) | NVLink 2 / NVSwitch 1 (12 switches) | NVLink 3 / NVSwitch 2 | NVLink 4 / NVSwitch 3 | NVLink 4 / NVSwitch 3 | NVLink 5 / NVSwitch 4 | NVLink 5 / NVSwitch 4 |
| NVLink BW per GPU | 300 GB/s | 300 GB/s | 600 GB/s | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| Cluster network | 4 x 100 Gbit/s (EDR IB) + 2 x 10 GbE | 8 x 100 Gbit/s (EDR IB) | up to 8 x 200 Gbit/s (HDR IB) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 800 Gbit/s (ConnectX-8) |
| CPU | 2 x Intel Xeon E5-2698 v4 (20C) | 2 x Intel Xeon Platinum 8168 (24C) | 2 x AMD EPYC 7742 (64C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8570 (56C) | 2 x Intel Xeon 6776P |
| System memory | 512 GB DDR4 | 1.5 TB DDR4 | 1 TB, up to 2 TB | 2 TB | 2 TB | 2 TB, up to 4 TB | 2 TB, up to 4 TB |
| Internal NVMe | 4 x 1.92 TB SSD (RAID 0) | 8 x 3.84 TB NVMe + 2 x 960 GB (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB E1.S + 2 x 1.9 TB M.2 (OS) |
| Height | 3U | 10U | 6U | 8U | 8U | 10U | 10U |
| Max power | 3.5 kW | 10 kW | 6.5 kW | 10.2 kW | 10.2 kW | 14.3 kW | ~14 kW |
| Cooling | air | air | air | air | air | air | air |
| Announced | 2017 | 2018 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - DGX-2 is the odd one out at 16 GPUs; every other DGX node here is an 8-GPU system. It was also the debut of NVSwitch.
> - DGX B300 GPU memory is listed by NVIDIA as 2.1 TB per node; 8 x 288 GB of B300 chip capacity would be 2.3 TB, so the shipping configuration reserves part of it.
> - Peak FLOPS are dense unless a sparse/dense pair is given; NVIDIA marketing numbers usually quote the sparse (2:4 structured sparsity) figure.
> - B200 is documented as 192 GB HBM3e at the chip level; DGX B200 ships a 180 GB per-GPU configuration (1,440 GB per node).

## Flagship Data Center GPUs (SXM)

Chip-level comparison of the SXM parts that go into HGX baseboards and DGX nodes. Numbers are per single GPU.

| Parameter | P100 SXM | V100 SXM2 | A100 SXM4 | H100 SXM5 | H200 SXM5 | B200 SXM | B300 SXM |
|---|---|---|---|---|---|---|---|
| Architecture | Pascal (GP100) | Volta (GV100) | Ampere (GA100) | Hopper (GH100) | Hopper (GH100) | Blackwell | Blackwell Ultra |
| Process | TSMC 16nm FinFET | TSMC 12nm FFN | TSMC N7 | TSMC 4N | TSMC 4N | TSMC 4NP | TSMC 4NP |
| Transistors | 15.3 B | 21.1 B | 54.2 B | 80 B | 80 B | 208 B | 208 B |
| Dies per package | 1 | 1 | 1 | 1 | 1 | 2 (chip-to-chip 10 TB/s) | 2 (chip-to-chip 10 TB/s) |
| Memory | 16 GB HBM2 | 16 or 32 GB HBM2 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180-192 GB HBM3e | 288 GB HBM3e |
| Memory bandwidth | 732 GB/s | 900 GB/s | 2,039 GB/s | 3,350 GB/s | 4,800 GB/s | 7.7-8 TB/s | 8 TB/s |
| FP64 / FP64 Tensor | 5.3 TFLOPS / no FP64 Tensor | 7.8 TFLOPS / no FP64 Tensor | 9.7 / 19.5 TFLOPS | 34 / 67 TFLOPS | 34 / 67 TFLOPS | 40 TFLOPS (FP64 Tensor) | de-emphasized vs B200 |
| TF32 Tensor (dense) | not supported | not supported | 156 TFLOPS | 495 TFLOPS | 495 TFLOPS | 1.1 PFLOPS | 1.1 PFLOPS |
| FP16/BF16 Tensor (dense) | no Tensor Cores (21.2 TFLOPS FP16 vector) | 125 TFLOPS (FP16 only, no BF16) | 312 TFLOPS | 989 TFLOPS | 989 TFLOPS | 2.2 PFLOPS | 2.2 PFLOPS |
| FP8 Tensor (dense) | not supported | not supported | not supported | 1,979 TFLOPS | 1,979 TFLOPS | 4.5 PFLOPS | 4.5 PFLOPS |
| FP4 Tensor (dense) | not supported | not supported | not supported | not supported | not supported | 9 PFLOPS | 13.5 PFLOPS (15 PFLOPS in GB300) |
| NVLink | NVLink 1, 160 GB/s | NVLink 2, 300 GB/s | NVLink 3, 600 GB/s | NVLink 4, 900 GB/s | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s | NVLink 5, 1.8 TB/s |
| TDP | 300 W | 300 W (350 W SXM3) | 400 W (up to 500 W) | up to 700 W | up to 700 W | 1,000 W (1,200 W in GB200) | ~1,400 W |
| MIG instances | not supported | not supported | up to 7 | up to 7 | up to 7 | up to 7 | up to 7 |
| Launch | 2016 | 2017 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - Volta and Pascal predate structured sparsity, TF32, BF16 and MIG; V100 Tensor Cores are FP16-only.
> - Multiply the dense numbers by 2 for the sparse (2:4 structured sparsity) figures NVIDIA quotes in marketing material.
> - The same die ships in different power/memory bins: HGX/DGX air-cooled parts are clocked lower than the liquid-cooled superchip variants.

## Consumer & Workstation GPUs

What people actually run local LLMs on. For inference the binding constraint is VRAM first and memory bandwidth second — peak FLOPS rarely decides anything.

| Parameter | RTX 2080 Ti | RTX 3090 | RTX 4090 | RTX 5090 | RTX PRO 6000 Blackwell |
|---|---|---|---|---|---|
| Architecture | Turing (TU102) | Ampere (GA102) | Ada Lovelace (AD102) | Blackwell (GB202) | Blackwell (GB202) |
| VRAM | 11 GB GDDR6 | 24 GB GDDR6X | 24 GB GDDR6X | 32 GB GDDR7 | 96 GB GDDR7 |
| Memory bandwidth | 616 GB/s | 936 GB/s | 1,008 GB/s | 1,792 GB/s | 1,792 GB/s |
| Lowest native precision | FP16 / INT8 (no BF16) | BF16 / INT8 | FP8 | FP4 | FP4 |
| NVIDIA tensor figure | ~108 TFLOPS FP16 (FP16 accumulate) | 285 TFLOPS FP16 (sparse) | 1,321 AI TOPS (FP8, sparse) | 3,352 AI TOPS (FP4, sparse) | 4,000 AI TOPS (FP4, sparse) |
| GPU-to-GPU link | NVLink 2 bridge, 100 GB/s (2 GPUs) | NVLink 3 bridge, 112.5 GB/s (2 GPUs) | PCIe 4.0 x16 only - no NVLink | PCIe 5.0 x16 only - no NVLink | PCIe 5.0 x16 only - no NVLink |
| ECC memory | no | no | no | no | yes |
| Board power | 250-260 W | 350 W | 450 W | 575 W | 600 W |
| Rough local LLM fit | 7-8B at 4-bit | ~30B at 4-bit, 14B at 8-bit | ~30B at 4-bit, 14B at 8-bit | ~30B at 4-bit with long context, 32B comfortable | 70B at 8-bit, 120B+ at 4-bit |
| Launch | 2018 | 2020 | 2022 | 2025 | 2025 |

> - The "NVIDIA tensor figure" row is NOT comparable across generations: NVIDIA quotes FP16 for Turing/Ampere, FP8 for Ada and FP4 for Blackwell, all with sparsity from Ampere on. A 5090 is not 2.5x a 4090 at the same precision.
> - NVLink is gone from GeForce after the RTX 3090. On a 4090/5090 box, multi-GPU tensor parallelism runs over PCIe, which is roughly an order of magnitude slower than the 1.8 TB/s NVLink inside a DGX node — fine for pipeline-parallel or per-GPU replicas, painful for tensor parallelism.
> - GeForce cards have no ECC and no MIG, and NVIDIA's GeForce driver licence restricts data center deployment. Read the licence yourself before renting them out; this is the main reason hosting providers buy RTX PRO or data center SKUs.
> - "Rough local LLM fit" assumes weights plus a modest KV cache. Long context, batching, or unquantized weights all move the ceiling down sharply.

## Quantization vs VRAM (weights)

Weight memory = parameters x bytes per parameter. Sizes below are in GiB (2^30 bytes), the same unit a card's "24 GB" label uses.

| Name | Bits/param | Per 1B params | 7B model | 13B model | 32B model | 70B model | Native support | Typical use |
|---|---|---|---|---|---|---|---|---|
| FP32 | 32 | 3.7 GiB | 26 GiB | 48 GiB | 119 GiB | 261 GiB | everything | training master weights; rarely used for inference |
| FP16 / BF16 | 16 | 1.9 GiB | 13 GiB | 24 GiB | 60 GiB | 130 GiB | FP16 from V100; BF16 from A100 / RTX 30 | the accuracy baseline everything else is measured against |
| FP8 (E4M3) | 8 | 0.93 GiB | 6.5 GiB | 12 GiB | 30 GiB | 65 GiB | H100 / H200 / Ada (RTX 40) / Blackwell | near-lossless; no dequantization step on supported hardware |
| INT8 | 8 | 0.93 GiB | 6.5 GiB | 12 GiB | 30 GiB | 65 GiB | Turing (RTX 20) onward | the 8-bit option on pre-Hopper hardware |
| INT4 / NF4 / GPTQ / AWQ | 4 | 0.47 GiB | 3.3 GiB | 6.1 GiB | 15 GiB | 33 GiB | any GPU (dequantized in software) | the workhorse for running a big model on one consumer card |
| FP4 (NVFP4 / MXFP4) | 4 | 0.47 GiB | 3.3 GiB | 6.1 GiB | 15 GiB | 33 GiB | Blackwell only (RTX 50 / B200 / B300) | 4-bit with tensor core support; no dequantization |

> - Add 10-15% to the 4-bit rows in practice: quantized formats store scales and zero-points alongside the weights, so "4-bit" is closer to 4.5 bits/param.
> - Weights are only part of it. Add the KV cache (next table), activations, the CUDA context (~0.5-1 GiB) and fragmentation before deciding a model fits.
> - Native hardware support buys speed, not capacity. INT4 on a 3090 takes the same VRAM as FP4 on a 5090, but the 3090 dequantizes to FP16 inside the kernel while the 5090 multiplies in 4-bit directly.

## KV Cache vs Context Length

KV bytes per token = 2 x layers x kv_heads x head_dim x bytes_per_element. Figures below are an FP16 KV cache for a single sequence, in GiB. Check your model's config.json for its real layer and kv_head counts.

| Name | Config | Per token | 1K context | 8K context | 32K context | 128K context |
|---|---|---|---|---|---|---|
| 7B, multi-head attention | 32 layers x 32 kv heads x 128 | 512 KiB | 0.5 GiB | 4 GiB | 16 GiB | 64 GiB |
| 8B, grouped-query (8 kv heads) | 32 layers x 8 kv heads x 128 | 128 KiB | 0.13 GiB | 1 GiB | 4 GiB | 16 GiB |
| 32B, grouped-query (8 kv heads) | 64 layers x 8 kv heads x 128 | 256 KiB | 0.25 GiB | 2 GiB | 8 GiB | 32 GiB |
| 70B, grouped-query (8 kv heads) | 80 layers x 8 kv heads x 128 | 320 KiB | 0.31 GiB | 2.5 GiB | 10 GiB | 40 GiB |

> - Halve every number for an FP8 or INT8 KV cache. This is usually the cheapest way to buy context length back.
> - Multiply by batch size. The KV cache is per sequence, so 8 concurrent requests cost 8x. On a serving GPU this, not the weights, is what runs out.
> - Grouped-query attention is the biggest lever here: the 7B MHA row costs 4x the 8B GQA row despite being the smaller model. Latent attention (MLA) cuts it by roughly another order of magnitude.
> - This is why a 24 GB card "fits" a 30B 4-bit model (15 GiB of weights) and then dies at long context: 32K of KV cache is another 8 GiB.

## Grace-based Superchips

CPU+GPU packages joined by NVLink-C2C, giving the GPU cache-coherent access to the CPU's LPDDR5X as a second memory tier.

| Parameter | GH200 Grace Hopper | GB200 Grace Blackwell | GB300 Grace Blackwell Ultra | VR200 Vera Rubin (announced) |
|---|---|---|---|---|
| Composition | 1 x Grace + 1 x H100/H200 | 1 x Grace + 2 x B200 | 1 x Grace + 2 x B300 | 1 x Vera + 2 x Rubin |
| CPU cores | 72 Arm Neoverse V2 | 72 Arm Neoverse V2 | 72 Arm Neoverse V2 | 88 custom Arm cores / 176 threads |
| HBM | 96 GB HBM3 or 144 GB HBM3e | 384 GB HBM3e | 576 GB HBM3e | 288 GB HBM4 per GPU |
| CPU memory | 480 GB LPDDR5X, ~500 GB/s | 480 GB LPDDR5X | up to 800 GB LPDDR5X | LPDDR5X (TBA) |
| NVLink-C2C | 900 GB/s | 900 GB/s | 900 GB/s | NVLink-C2C (next gen) |
| External NVLink | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s per GPU | NVLink 5, 1.8 TB/s per GPU | NVLink 6 |
| Module power | up to 1,000 W | up to ~2,700 W | ~3 kW class | TBA |
| Used in | GH200 NVL2, MGX servers | GB200 NVL72, GB200 NVL2 | GB300 NVL72 | Vera Rubin NVL144 |
| Availability | 2023-2024 | 2024-2025 | 2025 | 2026 (roadmap) |

> - Roadmap parts are listed from public announcements and may change before shipping.

## Rack-Scale NVLink Systems

One rack behaves as a single large GPU: every GPU in the rack sits inside one NVLink domain instead of talking over the network.

| Parameter | GB200 NVL72 | GB300 NVL72 | Vera Rubin NVL144 (announced) |
|---|---|---|---|
| GPUs | 72 x B200 | 72 x B300 | 144 Rubin dies (72 packages) |
| CPUs | 36 x Grace | 36 x Grace | 36 x Vera |
| NVLink domain | 72 GPUs | 72 GPUs | 144 GPU dies |
| Aggregate NVLink BW | 130 TB/s | 130 TB/s | NVLink 6 switch |
| HBM capacity | 13.4 TB HBM3e | 20 TB HBM3e | ~21 TB HBM4 |
| Fast memory (HBM+LPDDR) | ~30 TB | 40 TB | ~75 TB |
| FP4 inference | 1.4 EFLOPS (sparse) | 1.1 EFLOPS (dense) | 3.6 EFLOPS |
| FP8 training | 720 PFLOPS (sparse) | 0.36 EFLOPS (dense) | 1.2 EFLOPS |
| Scale-out NIC | ConnectX-7 400 Gb/s / BlueField-3 | ConnectX-8 800 Gb/s / BlueField-3 | ConnectX-9 / Spectrum-X |
| Rack power | ~120 kW | ~130-140 kW | TBA |
| Cooling | liquid | liquid | liquid |
| Availability | 2024-2025 | 2025 | 2026 (roadmap) |

> - "GPU count" follows NVIDIA's convention: NVL72 counts packages, NVL144 counts reticle-sized dies. Both racks hold 72 GPU packages.

## NVLink & NVSwitch Generations

Per-GPU NVLink bandwidth is bidirectional aggregate across all links, which is how NVIDIA quotes it.

| Name | Generation | First GPU | Year | Per-link BW | Links per GPU | Total BW per GPU | Switch | Max GPUs in domain |
|---|---|---|---|---|---|---|---|---|
| NVLink 1 | 1 | P100 | 2016 | 40 GB/s | 4 | 160 GB/s | none | 8 (hybrid cube mesh) |
| NVLink 2 | 2 | V100 | 2017 | 50 GB/s | 6 | 300 GB/s | NVSwitch 1 | 16 (DGX-2) |
| NVLink 3 | 3 | A100 | 2020 | 50 GB/s | 12 | 600 GB/s | NVSwitch 2 | 8 per node, 16 via NVLink Switch |
| NVLink 4 | 4 | H100 | 2022 | 50 GB/s | 18 | 900 GB/s | NVSwitch 3 | 8 per node, up to 256 with NVLink Switch System |
| NVLink 5 | 5 | B200 / B300 | 2024 | 100 GB/s | 18 | 1.8 TB/s | NVLink Switch (7.2 TB/s per chip) | 72 in one rack (NVL72), 576 across racks |

> - NVLink-C2C is the 900 GB/s CPU-to-GPU link used inside Grace superchips; it is separate from GPU-to-GPU NVLink.

## Scale-Out Networking

Once you leave the NVLink domain, GPU-to-GPU traffic runs over InfiniBand or Spectrum-X Ethernet.

| Parameter | Quantum-2 InfiniBand | Quantum-X800 InfiniBand | Spectrum-X Ethernet |
|---|---|---|---|
| Type | InfiniBand NDR | InfiniBand XDR | Ethernet (lossless, AI-tuned) |
| Port speed | 400 Gb/s | 800 Gb/s | 800 GbE |
| Switch | QM9700 / QM9790 | Q3400-RA | Spectrum-4 SN5600 |
| Switch capacity | 64 x 400 Gb/s, 51.2 Tb/s | 144 x 800 Gb/s | 64 x 800 GbE, 51.2 Tb/s |
| Matching NIC | ConnectX-7 | ConnectX-8 SuperNIC | BlueField-3 SuperNIC / ConnectX-8 |
| In-network compute | SHARPv3 | SHARPv4 | adaptive routing, congestion control |
| Availability | 2021-2022 | 2024-2025 | 2023-2024 |

> - A DGX/HGX node typically pairs 8 compute NICs (one per GPU, east-west) with 1-2 DPUs for storage and management traffic.

## Platform Roadmap

NVIDIA's publicly stated one-architecture-per-year cadence. Everything from 2026 on is announcement-level information.

| Name | Year | GPU | CPU | GPU memory | NVLink | Network | Rack system |
|---|---|---|---|---|---|---|---|
| Hopper | 2022-2023 | H100 / H200 | Grace (GH200) | HBM3 / HBM3e | NVLink 4 | Quantum-2 NDR 400G | - |
| Blackwell | 2024-2025 | B200 | Grace (GB200) | HBM3e 180-192 GB | NVLink 5 | Quantum-X800 / Spectrum-X | GB200 NVL72 |
| Blackwell Ultra | 2025 | B300 | Grace (GB300) | HBM3e 288 GB | NVLink 5 | ConnectX-8 800G | GB300 NVL72 |
| Rubin | 2026 | Rubin | Vera | HBM4 288 GB | NVLink 6 | ConnectX-9 / Spectrum-X | Vera Rubin NVL144 |
| Rubin Ultra | 2027 | Rubin Ultra | Vera | HBM4e | NVLink 7 | Spectrum-X / Quantum next-gen | Rubin Ultra NVL576 |
| Feynman | 2028 | Feynman | Vera | TBA | TBA | TBA | TBA |

> - Roadmap rows are from GTC keynotes and press releases; treat dates and specs as targets, not commitments.

## How to read the numbers

- **Sparse vs dense.** NVIDIA headline FLOPS are usually the sparse (2:4
  structured sparsity) number, which is 2x the dense number. Tables state which
  one they use.
- **Bandwidth.** NVLink figures are bidirectional aggregate per GPU.
- **Same die, different bins.** Air-cooled HGX/DGX parts run at lower power and
  lower clocks than the liquid-cooled superchip versions of the same chip.
- **Roadmap entries** come from keynotes and press releases, not datasheets.

## Contributing

Fix a number, add a product, add a source: edit the YAML in [`data/`](data/),
run the generator, commit both the data and the regenerated Markdown.

```bash
pip install -r requirements.txt
python scripts/generate.py
```

Corrections should cite an NVIDIA datasheet, product page, or press release —
see [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgements

The DGX comparison that started this repo comes from ServerMall's write-up
[NVIDIA DGX B300 vs DGX B200 vs DGX H100/H200](https://servermall.com/blog/nvidia-dgx-b300-vs-dgx-b200-vs-dgx-h100-h200-which-dgx-server-to-choose-under-llm-inference-and-fine/).
Spec values here are re-checked against NVIDIA's own material, so some differ.

## Disclaimer

Community-maintained and unaffiliated with NVIDIA Corporation. Specifications
are collected from public NVIDIA material and may be incomplete or out of date;
always confirm against the official datasheet before buying or sizing anything.
NVIDIA, DGX, Grace, Hopper, Blackwell, NVLink and Spectrum-X are trademarks of
NVIDIA Corporation.

## License

Data and documentation: [CC BY 4.0](LICENSE). Scripts: [MIT](LICENSE-CODE).
