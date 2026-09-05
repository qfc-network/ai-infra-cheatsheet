# 推理引擎与本地应用

模型权重和上面那些硬件之间的一层。你的加速卡能不能用，取决于哪个引擎支持它—— 没有引擎做后端的话，规格再好也是废的。

| 参数 | vLLM | SGLang | TensorRT-LLM | llama.cpp | Ollama | LM Studio |
|---|---|---|---|---|---|---|
| 是什么 | 服务引擎（Python） | 服务引擎（Python） | 编译式引擎（C++ / Python） | C/C++ 库 + 自带服务端 | 命令行 + 本地服务 | 桌面图形应用 |
| 硬件后端 | NVIDIA、AMD ROCm、Intel XPU、CPU；TPU / Gaudi / 昇腾 / Apple Silicon 有插件 | NVIDIA（含 GB200、B300、DGX Spark、5090）、AMD MI300/MI355、Intel Xeon CPU、TPU、昇腾 NPU | 仅 NVIDIA | CUDA、ROCm、Metal、SYCL/oneAPI、Vulkan、纯 CPU | CUDA、ROCm、Metal（封装 llama.cpp） | Mac 上 Metal / MLX；PC 上 CUDA、ROCm、Vulkan |
| 核心技术 | PagedAttention + 连续批处理 | RadixAttention 前缀缓存 + 前端 DSL | 预先编译 kernel、in-flight batching | GGUF 格式、激进量化、CPU/GPU 混合卸载 | 模型库，一条命令拉取即用 | llama.cpp 与 MLX 之上的图形界面 |
| 权重格式 | HF safetensors | HF safetensors | HF safetensors，需编译成 engine 文件 | GGUF | GGUF | GGUF, MLX |
| 量化支持 | GPTQ、AWQ、FP8、INT8 等 | FP8, AWQ, GPTQ | FP8、Blackwell 上的 FP4、INT4 AWQ、SmoothQuant | GGUF 的 K-quant 与 IQ-quant，约 2~8 bit | GGUF | GGUF, MLX |
| 多卡 | 张量并行 + 流水线并行 | 张量 + 流水线 + 数据并行 | 张量并行 + 流水线并行 | 按层切分到多卡，不是真正的张量并行 | 继承 llama.cpp | 有限 |
| 接口 | OpenAI 兼容 HTTP | OpenAI 兼容 HTTP | 经 Triton Inference Server 或 NVIDIA Dynamo | 自带 OpenAI 兼容服务端 | 自有 API + OpenAI 兼容 | 本地 OpenAI 兼容服务 |
| 适合场景 | 通用生产部署，默认选择 | 共享前缀多的场景、agent、结构化与多轮调用 | 能接受编译步骤、要把 NVIDIA 榨到极限时 | 哪儿都能跑——Mac、CPU/GPU 混合、冷门硬件 | 开发机上最快跑起一个模型 | 不碰终端就能找模型、跑模型 |
| 许可 | Apache 2.0 | Apache 2.0 | Apache 2.0 | MIT | MIT | 闭源，免费使用 |

> - 两大阵营，两种权重格式。vLLM、SGLang、TensorRT-LLM 吃 Hugging Face safetensors； llama.cpp、Ollama、LM Studio 吃 GGUF。一边量化好的权重在另一边加载不了。
> - 要服务多用户就需要分页 KV cache 和连续批处理，这正是 vLLM 和 SGLang 存在的理由。 笔记本上一次只有一个人用的话，llama.cpp 更简单，也没损失多少。
> - 后端支持变化很快，尤其是 Gaudi、昇腾、TPU、Apple Silicon 这些插件后端。 判断某颗芯片是否被支持前请查项目自己的安装文档——"支持"有时指社区插件， 而不是经过测试的一等公民路径。
> - 这张表也解释了上面那些硬件表里"软件栈"那一列为什么重要： 没有引擎做后端的 GPU，规格书写得再好也用不起来。


## 资料来源

- [vLLM](https://docs.vllm.ai/en/stable/getting_started/installation/)
- [vLLM](https://github.com/vllm-project/vllm)
- [SGLang](https://github.com/sgl-project/sglang)

---

[返回目录](../README.md)
