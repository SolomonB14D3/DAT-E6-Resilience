"""
DAT Pillar 7: Geometry Bridge Verification
Test: Ensures 4D rotation and Stress translate correctly to exported physical coordinates.
"""
import numpy as np
import os
from pillar4_thermal_diagnostic import get_h3_4d_base, project_h3, apply_stress_deformation

def verify_bridge():
    print("🧪 Verifying Pillar 7 Geometry Bridge...")
    n_points = 216
    stress = np.diag([1.1, 1.0, 0.9])
    
    # State A: No rotation
    u_base = get_h3_4d_base(n_points=n_points)
    lat_a = apply_stress_deformation(project_h3(u_base), stress)
    
    # State B: 45-degree Phason Shift
    u_rot = u_base.copy()
    theta = np.pi/4
    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    u_rot[:, 2:4] = u_rot[:, 2:4] @ rot.T
    lat_b = apply_stress_deformation(project_h3(u_rot), stress)
    
    # Calculate geometric delta
    movement = np.linalg.norm(lat_a - lat_b, axis=1)
    mean_drift = np.mean(movement)
    
    print(f"📊 Mean Phason Drift in 3D Space: {mean_drift:.6f} units")
    
    if mean_drift > 0:
        print("✅ SUCCESS: 4D Rotation successfully reconfigured the 3D lattice.")
        # Create the directories and export a test sample
        os.makedirs('data/pillar7', exist_ok=True)
        np.savetxt('data/pillar7/test_export.csv', lat_b, delimiter=',')
        print("✅ TEST EXPORT: 'data/pillar7/test_export.csv' generated.")
    else:
        print("❌ FAILURE: No geometric change detected. Check projection logic.")

if __name__ == "__main__":
    verify_bridge()
