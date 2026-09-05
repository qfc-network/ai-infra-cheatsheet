# AMD Instinct 整机与机柜

AMD 卖的是 8 卡 OAM 基板（"platform"）给 OEM，而不是 DGX 那样的自有整机品牌。 在 Helios 之前，其 scale-up 域上限就是 8 卡。

| 参数 | MI300X Platform | MI325X Platform | MI355X Platform | Helios (MI400 series, announced) |
|---|---|---|---|---|
| GPU 数量 | 8 x MI300X | 8 x MI325X | 8 x MI355X | 72 x MI400-series |
| 整机显存 | 1.5 TB HBM3 | 2 TB HBM3E | 2.3 TB HBM3E | 未公布 |
| 总显存带宽 | 42.4 TB/s | 48 TB/s | 64 TB/s | 未公布 |
| FP8（稠密） | 20.9 PFLOPS | 20.9 PFLOPS | 40.3 PFLOPS | 未公布 |
| FP4 / MXFP4（稠密） | 不支持 | 不支持 | 80.5 PFLOPS | 未公布 |
| scale-up 域 | 8 卡全互联网格，无交换芯片 | 8 卡全互联网格，无交换芯片 | 8 卡全互联网格，无交换芯片 | 72 卡经 UALink 互联，对标 NVL72 |
| 横向扩展网络 | 由 OEM 决定，通常 8 x 400 Gb/s | 由 OEM 决定，通常 8 x 400 Gb/s | 由 OEM 决定，最高 8 x 400 Gb/s | Ultra Ethernet |
| 散热 | 风冷 | 风冷 | 风冷或直接液冷 | 液冷 |
| 交付形态 | OCP UBB 基板，装进 OEM 机箱 | OCP UBB 基板，装进 OEM 机箱 | OCP UBB 基板，装进 OEM 机箱 | 整机柜参考设计 |
| 上市时间 | 2023-2024 | 2024-2025 | 2025 | 2026（路线图） |

> - 这才是结构性差异，不是规格表上的差异。一台 MI355X 是 8 卡一个一致性域， 一个 GB300 NVL72 机柜是 72 卡。今天在 AMD 上超过 8 卡就要过网络， 这会直接改变模型怎么切分。
> - AMD 的答案是 UALink（开放的 scale-up 互联标准）加 Ultra Ethernet 做横向扩展， 随 Helios 一起落地。开放标准 vs NVIDIA 垂直整合的 NVLink，这才是真正的战略分歧。
> - AMD 没有 DGX 的对应物：它出基板，戴尔、慧与、超微等厂商做整机。 所以机箱功耗和物理规格因 OEM 而异，本表不列。


## 资料来源

- [MI300X Platform](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-platform-data-sheet.pdf)
- [MI355X Platform](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x/platform.html)

---

[返回目录](../README.md)
