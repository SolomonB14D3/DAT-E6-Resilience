# Discrete Alignment Theory (DAT)

Computational tools for icosahedral quasicrystal generation via E₆ → H₃ Coxeter projection, with applications to phonon localization and phason dynamics.

## Status: REVISED (January 2026)

The original claim that DAT "bounds vorticity growth" and proves Navier-Stokes regularity has been **withdrawn**. Rigorous analysis shows bounded multiplicative depletion cannot change the supercritical Z^(3/2) exponent in the enstrophy inequality. The "81.4% turbulence reduction" was a numerical solver artifact.

What remains is a computational framework for generating icosahedral quasicrystal point sets and studying their phonon/phason properties.

## What This Repo Provides

### Validated
- **Quasicrystal point set generation** via cut-and-project method (`dat_core.py`)
- **E₆ → H₃ folding** — correct Coxeter group theory (known mathematics)
- **Phonon localization contrast** — 4.2× IPR vs cubic (real physics of quasicrystals)
- **Phason slip dynamics** — bond reconfiguration under perpendicular-space perturbation

### Withdrawn
- ~~Vortex stretching bound → NS regularity~~ — debunked (see [analysis](https://github.com/SolomonB14D3/navier-stokes-h3/blob/main/analytical_proof_attempt.md))
- ~~81.4% turbulence reduction~~ — solver artifact (integrating factor prevents blowup regardless)
- ~~δ₀ as universal constraint across Millennium Problems~~ — overstated

## The Constant

$$\delta_0 = \frac{\sqrt{5}-1}{4} = \frac{1}{2\varphi} \approx 0.309$$

This is a geometric property of the icosahedron (related to the vertex angle θ = 63.43°). It appears in:
- The alignment geometry of icosahedral point sets (valid)
- Measured depletion in NS simulations (observed, but cannot prove regularity)

## Core Code

### `dat_core.py` — Quasicrystal Generator

Generates icosahedral quasicrystal point sets using φ-based basis vectors, permutation symmetries, and stereographic projection:

```python
from dat_core import get_h3_lattice

# Generate 1000-point icosahedral quasicrystal
lattice = get_h3_lattice(n_points=1000)
```

### `core/geometry.py` — Projection Engine

Projects points through a φ-based 3×5 matrix for icosahedral-like geometry:

```python
from core.geometry import get_icosahedral_projection

pts_3d = get_icosahedral_projection(n_points=100)
```

## Quick Start

```bash
git clone https://github.com/SolomonB14D3/Discrete-Alignment-Theory.git
cd Discrete-Alignment-Theory
pip install -r requirements.txt

# Generate quasicrystal lattice
python dat_core.py

# Run thermal localization comparison
python pillar4_thermal_diagnostic.py
```

## Background: E₆ → H₃ Folding

The E₆ Lie algebra (72 roots) folds via Z₂ outer automorphism through F₄ to recover the non-crystallographic H₃ (icosahedral) Coxeter group. This is established mathematics:

```
E₆ (72 roots, rank 6)
    ↓ Z₂ outer automorphism
F₄ (48 roots, rank 4)
    ↓ Non-crystallographic projection
H₃ (icosahedral, order 120)
```

The golden ratio φ = (1+√5)/2 appears naturally in icosahedral geometry (vertex coordinates, dihedral angles, etc.). This is well-known — see Coxeter (1973), Humphreys (1990).

## What's Legitimate Physics

**Phonon localization in quasicrystals** is a real, well-studied phenomenon. Quasicrystalline structures lack translational periodicity, leading to:
- Modified phonon dispersion relations
- Enhanced vibrational localization (Anderson-like, but from quasiperiodicity)
- Anomalous thermal transport

The 4.2× IPR contrast vs cubic is consistent with literature on quasicrystalline thermal properties.

**Phason dynamics** are the real additional degrees of freedom in quasicrystals — fluctuations in the perpendicular-space component of the higher-dimensional embedding.

## What Was Wrong

The original DAT framework claimed δ₀ = 1/(2φ) acts as a universal constraint that:
1. Bounds vortex stretching → proves NS regularity
2. Governs phase transitions in SAT (P vs NP)
3. Constrains Riemann zero spacings
4. Appears in glueball mass ratios (Yang-Mills)

These connections were either **falsified** or shown to be **insufficient** for the claimed conclusions. The core mathematical issue: a bounded multiplicative factor on a supercritical nonlinearity does not make it subcritical.

## References

- Levine & Steinhardt (1984): Quasicrystals via cut-and-project
- Coxeter (1973): Regular Polytopes
- Baake & Grimm (2013): Aperiodic Order
- Humphreys (1990): Reflection Groups and Coxeter Groups

## License

MIT License
