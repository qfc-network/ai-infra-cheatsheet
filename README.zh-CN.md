# AI 基础设施速查表

一份"真正用来跑模型的硬件"对照速查表：从桌上的 Mac mini 到 72 卡的 NVLink 机柜，
涵盖 NVIDIA、AMD、Apple，以及决定"到底装不装得下"的显存换算。
所有表格都由 [`data/`](data/) 下的 YAML 自动生成，改一个数字就是一个 PR。

[English](README.md) · [简体中文](README.zh-CN.md)

> **姊妹项目：**[qfc-network/ai-infra](https://github.com/qfc-network/ai-infra) ——
> 这些数字背后的论文与开源系统深度解析（FlashAttention、PagedAttention、GQA、
> 量化、NVLink 等）。本仓库管硬件数字，那边讲原理。

## 目录

**桌面与本地**
- [桌面与本地 AI 主机](#桌面与本地-ai-主机)
- [消费级与工作站 GPU](#消费级与工作站-gpu)

**NVIDIA 数据中心**
- [DGX 整机](#dgx-整机)
- [数据中心旗舰 GPU（SXM）](#数据中心旗舰-gpusxm)
- [Grace 系列超级芯片](#grace-系列超级芯片)
- [机柜级 NVLink 系统](#机柜级-nvlink-系统)
- [NVLink / NVSwitch 各代对比](#nvlink--nvswitch-各代对比)
- [横向扩展网络](#横向扩展网络)
- [平台路线图](#平台路线图)

**AMD**
- [AMD Instinct 加速卡](#amd-instinct-加速卡)
- [AMD Instinct 整机与机柜](#amd-instinct-整机与机柜)

**正面对位**
- [NVIDIA 与 AMD 逐代对位](#nvidia-与-amd-逐代对位)

**容量换算**
- [量化格式与显存占用（权重）](#量化格式与显存占用权重)
- [KV Cache 与上下文长度](#kv-cache-与上下文长度)

## 桌面与本地

### 桌面与本地 AI 主机

能摆在桌上直接跑模型的机器，分两条路线：统一内存（容量大、带宽中等） 和独立显卡（容量小、带宽极高）。能装下多大模型看容量，出词多快看带宽。

| 参数 | NVIDIA DGX Spark | GB10 OEM boxes | Mac mini (M5 Pro) | Mac Studio (M5 Max) | Mac Studio (M5 Ultra) | RTX 5090 desktop |
|---|---|---|---|---|---|---|
| 芯片 | GB10 Grace Blackwell（20 核 Arm） | GB10 Grace Blackwell（同一颗芯片） | Apple M5 Pro | Apple M5 Max | Apple M5 Ultra | GB202 独立显卡 |
| 可用于模型的内存 | 128 GB LPDDR5X 统一内存 | 128 GB LPDDR5X 统一内存 | 24 / 48 / 64 GB 统一内存 | 36 / 48 / 64 / 128 GB 统一内存 | 96 / 256 / 512 GB 统一内存 | 32 GB GDDR7（仅显存） |
| 内存带宽 | 273 GB/s | 273 GB/s | 307 GB/s | 460-614 GB/s | 1.2 TB/s | 1,792 GB/s |
| 厂商标称算力 | 1 PFLOP FP4（稀疏） | 1 PFLOP FP4（稀疏） | 官方未给出可比口径 | 官方未给出可比口径 | 官方未给出可比口径 | 3,352 AI TOPS FP4（稀疏） |
| 低精度支持 | 原生 FP4 / FP8（Blackwell 张量核） | 原生 FP4 / FP8 | 无 FP4/FP8 张量通路，走 GPU + 神经引擎 | 无 FP4/FP8 张量通路 | 无 FP4/FP8 张量通路 | 原生 FP4 / FP8 |
| 网络 | ConnectX-7 200 GbE + 10 GbE | ConnectX-7 200 GbE + 10 GbE | 10 GbE, Thunderbolt 5 | 10 GbE, Thunderbolt 5 | 10 GbE, Thunderbolt 5 | 取决于主板 |
| 多机互联 | 最多 4 台互联，约 700B 参数 | 与 DGX Spark 相同 | 只有雷雳，算不上互联网络 | 只有雷雳 | 只有雷雳 | 只有 PCIe，无 NVLink |
| 整机功耗 | 240 W 电源（芯片 TDP 140 W） | ~240 W | 最大持续 155 W | 最大持续 480 W | 最大持续 480 W | 显卡 575 W，整机约 1 kW |
| 大致能跑到多大 | 单机 70B 四位量化 | 单机 70B 四位量化 | 64 GB 版可跑 32B 四位量化 | 128 GB 版可跑 70B 四位量化 | 512 GB 版可跑 400B+ 四位量化 | 30B 四位量化，32 GB 是硬上限 |
| 上市时间 | 2025 | 2025 | 2026 | 2026 | 2026 | 2025 |

> - "GB10 OEM 机型" 就是同一颗 GB10 换了个壳：华硕 Ascent GX10、戴尔 Pro Max with GB10、 惠普 ZGX Nano、联想和微星都有。差别在存储、机箱和价格，算力与带宽完全一样。
> - 看出词速度就看带宽。5090 的带宽是 DGX Spark 的 6.6 倍，但内存只有四分之一： Spark 能跑 5090 根本装不下的模型，而装得下的模型 5090 快得多。
> - 苹果没有公布可与 NVIDIA AI TOPS 对比的算力口径，且 Apple Silicon 没有 FP4/FP8 张量通路，4bit 模型要靠软件反量化。容量和带宽才是能诚实对比的两项。
> - 这些都不是集群硬件。这里只有 DGX Spark 的 ConnectX-7 算真正的互联网络，且最多 4 台； Mac 之间的雷雳连接和 NVLink、InfiniBand 不是一个量级。

### 消费级与工作站 GPU

大部分人本地跑 LLM 用的其实是这些卡。推理阶段的瓶颈依次是显存容量和显存带宽， 峰值算力基本不是决定因素。

| 参数 | RTX 2080 Ti | RTX 3090 | RTX 4090 | RTX 5090 | RTX PRO 6000 Blackwell |
|---|---|---|---|---|---|
| 架构 | Turing (TU102) | Ampere (GA102) | Ada Lovelace (AD102) | Blackwell (GB202) | Blackwell (GB202) |
| 显存 | 11 GB GDDR6 | 24 GB GDDR6X | 24 GB GDDR6X | 32 GB GDDR7 | 96 GB GDDR7 |
| 显存带宽 | 616 GB/s | 936 GB/s | 1,008 GB/s | 1,792 GB/s | 1,792 GB/s |
| 最低原生精度 | FP16 / INT8（无 BF16） | BF16 / INT8 | FP8 | FP4 | FP4 |
| NVIDIA 标称算力 | ~108 TFLOPS FP16 (FP16 accumulate) | 285 TFLOPS FP16（稀疏） | 1,321 AI TOPS（FP8，稀疏） | 3,352 AI TOPS（FP4，稀疏） | 4,000 AI TOPS（FP4，稀疏） |
| 卡间互联 | NVLink 2 桥接，100 GB/s（限 2 卡） | NVLink 3 桥接，112.5 GB/s（限 2 卡） | 仅 PCIe 4.0 x16，无 NVLink | 仅 PCIe 5.0 x16，无 NVLink | 仅 PCIe 5.0 x16，无 NVLink |
| ECC 显存 | 无 | 无 | 无 | 无 | 有 |
| 整卡功耗 | 250-260 W | 350 W | 450 W | 575 W | 600 W |
| 本地 LLM 大致可跑 | 7~8B 四位量化 | 约 30B 四位量化，14B 八位量化 | 约 30B 四位量化，14B 八位量化 | 约 30B 四位量化且能带长上下文 | 70B 八位量化，120B+ 四位量化 |
| 上市时间 | 2018 | 2020 | 2022 | 2025 | 2025 |

> - "NVIDIA 标称算力" 这一行跨代不可比：Turing/Ampere 报的是 FP16，Ada 报 FP8， Blackwell 报 FP4，且 Ampere 之后都是稀疏值。同精度下 5090 并不是 4090 的 2.5 倍。
> - RTX 3090 之后 GeForce 就没有 NVLink 了。4090/5090 多卡做张量并行只能走 PCIe， 比 DGX 机内 1.8 TB/s 的 NVLink 慢一个数量级左右——跑流水线并行或每卡一个副本没问题， 跑张量并行会很难受。
> - GeForce 没有 ECC、没有 MIG，而且 NVIDIA 的 GeForce 驱动许可协议对数据中心部署有限制。 要对外出租算力前请自己读一遍许可条款；这也是各家托管商买 RTX PRO 或数据中心卡的主要原因。
> - "本地 LLM 大致可跑" 按权重加少量 KV cache 估算。长上下文、批量推理或不量化都会显著拉低上限。

## NVIDIA 数据中心

### DGX 整机

NVIDIA 官方整机产品线，从 2017 年的 DGX-1 到今天的 Blackwell Ultra 节点。 DGX-2 之后每一代都把机内 GPU 挂在同一个 NVSwitch 全互联域上， 只有 DGX-1 用的是 NVLink 直连网格。

| 参数 | DGX-1 (V100) | DGX-2 | DGX A100 | DGX H100 | DGX H200 | DGX B200 | DGX B300 |
|---|---|---|---|---|---|---|---|
| 架构 | Volta | Volta | Ampere | Hopper | Hopper | Blackwell | Blackwell Ultra |
| GPU | 8 x V100 SXM2 | 16 x V100 SXM3 | 8 x A100 SXM4 | 8 x H100 SXM5 | 8 x H200 SXM5 | 8 x B200 SXM | 8 x B300 SXM |
| 单卡显存 | 16 GB，后期 32 GB HBM2 | 32 GB HBM2 | 80 GB HBM2e | 80 GB HBM3 | 141 GB HBM3e | 180 GB HBM3e | 288 GB HBM3e |
| 整机显存 | 128 GB（32 GB 版 V100 为 256 GB） | 512 GB | 640 GB | 640 GB | 1,128 GB | 1,440 GB | 2.1 TB (NVIDIA spec) |
| 单卡显存带宽 | 900 GB/s | 900 GB/s | 2.0 TB/s | 3.35 TB/s | 4.8 TB/s | 8 TB/s (64 TB/s per node) | 8 TB/s |
| FP4（稀疏/稠密） | 不支持 | 不支持 | 不支持 | 无原生 FP4 | 无原生 FP4 | 144 / 72 PFLOPS | 144 / 108 PFLOPS |
| FP8（稀疏/稠密） | 不支持 | 不支持 | 不支持 | ~32 / 16 PFLOPS | ~32 / 16 PFLOPS | 72 / 36 PFLOPS | 72 / 36 PFLOPS |
| FP16/BF16 张量 | 1 PFLOPS（稠密） | 2 PFLOPS（稠密） | 5 PFLOPS（稀疏） | 约 16 PFLOPS（稀疏） | 约 16 PFLOPS（稀疏） | 36 PFLOPS（稀疏） | 36 PFLOPS（稀疏） |
| GPU 互联 | NVLink 2 立方网格直连（无 NVSwitch） | NVLink 2 / NVSwitch 1（12 颗） | NVLink 3 / NVSwitch 2 | NVLink 4 / NVSwitch 3 | NVLink 4 / NVSwitch 3 | NVLink 5 / NVSwitch 4 | NVLink 5 / NVSwitch 4 |
| 单卡 NVLink 带宽 | 300 GB/s | 300 GB/s | 600 GB/s | 900 GB/s | 900 GB/s | 1.8 TB/s | 1.8 TB/s |
| 集群网络 | 4 x 100 Gbit/s (EDR IB) + 2 x 10 GbE | 8 x 100 Gbit/s (EDR IB) | up to 8 x 200 Gbit/s (HDR IB) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 400 Gbit/s (ConnectX-7) | up to 8 x 800 Gbit/s (ConnectX-8) |
| CPU | 2 x Intel Xeon E5-2698 v4 (20C) | 2 x Intel Xeon Platinum 8168 (24C) | 2 x AMD EPYC 7742 (64C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8480C (56C) | 2 x Intel Xeon Platinum 8570 (56C) | 2 x Intel Xeon 6776P |
| 系统内存 | 512 GB DDR4 | 1.5 TB DDR4 | 1 TB, up to 2 TB | 2 TB | 2 TB | 2 TB, up to 4 TB | 2 TB, up to 4 TB |
| 内置 NVMe | 4 x 1.92 TB SSD (RAID 0) | 8 x 3.84 TB NVMe + 2 x 960 GB (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB U.2 + 2 x 1.9 TB M.2 (OS) | 8 x 3.84 TB E1.S + 2 x 1.9 TB M.2 (OS) |
| 高度 | 3U | 10U | 6U | 8U | 8U | 10U | 10U |
| 最大功耗 | 3.5 kW | 10 kW | 6.5 kW | 10.2 kW | 10.2 kW | 14.3 kW | ~14 kW |
| 散热 | 风冷 | 风冷 | 风冷 | 风冷 | 风冷 | 风冷 | 风冷 |
| 发布时间 | 2017 | 2018 | 2020 | 2022 | 2023 | 2024 | 2025 |

> - DGX-2 是唯一的 16 卡机型，其余 DGX 节点都是 8 卡；它也是 NVSwitch 的首发平台。
> - NVIDIA 官方页面标注 DGX B300 整机显存为 2.1 TB；按 B300 芯片 8 x 288 GB 计算应为 2.3 TB，说明出厂配置保留了一部分。
> - 未特别标注时算力为稠密值；NVIDIA 官方宣传数字通常是稀疏（2:4 结构化稀疏）值。
> - B200 芯片规格为 192 GB HBM3e，但 DGX B200 整机按每卡 180 GB 配置（整机 1,440 GB）。

### 数据中心旗舰 GPU（SXM）

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

### Grace 系列超级芯片

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

### 机柜级 NVLink 系统

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

### NVLink / NVSwitch 各代对比

单卡 NVLink 带宽为所有链路的双向合计值（与 NVIDIA 官方口径一致）。

| 名称 | 代次 | 首发 GPU | 年份 | 单链路带宽 | 单卡链路数 | 单卡总带宽 | 配套交换 | 最大互联规模 |
|---|---|---|---|---|---|---|---|---|
| NVLink 1 | 1 | P100 | 2016 | 40 GB/s | 4 | 160 GB/s | 无 | 8（立方网格） |
| NVLink 2 | 2 | V100 | 2017 | 50 GB/s | 6 | 300 GB/s | NVSwitch 1 | 16 (DGX-2) |
| NVLink 3 | 3 | A100 | 2020 | 50 GB/s | 12 | 600 GB/s | NVSwitch 2 | 单机 8 卡，经 NVLink Switch 可 16 卡 |
| NVLink 4 | 4 | H100 | 2022 | 50 GB/s | 18 | 900 GB/s | NVSwitch 3 | 单机 8 卡，NVLink Switch System 最多 256 卡 |
| NVLink 5 | 5 | B200 / B300 | 2024 | 100 GB/s | 18 | 1.8 TB/s | NVLink Switch（单芯片 7.2 TB/s） | 单柜 72 卡（NVL72），跨柜可达 576 卡 |

> - NVLink-C2C 是 Grace 超级芯片内部 900 GB/s 的 CPU-GPU 互联，与 GPU 间 NVLink 不是同一条链路。

### 横向扩展网络

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

### 平台路线图

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

## AMD

### AMD Instinct 加速卡

AMD 的数据中心 GPU 线。相对同期 NVIDIA 产品，AMD 一直在 HBM 容量上领先， 短板在 scale-up 域的规模。

| 参数 | MI250X | MI300X | MI325X | MI350X | MI355X |
|---|---|---|---|---|---|
| 架构 | CDNA 2 | CDNA 3 | CDNA 3 | CDNA 4 | CDNA 4 |
| 制程 | TSMC 6nm | TSMC 5nm + 6nm 小芯片 | TSMC 5nm + 6nm 小芯片 | TSMC 3nm + 6nm 小芯片 | TSMC 3nm + 6nm 小芯片 |
| 计算单元 | 220 | 304 | 304 | 256 | 256 |
| 显存 | 128 GB HBM2e | 192 GB HBM3 | 256 GB HBM3E | 288 GB HBM3E | 288 GB HBM3E |
| 显存带宽 | 3.2 TB/s | 5.3 TB/s | 6 TB/s | 8 TB/s | 8 TB/s |
| FP64 矩阵 | 95.7 TFLOPS | 163.4 TFLOPS | 163.4 TFLOPS | ~78.6 TFLOPS | ~78.6 TFLOPS |
| FP16/BF16（稠密） | 383 TFLOPS | 1.3 PFLOPS | 1.3 PFLOPS | ~2.3 PFLOPS | 2.5 PFLOPS |
| FP8（稠密） | 不支持 | 2.6 PFLOPS | 2.6 PFLOPS | 4.6 PFLOPS | 5.0 PFLOPS |
| FP4 / MXFP4（稠密） | 不支持 | 不支持 | 不支持 | 9.2 PFLOPS | 10 PFLOPS |
| GPU 互联 | Infinity Fabric 3rd gen | Infinity Fabric，8 卡全互联网格 | Infinity Fabric，8 卡全互联网格 | 第 4 代 Infinity Fabric，8 卡网格 | 第 4 代 Infinity Fabric，8 卡网格 |
| 整卡功耗 | 560 W | 750 W | 1,000 W | 1,000 W | 1,400 W |
| 散热 | 风冷或液冷 | 风冷 | 风冷 | 风冷 | 直接液冷 |
| 上市时间 | 2021 | 2023 | 2024 | 2025 | 2025 |

> - AMD 标的是 MXFP4 / MXFP6（OCP microscaling 格式），NVIDIA 标的是 NVFP4。 两者是不同的 4bit 编码，缩放块布局也不同，为其一量化的模型不能直接搬到另一边。
> - CDNA 4 砍掉了 FP64：MI355X 的 FP64 矩阵算力大约只有 MI300X 的一半， 而 CDNA 3 本来是 HPC 友好的选择。NVIDIA 在 Blackwell Ultra 上是同一个方向。
> - MI350 系列的 FP64 与 FP16 数字是用 AMD 公布的整机数据除以 8 推算的， 写进采购文件前请核对官方 datasheet PDF。

### AMD Instinct 整机与机柜

AMD 卖的是 8 卡 OAM 基板（"platform"）给 OEM，而不是 DGX 那样的自有整机品牌。 在 Helios 之前，其 scale-up 域上限就是 8 卡。

| 参数 | MI300X Platform | MI325X Platform | MI355X Platform | Helios (MI400 series, announced) |
|---|---|---|---|---|
| GPU 数量 | 8 x MI300X | 8 x MI325X | 8 x MI355X | 72 x MI400-series |
| 整机显存 | 1.5 TB HBM3 | 2 TB HBM3E | 2.3 TB HBM3E | 未公布 |
| 总显存带宽 | 42.4 TB/s | 48 TB/s | 64 TB/s | 未公布 |
| FP8（稠密） | 20.8 PFLOPS | 20.8 PFLOPS | 40.3 PFLOPS | 未公布 |
| FP4 / MXFP4（稠密） | 不支持 | 不支持 | 80.5 PFLOPS | 未公布 |
| scale-up 域 | 8 卡全互联网格，无交换芯片 | 8 卡全互联网格，无交换芯片 | 8 卡全互联网格，无交换芯片 | 72 卡经 UALink 互联，对标 NVL72 |
| 横向扩展网络 | 由 OEM 决定，通常 8 x 400 Gb/s | 由 OEM 决定，通常 8 x 400 Gb/s | 由 OEM 决定，最高 8 x 400 Gb/s | Ultra Ethernet |
| 散热 | 风冷 | 风冷 | 风冷或直接液冷 | 液冷 |
| 交付形态 | OCP UBB 基板，装进 OEM 机箱 | OCP UBB 基板，装进 OEM 机箱 | OCP UBB 基板，装进 OEM 机箱 | 整机柜参考设计 |
| 上市时间 | 2023-2024 | 2024-2025 | 2025 | 2026（路线图） |

> - 这才是结构性差异，不是规格表上的差异。一台 MI355X 是 8 卡一个一致性域， 一个 GB300 NVL72 机柜是 72 卡。今天在 AMD 上超过 8 卡就要过网络， 这会直接改变模型怎么切分。
> - AMD 的答案是 UALink（开放的 scale-up 互联标准）加 Ultra Ethernet 做横向扩展， 随 Helios 一起落地。开放标准 vs NVIDIA 垂直整合的 NVLink，这才是真正的战略分歧。
> - AMD 没有 DGX 的对应物：它出基板，戴尔、慧与、超微等厂商做整机。 所以机箱功耗和物理规格因 OEM 而异，本表不列。

## 正面对位

### NVIDIA 与 AMD 逐代对位

哪张 AMD 卡对标哪张 NVIDIA 卡，以及真正拉开差距的是什么。 AMD 的杠杆一直是显存容量，NVIDIA 的是互联域规模和软件。

| 名称 | 时期 | NVIDIA | NVIDIA 显存 | AMD | AMD 显存 | 决定因素 |
|---|---|---|---|---|---|---|
| Hopper vs CDNA 3 | 2023 | H100 SXM | 80 GB | MI300X | 192 GB | AMD 装得下 H100 装不下的模型；NVIDIA 赢在软件成熟度和 256 卡 NVLink 域 |
| Hopper refresh vs CDNA 3 refresh | 2024 | H200 SXM | 141 GB | MI325X | 256 GB | 同一组对位，双方都加了 HBM；AMD 容量仍约为 1.8 倍 |
| Blackwell vs CDNA 4 | 2025 | B200 SXM | 180 GB | MI355X | 288 GB | 双方第一次都有原生 4bit，但格式互不兼容（NVFP4 与 MXFP4） |
| Blackwell Ultra vs CDNA 4 | 2025 | B300 SXM | 288 GB | MI355X | 288 GB | 显存首次持平，差距完全转移到机柜级（NVL72 对 8 卡节点） |
| Rubin vs MI400 | 2026（路线图） | Rubin / VR200 NVL144 | 288 GB HBM4 | MI400 series / Helios | 未公布 | 双方都上机柜级；AMD 押注开放的 UALink + Ultra Ethernet 对抗 NVLink |

> - 显存容量决定"能不能跑"，而在 B300 之前 AMD 每一代都领先。 如果一个模型单张 MI300X 装得下、却要两张 H100，那还没跑分 AMD 就已经赢了这一局。
> - scale-up 域的规模决定"怎么切模型"。NVIDIA 把 NVLink 扩到了单柜 72 卡， 而 Helios 之前 AMD 的一致性域是 8 卡。超过 8 卡做张量并行时， 这是结构性差异，不是调优能解决的问题。
> - 软件是规格表里看不到的那部分。CUDA 在算子、库和框架默认路径上领先十年以上。 ROCm 在主流模型的推理和训练上已经追上不少，但一旦涉及自定义或全新的东西差距依然明显。
> - 两家的 4bit 格式不通用。NVIDIA 的 NVFP4 和 AMD 的 MXFP4 缩放块布局不同， 为其一量化好的权重要重新量化才能给另一边用。

## 容量换算

### 量化格式与显存占用（权重）

权重显存 = 参数量 x 每参数字节数。下表单位为 GiB（2^30 字节）， 与显卡标称的 "24 GB" 是同一口径。

| 名称 | 每参数位数 | 每 10 亿参数 | 7B 模型 | 13B 模型 | 32B 模型 | 70B 模型 | 硬件原生支持 | 典型用途 |
|---|---|---|---|---|---|---|---|---|
| FP32 | 32 | 3.7 GiB | 26 GiB | 48 GiB | 119 GiB | 261 GiB | 全部 | 训练主权重，推理基本不用 |
| FP16 / BF16 | 16 | 1.9 GiB | 13 GiB | 24 GiB | 60 GiB | 130 GiB | FP16 自 V100 起；BF16 自 A100 / RTX 30 起 | 精度基线，其他格式都拿它做对比 |
| FP8 (E4M3) | 8 | 0.93 GiB | 6.5 GiB | 12 GiB | 30 GiB | 65 GiB | H100 / H200 / Ada（RTX 40）/ Blackwell | 接近无损，且在支持的硬件上不需要反量化 |
| INT8 | 8 | 0.93 GiB | 6.5 GiB | 12 GiB | 30 GiB | 65 GiB | Turing（RTX 20）及以后 | Hopper 之前硬件上的 8bit 方案 |
| INT4 / NF4 / GPTQ / AWQ | 4 | 0.47 GiB | 3.3 GiB | 6.1 GiB | 15 GiB | 33 GiB | 任意 GPU（软件反量化） | 单张消费卡跑大模型的主力方案 |
| FP4 (NVFP4 / MXFP4) | 4 | 0.47 GiB | 3.3 GiB | 6.1 GiB | 15 GiB | 33 GiB | 仅 Blackwell（RTX 50 / B200 / B300） | 有张量核原生支持的 4bit，无需反量化 |

> - 实际用 4bit 时在表上再加 10~15%：量化格式要额外存 scale 和 zero-point， 所谓 "4bit" 实际接近每参数 4.5 bit。
> - 权重只是一部分。判断能不能装下，还要加上 KV cache（见下表）、激活值、 CUDA 上下文（约 0.5~1 GiB）以及显存碎片。
> - 硬件原生支持买到的是速度不是容量。3090 上的 INT4 和 5090 上的 FP4 占显存一样多， 但 3090 要在 kernel 里反量化回 FP16 再算，5090 可以直接用 4bit 做乘法。

### KV Cache 与上下文长度

每 token 的 KV 字节数 = 2 x 层数 x kv_head 数 x head_dim x 每元素字节数。 下表是单条序列、FP16 KV cache 的占用（GiB）。具体层数和 kv_head 数请查模型的 config.json。

| 名称 | 配置 | 每 token | 1K 上下文 | 8K 上下文 | 32K 上下文 | 128K 上下文 |
|---|---|---|---|---|---|---|
| 7B, multi-head attention | 32 层 x 32 kv head x 128 | 512 KiB | 0.5 GiB | 4 GiB | 16 GiB | 64 GiB |
| 8B, grouped-query (8 kv heads) | 32 层 x 8 kv head x 128 | 128 KiB | 0.13 GiB | 1 GiB | 4 GiB | 16 GiB |
| 32B, grouped-query (8 kv heads) | 64 层 x 8 kv head x 128 | 256 KiB | 0.25 GiB | 2 GiB | 8 GiB | 32 GiB |
| 70B, grouped-query (8 kv heads) | 80 层 x 8 kv head x 128 | 320 KiB | 0.31 GiB | 2.5 GiB | 10 GiB | 40 GiB |

> - KV cache 量化到 FP8 或 INT8，所有数字直接减半——这通常是换回上下文长度最划算的做法。
> - 还要乘以 batch size。KV cache 是每条序列一份，同时服务 8 个请求就是 8 倍。 在服务端把显存撑爆的通常是它，不是权重。
> - GQA 是这里影响最大的一项：7B 的 MHA 行比 8B 的 GQA 行贵 4 倍，尽管模型更小。 MLA（潜在注意力）还能在此基础上再降大约一个数量级。
> - 这就是为什么 24 GB 的卡"装得下" 30B 四位量化模型（权重 15 GiB）， 但一开长上下文就 OOM：32K 的 KV cache 又要 8 GiB。

## 数字怎么看

- **稀疏 vs 稠密**：宣传用的算力通常是稀疏（2:4 结构化稀疏）值，为稠密值的 2 倍。
  本表会标明用的是哪一个。
- **带宽口径**：NVLink 与 Infinity Fabric 带宽均为单卡所有链路的双向合计值。
- **同 die 不同档**：风冷版本的功耗与频率都低于同一颗芯片的液冷版本。
- **厂商标称算力不可跨家对比**：NVIDIA 对 Ada 报 FP8、对 Blackwell 报 FP4，
  AMD 报 MXFP4，苹果压根没有对应口径。
- **路线图条目**来自发布会与新闻稿，不是规格书。

## 参与贡献

修数字、加产品、补来源：改 [`data/`](data/) 里的 YAML，跑一下生成脚本，
把数据和重新生成的 Markdown 一起提交。

```bash
pip install -r requirements.txt
python scripts/generate.py
```

修改请附上厂商官方规格书、产品页或新闻稿链接，详见
[CONTRIBUTING.md](CONTRIBUTING.md)。

## 致谢

本项目最初的 DGX 对照表来自 ServerMall 的这篇文章
[NVIDIA DGX B300 vs DGX B200 vs DGX H100/H200](https://servermall.com/blog/nvidia-dgx-b300-vs-dgx-b200-vs-dgx-h100-h200-which-dgx-server-to-choose-under-llm-inference-and-fine/)。
本仓库的数值都会再对照厂商官方资料核一遍，因此个别数字与原文不同。

## 免责声明

本项目由社区维护，与 NVIDIA、AMD、Apple 均无关。规格数据整理自各厂商公开资料，
可能不完整或已过时；采购与容量规划请以官方规格书为准。
所有商标归各自所有者所有。

## 许可

数据与文档采用 [CC BY 4.0](LICENSE)，脚本采用 [MIT](LICENSE-CODE)。
