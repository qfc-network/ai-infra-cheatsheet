# KV Cache vs Context Length

KV bytes per token = 2 x layers x kv_heads x head_dim x bytes_per_element. Figures below are an FP16 KV cache for a single sequence, in GiB. Check your model's config.json for its real layer and kv_head counts.

| Name | Config | Per token | 1K context | 8K context | 32K context | 128K context |
|---|---|---|---|---|---|---|
| 7B, multi-head attention | 32 layers x 32 kv heads x 128 | 512 KiB | 0.5 GiB | 4 GiB | 16 GiB | 64 GiB |
| 8B, grouped-query (8 kv heads) | 32 layers x 8 kv heads x 128 | 128 KiB | 0.13 GiB | 1 GiB | 4 GiB | 16 GiB |
| 32B, grouped-query (8 kv heads) | 64 layers x 8 kv heads x 128 | 256 KiB | 0.25 GiB | 2 GiB | 8 GiB | 32 GiB |
| 70B, grouped-query (8 kv heads) | 80 layers x 8 kv heads x 128 | 320 KiB | 0.31 GiB | 2.5 GiB | 10 GiB | 40 GiB |

> - Halve every number for an FP8 or INT8 KV cache. This is usually the cheapest way to buy context length back.
> - Multiply by batch size. The KV cache is per sequence, so 8 concurrent requests cost 8x. On a serving GPU this, not the weights, is what runs out.
> - Grouped-query attention is the biggest lever here: the 7B MHA row costs 4x the 8B GQA row despite being the smaller model. Latent attention (MLA) cuts it by roughly another order of magnitude.
> - This is why a 24 GB card "fits" a 30B 4-bit model (15 GiB of weights) and then dies at long context: 32K of KV cache is another 8 GiB.


---

[Back to index](../README.zh-CN.md)
