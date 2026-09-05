# 训练框架

模型真正是用这一层写的，上接推理引擎，下接计算栈。PyTorch 是引力中心： 每家硬件厂商都得给它写后端；而另外自建一整套垂直栈的两家——华为和苹果—— 是因为不得不这么做。

| 参数 | PyTorch | JAX | TensorFlow + Keras 3 | MLX | MindSpore | PaddlePaddle |
|---|---|---|---|---|---|---|
| 出处 | Meta，现由 PyTorch 基金会托管 | Google | Google | Apple | 华为（昇思） | 百度（飞桨） |
| 编程范式 | 默认即时执行，torch.compile 转图 | 函数式；grad / jit / vmap / pmap 可组合 | 图优先，也有即时模式 | 即时 API + 惰性求值 | 图模式与即时模式 | 动态图与静态图 |
| 编译路径 | TorchDynamo + Inductor | XLA | XLA, Grappler | 惰性图，mx.compile | GraphEngine 下接 CANN | 自有图编译器 |
| 神经网络层 | 内置 torch.nn | 需另配——Flax 或 NNX | Keras 3，现在也能跑在 JAX 和 PyTorch 上 | 内置 mlx.nn | 内置 | 内置 |
| 硬件后端 | CUDA、ROCm、Intel XPU、Apple MPS；厂商插件 torch_npu、torch_musa | 首选 TPU，其次 CUDA 与 ROCm | CUDA、TPU、CPU；端侧走 LiteRT | 仅 Apple Silicon | 首选昇腾 NPU，另支持 GPU 与 CPU | CUDA、昆仑芯、昇腾、CPU |
| 分布式训练 | DDP、FSDP；张量与流水线并行靠外部库 | jit 分片与 GSPMD | tf.distribute | 有限，实际是单机 | 自动并行 | 4D 混合并行 |
| 生态 | 所有东西都优先适配它——HF Transformers、vLLM、SGLang | DeepMind stack, MaxText | 生产部署与移动/边缘端 | mlx-lm；Mac 上 LM Studio 的一种后端 | 昇腾软件栈 | 中文产业生态大——PaddleOCR 等 |
| 适合场景 | 研究和开源模型的默认选择 | TPU 上的大规模训练，以及需要可组合变换的场景 | 存量部署；研究侧已经转移 | Mac 本地开发，吃统一内存的红利 | 不绕道 PyTorch，直接在昇腾上训练 | 国内产业部署，尤其是国产芯片上 |

> - PyTorch 自带神经网络层，JAX 没有——所以 JAX 项目还要另选 Flax 或 NNX。 Keras 3 比较特殊，它现在是 TensorFlow / JAX / PyTorch 三者之上的公共前端， 不再只属于 TensorFlow。
> - 大家嘴里的"训练框架"多半不是这一层的同类。HF Transformers、Lightning、DeepSpeed、 Megatron-LM、torchtitan、TRL、Axolotl、Unsloth 都长在 PyTorch 之上。 说"用 PyTorch 训练"，动的通常是那一层，不是这一层。
> - 同层但没进表的还有：OneFlow（API 兼容 PyTorch，SBP 并行抽象）、 tinygrad（约万行，多后端），以及 Rust 的 Candle 和 Burn，主打推理与嵌入式部署。
> - 选框架和选芯片是绑在一起的。昇思是为昇腾存在的，MLX 是为 Apple Silicon， 飞桨能接昆仑芯。只有 PyTorch 是每家都得为它写后端的那个—— 和下面一层 CUDA 在计算栈表里的引力是同一回事。


---

[返回目录](../README.md)
