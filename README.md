# NVIDIA AI Infrastructure Cheat Sheet

Side-by-side spec tables for NVIDIA's AI data center stack — GPUs, DGX systems,
Grace superchips, rack-scale NVLink systems, and the networking that ties them
together. Every table is generated from the YAML files in [`data/`](data/), so
corrections are a one-line pull request.

[English](README.md) · [简体中文](README.zh-CN.md)

## Contents

- [DGX Systems (8-GPU nodes)](#dgx-systems-8-gpu-nodes)
- [Flagship Data Center GPUs (SXM)](#flagship-data-center-gpus-sxm)
- [Grace-based Superchips](#grace-based-superchips)
- [Rack-Scale NVLink Systems](#rack-scale-nvlink-systems)
- [NVLink & NVSwitch Generations](#nvlink--nvswitch-generations)
- [Scale-Out Networking](#scale-out-networking)
- [Platform Roadmap](#platform-roadmap)

## DGX Systems (8-GPU nodes)

NVIDIA's own 8-GPU appliance line. One node = 8 SXM GPUs on a single NVSwitch fabric, dual x86 CPUs, and 8-10 network ports for scale-out.

| Parameter | DGX A100 | DGX H100 | DGX H200 | DGX B200 | DGX B300 |
|---|---|---|---|---|---|
| Architecture | Ampere | Hopper | Hopper | Blackwell | Blackwell Ultra |
| GPU | 8 x A100 SXM4 | 8 x H100 SXM5 | 8 x H200 SXM5 | 8 x B200 SXM | 8 x B300 SXM |
| Memory per GPU | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180 GB HBM3e | 288 GB HBM3e |
| Total GPU memory | 640 GB | 640 GB | 1,128 GB | 1,440 GB | 2,304 GB |
| Memory bandwidth/GPU | 2.0 TB/s | 3.35 TB/s | 4.8 TB/s | 7.7 TB/s | 8 TB/s |
| FP4 (sparse/dense) | not supported | no native FP4 | no native FP4 | 144 / 72 PFLOPS | 144 / 108 PFLOPS |
| FP8 (sparse/dense) | not supported | ~32 / 16 PFLOPS | ~32 / 16 PFLOPS | 72 / 36 PFLOPS | 72 / 36 PFLOPS |
| FP16/BF16 (sparse) | 5 PFLOPS | ~16 PFLOPS | ~16 PFLOPS | 36 PFLOPS | 36 PFLOPS |
| GPU interconnect | NVLink 3 / NVSwitch 2 | NVLink 4 / NVSwitch 3 | NVLink 4 / NVSwitch 3 | NVLink 5 / NVSwitch 4 | NVLink 5 / NVSwitch 4 |
| NVLink BW per GPU | 600 GB/s | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| Cluster network | up to 8 x 200 Gbit/s (HDR IB) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 800 Gbit/s (ConnectX-8) |
| CPU | 2 x AMD EPYC 7742 (64C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8570 (56C) | 2 x Intel Xeon 6 (6776P class) |
| System memory | 1 TB, up to 2 TB | 2 TB | 2 TB | 2 TB, up to 4 TB | 2 TB, up to 4 TB |
| Internal NVMe | 30 TB U.2 NVMe | 30 TB U.2 NVMe | 30 TB U.2 NVMe | 30 TB U.2 NVMe | 30 TB U.2 NVMe |
| Height | 6U | 8U | 8U | 10U | 10U |
| Max power | 6.5 kW | 10.2 kW | 10.2 kW | 14.3 kW | ~14-15 kW |
| Cooling | air | air | air | air | air |
| Announced | 2020 | 2022 | 2023 | 2024 | 2025 |

> - Peak FLOPS are dense unless a sparse/dense pair is given; NVIDIA marketing numbers usually quote the sparse (2:4 structured sparsity) figure.
> - B200 is documented as 192 GB HBM3e at the chip level; DGX B200 ships a 180 GB per-GPU configuration (1,440 GB per node).

## Flagship Data Center GPUs (SXM)

Chip-level comparison of the SXM parts that go into HGX baseboards and DGX nodes. Numbers are per single GPU.

| Parameter | A100 SXM4 | H100 SXM5 | H200 SXM5 | B200 SXM | B300 SXM |
|---|---|---|---|---|---|
| Architecture | Ampere (GA100) | Hopper (GH100) | Hopper (GH100) | Blackwell | Blackwell Ultra |
| Process | TSMC N7 | TSMC 4N | TSMC 4N | TSMC 4NP | TSMC 4NP |
| Transistors | 54.2 B | 80 B | 80 B | 208 B | 208 B |
| Dies per package | 1 | 1 | 1 | 2 (chip-to-chip 10 TB/s) | 2 (chip-to-chip 10 TB/s) |
| Memory | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180-192 GB HBM3e | 288 GB HBM3e |
| Memory bandwidth | 2,039 GB/s | 3,350 GB/s | 4,800 GB/s | 7.7-8 TB/s | 8 TB/s |
| FP64 / FP64 Tensor | 9.7 / 19.5 TFLOPS | 34 / 67 TFLOPS | 34 / 67 TFLOPS | 40 TFLOPS (FP64 Tensor) | de-emphasized vs B200 |
| TF32 Tensor (dense) | 156 TFLOPS | 495 TFLOPS | 495 TFLOPS | 1.1 PFLOPS | 1.1 PFLOPS |
| FP16/BF16 Tensor (dense) | 312 TFLOPS | 989 TFLOPS | 989 TFLOPS | 2.2 PFLOPS | 2.2 PFLOPS |
| FP8 Tensor (dense) | not supported | 1,979 TFLOPS | 1,979 TFLOPS | 4.5 PFLOPS | 4.5 PFLOPS |
| FP4 Tensor (dense) | not supported | not supported | not supported | 9 PFLOPS | 13.5 PFLOPS (15 PFLOPS in GB300) |
| NVLink | NVLink 3, 600 GB/s | NVLink 4, 900 GB/s | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s | NVLink 5, 1.8 TB/s |
| TDP | 400 W (up to 500 W) | up to 700 W | up to 700 W | 1,000 W (1,200 W in GB200) | ~1,400 W |
| MIG instances | up to 7 | up to 7 | up to 7 | up to 7 | up to 7 |
| Launch | 2020 | 2022 | 2023 | 2024 | 2025 |

> - Multiply the dense numbers by 2 for the sparse (2:4 structured sparsity) figures NVIDIA quotes in marketing material.
> - The same die ships in different power/memory bins: HGX/DGX air-cooled parts are clocked lower than the liquid-cooled superchip variants.

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
