import numpy as np
import matplotlib.pyplot as plt

def calculate_scaling_law():
    print("📈 Pillar 3: Kissing Number & Entropy Delay Scaling")
    
    # n-values representing lattice coordination
    n = np.linspace(2, 24, 100)
    delta = 0.309  # The verified depletion constant
    
    # DAT 2.0 Scaling Law: A(n) ≈ 12 / sin(π/(n-δ))
    A_n = 12 / np.sin(np.pi / (n - delta))
    
    # Tau delay: φ^{(12-|n-12|)/12}
    phi = (1 + np.sqrt(5)) / 2
    tau_d = phi**((12 - np.abs(n - 12)) / 12)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n, A_n, label='Area Scaling A(n)', color='gold', linewidth=2)
    plt.axvline(x=12, color='red', linestyle='--', label='Dozenal Harmony (n=12)')
    plt.title("Pillar 3: Non-Monotonic Frustration Scaling")
    plt.xlabel("Coordination Number (n)")
    plt.ylabel("Scaling Amplitude")
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.savefig('plots/pillar3_scaling_law.png')
    print("✅ Pillar 3 Scaling Plot saved to plots/pillar3_scaling_law.png")

if __name__ == "__main__":
    calculate_scaling_law()
