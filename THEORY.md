# Theory: E₆ → H₃ Projection for Quasicrystal Generation

## 1. Geometric Foundation: The E₆ Projection

The E₆ Lie algebra has 72 roots forming a highly symmetric structure in 6-dimensional space. The Z₂ outer automorphism of the E₆ Dynkin diagram folds it into F₄ (48 roots, rank 4). The non-crystallographic H₃ (icosahedral) Coxeter group is recovered as a sub-structure of this projection.

This is established mathematics — see Humphreys (1990), Coxeter (1973).

## 2. Cut-and-Project Method

The code uses the standard Levine-Steinhardt (1984) cut-and-project method:
1. Define basis vectors in higher-dimensional space using φ = (1+√5)/2
2. Apply permutation symmetries to generate the full point set
3. Project to 3D via stereographic projection
4. Filter for unique points

The resulting point sets have icosahedral symmetry and quasiperiodic order.

## 3. The Constant δ₀

$$\delta_0 = \frac{\sqrt{5}-1}{4} = \frac{1}{2\varphi} \approx 0.309$$

This appears naturally in icosahedral geometry. The icosahedral vertex angle is θ = arccos(1/√5) ≈ 63.43°, and various trigonometric functions of θ yield φ-related constants.

**Note**: The original claim that δ₀ "bounds vortex stretching" and proves Navier-Stokes regularity has been **withdrawn**. A bounded multiplicative reduction of the stretching term cannot change the supercritical Z^(3/2) exponent in the enstrophy inequality. See the [full analysis](https://github.com/SolomonB14D3/navier-stokes-h3/blob/main/analytical_proof_attempt.md).

## 4. Phonon Localization (Validated)

Quasicrystalline structures exhibit enhanced phonon localization compared to periodic crystals. This is well-established physics:
- Lack of translational periodicity → no Bloch theorem
- Critical wave functions (neither extended nor exponentially localized)
- Anomalous thermal transport properties

The 4.2× IPR (Inverse Participation Ratio) contrast vs cubic lattices is consistent with literature on icosahedral quasicrystals.

## 5. Phason Dynamics (Validated)

Phasons are the additional degrees of freedom unique to quasicrystals — they correspond to fluctuations in the perpendicular-space component of the higher-dimensional embedding. Under phason strain:
- Bonds reconfigure (tiles flip)
- Local order changes while global quasiperiodicity is preserved
- This is a real physical mechanism in Al-Mn, Al-Cu-Fe, and other icosahedral quasicrystals

## 6. What Was Withdrawn

### Navier-Stokes Regularity (DEBUNKED)

The claim that the "DAT manifold constrains vorticity growth" was based on:
- A modified PDE (not standard NS)
- A spectral solver that is inherently stable (can't blow up regardless)
- The mathematical error of assuming a constant factor reduction changes criticality

The enstrophy inequality dZ/dt ≤ (1-δ₀)·C·Z^(3/2) - ν·λ₁·Z still admits blowup for any (1-δ₀) > 0. The problem is the exponent, not the coefficient.

### Universal φ-Connections (OVERSTATED)

The original claims that δ₀ governs P vs NP phase transitions, Riemann zero spacings, Yang-Mills mass gaps, etc. were either falsified by experiment or shown to be insufficient for the claimed conclusions.

## References

- Levine, D. & Steinhardt, P. (1984). Quasicrystals: A New Class of Ordered Structures. *Phys. Rev. Lett.* 53, 2477.
- Coxeter, H.S.M. (1973). *Regular Polytopes*. Dover.
- Baake, M. & Grimm, U. (2013). *Aperiodic Order, Vol. 1*. Cambridge.
- Humphreys, J.E. (1990). *Reflection Groups and Coxeter Groups*. Cambridge.
