# AMD Instinct Platforms & Racks

AMD sells an 8-GPU OAM baseboard (the "platform") to OEMs rather than a branded appliance like DGX. The scale-up domain stops at 8 GPUs until Helios.

| Parameter | MI300X Platform | MI325X Platform | MI355X Platform | Helios (MI400 series, announced) |
|---|---|---|---|---|
| GPUs | 8 x MI300X | 8 x MI325X | 8 x MI355X | 72 x MI400-series |
| Total GPU memory | 1.5 TB HBM3 | 2 TB HBM3E | 2.3 TB HBM3E | TBA |
| Aggregate bandwidth | 42.4 TB/s | 48 TB/s | 64 TB/s | TBA |
| FP8 (dense) | 20.8 PFLOPS | 20.8 PFLOPS | 40.3 PFLOPS | TBA |
| FP4 / MXFP4 (dense) | not supported | not supported | 80.5 PFLOPS | TBA |
| Scale-up domain | 8 GPUs, fully connected mesh, no switch | 8 GPUs, fully connected mesh, no switch | 8 GPUs, fully connected mesh, no switch | 72 GPUs over UALink - AMD's answer to NVL72 |
| Scale-out network | OEM choice, typically 8 x 400 Gb/s | OEM choice, typically 8 x 400 Gb/s | OEM choice, up to 8 x 400 Gb/s | Ultra Ethernet |
| Cooling | air | air | air or direct liquid | liquid |
| Sold as | OCP UBB baseboard for OEM chassis | OCP UBB baseboard for OEM chassis | OCP UBB baseboard for OEM chassis | full rack reference design |
| Availability | 2023-2024 | 2024-2025 | 2025 | 2026 (roadmap) |

> - This is the structural difference, not a spec-sheet one. An MI355X node is 8 GPUs in one coherent domain; a GB300 NVL72 rack is 72. Anything larger than 8 GPUs on AMD crosses the network today, which changes how you shard a model.
> - AMD's answer is UALink (an open scale-up interconnect standard) plus Ultra Ethernet for scale-out, arriving with Helios. Open standards versus NVIDIA's vertically integrated NVLink is the actual strategic bet.
> - There is no DGX equivalent: AMD ships baseboards, and Dell, HPE, Supermicro and others build the box. Chassis power and physical specs therefore vary by OEM and are not listed here.


## Sources

- [MI300X Platform](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-platform-data-sheet.pdf)
- [MI355X Platform](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x/platform.html)

---

[Back to index](../README.zh-CN.md)
