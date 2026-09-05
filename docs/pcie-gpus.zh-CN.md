# 数据中心 PCIe 加速卡

SXM 基板之外的另一条部署路线。这些卡的区别在功耗和形态，不在峰值算力—— 70 W 单槽卡随便哪台服务器都插得下，600 W 双槽卡得配专门的机箱。

| 参数 | T4 | A10 | L4 | L40S | H100 NVL | H200 NVL |
|---|---|---|---|---|---|---|
| 架构 | Turing | Ampere | Ada Lovelace | Ada Lovelace | Hopper | Hopper |
| 显存 | 16 GB GDDR6 | 24 GB GDDR6 | 24 GB GDDR6 | 48 GB GDDR6，带 ECC | 94 GB HBM3 | 141 GB HBM3e |
| 显存带宽 | 300 GB/s | 600 GB/s | 300 GB/s | 864 GB/s | 3,938 GB/s | 4.8 TB/s |
| FP16 张量 | 65 TFLOPS（稠密——Turing 没有稀疏） | 125 / 250 TFLOPS（稠密 / 稀疏） | 242 TFLOPS（稀疏） | 733 TFLOPS（稀疏） | 1,671 TFLOPS（稀疏） | 1,671 TFLOPS（稀疏） |
| FP8 张量 | 不支持 | 不支持 | 485 TFLOPS（稀疏） | 1,466 TFLOPS（稀疏） | 3,341 TFLOPS（稀疏） | 3,341 TFLOPS（稀疏） |
| 形态 | 半高单槽 | 全高全长单槽 | 半高单槽 | 全高全长双槽 | 全高全长双槽 | 双槽风冷 |
| PCIe | Gen3 x16, 32 GB/s | Gen4 x16, 64 GB/s | Gen4 x16, 64 GB/s | Gen4 x16, 64 GB/s | Gen5 x16, 128 GB/s | Gen5 x16, 128 GB/s |
| NVLink | 无 | 无 | 无 | 无 | 桥接，成对使用 | 2 卡或 4 卡桥接，单卡 900 GB/s |
| MIG | 不支持 | 不支持 | 不支持 | 不支持 | 最多 7 个实例 | 最多 7 个实例，每个 16.5 GB |
| 最大功耗 | 70 W | 150 W | 72 W | 350 W | 400 W | 最高 600 W（可配置） |
| 上市时间 | 2018 | 2021 | 2023 | 2023 | 2023 | 2024 |

> - 功耗才是真正的分界线。70 W 的 L4 或 T4 插进标准服务器不用动任何东西； 350 W 的 L40S 要考虑风道；最高 600 W 的 H200 NVL 需要为它设计的机箱。 决定一个机群标准化选哪张卡的通常是这个约束，不是算力。
> - 只有 HBM 卡才有 MIG 和 NVLink 桥接。GDDR6 卡的多卡协作只能走 PCIe， 各卡显存互不相通；H100 NVL 和 H200 NVL 则可以两卡或四卡通过桥接互联。
> - H100 NVL 与 H200 NVL 是同一颗 Hopper die、同一个 PCIe 功耗档， 所以 FP8 和 FP16 数字完全一样。区别在显存：94 GB HBM3 对 141 GB HBM3e。
> - Blackwell 这一代的 PCIe 选择见"消费级与工作站 GPU"表里的 RTX PRO 6000 Blackwell 一行—— 96 GB GDDR7 带 ECC、双槽、600 W。放在那边，不在此重复。


## 资料来源

- [T4](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-t4/t4-tensor-core-datasheet-951643.pdf)
- [A10](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a10/pdf/datasheet-new/nvidia-a10-datasheet.pdf)
- [L4](https://www.nvidia.com/en-us/data-center/l4/)
- [L40S](https://www.nvidia.com/en-us/data-center/l40s/)
- [H100 NVL](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/h100/PB-11773-001_v01.pdf)
- [H100 NVL](https://www.nvidia.com/en-us/data-center/h100/)
- [H200 NVL](https://www.nvidia.com/en-us/data-center/h200/)

---

[返回目录](../README.md)
