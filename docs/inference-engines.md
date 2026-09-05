# Inference Engines & Local Apps

The layer between model weights and the hardware above. Which engine runs on your accelerator decides whether the chip is usable at all - a spec sheet is worth nothing if no engine targets the backend.

| Parameter | vLLM | SGLang | TensorRT-LLM | llama.cpp | Ollama | LM Studio |
|---|---|---|---|---|---|---|
| What it is | serving engine (Python) | serving engine (Python) | compiled engine (C++ / Python) | C/C++ library + bundled server | CLI + local server | desktop GUI app |
| Hardware backends | NVIDIA, AMD ROCm, Intel XPU, CPU; plugins for TPU, Gaudi, Ascend, Apple Silicon | NVIDIA (incl. GB200, B300, DGX Spark, 5090), AMD MI300/MI355, Intel Xeon CPU, TPU, Ascend NPU | NVIDIA only | CUDA, ROCm, Metal, SYCL/oneAPI, Vulkan, plain CPU | CUDA, ROCm, Metal (wraps llama.cpp) | Metal / MLX on Mac; CUDA, ROCm, Vulkan on PC |
| Key technique | PagedAttention + continuous batching | RadixAttention prefix caching + frontend DSL | ahead-of-time kernel compilation, in-flight batching | GGUF format, aggressive quantization, CPU/GPU hybrid offload | model library with one-command pull and run | GUI over llama.cpp and MLX |
| Weight format | HF safetensors | HF safetensors | HF safetensors, compiled to an engine file | GGUF | GGUF | GGUF, MLX |
| Quantization | GPTQ, AWQ, FP8, INT8, and more | FP8, AWQ, GPTQ | FP8, FP4 on Blackwell, INT4 AWQ, SmoothQuant | GGUF K-quants and IQ-quants, roughly 2-8 bit | GGUF | GGUF, MLX |
| Multi-GPU | tensor + pipeline parallel | tensor + pipeline + data parallel | tensor + pipeline parallel | split layers across GPUs, not true tensor parallel | inherited from llama.cpp | limited |
| API | OpenAI-compatible HTTP | OpenAI-compatible HTTP | via Triton Inference Server or NVIDIA Dynamo | OpenAI-compatible server included | own API plus OpenAI-compatible | local OpenAI-compatible server |
| Best for | general production serving, the default choice | shared prefixes, agents, structured and multi-call programs | squeezing the last throughput out of NVIDIA when a build step is acceptable | running anywhere - Mac, mixed CPU/GPU, odd hardware | fastest path to a model running on a dev machine | browsing and running models without touching a terminal |
| License | Apache 2.0 | Apache 2.0 | Apache 2.0 | MIT | MIT | proprietary, free to use |

> - Two families, two weight formats. vLLM, SGLang and TensorRT-LLM consume Hugging Face safetensors; llama.cpp, Ollama and LM Studio consume GGUF. A quantized checkpoint from one family does not load in the other.
> - Serving many users needs paged KV cache and continuous batching, which is what vLLM and SGLang exist for. For one user at a time on a laptop, llama.cpp is simpler and gives up little.
> - Backend support moves fast, especially the plugin backends for Gaudi, Ascend, TPU and Apple Silicon. Check the project's own install docs before assuming a chip is covered; "supported" can mean a community plugin rather than a tested first-class path.
> - This table is why the software column matters in the hardware tables above. A GPU with no engine targeting it is not usable no matter what its datasheet says.


## Sources

- [vLLM](https://docs.vllm.ai/en/stable/getting_started/installation/)
- [vLLM](https://github.com/vllm-project/vllm)
- [SGLang](https://github.com/sgl-project/sglang)

---

[Back to index](../README.zh-CN.md)
