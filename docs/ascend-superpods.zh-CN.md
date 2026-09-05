# 华为 Atlas SuperPoD

华为对 NVL72 的回应不是更强的芯片，而是大得多的一致性域。 GB300 NVL72 一个机柜 72 卡，Atlas 950 是 8,192 张卡挂在同一套互联上。

| 参数 | Atlas 900 A3 (CloudMatrix 384) | Atlas 950 SuperPoD | Atlas 960 SuperPoD |
|---|---|---|---|
| 加速卡数量 | 384 x Ascend 910C | 8,192 x Ascend 950DT | 15,488 x Ascend 960 |
| 总内存 | 未公布 | 1,152 TB | 4,460 TB |
| 互联总带宽 | Unified Bus，全互联无阻塞 | 16 PB/s | 34 PB/s |
| FP8 算力 | 未公布 | 8 EFLOPS | 30 EFLOPS |
| FP4 算力 | 不支持 | 16 EFLOPS | 60 EFLOPS |
| 机柜数 | 16 | 160（128 计算 + 32 通信） | 220（176 计算 + 44 通信） |
| NVIDIA 对位 | GB200 NVL72 | 已超出 NVL72 的尺度，只能在集群层面比 | 已超出 NVL72 的尺度，只能在集群层面比 |
| 可用时间 | 2025 年 3 月，已部署 300+ 套 | 2026 Q4 | 2027 Q4 |

> - 比的时候要注意口径。GB300 NVL72 是一个机柜，Atlas 950 是 160 个机柜。 华为是拿功耗和占地换互联域规模，因为单芯片受制程限制打不过 Blackwell。
> - 本表数据全部出自华为全联接 2025 的主题演讲。流传很广的 CloudMatrix "48 TB HBM"、 "300 PFLOPS 稠密 BF16" 等数字来自分析机构拆解，不是华为公布的，这里没有采用。
> - 功耗是华为不放在标题里、而 NVIDIA 会放的数字。在有人公布实测整柜功耗之前， 任何和 NVL72 的能效比对比都该打个问号。


## 资料来源

- [Atlas 900 A3 (CloudMatrix 384)](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- [Atlas 950 SuperPoD](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- [Atlas 960 SuperPoD](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)

---

[返回目录](../README.md)
