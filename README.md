# AI Infrastructure Cheat Sheet

Side-by-side spec tables for the hardware people actually run models on — from a
Mac mini on a desk to a 72-GPU NVLink rack. NVIDIA, AMD and Apple, plus the
sizing math that decides what fits. Every table is generated from the YAML in
[`data/`](data/), so a correction is a one-line pull request.

[English](README.md) · [简体中文](README.zh-CN.md)

> **Companion repo:** [qfc-network/ai-infra](https://github.com/qfc-network/ai-infra) —
> deep dives into the papers and open-source systems behind these numbers
> (FlashAttention, PagedAttention, GQA, quantization, NVLink and more).
> This repo holds the hardware numbers; that one explains the mechanisms.

## Contents

**Desktop and local**
- [Desktop & Local AI Systems](#desktop--local-ai-systems)
- [Consumer & Workstation GPUs](#consumer--workstation-gpus)
- [AMD Radeon for Local AI](#amd-radeon-for-local-ai)
- [Intel Arc Pro for Local AI](#intel-arc-pro-for-local-ai)

**NVIDIA data center**
- [DGX Systems](#dgx-systems)
- [Flagship Data Center GPUs (SXM)](#flagship-data-center-gpus-sxm)
- [Grace-based Superchips](#grace-based-superchips)
- [Rack-Scale NVLink Systems](#rack-scale-nvlink-systems)
- [NVLink & NVSwitch Generations](#nvlink--nvswitch-generations)
- [Scale-Out Networking](#scale-out-networking)
- [Platform Roadmap](#platform-roadmap)

**AMD**
- [AMD Instinct Accelerators](#amd-instinct-accelerators)
- [AMD Instinct Platforms & Racks](#amd-instinct-platforms--racks)

**Intel**
- [Intel Gaudi Accelerators](#intel-gaudi-accelerators)

**China**
- [Huawei Ascend Accelerators](#huawei-ascend-accelerators)
- [Huawei Atlas SuperPoDs](#huawei-atlas-superpods)
- [Other Chinese AI Accelerators](#other-chinese-ai-accelerators)

**Head to head**
- [Data Center - NVIDIA vs AMD vs Intel](#data-center---nvidia-vs-amd-vs-intel)
- [Local Options by Memory Tier](#local-options-by-memory-tier)

**Sizing math**
- [Quantization vs VRAM (weights)](#quantization-vs-vram-weights)
- [KV Cache vs Context Length](#kv-cache-vs-context-length)

## Desktop and local

### Desktop & Local AI Systems

Boxes you can put on a desk and run a model on. Two different bets: unified memory (lots of capacity, moderate bandwidth) versus a discrete GPU (little capacity, huge bandwidth). Decode speed tracks bandwidth; what fits at all tracks capacity.

| Parameter | NVIDIA DGX Spark | GB10 OEM boxes | Ryzen AI Max+ 395 box | Mac mini (M5 Pro) | Mac Studio (M5 Max) | Mac Studio (M5 Ultra) | RTX 5090 desktop |
|---|---|---|---|---|---|---|---|
| Chip | GB10 Grace Blackwell (20-core Arm) | GB10 Grace Blackwell (same silicon) | AMD Ryzen AI Max+ 395 (16 x Zen 5 + Radeon 8060S) | Apple M5 Pro | Apple M5 Max | Apple M5 Ultra | GB202 discrete GPU |
| Memory for the model | 128 GB LPDDR5X unified | 128 GB LPDDR5X unified | up to 128 GB unified, up to 96 GB as VRAM | 24 / 48 / 64 GB unified | 36 / 48 / 64 / 128 GB unified | 96 / 256 / 512 GB unified | 32 GB GDDR7 (VRAM only) |
| Memory bandwidth | 273 GB/s | 273 GB/s | 256 GB/s | 307 GB/s | 460-614 GB/s | 1.2 TB/s | 1,792 GB/s |
| Vendor AI figure | 1 PFLOP FP4 (sparse) | 1 PFLOP FP4 (sparse) | 50+ NPU TOPS (INT8); no comparable GPU FLOPS figure | not published in comparable terms | not published in comparable terms | not published in comparable terms | 3,352 AI TOPS FP4 (sparse) |
| Low precision support | FP4 / FP8 native (Blackwell tensor cores) | FP4 / FP8 native | FP16 / INT8 (RDNA 3.5, no FP8 or FP4) | no FP4/FP8 tensor path; GPU + Neural Engine | no FP4/FP8 tensor path | no FP4/FP8 tensor path | FP4 / FP8 native |
| Networking | ConnectX-7 200 GbE + 10 GbE | ConnectX-7 200 GbE + 10 GbE | 2.5-10 GbE depending on the box | 10 GbE, Thunderbolt 5 | 10 GbE, Thunderbolt 5 | 10 GbE, Thunderbolt 5 | whatever the motherboard has |
| Multi-box linking | up to 4 units, ~700B params | same as DGX Spark | none | Thunderbolt only, not a real fabric | Thunderbolt only | Thunderbolt only | PCIe only, no NVLink |
| System power | 240 W PSU (140 W chip TDP) | ~240 W | ~120 W chip, box dependent | 155 W max continuous | 480 W max continuous | 480 W max continuous | 575 W card, ~1 kW system |
| Rough model ceiling | 70B at 4-bit on one box | 70B at 4-bit on one box | 70B at 4-bit inside a 96 GB VRAM allocation | 32B at 4-bit on 64 GB | 70B at 4-bit on 128 GB | 400B+ at 4-bit on 512 GB | 30B at 4-bit, hard ceiling at 32 GB |
| Launch | 2025 | 2025 | 2025 | 2026 | 2026 | 2026 | 2025 |

> - Ryzen AI Max+ 395 ships in the Framework Desktop, GMKtec EVO-X2, HP ZBook Ultra G1a and AMD's own Ryzen AI Halo developer platform. It is AMD's answer to DGX Spark and the Mac Studio: unified memory, no FP4, no cluster fabric.
> - "GB10 OEM boxes" are the same GB10 superchip in someone else's case - ASUS Ascent GX10, Dell Pro Max with GB10, HP ZGX Nano, Lenovo and MSI all ship one. They differ in storage, chassis and price, not in compute or bandwidth.
> - Bandwidth is the number to watch for token generation. A 5090 has 6.6x the bandwidth of a DGX Spark but a quarter of the memory: the Spark runs models the 5090 cannot load at all, and the 5090 runs the models that fit far faster.
> - Apple does not publish FLOPS in a form comparable to NVIDIA's AI TOPS, and Apple Silicon has no FP4/FP8 tensor path, so 4-bit models are dequantized in software. Capacity and bandwidth are the honest comparison points.
> - None of these are cluster hardware. DGX Spark's ConnectX-7 is the only real fabric here, and it tops out at 4 boxes; Thunderbolt between Macs is not comparable to NVLink or InfiniBand.

### Consumer & Workstation GPUs

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

### AMD Radeon for Local AI

Radeon's pitch for local inference is VRAM per dollar: a W7900 carries 48 GB and an R9700 32 GB where NVIDIA's consumer ceiling is 32 GB. The catch is which cards ROCm actually supports.

| Parameter | RX 7900 XTX | RX 9070 XT | Radeon AI PRO R9700 | Radeon PRO W7900 |
|---|---|---|---|---|
| Architecture | RDNA 3 | RDNA 4 | RDNA 4 | RDNA 3 |
| Compute units | 96 | 64 | 64 | 96 |
| VRAM | 24 GB GDDR6 | 16 GB GDDR6 | 32 GB GDDR6 | 48 GB GDDR6 |
| Memory bandwidth | 960 GB/s | 645 GB/s | 645 GB/s | 864 GB/s |
| Lowest matrix precision | FP16 / INT8 / INT4 (WMMA) | FP8 (RDNA 4 adds FP8 WMMA) | FP8 | FP16 / INT8 / INT4 (WMMA) |
| ROCm support | officially supported | supported from ROCm 7.0 | officially supported, AI-targeted SKU | officially supported |
| GPU-to-GPU link | PCIe only | PCIe only | PCIe only | PCIe only |
| Board power | 355 W | 304 W | 300 W | 295 W |
| Rough local LLM fit | ~30B at 4-bit | 14B at 4-bit | ~30B at 4-bit, 70B is tight | 70B at 4-bit on one card |
| Launch | 2022 | 2025 | 2025 | 2023 |

> - Check the ROCm compatibility matrix before buying, not the marketing page. AMD's officially supported consumer list is short and version-dependent, and unsupported cards often work only through community builds.
> - Ignore AMD's "5.3 TB/s" figure for the 7900 XTX. That is Infinity Cache bandwidth, not memory bandwidth; the GDDR6 number that governs decode speed is 960 GB/s.
> - RDNA 3 has no FP8 matrix path and no FP4 anywhere in the Radeon line, so 4-bit models are dequantized in software on every card here. Only RDNA 4 (9070 XT, R9700) adds FP8 WMMA.
> - Radeon has no NVLink equivalent at any tier. Multi-card is PCIe only, which is the same constraint as an RTX 4090/5090 box.

### Intel Arc Pro for Local AI

Intel's angle is VRAM and multi-GPU per dollar at low power - a B50 does 16 GB in 70 W. The trade is a software stack (oneAPI / OpenVINO / IPEX-LLM) with far less coverage than CUDA, and INT8 as the practical floor.

| Parameter | Arc Pro B50 | Arc Pro B60 | Arc Pro B70 |
|---|---|---|---|
| Architecture | Xe2 (Battlemage) | Xe2 (Battlemage) | Xe2-HPG |
| Xe cores / XMX engines | 16 Xe cores / 128 EU | 20 Xe cores / 160 EU | 32 Xe cores / 256 XMX |
| VRAM | 16 GB | 24 GB | 32 GB |
| Memory interface | 128-bit | 192-bit | 256-bit |
| Memory bandwidth | 224 GB/s | 456 GB/s | 608 GB/s |
| Peak INT8 (dense) | 170 TOPS | 197 TOPS | 367 TOPS |
| Multi-GPU | PCIe only | PCIe, dual-GPU partner boards exist (2 x 24 GB) | PCIe Gen5 x16, Linux multi-GPU via oneAPI |
| Software | oneAPI / OpenVINO / IPEX-LLM | oneAPI / OpenVINO / IPEX-LLM | oneAPI / OpenVINO / IPEX-LLM |
| Board power | 70 W | 120-200 W | varies by board partner |
| Rough local LLM fit | 14B at 4-bit | ~30B at 4-bit | ~30B at 4-bit |
| Launch | 2025 | 2025 | 2026 |

> - Intel quotes INT8 TOPS, not FP8 or FP4 FLOPS. Arc has XMX matrix engines but no FP4 path, so 4-bit weights are dequantized in software - the same situation as Radeon.
> - Intel does not publish a TDP for the B70; the datasheet lists power, connector and form factor as "varies by partner". An Arc Pro B65 also exists but is not listed here for lack of a published spec sheet.
> - The software stack is the real question. OpenVINO and IPEX-LLM cover popular models well and llama.cpp has a SYCL backend, but anything depending on a custom CUDA kernel needs porting.

## NVIDIA data center

### DGX Systems

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

### Flagship Data Center GPUs (SXM)

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

### Grace-based Superchips

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

### Rack-Scale NVLink Systems

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

### NVLink & NVSwitch Generations

Per-GPU NVLink bandwidth is bidirectional aggregate across all links, which is how NVIDIA quotes it.

| Name | Generation | First GPU | Year | Per-link BW | Links per GPU | Total BW per GPU | Switch | Max GPUs in domain |
|---|---|---|---|---|---|---|---|---|
| NVLink 1 | 1 | P100 | 2016 | 40 GB/s | 4 | 160 GB/s | none | 8 (hybrid cube mesh) |
| NVLink 2 | 2 | V100 | 2017 | 50 GB/s | 6 | 300 GB/s | NVSwitch 1 | 16 (DGX-2) |
| NVLink 3 | 3 | A100 | 2020 | 50 GB/s | 12 | 600 GB/s | NVSwitch 2 | 8 per node, 16 via NVLink Switch |
| NVLink 4 | 4 | H100 | 2022 | 50 GB/s | 18 | 900 GB/s | NVSwitch 3 | 8 per node, up to 256 with NVLink Switch System |
| NVLink 5 | 5 | B200 / B300 | 2024 | 100 GB/s | 18 | 1.8 TB/s | NVLink Switch (7.2 TB/s per chip) | 72 in one rack (NVL72), 576 across racks |

> - NVLink-C2C is the 900 GB/s CPU-to-GPU link used inside Grace superchips; it is separate from GPU-to-GPU NVLink.

### Scale-Out Networking

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

### Platform Roadmap

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

## AMD

### AMD Instinct Accelerators

AMD's data center GPU line. HBM capacity has been AMD's consistent lead over the equivalent NVIDIA part; scale-up domain size is where it falls behind.

| Parameter | MI250X | MI300X | MI325X | MI350X | MI355X |
|---|---|---|---|---|---|
| Architecture | CDNA 2 | CDNA 3 | CDNA 3 | CDNA 4 | CDNA 4 |
| Process | TSMC 6nm | TSMC 5nm + 6nm chiplets | TSMC 5nm + 6nm chiplets | TSMC 3nm + 6nm chiplets | TSMC 3nm + 6nm chiplets |
| Compute units | 220 | 304 | 304 | 256 | 256 |
| Memory | 128 GB HBM2e | 192 GB HBM3 | 256 GB HBM3E | 288 GB HBM3E | 288 GB HBM3E |
| Memory bandwidth | 3.2 TB/s | 5.3 TB/s | 6 TB/s | 8 TB/s | 8 TB/s |
| FP64 matrix | 95.7 TFLOPS | 163.4 TFLOPS | 163.4 TFLOPS | ~78.6 TFLOPS | ~78.6 TFLOPS |
| FP16/BF16 (dense) | 383 TFLOPS | 1.3 PFLOPS | 1.3 PFLOPS | ~2.3 PFLOPS | 2.5 PFLOPS |
| FP8 (dense) | not supported | 2.6 PFLOPS | 2.6 PFLOPS | 4.6 PFLOPS | 5.0 PFLOPS |
| FP4 / MXFP4 (dense) | not supported | not supported | not supported | 9.2 PFLOPS | 10 PFLOPS |
| GPU interconnect | Infinity Fabric 3rd gen | Infinity Fabric, 8-GPU fully connected mesh | Infinity Fabric, 8-GPU fully connected mesh | Infinity Fabric 4th gen, 8-GPU mesh | Infinity Fabric 4th gen, 8-GPU mesh |
| Total board power | 560 W | 750 W | 1,000 W | 1,000 W | 1,400 W |
| Cooling | air or liquid | air | air | air | direct liquid |
| Launch | 2021 | 2023 | 2024 | 2025 | 2025 |

> - AMD quotes MXFP4 and MXFP6 (OCP microscaling formats) where NVIDIA quotes NVFP4. They are different 4-bit encodings with different scaling-block layouts; a model quantized for one is not automatically portable.
> - CDNA 4 traded FP64 away: MI355X FP64 matrix is roughly half MI300X's, after CDNA 3 had been the HPC-friendly choice. Same direction NVIDIA took with Blackwell Ultra.
> - FP64 and FP16 figures for the MI350 series are derived from AMD's published platform totals divided by eight; check the datasheet PDFs before quoting them in a procurement document.

### AMD Instinct Platforms & Racks

AMD sells an 8-GPU OAM baseboard (the "platform") to OEMs rather than a branded appliance like DGX. The scale-up domain stops at 8 GPUs until Helios.

| Parameter | MI300X Platform | MI325X Platform | MI355X Platform | Helios (MI400 series, announced) |
|---|---|---|---|---|
| GPUs | 8 x MI300X | 8 x MI325X | 8 x MI355X | 72 x MI400-series |
| Total GPU memory | 1.5 TB HBM3 | 2 TB HBM3E | 2.3 TB HBM3E | TBA |
| Aggregate bandwidth | 42.4 TB/s | 48 TB/s | 64 TB/s | TBA |
| FP8 (dense) | 20.8 PFLOPS | 20.8 PFLOPS | 40.3 PFLOPS | TBA |
| FP4 / MXFP4 (dense) | not supported | not supported | 80.5 PFLOPS | TBA |
| Scale-up domain | 8 GPUs, fully connected mesh, no switch | 8 GPUs, fully connected mesh, no switch | 8 GPUs, fully connected mesh, no switch | 72 GPUs over UALink - AMD's answer to NVL72 |
| Scale-out network | OEM choice, typically 8 x 400 Gb/s | OEM choice, typically 8 x 400 Gb/s | OEM choice, up to 8 x 400 Gb/s | Ultra Ethernet |
| Cooling | air | air | air or direct liquid | liquid |
| Sold as | OCP UBB baseboard for OEM chassis | OCP UBB baseboard for OEM chassis | OCP UBB baseboard for OEM chassis | full rack reference design |
| Availability | 2023-2024 | 2024-2025 | 2025 | 2026 (roadmap) |

> - This is the structural difference, not a spec-sheet one. An MI355X node is 8 GPUs in one coherent domain; a GB300 NVL72 rack is 72. Anything larger than 8 GPUs on AMD crosses the network today, which changes how you shard a model.
> - AMD's answer is UALink (an open scale-up interconnect standard) plus Ultra Ethernet for scale-out, arriving with Helios. Open standards versus NVIDIA's vertically integrated NVLink is the actual strategic bet.
> - There is no DGX equivalent: AMD ships baseboards, and Dell, HPE, Supermicro and others build the box. Chassis power and physical specs therefore vary by OEM and are not listed here.

## Intel

### Intel Gaudi Accelerators

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

## China

### Huawei Ascend Accelerators

Huawei publishes compute and interconnect figures for the 950 series and later but never released per-chip datasheets for the 910B or 910C, so the older rows are marked as unpublished rather than filled with analyst estimates.

| Parameter | Ascend 910B | Ascend 910C | Ascend 950PR | Ascend 950DT | Ascend 960 | Ascend 970 |
|---|---|---|---|---|---|---|
| FP8 | not officially published | not officially published | 1 PFLOPS | 1 PFLOPS | 2 PFLOPS | 4 PFLOPS |
| FP4 / MXFP4 | not supported | not supported | 2 PFLOPS (MXFP4) | 2 PFLOPS (MXFP4) | 4 PFLOPS | 8 PFLOPS |
| Memory | not officially published | not officially published | not stated in the keynote | not stated in the keynote | not stated in the keynote | not stated in the keynote |
| Interconnect per chip | not officially published | Unified Bus (UB) | 2 TB/s | 2 TB/s | not stated | 4 TB/s |
| Used in | Atlas 800 servers | Atlas 900 A3 SuperPoD | Atlas 950 SuperPoD | Atlas 950 SuperPoD | Atlas 960 SuperPoD | TBA |
| Availability | shipping since 2023 | shipping since 2025 | Q1 2026 | Q4 2026 | Q4 2027 | Q4 2028 |
| Spec source | no public datasheet | no public datasheet | Huawei Connect 2025 keynote | Huawei Connect 2025 keynote | Huawei Connect 2025 keynote | Huawei Connect 2025 keynote |

> - For scale: an Ascend 950 at 1 PFLOPS FP8 sits near a B200 (4.5 PFLOPS FP8 dense) per chip. Huawei's strategy is not per-chip parity - it is putting far more chips in one interconnect domain, which the SuperPoD table shows.
> - Widely circulated 910B and 910C figures (64/128 GB HBM, 376/780 TFLOPS) come from analysts and secondary reporting, not Huawei. They are omitted here rather than presented as specifications.

### Huawei Atlas SuperPoDs

Huawei's answer to NVL72 is not a better chip, it is a much larger coherent domain. Where a GB300 NVL72 rack holds 72 GPUs, an Atlas 950 puts 8,192 accelerators on one interconnect.

| Parameter | Atlas 900 A3 (CloudMatrix 384) | Atlas 950 SuperPoD | Atlas 960 SuperPoD |
|---|---|---|---|
| Accelerators | 384 x Ascend 910C | 8,192 x Ascend 950DT | 15,488 x Ascend 960 |
| Total memory | not officially published | 1,152 TB | 4,460 TB |
| Interconnect BW | Unified Bus, all-to-all non-blocking | 16 PB/s | 34 PB/s |
| FP8 compute | not officially published | 8 EFLOPS | 30 EFLOPS |
| FP4 compute | not supported | 16 EFLOPS | 60 EFLOPS |
| Cabinets | 16 | 160 (128 compute + 32 comms) | 220 (176 compute + 44 comms) |
| NVIDIA counterpart | GB200 NVL72 | beyond NVL72 scale - compare at cluster level | beyond NVL72 scale - compare at cluster level |
| Availability | March 2025, 300+ deployed | Q4 2026 | Q4 2027 |

> - Compare like with like. A GB300 NVL72 is one rack; an Atlas 950 is 160 cabinets. Huawei is trading power and floor space for domain size because per-chip it cannot match Blackwell on process node.
> - Everything here is from Huawei's own Huawei Connect 2025 keynote. Widely quoted CloudMatrix figures such as "48 TB HBM" and "300 PFLOPS dense BF16" come from analyst teardowns, not Huawei, and are left out.
> - Power draw is the number Huawei does not headline and NVIDIA does. Treat any performance-per-watt comparison against NVL72 with suspicion until someone publishes measured rack power.

### Other Chinese AI Accelerators

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

## Head to head

### Data Center - NVIDIA vs AMD vs Intel

Which part competes with which, and what actually separates them. AMD's lever is memory capacity, Intel's is on-die Ethernet and price, NVIDIA's is domain size and software. Apple is absent because it sells no data center accelerator.

| Name | Era | NVIDIA | NVIDIA HBM | AMD | AMD HBM | Intel | Intel HBM | What decides it |
|---|---|---|---|---|---|---|---|---|
| Hopper vs CDNA 3 | 2023 | H100 SXM | 80 GB | MI300X | 192 GB | Gaudi 2 | 96 GB | AMD fits models H100 cannot; NVIDIA wins on software maturity and a 256-GPU NVLink domain |
| Hopper refresh vs CDNA 3 refresh | 2024 | H200 SXM | 141 GB | MI325X | 256 GB | Gaudi 3 | 128 GB | same matchup, both sides added HBM; AMD still ~1.8x the capacity |
| Blackwell vs CDNA 4 | 2025 | B200 SXM | 180 GB | MI355X | 288 GB | Gaudi 3 (no successor shipping) | 128 GB | first generation where both have native 4-bit, but in incompatible formats (NVFP4 vs MXFP4) |
| Blackwell Ultra vs CDNA 4 | 2025 | B300 SXM | 288 GB | MI355X | 288 GB | Gaudi 3 (no successor shipping) | 128 GB | memory parity for the first time; the gap moves entirely to rack scale (NVL72 vs 8-GPU nodes) |
| Rubin vs MI400 | 2026 (roadmap) | Rubin / VR200 NVL144 | 288 GB HBM4 | MI400 series / Helios | TBA | roadmap unsettled | TBA | both go rack-scale; AMD bets on open UALink + Ultra Ethernet against NVLink |

> - Gaudi 3 has no FP4 and no successor shipping, so it competes on FP8 against Hopper-class parts on price and on not needing InfiniBand, not on peak numbers against Blackwell.
> - Memory capacity decides what you can run at all, and AMD has led on it every generation until B300. If a model fits on one MI300X but needs two H100s, AMD wins that comparison before any benchmark runs.
> - Scale-up domain size decides how you shard. NVIDIA extended NVLink to 72 GPUs in one rack; AMD's coherent domain is 8 GPUs until Helios ships. For tensor parallelism across more than 8 GPUs that difference is structural, not a tuning problem.
> - Software is the part no spec table shows. CUDA has a decade-plus lead in kernels, libraries and framework defaults. ROCm has closed much of the gap for mainstream inference and training on popular models, and much less of it for anything custom or new.
> - The 4-bit formats are not interchangeable. NVIDIA's NVFP4 and AMD's MXFP4 use different scaling-block layouts, so a checkpoint quantized for one needs requantizing for the other.

### Local Options by Memory Tier

The practical way to shop: pick the capacity your model needs, then see who sells it. Bandwidth falls off a cliff above 48 GB, because everything past that point is unified memory rather than dedicated VRAM.

| Name | NVIDIA | AMD | Apple | Intel | Typical bandwidth | Runs comfortably |
|---|---|---|---|---|---|---|
| 16 GB | RTX 5060 Ti / 4060 Ti 16 GB | RX 9070 XT | Mac mini M6 | Arc Pro B50 | 200-650 GB/s | 14B at 4-bit |
| 24 GB | RTX 3090 / RTX 4090 | RX 7900 XTX | Mac mini M5 Pro | Arc Pro B60 | 300-1,000 GB/s | ~30B at 4-bit |
| 32 GB | RTX 5090 | Radeon AI PRO R9700 | Mac mini M6 (32 GB) | Arc Pro B70 | 170-1,792 GB/s | 30B at 4-bit with real context |
| 48 GB | RTX 6000 Ada | Radeon PRO W7900 | Mac Studio M5 Max (48 GB) | nothing at this tier | 460-960 GB/s | 70B at 4-bit |
| 96-128 GB | RTX PRO 6000 (96 GB VRAM), DGX Spark (128 GB unified) | Ryzen AI Max+ 395 (128 GB unified) | Mac Studio M5 Max 128 GB / M5 Ultra 96 GB | nothing at this tier | 256 GB/s unified, 1,792 GB/s on the RTX PRO card | 70B at 8-bit, 120B+ at 4-bit |
| 256-512 GB | nothing at this tier | nothing at this tier | Mac Studio M5 Ultra | nothing at this tier | 1.2 TB/s | 400B+ at 4-bit |

> - Capacity and bandwidth stop moving together above 48 GB. A 96 GB RTX PRO 6000 holds 1,792 GB/s; a 128 GB DGX Spark or Strix Halo box holds 256-273 GB/s. Same tier on paper, roughly 7x apart on decode speed.
> - Apple is the only vendor selling 256-512 GB to one machine, and the M5 Ultra holds 1.2 TB/s while doing it - but with no FP4 path and no cluster fabric.
> - Intel stops at 32 GB. Above that tier its answer is multiple B60 or B70 cards over PCIe, not a bigger card.
> - Parts named here that have no row of their own elsewhere in this repo (RTX 5060 Ti, RTX 6000 Ada) are listed for orientation only; no specs are claimed for them beyond the memory tier.

## Sizing math

### Quantization vs VRAM (weights)

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

### KV Cache vs Context Length

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

## How to read the numbers

- **Sparse vs dense.** Headline FLOPS are usually the sparse (2:4 structured
  sparsity) number, which is 2x the dense number. Tables state which one they
  use.
- **Bandwidth.** NVLink and Infinity Fabric figures are bidirectional aggregate
  per GPU.
- **Same die, different bins.** Air-cooled parts run at lower power and lower
  clocks than the liquid-cooled versions of the same chip.
- **Vendor AI figures are not comparable.** NVIDIA quotes FP8 for Ada and FP4
  for Blackwell; AMD quotes MXFP4; Apple does not publish an equivalent at all.
- **Roadmap entries** come from keynotes and press releases, not datasheets.
- **Sourcing is uneven by vendor.** NVIDIA, AMD, Intel and Apple publish
  datasheets; Huawei publishes keynote figures for the 950 series and nothing
  per-chip for the 910 series; other Chinese vendors publish little. Cells say
  "not officially published" rather than borrowing analyst estimates.

## Contributing

Fix a number, add a product, add a source: edit the YAML in [`data/`](data/),
run the generator, commit both the data and the regenerated Markdown.

```bash
pip install -r requirements.txt
python scripts/generate.py
```

Corrections should cite a vendor datasheet, product page, or press release —
see [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgements

The DGX comparison that started this repo comes from ServerMall's write-up
[NVIDIA DGX B300 vs DGX B200 vs DGX H100/H200](https://servermall.com/blog/nvidia-dgx-b300-vs-dgx-b200-vs-dgx-h100-h200-which-dgx-server-to-choose-under-llm-inference-and-fine/).
Spec values here are re-checked against vendor material, so some differ.

## Disclaimer

Community-maintained and unaffiliated with NVIDIA, AMD or Apple. Specifications
are collected from public vendor material and may be incomplete or out of date;
always confirm against the official datasheet before buying or sizing anything.
All trademarks belong to their respective owners.

## License

Data and documentation: [CC BY 4.0](LICENSE). Scripts: [MIT](LICENSE-CODE).
