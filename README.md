# DAT-E6: Resilience & Global Regularity in Quasi-Lattices

![Master Dashboard](plots/master_manuscript_dashboard.png)

## Overview
This repository contains the computational framework and simulation suite for the **DAT-E6 Resilience Project**. Our research demonstrates that icosahedral projection lattices (DAT-E6) exhibit superior stability and thermal resilience compared to standard Euclidean cubic grids.

The project is structured around **Five Pillars of Research**:
1.  **Global Regularity**: Bounded vorticity in Navier-Stokes simulations (=10^3–10^5$).
2.  **Information Efficiency**: High-fidelity data capture measured via Shannon Entropy.
3.  **Symmetry Optimization**: Resonance detection at the structural singularity $\delta_0 \approx 0.309$.
4.  **Thermal Resilience**: Near-zero heat leakage (-zsh.004\%$) through phononic mirroring.
5.  **Reproducibility**: Fully containerized execution environment via Docker.

## Project Structure
```text
.
├── manuscript/             # Master execution scripts and LaTeX source
├── simulations/            # Core Python simulation engines
├── notebooks/              # Interactive verification (Jupyter)
├── appendices/             # Mathematical derivations (LaTeX)
├── data/                   # Validated CSV results (Pillars 1-4)
├── plots/                  # Publication-ready figures
├── Dockerfile              # Containerization for Pillar 5
└── THEORY_SUPPLEMENT.md    # Detailed mathematical scaffolding
```

## Quick Start
To reproduce the full manuscript dataset, ensure you have Docker installed and run:

```bash
# Build and run the full simulation suite
docker build -t dat-e6-resilience .
docker run -v $(pwd)/data:/app/data dat-e6-resilience
```

Alternatively, run the master script locally:
```bash
bash manuscript/run_all_sims.sh
```

## Key Findings
- **Vorticity Bounding**: Unlike cubic grids that diverge at high Reynolds numbers, DAT-E6 maintains a bounded vorticity state ($\omega_{max} \approx 1.06$) through a geometric depletion mechanism.
- **Phononic Bandgap**: The quasi-periodic nature of the lattice creates an effective "mirror" for thermal vibrations, leading to extreme insulation properties at ^\circ C$.

## Citation
If you use this code or the DAT-E6 lattice geometry in your research, please cite:
> *Bryan et al., "Resilience and Global Regularity in Icosahedral Projection Lattices," DAT-E6 Research Series, 2024.*
