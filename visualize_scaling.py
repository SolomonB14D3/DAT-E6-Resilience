import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('data/SCALING_LAW_VALIDATION.csv')

def plot_scaling_laws():
    plt.figure(figsize=(12, 5))

    # Subplot 1: Complexity vs. Time (Computational Scaling)
    plt.subplot(1, 2, 1)
    plt.loglog(df['Complexity_N'], df['Compute_Time'], 'o-', color='teal', linewidth=2)
    plt.xlabel('Complexity (Grid Points $N^2$)')
    plt.ylabel('Compute Time (s)')
    plt.title('Pillar 3: $O(N \log N)$ Scaling Efficiency')
    plt.grid(True, which="both", ls="-", alpha=0.2)

    # Subplot 2: Complexity vs. Energy (Physical Consistency)
    plt.subplot(1, 2, 2)
    plt.semilogx(df['Complexity_N'], df['Filtered_Energy'], 's--', color='darkorange', linewidth=2)
    plt.xlabel('Complexity (Grid Points $N^2$)')
    plt.ylabel('Filtered Energy Density')
    plt.title('Physical Consistency: Energy Stability')
    plt.grid(True, which="both", ls="-", alpha=0.2)

    plt.tight_layout()
    plt.savefig('PILLAR_3_SCALING_FIGURE.png', dpi=300)
    print("✅ Scaling Figure saved as PILLAR_3_SCALING_FIGURE.png")

if __name__ == "__main__":
    plot_scaling_laws()
