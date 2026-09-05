# AMD Instinct 加速卡

AMD 的数据中心 GPU 线。相对同期 NVIDIA 产品，AMD 一直在 HBM 容量上领先， 短板在 scale-up 域的规模。

| 参数 | MI250X | MI300X | MI325X | MI350X | MI355X |
|---|---|---|---|---|---|
| 架构 | CDNA 2 | CDNA 3 | CDNA 3 | CDNA 4 | CDNA 4 |
| 制程 | TSMC 6nm | TSMC 5nm + 6nm 小芯片 | TSMC 5nm + 6nm 小芯片 | TSMC 3nm + 6nm 小芯片 | TSMC 3nm + 6nm 小芯片 |
| 计算单元 | 220 | 304 | 304 | 256 | 256 |
| 显存 | 128 GB HBM2e | 192 GB HBM3 | 256 GB HBM3E | 288 GB HBM3E | 288 GB HBM3E |
| 显存带宽 | 3.2 TB/s | 5.3 TB/s | 6 TB/s | 8 TB/s | 8 TB/s |
| FP64 矩阵 | 95.7 TFLOPS | 163.4 TFLOPS | 163.4 TFLOPS | 72.1 TFLOPS (vector and matrix) | 78.6 TFLOPS (vector and matrix) |
| FP16/BF16（稠密） | 383 TFLOPS | 1.3 PFLOPS | 1.3 PFLOPS | 2.31 PFLOPS | 2.52 PFLOPS |
| FP8（稠密） | 不支持 | 2.6 PFLOPS | 2.6 PFLOPS | 4.61 PFLOPS | 5.03 PFLOPS |
| FP4 / MXFP4（稠密） | 不支持 | 不支持 | 不支持 | 9.23 PFLOPS (MXFP4) | 10.07 PFLOPS (MXFP4) |
| GPU 互联 | Infinity Fabric 3rd gen | Infinity Fabric，8 卡环形，合计 896 GB/s | Infinity Fabric，8 卡环形，合计 896 GB/s | Infinity Fabric，卡对卡 160 GB/s，8 卡网格 | Infinity Fabric，卡对卡 160 GB/s，8 卡网格 |
| 整卡功耗 | 560 W | 750 W | 1,000 W | 1,000 W | 1,400 W |
| 散热 | 风冷或液冷 | 风冷 | 风冷 | 风冷 | 直接液冷 |
| 上市时间 | 2021 | 2023 | 2024 | 2025 | 2025 |

> - AMD 标的是 MXFP4 / MXFP6（OCP microscaling 格式），NVIDIA 标的是 NVFP4。 两者是不同的 4bit 编码，缩放块布局也不同，为其一量化的模型不能直接搬到另一边。
> - CDNA 4 砍掉了 FP64：MI355X 的 FP64 矩阵算力大约只有 MI300X 的一半， 而 CDNA 3 本来是 HPC 友好的选择。NVIDIA 在 Blackwell Ultra 上是同一个方向。
> - 4bit 格式没有稀疏加成。AMD 规格书里只有 FP16、BF16、INT8 和 OCP-FP8 有"含稀疏" 那一列，MXFP6 和 MXFP4 都是 N/A——所以表里的 FP4 数字就是峰值本身，不是峰值的一半。


## 资料来源

- [MI300X](https://www.amd.com/en/products/accelerators/instinct/mi300.html)
- [MI325X](https://www.amd.com/en/products/accelerators/instinct/mi300.html)
- [MI350X](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi350x-gpu-brochure.pdf)
- [MI355X](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi355x-gpu-brochure.pdf)

---

[返回目录](../README.md)
