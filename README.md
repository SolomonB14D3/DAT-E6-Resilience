# DAT 2.0: E₆ Lattice Resilience and Topological Alignment

This repository provides the "Gold Standard" simulation engine for **Dynamic Alignment Theory (DAT) 2.0**. It demonstrates the structural resilience of a 6D E₆ root lattice projected onto a 3D icosahedral manifold.

## Abstract
This research presents a deterministic verification of DAT 2.0. Utilizing a damped Hamiltonian framework, we subject an r=7 E₆ lattice (2,442 nodes) to stochastic phason strain. Our results confirm a universal **Topological Snap-back** effect: despite high-magnitude entropy induction driving the spectral exponent into a chaotic regime (β < 0), the system exhibits autonomous realignment with its 6D anchors. Post-strain analysis shows a consistent convergence to a ground-state stasis of β ≈ 3.01, characterized by the formation of **"Frozen Stars"**.

## Core Components
- **dat_gold_standard.py**: The primary engine implementing E₆ root generation and Hamiltonian dynamics.
- **dat_sweep_analysis.py**: Multi-trial stress test (σ = 0.2, 0.5, 0.8) for verifying resilience.
- **THEORY.md**: Full mathematical derivation of the embedding and stability analysis.

## Usage
1. Ensure `torch`, `numpy`, `pandas`, and `scipy` are installed.
2. Run the sweep: `python dat_sweep_analysis.py`
3. View results in `DAT_Sweep_Results.png` and `sweep_statistics.csv`.
