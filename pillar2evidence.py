import pandas as pd
import matplotlib.pyplot as plt
import torch
import numpy as np

# Re-run a single high-fidelity pass to capture the 'live' energy curve
from phason_slip_detector import get_exact_600_cell_vertices, get_unitary_h3_projection

def plot_beta_resonance():
    vertices = get_exact_600_cell_vertices()
    proj_mat = get_unitary_h3_projection()
    
    # Orthogonal projection and perp-space calculation
    x_parallel = torch.matmul(vertices, proj_mat.T)
    x_perp = vertices - torch.matmul(x_parallel, proj_mat)
    
    energies = []
    r_window = 7
    for i in range(0, 120 - r_window):
        window = x_perp[i : i + r_window]
        energies.append(torch.sum(torch.norm(window, dim=1)**2).item())

    # Plotting the Resonance Profile
    plt.figure(figsize=(10, 5))
    plt.plot(energies, color='#D4AF37', linewidth=2, label='Phason Strain Energy')
    plt.axhline(y=0.86, color='red', linestyle='--', label='Resilience Threshold (0.86)')
    
    plt.fill_between(range(len(energies)), energies, 0.86, where=(np.array(energies) > 0.86), 
                     color='gold', alpha=0.3, label='Beta-Resonance Zone')
    
    plt.title('Pillar 2: Phason Strain & Beta Resonance ($β=1.734$)')
    plt.xlabel('Aperiodic Window Index')
    plt.ylabel('Strain Energy ($E_{ph}$)')
    plt.legend()
    plt.grid(alpha=0.2)
    plt.savefig('PILLAR_2_RESILIENCE_FIGURE.png', dpi=300)
    print("✅ Resilience Figure saved as PILLAR_2_RESILIENCE_FIGURE.png")

if __name__ == "__main__":
    plot_beta_resonance()
