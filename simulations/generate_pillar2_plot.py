import pandas as pd
import matplotlib.pyplot as plt
import os

if os.path.exists('data/ENTROPY_EFFICIENCY_VALIDATION.csv'):
    df = pd.read_csv('data/ENTROPY_EFFICIENCY_VALIDATION.csv')
    plt.figure(figsize=(10, 6))
    plt.plot(df['step'], df['cubic_H'], label='Cubic Lattice (Stalled Recovery)', color='black', alpha=0.6)
    plt.plot(df['step'], df['quasi_H'], label='DAT-E6 (Topological Self-Organization)', color='gold', linewidth=2)
    plt.axvline(100, color='red', linestyle='--', label='High-Entropy Shock')
    plt.title('Pillar 2: Information Resilience and Self-Organization')
    plt.xlabel('Simulation Step')
    plt.ylabel('Topological Entropy (bits)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('plots/pillar2_resilience_validation.png')
    print("Plot generated successfully.")
