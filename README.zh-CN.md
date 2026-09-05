# NVIDIA AI 基础设施速查表

一份 NVIDIA AI 数据中心全栈的对照速查表：GPU、DGX 整机、Grace 超级芯片、
机柜级 NVLink 系统，以及把它们连起来的网络。所有表格都由
[`data/`](data/) 下的 YAML 自动生成，改一个数字就是一个 PR。

[English](README.md) · [简体中文](README.zh-CN.md)

## 目录

- [DGX 整机（8 卡节点）](#dgx-整机8-卡节点)
- [数据中心旗舰 GPU（SXM）](#数据中心旗舰-gpusxm)
- [Grace 系列超级芯片](#grace-系列超级芯片)
- [机柜级 NVLink 系统](#机柜级-nvlink-系统)
- [NVLink / NVSwitch 各代对比](#nvlink--nvswitch-各代对比)
- [横向扩展网络](#横向扩展网络)
- [平台路线图](#平台路线图)

## DGX 整机（8 卡节点）

NVIDIA 官方的 8 卡整机产品线。一台 = 8 张 SXM GPU + 单机内 NVSwitch 全互联 + 双路 x86 CPU + 8~10 个横向扩展网口。

| 参数 | DGX A100 | DGX H100 | DGX H200 | DGX B200 | DGX B300 |
|---|---|---|---|---|---|
| 架构 | Ampere | Hopper | Hopper | Blackwell | Blackwell Ultra |
| GPU | 8 x A100 SXM4 | 8 x H100 SXM5 | 8 x H200 SXM5 | 8 x B200 SXM | 8 x B300 SXM |
| 单卡显存 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180 GB HBM3e | 288 GB HBM3e |
| 整机显存 | 640 GB | 640 GB | 1,128 GB | 1,440 GB | 2.1 TB (NVIDIA spec) |
| 单卡显存带宽 | 2.0 TB/s | 3.35 TB/s | 4.8 TB/s | 8 TB/s (64 TB/s per node) | 8 TB/s |
| FP4（稀疏/稠密） | 不支持 | 无原生 FP4 | 无原生 FP4 | 144 / 72 PFLOPS | 144 / 108 PFLOPS |
| FP8（稀疏/稠密） | 不支持 | ~32 / 16 PFLOPS | ~32 / 16 PFLOPS | 72 / 36 PFLOPS | 72 / 36 PFLOPS |
| FP16/BF16（稀疏） | 5 PFLOPS | ~16 PFLOPS | ~16 PFLOPS | 36 PFLOPS | 36 PFLOPS |
| GPU 互联 | NVLink 3 / NVSwitch 2 | NVLink 4 / NVSwitch 3 | NVLink 4 / NVSwitch 3 | NVLink 5 / NVSwitch 4 | NVLink 5 / NVSwitch 4 |
| 单卡 NVLink 带宽 | 600 GB/s | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| 集群网络 | up to 8 x 200 Gbit/s (HDR IB) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 800 Gbit/s (ConnectX-8) |
| CPU | 2 x AMD EPYC 7742 (64C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8570 (56C) | 2 x Intel Xeon 6776P |
| 系统内存 | 1 TB, up to 2 TB | 2 TB | 2 TB | 2 TB, up to 4 TB | 2 TB, up to 4 TB |
| 内置 NVMe | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB E1.S + 2 x 1.9 TB M.2 (OS) |
| 高度 | 6U | 8U | 8U | 10U | 10U |
| 最大功耗 | 6.5 kW | 10.2 kW | 10.2 kW | 14.3 kW | ~14 kW |
| 散热 | 风冷 | 风冷 | 风冷 | 风冷 | 风冷 |
| 发布时间 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - NVIDIA 官方页面标注 DGX B300 整机显存为 2.1 TB；按 B300 芯片 8 x 288 GB 计算应为 2.3 TB，说明出厂配置保留了一部分。
> - 未特别标注时算力为稠密值；NVIDIA 官方宣传数字通常是稀疏（2:4 结构化稀疏）值。
> - B200 芯片规格为 192 GB HBM3e，但 DGX B200 整机按每卡 180 GB 配置（整机 1,440 GB）。

## 数据中心旗舰 GPU（SXM）

用于 HGX 基板与 DGX 整机的 SXM 芯片级对比，所有数字均为单卡值。

| 参数 | P100 SXM | V100 SXM2 | A100 SXM4 | H100 SXM5 | H200 SXM5 | B200 SXM | B300 SXM |
|---|---|---|---|---|---|---|---|
| 架构 | Pascal (GP100) | Volta (GV100) | Ampere (GA100) | Hopper (GH100) | Hopper (GH100) | Blackwell | Blackwell Ultra |
| 制程 | TSMC 16nm FinFET | TSMC 12nm FFN | TSMC N7 | TSMC 4N | TSMC 4N | TSMC 4NP | TSMC 4NP |
| 晶体管数 | 15.3 B | 21.1 B | 54.2 B | 80 B | 80 B | 208 B | 208 B |
| 封装内 die 数 | 1 | 1 | 1 | 1 | 1 | 2（片间 10 TB/s） | 2（片间 10 TB/s） |
| 显存 | 16 GB HBM2 | 16 或 32 GB HBM2 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180-192 GB HBM3e | 288 GB HBM3e |
| 显存带宽 | 732 GB/s | 900 GB/s | 2,039 GB/s | 3,350 GB/s | 4,800 GB/s | 7.7-8 TB/s | 8 TB/s |
| FP64 / FP64 张量 | 5.3 TFLOPS / 无 FP64 张量核 | 7.8 TFLOPS / 无 FP64 张量核 | 9.7 / 19.5 TFLOPS | 34 / 67 TFLOPS | 34 / 67 TFLOPS | 40 TFLOPS (FP64 Tensor) | 相对 B200 大幅弱化 |
| TF32 张量（稠密） | 不支持 | 不支持 | 156 TFLOPS | 495 TFLOPS | 495 TFLOPS | 1.1 PFLOPS | 1.1 PFLOPS |
| FP16/BF16 张量（稠密） | 无 Tensor Core（FP16 向量 21.2 TFLOPS） | 125 TFLOPS（仅 FP16，无 BF16） | 312 TFLOPS | 989 TFLOPS | 989 TFLOPS | 2.2 PFLOPS | 2.2 PFLOPS |
| FP8 张量（稠密） | 不支持 | 不支持 | 不支持 | 1,979 TFLOPS | 1,979 TFLOPS | 4.5 PFLOPS | 4.5 PFLOPS |
| FP4 张量（稠密） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | 9 PFLOPS | 13.5 PFLOPS（GB300 中为 15 PFLOPS） |
| NVLink | NVLink 1, 160 GB/s | NVLink 2, 300 GB/s | NVLink 3, 600 GB/s | NVLink 4, 900 GB/s | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s | NVLink 5, 1.8 TB/s |
| 功耗 | 300 W | 300 W (350 W SXM3) | 400 W (up to 500 W) | up to 700 W | up to 700 W | 1,000 W (1,200 W in GB200) | ~1,400 W |
| MIG 实例 | 不支持 | 不支持 | up to 7 | up to 7 | up to 7 | up to 7 | up to 7 |
| 上市时间 | 2016 | 2017 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - Volta 与 Pascal 早于结构化稀疏、TF32、BF16 和 MIG；V100 的 Tensor Core 只支持 FP16。
> - 稠密算力 x2 即为 NVIDIA 宣传常用的稀疏（2:4 结构化稀疏）算力。
> - 同一颗 die 会按功耗/显存分档：风冷 HGX/DGX 版本频率低于液冷超级芯片版本。

## Grace 系列超级芯片

通过 NVLink-C2C 把 CPU 与 GPU 封装在一起，GPU 可缓存一致地访问 CPU 侧 LPDDR5X， 形成第二级大容量内存。

| 参数 | GH200 Grace Hopper | GB200 Grace Blackwell | GB300 Grace Blackwell Ultra | VR200 Vera Rubin (announced) |
|---|---|---|---|---|
| 组成 | 1 x Grace + 1 x H100/H200 | 1 x Grace + 2 x B200 | 1 x Grace + 2 x B300 | 1 x Vera + 2 x Rubin |
| CPU 核心 | 72 Arm Neoverse V2 | 72 Arm Neoverse V2 | 72 Arm Neoverse V2 | 88 custom Arm cores / 176 threads |
| HBM 显存 | 96 GB HBM3 or 144 GB HBM3e | 384 GB HBM3e | 576 GB HBM3e | 288 GB HBM4 per GPU |
| CPU 内存 | 480 GB LPDDR5X, ~500 GB/s | 480 GB LPDDR5X | up to 800 GB LPDDR5X | LPDDR5X（未公布） |
| NVLink-C2C | 900 GB/s | 900 GB/s | 900 GB/s | NVLink-C2C (next gen) |
| 对外 NVLink | NVLink 4, 900 GB/s | NVLink 5, 1.8 TB/s per GPU | NVLink 5, 1.8 TB/s per GPU | NVLink 6 |
| 模组功耗 | up to 1,000 W | up to ~2,700 W | 约 3 kW 级 | 未公布 |
| 用于 | GH200 NVL2, MGX servers | GB200 NVL72, GB200 NVL2 | GB300 NVL72 | Vera Rubin NVL144 |
| 上市时间 | 2023-2024 | 2024-2025 | 2025 | 2026（路线图） |

> - 路线图产品来自公开发布信息，量产前规格可能变化。

## 机柜级 NVLink 系统

整机柜当作一块大 GPU 使用：柜内所有 GPU 处于同一个 NVLink 域内，卡间通信不走网络。

| 参数 | GB200 NVL72 | GB300 NVL72 | Vera Rubin NVL144 (announced) |
|---|---|---|---|
| GPU 数量 | 72 x B200 | 72 x B300 | 144 Rubin dies (72 packages) |
| CPU 数量 | 36 x Grace | 36 x Grace | 36 x Vera |
| NVLink 域 | 72 GPUs | 72 GPUs | 144 GPU dies |
| NVLink 总带宽 | 130 TB/s | 130 TB/s | NVLink 6 交换 |
| HBM 容量 | 13.4 TB HBM3e | 20 TB HBM3e | ~21 TB HBM4 |
| 快速内存（HBM+LPDDR） | ~30 TB | 40 TB | ~75 TB |
| FP4 推理算力 | 1.4 EFLOPS（稀疏） | 1.1 EFLOPS（稠密） | 3.6 EFLOPS |
| FP8 训练算力 | 720 PFLOPS（稀疏） | 0.36 EFLOPS（稠密） | 1.2 EFLOPS |
| 横向扩展网卡 | ConnectX-7 400 Gb/s / BlueField-3 | ConnectX-8 800 Gb/s / BlueField-3 | ConnectX-9 / Spectrum-X |
| 机柜功耗 | ~120 kW | ~130-140 kW | 未公布 |
| 散热 | 液冷 | 液冷 | 液冷 |
| 上市时间 | 2024-2025 | 2025 | 2026（路线图） |

> - "GPU 数量" 沿用 NVIDIA 的口径：NVL72 按封装计数，NVL144 按 die 计数， 两者机柜内都是 72 个 GPU 封装。

## NVLink / NVSwitch 各代对比

单卡 NVLink 带宽为所有链路的双向合计值（与 NVIDIA 官方口径一致）。

| 名称 | 代次 | 首发 GPU | 年份 | 单链路带宽 | 单卡链路数 | 单卡总带宽 | 配套交换 | 最大互联规模 |
|---|---|---|---|---|---|---|---|---|
| NVLink 1 | 1 | P100 | 2016 | 40 GB/s | 4 | 160 GB/s | 无 | 8（立方网格） |
| NVLink 2 | 2 | V100 | 2017 | 50 GB/s | 6 | 300 GB/s | NVSwitch 1 | 16 (DGX-2) |
| NVLink 3 | 3 | A100 | 2020 | 50 GB/s | 12 | 600 GB/s | NVSwitch 2 | 单机 8 卡，经 NVLink Switch 可 16 卡 |
| NVLink 4 | 4 | H100 | 2022 | 50 GB/s | 18 | 900 GB/s | NVSwitch 3 | 单机 8 卡，NVLink Switch System 最多 256 卡 |
| NVLink 5 | 5 | B200 / B300 | 2024 | 100 GB/s | 18 | 1.8 TB/s | NVLink Switch（单芯片 7.2 TB/s） | 单柜 72 卡（NVL72），跨柜可达 576 卡 |

> - NVLink-C2C 是 Grace 超级芯片内部 900 GB/s 的 CPU-GPU 互联，与 GPU 间 NVLink 不是同一条链路。

## 横向扩展网络

出了 NVLink 域之后，GPU 之间的流量走 InfiniBand 或 Spectrum-X 以太网。

| 参数 | Quantum-2 InfiniBand | Quantum-X800 InfiniBand | Spectrum-X Ethernet |
|---|---|---|---|
| 类型 | InfiniBand NDR | InfiniBand XDR | 以太网（无损、面向 AI 调优） |
| 端口速率 | 400 Gb/s | 800 Gb/s | 800 GbE |
| 交换机 | QM9700 / QM9790 | Q3400-RA | Spectrum-4 SN5600 |
| 交换容量 | 64 x 400 Gb/s, 51.2 Tb/s | 144 x 800 Gb/s | 64 x 800 GbE, 51.2 Tb/s |
| 配套网卡 | ConnectX-7 | ConnectX-8 SuperNIC | BlueField-3 SuperNIC / ConnectX-8 |
| 网内计算 | SHARPv3 | SHARPv4 | 自适应路由 + 拥塞控制 |
| 上市时间 | 2021-2022 | 2024-2025 | 2023-2024 |

> - 一台 DGX/HGX 通常是 8 张计算网卡（每卡一张，用于东西向）+ 1~2 张 DPU （用于存储与管理流量）。

## 平台路线图

NVIDIA 公开宣布的"一年一代架构"节奏。2026 年及以后均为发布会公布信息，非量产规格。

| 名称 | 年份 | GPU | CPU | GPU 显存 | NVLink | 网络 | 机柜系统 |
|---|---|---|---|---|---|---|---|
| Hopper | 2022-2023 | H100 / H200 | Grace (GH200) | HBM3 / HBM3e | NVLink 4 | Quantum-2 NDR 400G | - |
| Blackwell | 2024-2025 | B200 | Grace (GB200) | HBM3e 180-192 GB | NVLink 5 | Quantum-X800 / Spectrum-X | GB200 NVL72 |
| Blackwell Ultra | 2025 | B300 | Grace (GB300) | HBM3e 288 GB | NVLink 5 | ConnectX-8 800G | GB300 NVL72 |
| Rubin | 2026 | Rubin | Vera | HBM4 288 GB | NVLink 6 | ConnectX-9 / Spectrum-X | Vera Rubin NVL144 |
| Rubin Ultra | 2027 | Rubin Ultra | Vera | HBM4e | NVLink 7 | Spectrum-X / Quantum next-gen | Rubin Ultra NVL576 |
| Feynman | 2028 | Feynman | Vera | 未公布 | 未公布 | 未公布 | 未公布 |

> - 路线图内容来自 GTC 主题演讲与新闻稿，时间与规格均为目标值而非承诺。

## 数字怎么看

- **稀疏 vs 稠密**：NVIDIA 宣传的算力通常是稀疏（2:4 结构化稀疏）值，
  为稠密值的 2 倍。本表会标明用的是哪一个。
- **带宽口径**：NVLink 带宽为单卡所有链路的双向合计值。
- **同 die 不同档**：风冷 HGX/DGX 版本的功耗与频率都低于同一颗芯片的液冷超级芯片版本。
- **路线图条目**来自发布会与新闻稿，不是规格书。

## 参与贡献

修数字、加产品、补来源：改 [`data/`](data/) 里的 YAML，跑一下生成脚本，
把数据和重新生成的 Markdown 一起提交。

```bash
pip install -r requirements.txt
python scripts/generate.py
```

修改请附上 NVIDIA 官方规格书、产品页或新闻稿链接，详见
[CONTRIBUTING.md](CONTRIBUTING.md)。

## 致谢

本项目最初的 DGX 对照表来自 ServerMall 的这篇文章
[NVIDIA DGX B300 vs DGX B200 vs DGX H100/H200](https://servermall.com/blog/nvidia-dgx-b300-vs-dgx-b200-vs-dgx-h100-h200-which-dgx-server-to-choose-under-llm-inference-and-fine/)。
本仓库的数值都会再对照 NVIDIA 官方资料核一遍，因此个别数字与原文不同。

## 免责声明

本项目由社区维护，与 NVIDIA Corporation 无关。规格数据整理自 NVIDIA 公开资料，
可能不完整或已过时；采购与容量规划请以官方规格书为准。
NVIDIA、DGX、Grace、Hopper、Blackwell、NVLink、Spectrum-X 均为 NVIDIA Corporation 的商标。

## 许可

数据与文档采用 [CC BY 4.0](LICENSE)，脚本采用 [MIT](LICENSE-CODE)。
