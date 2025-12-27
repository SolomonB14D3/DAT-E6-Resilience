import numpy as np
import matplotlib.pyplot as plt
import time
import os
from itertools import product

# Parameters
N_POINTS = 1000
WINDOW_SIZE = 7
TARGET_BETA = 1.734
DELTA_QUANT = 0.618
INITIAL_STD = 0.15
LR_BETA = 0.005  # Lowered for stability
LR_SNAP = 0.01  # Lowered to act as 'guide'
STEPS = 3000
DYNAMIC_THRESHOLD = 0.1

def generate_h3_vertices():
    phi = (1 + np.sqrt(5)) / 2
    CP3 = list(product([-1, 1], repeat=3))
    fv1 = np.array([0.5, phi/2, (phi-1)/2, 0])
    fv2 = np.array([(phi-1)/2, 0.5, phi/2, 0])
    fv3 = np.array([phi/2, (phi-1)/2, 0.5, 0])
    xx = []
    for sign in CP3:
        s = np.concatenate((np.array(sign), np.array([1])))
        xx.append(fv1 * s)
    for sign in CP3:
        s = np.concatenate((np.array(sign), np.array([1])))
        xx.append(fv2 * s)
    for sign in CP3:
        s = np.concatenate((np.array(sign), np.array([1])))
        xx.append(fv3 * s)
    mm = np.array(xx)
    mma = mm[:, [1, 0, 3, 2]]
    mmb = mm[:, [2, 3, 0, 1]]
    mmc = mm[:, [3, 2, 1, 0]]
    MM = np.vstack((mm, mma, mmb, mmc))
    CP4 = list(product([-1, 1], repeat=4))
    ww = np.array([0.5, 0.5, 0.5, 0.5])
    xxd = []
    for sign in CP4:
        xxd.append(ww * np.array(sign))
    for i in range(4):
        e = np.zeros(4)
        e[i] = 1
        xxd.append(e)
        xxd.append(-e)
    xxd = np.array(xxd)
    U = np.vstack((MM, xxd))
    norms = np.linalg.norm(U, axis=1)
    U_norm = U / norms[:, np.newaxis]
    def stereographic(p):
        return p[:3] / (1 - p[3] + 1e-8)
    proj = np.array([stereographic(p) for p in U_norm])
    unique_proj = np.unique(np.round(proj, 10), axis=0)
    proj_norms = np.linalg.norm(unique_proj, axis=1)
    scale = TARGET_BETA / np.mean(proj_norms[proj_norms > 0])
    unique_proj *= scale
    return unique_proj

def compute_e_phason(points, w_size):
    if len(points) < w_size:
        return 0.0
    shape = (points.shape[0] - w_size + 1, w_size, points.shape[1])
    strides = (points.strides[0], points.strides[0], points.strides[1])
    windows = np.lib.stride_tricks.as_strided(points, shape=shape, strides=strides)
    window_energies = np.sum(np.square(windows), axis=(1,2))
    return np.mean(window_energies)

def simulate_h3_recovery(points, ideal_pool):
    flips = 0
    prev_points = points.copy()
    beta_history = [np.mean(np.linalg.norm(points, axis=1))]
    
    for i in range(STEPS):
        norms = np.linalg.norm(points, axis=1, keepdims=True)
        # 1. Attractor Pull (Lowered for stability)
        beta_grads = (norms - TARGET_BETA) * (points / (norms + 1e-8))
        
        # 2. Geometry Snap (Lowered to act as a 'guide' not a 'teleport')
        dists = np.linalg.norm(ideal_pool[:, None] - points[None, :], axis=2)
        nearest_idx = np.argmin(dists, axis=0)
        target_sites = ideal_pool[nearest_idx]
        snap_grads = target_sites - points # Note: Fixed direction
        
        # 3. Apply the Damped Blend
        points += (LR_BETA * -beta_grads) + (LR_SNAP * snap_grads)
        
        # 4. Discrete Quantization ONLY at the end to prevent explosion
        if i == STEPS - 1:
            points = np.round(points / DELTA_QUANT) * DELTA_QUANT
            
        diff = np.linalg.norm(points - prev_points, axis=1)
        flips += np.sum(diff > DYNAMIC_THRESHOLD)
        prev_points = points.copy()
        beta_history.append(np.mean(np.linalg.norm(points, axis=1)))
        
        if i % 500 == 0:
             # Safety check to prevent the console from filling with INF
             current_beta = beta_history[-1]
             if np.isnan(current_beta) or current_beta > 100:
                 print(f"⚠️ Stability Lost at Step {i}. Beta: {current_beta}")
                 break
             print(f"Step {i}: Beta = {current_beta:.4f}")
             
    return points, flips, beta_history

# Execution
print("🚀 Initializing Pillar 2 Validation...")
h3_pool = generate_h3_vertices()
norms_h3 = np.linalg.norm(h3_pool, axis=1)
h3_pool = h3_pool[(norms_h3 > 1.0) & (norms_h3 < 2.5)]
print(f"Filtered {len(h3_pool)} H3 vertices, mean norm: {np.mean(norms_h3[(norms_h3 > 1.0) & (norms_h3 < 2.5)]):.4f}")
indices = np.random.randint(0, len(h3_pool), N_POINTS)
ideal_lattice = h3_pool[indices]
damaged_lattice = ideal_lattice + np.random.normal(0, INITIAL_STD, ideal_lattice.shape)
initial_beta = np.mean(np.linalg.norm(damaged_lattice, axis=1))
initial_energy = compute_e_phason(damaged_lattice, WINDOW_SIZE)
start = time.time()
healed_lattice, total_flips, beta_history = simulate_h3_recovery(damaged_lattice.copy(), h3_pool)
end = time.time()
final_beta = np.mean(np.linalg.norm(healed_lattice, axis=1))
final_energy = compute_e_phason(healed_lattice, WINDOW_SIZE)
reduction = ((initial_energy - final_energy) / initial_energy * 100) if initial_energy > 0 else 0
print("\n--- RESULTS ---")
print(f"Time: {end-start:.4f}s")
print(f"Initial Beta: {initial_beta:.4f}")
print(f"Final Beta: {final_beta:.4f}")
print(f"Phason Flips: {total_flips}")
if reduction >= 0:
    print(f"Energy Reduction: {reduction:.2f}%")
else:
    print("Energy Reduction: No significant (negative).")
# Visualization
os.makedirs('docs', exist_ok=True)
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(damaged_lattice[:,0], damaged_lattice[:,1], damaged_lattice[:,2], c='red', s=2, alpha=0.5)
ax1.set_title("Damaged State (High Entropy)")
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(healed_lattice[:,0], healed_lattice[:,1], healed_lattice[:,2], c='green', s=2, alpha=0.5)
ax2.set_title("Healed H3 State (Topological Order)")
plt.savefig('docs/pillar2_recovery_visual_v2.png')
plt.close()
# Beta history plot
fig, ax = plt.subplots()
ax.plot(beta_history)
ax.set_title("Beta Convergence Over Steps")
ax.set_xlabel("Step")
ax.set_ylabel("Mean Beta")
ax.grid(True)
plt.savefig('docs/beta_convergence_v2.png')
print(f"\n✅ Visualization saved to docs/pillar2_recovery_visual_v2.png")
print(f"✅ Beta convergence plot saved to docs/beta_convergence_v2.png")
