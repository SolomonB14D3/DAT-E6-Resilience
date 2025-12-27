import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('data/THERMAL_CONDUCTIVITY_LOG.csv')

def plot_thermal_results():
    plt.figure(figsize=(12, 5))

    # Subplot 1: Thermal Conductivity Stability
    plt.subplot(1, 2, 1)
    plt.plot(df['Temperature_K'], df['Thermal_Conductivity'], 'o-', color='crimson', linewidth=2)
    plt.ylim(30000, 32000) # Zoomed in to show the extreme stability
    plt.xlabel('Temperature (K)')
    plt.ylabel('Thermal Conductivity (k)')
    plt.title('Pillar 4: Thermal Invariance')
    plt.grid(True, alpha=0.3)

    # Subplot 2: H3 Scattering Potential (The "Heat Trap")
    plt.subplot(1, 2, 2)
    L = 100
    phi = (1 + np.sqrt(5)) / 2
    x = np.linspace(-phi, phi, L)
    KX, KY = np.meshgrid(x, x)
    potential = np.zeros_like(KX)
    angles = np.linspace(0, 2 * np.pi, 13)[:-1]
    for theta in angles:
        potential += np.cos(KX * np.cos(theta) + KY * np.sin(theta))
    
    plt.imshow(potential, cmap='inferno')
    plt.colorbar(label='Phonon Scattering Intensity')
    plt.title('H3 Interference Potential')
    plt.axis('off')

    plt.tight_layout()
    plt.savefig('PILLAR_4_THERMAL_FIGURE.png', dpi=300)
    print("✅ Final Validation Figure saved as PILLAR_4_THERMAL_FIGURE.png")

if __name__ == "__main__":
    plot_thermal_results()
