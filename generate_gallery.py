import torch
import matplotlib.pyplot as plt
from dat_gold_standard import DAT_GoldStandard_Engine

engine = DAT_GoldStandard_Engine(r=7)
frames_to_capture = [400, 850, 1500]
titles = ["Initial_Order", "Peak_Chaos", "Frozen_Stars"]

for frame, title in zip(frames_to_capture, titles):
    noise = 0.8 if frame == 850 else 0.0
    # Run a few steps to settle if it's the recovery frame
    proj = engine.apply_hamiltonian_dynamics(noise_level=noise)
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(proj[:,0], proj[:,1], proj[:,2], s=2, alpha=0.6, c=proj[:,2])
    ax.set_title(f"DAT 2.0 Manifold: {title}")
    plt.savefig(f"{title}.png")
    plt.close()
print("Gallery Generated.")
