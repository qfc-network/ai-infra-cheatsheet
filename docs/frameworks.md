# Training Frameworks

The layer models are actually written in, between the inference engines above and the compute stacks below. PyTorch is the gravity centre: every vendor writes a PyTorch backend, and the two that also build a full vertical stack - Huawei and Apple - do it because they had to.

| Parameter | PyTorch | JAX | TensorFlow + Keras 3 | MLX | MindSpore | PaddlePaddle |
|---|---|---|---|---|---|---|
| Origin | Meta, now the PyTorch Foundation | Google | Google | Apple | Huawei | Baidu |
| Programming model | eager by default, graphs via torch.compile | functional; grad, jit, vmap and pmap compose | graph-first with an eager mode | eager API with lazy evaluation | graph and eager | eager and static graph |
| Compiler path | TorchDynamo + Inductor | XLA | XLA, Grappler | lazy graph, mx.compile | GraphEngine into CANN | its own graph compiler |
| Neural net layer | torch.nn, built in | separate - Flax or NNX | Keras 3, which now also runs on JAX and PyTorch | mlx.nn, built in | built in | built in |
| Hardware backends | CUDA, ROCm, Intel XPU, Apple MPS; vendor plugins torch_npu and torch_musa | TPU first, then CUDA and ROCm | CUDA, TPU, CPU; LiteRT on device | Apple Silicon only | Ascend NPU first, plus GPU and CPU | CUDA, Kunlun, Ascend, CPU |
| Distributed training | DDP, FSDP; tensor and pipeline parallel via libraries | jit sharding and GSPMD | tf.distribute | limited, single machine in practice | auto-parallel | 4D hybrid parallelism |
| Ecosystem | everything targets it first - HF Transformers, vLLM, SGLang | DeepMind stack, MaxText | production serving and mobile or edge | mlx-lm; an LM Studio backend on Mac | the Ascend software stack | large Chinese industrial ecosystem - PaddleOCR and friends |
| Best for | the default for research and open-source models | TPU-scale training, and anything that wants composable transforms | existing deployments; research has moved on | local work on a Mac, exploiting unified memory | training on Ascend without going through PyTorch | industrial deployment in China, especially on domestic silicon |

> - PyTorch bundles its neural-network layer; JAX does not, which is why a JAX project also picks Flax or NNX. Keras 3 is the odd one out - it is now a front end over TensorFlow, JAX or PyTorch rather than TensorFlow's own.
> - The training frameworks people name most often are not peers of these. HF Transformers, Lightning, DeepSpeed, Megatron-LM, torchtitan, TRL, Axolotl and Unsloth all sit on top of PyTorch. "Training in PyTorch" usually means touching that layer, not this one.
> - Also in this layer but not tabled: OneFlow (PyTorch-compatible API, SBP parallelism), tinygrad (about ten thousand lines, many backends), and the Rust pair Candle and Burn, aimed at inference and embedded deployment.
> - Framework choice and silicon choice are coupled. MindSpore exists for Ascend, MLX for Apple Silicon, Paddle reaches Kunlun. Only PyTorch is something every vendor writes a backend for, which is the same gravity the compute stacks table shows for CUDA one layer down.


---

[Back to index](../README.zh-CN.md)
