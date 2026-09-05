# CUDA 版本与计算能力

哪个 sm_ 目标属于哪代架构，以及哪个工具链还支持它。 sm_ 与架构的对应关系摘自 CUDA 13.3 的 nvcc 文档，GPU 那一列是为了方便定位补的。

| 名称 | sm_ 目标 | 代表性 GPU | 起始 CUDA 版本 | 主要新增 | CUDA 13.3 是否支持 |
|---|---|---|---|---|---|
| Maxwell | sm_50, sm_52, sm_53 | GTX 900 系列、Tesla M40 | CUDA 6.5 | 统一内存改进 | 已移除 |
| Pascal | sm_60, sm_61 | P100（60）、P40 与 GTX 10 系列（61） | CUDA 8 | 首代 NVLink，P100 支持 FP16 | 已移除 |
| Volta | sm_70, sm_72 | V100, Titan V | CUDA 9 | 首代 Tensor Core、独立线程调度 | 已移除 |
| Turing | sm_75 | T4、RTX 20 系列、Quadro RTX | CUDA 10 | INT8 / INT4 张量运算、RT Core | 支持——目前支持的最老一代，也是 nvcc 的默认目标 |
| Ampere | sm_80, sm_86, sm_87, sm_88 | A100（80）、A40 与 RTX 30（86）、Jetson Orin（87） | CUDA 11 | TF32、BF16、2:4 结构化稀疏、MIG | 支持 |
| Ada Lovelace | sm_89 | L40S、L4、RTX 40 系列、RTX 6000 Ada | CUDA 11.8 | FP8 张量核 | 支持 |
| Hopper | sm_90, sm_90a | H100, H200, GH200 | CUDA 12 | FP8 Transformer Engine、TMA、线程块簇、DPX | 支持 |
| Blackwell | sm_100、sm_103、sm_110、sm_120、sm_121（各有 f 与 a 变体） | B200 与 GB200、B300 与 GB300、RTX 50 系列、RTX PRO 6000 | CUDA 12.8 | FP4 张量核、第二代 Transformer Engine | 支持 |

> - CUDA 13 移除了 Maxwell、Pascal 和 Volta。nvcc 13.3 最低只接受 sm_75， 也就是说 V100 必须用 CUDA 12.x 工具链——围绕老硬件做规划前值得先确认这一条。
> - 后缀是有讲究的。裸的 sm_90 向前兼容；sm_90a 是架构专属，会解锁只有该架构才有的指令 （CUTLASS 和 FlashAttention-3 用的 Hopper wgmma 就是这条路径）。 CUDA 13 新增了 f 后缀表示"家族专属"，介于两者之间。
> - 计算能力不代表性能。sm_87（Jetson Orin）和 sm_80（A100）都是 Ampere， 它们共享特性，除此之外毫无共同之处。
> - NVIDIA 并没有给每个 sm_ 值都公布对应产品。文档里 sm_88 归 Ampere、sm_110 归 Blackwell， 但都没点名具体 GPU，所以本表不去猜。
> - 次版本兼容：自 CUDA 11 起，用某个次版本编译的程序可以在同一大版本的任意更新驱动上运行， 不需要工具链和驱动严格对齐。


---

[返回目录](../README.md)
