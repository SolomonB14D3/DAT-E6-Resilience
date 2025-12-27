import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import torch

# Load the data we just generated
df = pd.read_csv('data/DEPLETION_CONSTANT_VALIDATION.csv')

def plot_results():
    plt.figure(figsize=(12, 5))

    # Subplot 1: Energy Stability across Re
    plt.subplot(1, 2, 1)
    plt.bar(df['Re'].astype(str), df['Energy_Density'], color='skyblue', edgecolor='black')
    plt.yscale('log')
    plt.xlabel('Reynolds Number (Re)')
    plt.ylabel('Steady-State Energy Density')
    plt.title('Pillar 1: Topological Stability')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Subplot 2: The 12-Fold Spectral Manifold (Visual Proof)
    plt.subplot(1, 2, 2)
    grid_res = 128
    k = np.fft.fftfreq(grid_res) * grid_res
    KX, KY = np.meshgrid(k, k)
    
    # Re-create the filter logic for visualization
    n = 12
    d0 = 0.309
    sigma = d0 * (grid_res / 2)
    angles = np.linspace(0, 2 * np.pi, n + 1)[:-1]
    filter_sum = np.zeros_like(KX)
    
    for theta in angles:
        k_proj = KX * np.cos(theta) + KY * np.sin(theta)
        filter_sum += np.exp(-(k_proj**2) / (2 * sigma**2))
    
    plt.imshow(filter_sum / n, cmap='magma', extent=[-64, 64, -64, 64])
    plt.colorbar(label='Symmetry Alignment Strength')
    plt.title('H3 Spectral Manifold (12-Fold)')
    plt.xlabel('kx')
    plt.ylabel('ky')

    plt.tight_layout()
    plt.savefig('PILLAR_1_STABILITY_FIGURE.png', dpi=300)
    print("✅ Figure saved as PILLAR_1_STABILITY_FIGURE.png")

if __name__ == "__main__":
    plot_results()
