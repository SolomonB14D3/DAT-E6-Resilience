import subprocess
import os

pillars = [
    "navier_stokes_lattice_cap.py",  # Pillar 1
    "phason_slip_detector.py",       # Pillar 2
    "scaling_law_validator.py",      # Pillar 3
    "Phonon_validator.py"            # Pillar 4
]

print("🚀 Starting DAT-E6 Unified Validation Suite...")

for script in pillars:
    if os.path.exists(script):
        print(f"--- Running {script} ---")
        subprocess.run(["python", script])
    else:
        print(f"⚠️ Warning: {script} not found in root.")

print("\n✅ All Pillars validated. Check data/ and docs/ for updated results.")
