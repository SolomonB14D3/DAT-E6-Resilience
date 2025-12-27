import numpy as np
import matplotlib.pyplot as plt
import os
import time
from itertools import product

# --- PILLAR 5 PARAMETERS ---
N_POINTS = 1000
TARGET_BETA = 1.734
STEPS = 500
SHOCK_FREQUENCY = 100  # Introduce damage every 100 steps
SHOCK_STRENGTH = 0.15  # Magnitude of structural disruption
LR_RECOVERY = 0.05     # Speed of the H3 Snap-Back
PHONON_FREQ = 1.618
DELTA_QUANT = 0.618

def generate_validated_lattice():
    phi = (1 + np.sqrt(5)) / 2
    CP3 = list(product([-1, 1], repeat=3))
    fv = [np.array([0.5, phi/2, (phi-1)/2, 0]), 
          np.array([(phi-1)/2, 0.5, phi/2, 0]), 
          np.array([phi/2, (phi-1)/2, 0.5, 0])]
    xx = [f * np.concatenate((np.array(sign), [1])) for f in fv for sign in CP3]
    mm = np.array(xx)
    MM = np.vstack((mm, mm[:, [1,0,3,2]], mm[:, [2,3,0,1]], mm[:, [3,2,1,0]]))
    norms = np.linalg.norm(MM, axis=1)
    U_norm = MM / norms[:, np.newaxis]
    proj = U_norm[:, :3] / (1 - U_norm[:, 3, np.newaxis] + 1e-8)
    unique_proj = np.unique(np.round(proj, 10), axis=0)
    scale = TARGET_BETA / np.mean(np.linalg.norm(unique_proj, axis=1))
    h3_pool = unique_proj * scale
    norms_h3 = np.linalg.norm(h3_pool, axis=1)
    h3_pool = h3_pool[(norms_h3 > 1.0) & (norms_h3 < 2.5)]
    np.random.seed(42)
    return h3_pool[np.random.randint(0, len(h3_pool), N_POINTS)]

def run_coupled_resilience(lattice):
    n_points = len(lattice)
    psi = np.zeros(n_points, dtype=complex)
    psi[np.argmin(lattice[:, 0])] = 1.0  # Seed heat on one side
    
    h3_pool = generate_validated_lattice() 
    ipr_history, beta_history = [], []
    
    print("🚀 Initializing Pillar 5: Thermo-Structural Resilience Test...")
    for t in range(STEPS):
        # 1. Structural Shock (Damage)
        if t % SHOCK_FREQUENCY == 0 and t > 0:
            lattice += np.random.normal(0, SHOCK_STRENGTH, lattice.shape)
            
        # 2. H3 Healing (Attractor Snap)
        norms = np.linalg.norm(lattice, axis=1, keepdims=True)
        beta_grads = (norms - TARGET_BETA) * (lattice / (norms + 1e-8))
        dists = np.linalg.norm(h3_pool[:, None] - lattice[None, :], axis=2)
        target_sites = h3_pool[np.argmin(dists, axis=0)]
        lattice -= LR_RECOVERY * (lattice - target_sites) + 0.01 * beta_grads
        
        # 3. Phononic Mirror (Wave Scattering)
        dist_matrix = np.linalg.norm(lattice[:, None] - lattice[None, :], axis=2)
        coupling = np.exp(-dist_matrix**2 / (DELTA_QUANT**2))
        laplacian = coupling @ psi - np.sum(coupling, axis=1) * psi
        psi += -1j * PHONON_FREQ * laplacian * 0.01
        
        # 4. Record Metrics
        ipr = np.sum(np.abs(psi)**4) / (np.sum(np.abs(psi)**2)**2 + 1e-10)
        current_beta = np.mean(np.linalg.norm(lattice, axis=1))
        ipr_history.append(ipr)
        beta_history.append(current_beta)
        
        if t % 100 == 0:
            print(f" Step {t}: Beta={current_beta:.4f}, IPR={ipr:.4f}")
            
    return ipr_history, beta_history

# --- EXECUTION ---
lattice_start = generate_validated_lattice()
ipr_trace, beta_trace = run_coupled_resilience(lattice_start.copy())

# --- VISUALIZATION ---
os.makedirs('docs', exist_ok=True)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Beta Plot (Structural)
ax1.plot(beta_trace, color='limegreen', linewidth=2)
ax1.axhline(y=TARGET_BETA, color='red', linestyle='--', alpha=0.6, label='H3 Target')
ax1.set_title("Structural Stability Under Dynamic Load")
ax1.set_ylabel("Mean Beta (Norm)")
ax1.grid(True, alpha=0.2)
ax1.legend()

# IPR Plot (Thermal)
ax2.plot(ipr_trace, color='deepskyblue', linewidth=2)
ax2.set_title("Phononic Mirror Performance (Thermal IPR)")
ax2.set_xlabel("Simulation Step")
ax2.set_ylabel("Localization Index")
ax2.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig('docs/pillar5_thermo_structural_results.png')
print("\n✅ Simulation Complete. Results saved to docs/pillar5_thermo_structural_results.png")
