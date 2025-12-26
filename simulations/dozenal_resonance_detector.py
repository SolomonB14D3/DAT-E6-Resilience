import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
import os

def run_unification():
    print("💎 Pillar 1: Emergent Dozenal Resonance Detector\n")
    
    # Simulation Parameters
    N_POINTS = 2000
    phi = (1 + np.sqrt(5)) / 2
    
    # Generate Icosahedral Lattice Projection
    P = np.array([[1, phi, 0, -phi, -1], [1, -phi, 0, -phi, 1], [0, 1, phi, 1, 0]]) / np.sqrt(10)
    points_5d = np.random.uniform(-np.pi, np.pi, (N_POINTS, 5))
    points = points_5d @ P.T
    
    # Simulate a "Snapshot" of turbulent-like flow on the lattice
    u = np.sin(points[:, 0]) * np.cos(points[:, 1])
    v = -np.cos(points[:, 0]) * np.sin(points[:, 1])
    energy = u**2 + v**2
    
    # Compute Spectrum via 1D projection (standard for irregular meshes)
    x_coords = points[:, 0]
    idx = np.argsort(x_coords)
    energy_sorted = energy[idx]
    
    freqs = np.fft.rfftfreq(N_POINTS)
    spectrum = np.abs(np.fft.rfft(energy_sorted))**2
    
    # Fit slope in the "Inertial Range"
    mask = (freqs > 0.05) & (freqs < 0.3)
    slope, intercept = np.polyfit(np.log10(freqs[mask]), np.log10(spectrum[mask]), 1)
    
    # Dozenal Resonance Analysis: 
    # Does the slope converge to a fraction of 12 (e.g., -24/12 = -2.0)?
    target = -2.0 
    deviation = abs(slope - target)
    is_resonant = deviation < 0.15 # Tolerance for N=2000
    
    print(f"📈 Measured Spectral Slope: {slope:.4f}")
    print(f"🎯 Target Dozenal Ratio: -24/12 (-2.0000)")
    print(f"✅ Dozenal Resonance Detected: {'YES' if is_resonant else 'NO'}")
    
    # Save Plot
    os.makedirs('plots', exist_ok=True)
    plt.figure(figsize=(8,5))
    plt.loglog(freqs[1:], spectrum[1:], 'k', alpha=0.6, label='DAT-E6 Spectrum')
    plt.loglog(freqs[mask], 10**intercept * freqs[mask]**slope, 'r--', label=f'Fit (Slope: {slope:.2f})')
    plt.title("Pillar 1: Emergent Spectral Resonance")
    plt.legend()
    plt.savefig('plots/dozenal_resonance_spectrum.png')
    print("\n📊 Plot saved to plots/dozenal_resonance_spectrum.png")

if __name__ == "__main__":
    run_unification()
