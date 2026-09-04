# 横向扩展网络

出了 NVLink 域之后，GPU 之间的流量走 InfiniBand 或 Spectrum-X 以太网。

| 参数 | Quantum-2 InfiniBand | Quantum-X800 InfiniBand | Spectrum-X Ethernet |
|---|---|---|---|
| 类型 | InfiniBand NDR | InfiniBand XDR | 以太网（无损、面向 AI 调优） |
| 端口速率 | 400 Gb/s | 800 Gb/s | 800 GbE |
| 交换机 | QM9700 / QM9790 | Q3400-RA | Spectrum-4 SN5600 |
| 交换容量 | 64 x 400 Gb/s, 51.2 Tb/s | 144 x 800 Gb/s | 64 x 800 GbE, 51.2 Tb/s |
| 配套网卡 | ConnectX-7 | ConnectX-8 SuperNIC | BlueField-3 SuperNIC / ConnectX-8 |
| 网内计算 | SHARPv3 | SHARPv4 | 自适应路由 + 拥塞控制 |
| 上市时间 | 2021-2022 | 2024-2025 | 2023-2024 |

> - 一台 DGX/HGX 通常是 8 张计算网卡（每卡一张，用于东西向）+ 1~2 张 DPU （用于存储与管理流量）。


## 资料来源

- [Quantum-2 InfiniBand](https://www.nvidia.com/en-us/networking/quantum2/)
- [Quantum-X800 InfiniBand](https://www.nvidia.com/en-us/networking/quantum-x800/)
- [Spectrum-X Ethernet](https://www.nvidia.com/en-us/networking/spectrumx/)

---

[返回目录](../README.md)
