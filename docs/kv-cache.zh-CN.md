# KV Cache 与上下文长度

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


---

[返回目录](../README.md)
