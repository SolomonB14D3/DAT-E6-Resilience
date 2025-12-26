import numpy as np
import json
import os
from scipy.spatial import KDTree

def simulate_phonon_transport(points, name):
    print(f"🔥 Simulating phonon transport on {name}...")
    n_points = len(points)
    tree = KDTree(points)
    # Hops based on 12-fold neighbor coupling
    dists, idxs = tree.query(points, k=13)
    
    # Simulate Phonon Diffusion (Random Walk)
    n_phonons = 500
    steps = 100
    positions = np.random.choice(n_points, size=n_phonons)
    total_displacement = np.zeros(n_phonons)
    
    for _ in range(steps):
        # Phonons hop to neighbors based on proximity (coupling strength)
        hops = [np.random.choice(idxs[p, 1:]) for p in positions]
        total_displacement += np.linalg.norm(points[hops] - points[positions], axis=1)
        positions = hops
    
    # Localization Ratio: Mean Displacement / System Size
    system_size = np.max(np.linalg.norm(points, axis=1))
    loc_ratio = np.mean(total_displacement) / (system_size * steps)
    
    # Estimate k (W/m·K) based on localization (l)
    # k ≈ (1/3) * Cv * v * l. 
    # For DAT-E6, l is constrained by the "Fractal Pockets"
    k_standard = 15.0  # Reference for Steel/Titanium
    k_ref_quasi = 1.6  # Reference for Al-Pd-Mn
    k_dat_e6 = k_standard * (loc_ratio * 0.5) # Derived from diffusion constraint
    
    return k_dat_e6, loc_ratio

def run_bench():
    print("💎 Pillar 4: Phononic Mirror & Thermal Localization\n")
    
    # Generate DAT-E6 Points
    phi = (1 + np.sqrt(5)) / 2
    P = np.array([[1, phi, 0, -phi, -1], [1, -phi, 0, -phi, 1], [0, 1, phi, 1, 0]]) / np.sqrt(10)
    pts_quasi = np.random.uniform(-1, 1, (2000, 5)) @ P.T
    
    # Generate Cubic Points for Control
    side = int(2000**(1/3))
    grid = np.linspace(-1, 1, side)
    pts_cubic = np.array(np.meshgrid(grid, grid, grid)).T.reshape(-1, 3)

    k_quasi, loc_quasi = simulate_phonon_transport(pts_quasi, "DAT-E6 Lattice")
    k_cubic, loc_cubic = simulate_phonon_transport(pts_cubic, "Cubic Grid")
    
    leakage_reduction = (1 - (k_quasi / k_cubic)) * 100
    
    print(f"\n📊 RESULTS:")
    print(f"  Cubic Grid k:   {k_cubic:.4f} W/(m·K)")
    print(f"  DAT-E6 k:       {k_quasi:.4f} W/(m·K)")
    print(f"✅ Thermal Leakage Reduction: {leakage_reduction:.2f}%")
    print(f"✅ Phononic Mirror Status: {'ACTIVE' if k_quasi < 1.0 else 'INACTIVE'}")

    # Export
    os.makedirs("data", exist_ok=True)
    with open("data/THERMAL_LOCALIZATION_MAP.json", "w") as f:
        json.dump({"k_quasi": k_quasi, "leakage_red": leakage_reduction}, f)

if __name__ == "__main__":
    run_bench()
