# NVIDIA AI 基础设施速查表

一份 NVIDIA AI 数据中心全栈的对照速查表：GPU、DGX 整机、Grace 超级芯片、
机柜级 NVLink 系统，以及把它们连起来的网络。所有表格都由
[`data/`](data/) 下的 YAML 自动生成，改一个数字就是一个 PR。

[English](README.md) · [简体中文](README.zh-CN.md)

## 目录

- [DGX 整机](#dgx-整机)
- [数据中心旗舰 GPU（SXM）](#数据中心旗舰-gpusxm)
- [消费级与工作站 GPU](#消费级与工作站-gpu)
- [量化格式与显存占用（权重）](#量化格式与显存占用权重)
- [KV Cache 与上下文长度](#kv-cache-与上下文长度)
- [Grace 系列超级芯片](#grace-系列超级芯片)
- [机柜级 NVLink 系统](#机柜级-nvlink-系统)
- [NVLink / NVSwitch 各代对比](#nvlink--nvswitch-各代对比)
- [横向扩展网络](#横向扩展网络)
- [平台路线图](#平台路线图)

## DGX 整机

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

## 消费级与工作站 GPU

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

## 量化格式与显存占用（权重）

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

## KV Cache 与上下文长度

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
