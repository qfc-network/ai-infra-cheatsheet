# AMD Instinct 加速卡

AMD 的数据中心 GPU 线。相对同期 NVIDIA 产品，AMD 一直在 HBM 容量上领先， 短板在 scale-up 域的规模。

| 参数 | MI250X | MI300X | MI325X | MI350X | MI355X |
|---|---|---|---|---|---|
| 架构 | CDNA 2 | CDNA 3 | CDNA 3 | CDNA 4 | CDNA 4 |
| 制程 | TSMC 6nm | TSMC 5nm + 6nm 小芯片 | TSMC 5nm + 6nm 小芯片 | TSMC 3nm + 6nm 小芯片 | TSMC 3nm + 6nm 小芯片 |
| 计算单元 | 220 | 304 | 304 | 256 | 256 |
| 显存 | 128 GB HBM2e | 192 GB HBM3 | 256 GB HBM3E | 288 GB HBM3E | 288 GB HBM3E |
| 显存带宽 | 3.2 TB/s | 5.3 TB/s | 6 TB/s | 8 TB/s | 8 TB/s |
| FP64 矩阵 | 95.7 TFLOPS | 163.4 TFLOPS | 163.4 TFLOPS | ~78.6 TFLOPS | ~78.6 TFLOPS |
| FP16/BF16（稠密） | 383 TFLOPS | 1.3 PFLOPS | 1.3 PFLOPS | ~2.3 PFLOPS | 2.5 PFLOPS |
| FP8（稠密） | 不支持 | 2.6 PFLOPS | 2.6 PFLOPS | 4.6 PFLOPS | 5.0 PFLOPS |
| FP4 / MXFP4（稠密） | 不支持 | 不支持 | 不支持 | 9.2 PFLOPS | 10 PFLOPS |
| GPU 互联 | Infinity Fabric 3rd gen | Infinity Fabric，8 卡全互联网格 | Infinity Fabric，8 卡全互联网格 | 第 4 代 Infinity Fabric，8 卡网格 | 第 4 代 Infinity Fabric，8 卡网格 |
| 整卡功耗 | 560 W | 750 W | 1,000 W | 1,000 W | 1,400 W |
| 散热 | 风冷或液冷 | 风冷 | 风冷 | 风冷 | 直接液冷 |
| 上市时间 | 2021 | 2023 | 2024 | 2025 | 2025 |

> - AMD 标的是 MXFP4 / MXFP6（OCP microscaling 格式），NVIDIA 标的是 NVFP4。 两者是不同的 4bit 编码，缩放块布局也不同，为其一量化的模型不能直接搬到另一边。
> - CDNA 4 砍掉了 FP64：MI355X 的 FP64 矩阵算力大约只有 MI300X 的一半， 而 CDNA 3 本来是 HPC 友好的选择。NVIDIA 在 Blackwell Ultra 上是同一个方向。
> - MI350 系列的 FP64 与 FP16 数字是用 AMD 公布的整机数据除以 8 推算的， 写进采购文件前请核对官方 datasheet PDF。


## 资料来源

- [MI300X](https://www.amd.com/en/products/accelerators/instinct/mi300.html)
- [MI325X](https://www.amd.com/en/products/accelerators/instinct/mi300.html)
- [MI350X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi350x.html)
- [MI355X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html)
- [MI355X](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi355x-gpu-brochure.pdf)

---

[返回目录](../README.md)
