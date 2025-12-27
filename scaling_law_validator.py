import torch
import numpy as np
import pandas as pd
import time
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Parameters
N_resolutions = [64, 128, 256, 512] 
dt = 0.001
steps = 100
delta_0 = (np.sqrt(5) - 1) / 4

def build_dealiased_filter(grid_size, d0=0.309):
    """Enforces 12-fold symmetry and implements the 2/3 cutoff for dealiasing."""
    k = torch.fft.fftfreq(grid_size, device=device) * grid_size
    KX, KY = torch.meshgrid(k, k, indexing='ij')
    
    # 1. 12-Fold Symmetry Filter
    angles = torch.linspace(0, 2 * torch.pi, 13, device=device)[:-1]
    filter_sum = torch.zeros_like(KX)
    sigma = d0 * (grid_size / 2)
    for theta in angles:
        k_proj = KX * torch.cos(theta) + KY * torch.sin(theta)
        filter_sum += torch.exp(-(k_proj**2) / (2 * sigma**2))
    manifold = filter_sum / 12

    # 2. Dealiasing: Zero out modes above 2/3 Nyquist
    cutoff = (2/3) * (grid_size / 2)
    k_mag = torch.sqrt(KX**2 + KY**2)
    manifold[k_mag > cutoff] = 0
    
    return manifold.to(torch.complex64)

def run_scaling_test(n):
    u = torch.randn((n, n), device=device) * 5.0
    v = torch.randn((n, n), device=device) * 5.0
    
    k_freq = torch.fft.fftfreq(n, device=device) * n
    KX, KY = torch.meshgrid(k_freq, k_freq, indexing='ij')
    
    proj = build_dealiased_filter(n, d0=delta_0)
    
    start_time = time.time()
    for _ in range(steps):
        u_hat, v_hat = torch.fft.fftn(u), torch.fft.fftn(v)
        
        # Spectral derivatives
        ux = torch.fft.ifftn(1j * KX * u_hat).real
        uy = torch.fft.ifftn(1j * KY * u_hat).real
        vx = torch.fft.ifftn(1j * KX * v_hat).real
        vy = torch.fft.ifftn(1j * KY * v_hat).real

        # Update with dealiased projection
        u_hat = (u_hat - dt * torch.fft.fftn(u*ux + v*uy)) * proj
        v_hat = (v_hat - dt * torch.fft.fftn(u*vx + v*vy)) * proj
        
        u, v = torch.fft.ifftn(u_hat).real, torch.fft.ifftn(v_hat).real
    
    end_time = time.time()
    # Corrected label: Filtered Energy Decay
    energy_decay = 0.5 * torch.mean(u**2 + v**2).item()
    return energy_decay, (end_time - start_time)

# Execution
scaling_results = []
os.makedirs("data", exist_ok=True)
for res in N_resolutions:
    energy, duration = run_scaling_test(res)
    scaling_results.append({
        "Resolution": res,
        "Complexity_N": res**2,
        "Filtered_Energy": energy,
        "Compute_Time": duration
    })
    print(f"  N: {res}x{res} | Decay Energy: {energy:.6f} | Time: {duration:.2f}s")

df = pd.DataFrame(scaling_results)
df.to_csv('data/SCALING_LAW_VALIDATION.csv', index=False)
print("\n✅ Pillar 3 Data Logged with Spectral Dealiasing.")
