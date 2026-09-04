# Scale-Out Networking

Once you leave the NVLink domain, GPU-to-GPU traffic runs over InfiniBand or Spectrum-X Ethernet.

| Parameter | Quantum-2 InfiniBand | Quantum-X800 InfiniBand | Spectrum-X Ethernet |
|---|---|---|---|
| Type | InfiniBand NDR | InfiniBand XDR | Ethernet (lossless, AI-tuned) |
| Port speed | 400 Gb/s | 800 Gb/s | 800 GbE |
| Switch | QM9700 / QM9790 | Q3400-RA | Spectrum-4 SN5600 |
| Switch capacity | 64 x 400 Gb/s, 51.2 Tb/s | 144 x 800 Gb/s | 64 x 800 GbE, 51.2 Tb/s |
| Matching NIC | ConnectX-7 | ConnectX-8 SuperNIC | BlueField-3 SuperNIC / ConnectX-8 |
| In-network compute | SHARPv3 | SHARPv4 | adaptive routing, congestion control |
| Availability | 2021-2022 | 2024-2025 | 2023-2024 |

> - A DGX/HGX node typically pairs 8 compute NICs (one per GPU, east-west) with 1-2 DPUs for storage and management traffic.


## Sources

- [Quantum-2 InfiniBand](https://www.nvidia.com/en-us/networking/quantum2/)
- [Quantum-X800 InfiniBand](https://www.nvidia.com/en-us/networking/quantum-x800/)
- [Spectrum-X Ethernet](https://www.nvidia.com/en-us/networking/spectrumx/)

---

[Back to index](../README.zh-CN.md)
