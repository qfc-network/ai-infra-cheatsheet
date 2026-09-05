# AMD Instinct Accelerators

AMD's data center GPU line. HBM capacity has been AMD's consistent lead over the equivalent NVIDIA part; scale-up domain size is where it falls behind.

| Parameter | MI250X | MI300X | MI325X | MI350X | MI355X |
|---|---|---|---|---|---|
| Architecture | CDNA 2 | CDNA 3 | CDNA 3 | CDNA 4 | CDNA 4 |
| Process | TSMC 6nm | TSMC 5nm + 6nm chiplets | TSMC 5nm + 6nm chiplets | TSMC 3nm + 6nm chiplets | TSMC 3nm + 6nm chiplets |
| Compute units | 220 | 304 | 304 | 256 | 256 |
| Memory | 128 GB HBM2e | 192 GB HBM3 | 256 GB HBM3E | 288 GB HBM3E | 288 GB HBM3E |
| Memory bandwidth | 3.2 TB/s | 5.3 TB/s | 6 TB/s | 8 TB/s | 8 TB/s |
| FP64 matrix | 95.7 TFLOPS | 163.4 TFLOPS | 163.4 TFLOPS | 72.1 TFLOPS (vector and matrix) | 78.6 TFLOPS (vector and matrix) |
| FP16/BF16 (dense) | 383 TFLOPS | 1.3 PFLOPS | 1.3 PFLOPS | 2.31 PFLOPS | 2.52 PFLOPS |
| FP8 (dense) | not supported | 2.6 PFLOPS | 2.6 PFLOPS | 4.61 PFLOPS | 5.03 PFLOPS |
| FP4 / MXFP4 (dense) | not supported | not supported | not supported | 9.23 PFLOPS (MXFP4) | 10.07 PFLOPS (MXFP4) |
| GPU interconnect | Infinity Fabric 3rd gen | Infinity Fabric, ring of 8, 896 GB/s aggregate | Infinity Fabric, ring of 8, 896 GB/s aggregate | Infinity Fabric, 160 GB/s per GPU pair, 8-GPU mesh | Infinity Fabric, 160 GB/s per GPU pair, 8-GPU mesh |
| Total board power | 560 W | 750 W | 1,000 W | 1,000 W | 1,400 W |
| Cooling | air or liquid | air | air | air | direct liquid |
| Launch | 2021 | 2023 | 2024 | 2025 | 2025 |

> - AMD quotes MXFP4 and MXFP6 (OCP microscaling formats) where NVIDIA quotes NVFP4. They are different 4-bit encodings with different scaling-block layouts; a model quantized for one is not automatically portable.
> - CDNA 4 traded FP64 away: MI355X FP64 matrix is roughly half MI300X's, after CDNA 3 had been the HPC-friendly choice. Same direction NVIDIA took with Blackwell Ultra.
> - Sparsity does not apply to the 4-bit formats. AMD's datasheets carry a with-sparsity column for FP16, BF16, INT8 and OCP-FP8 only; MXFP6 and MXFP4 show N/A, so the FP4 figures here are the peak, not half of it.


## Sources

- [MI300X](https://www.amd.com/en/products/accelerators/instinct/mi300.html)
- [MI325X](https://www.amd.com/en/products/accelerators/instinct/mi300.html)
- [MI350X](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi350x-gpu-brochure.pdf)
- [MI355X](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi355x-gpu-brochure.pdf)

---

[Back to index](../README.zh-CN.md)
