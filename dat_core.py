import numpy as np
from itertools import product

def get_h3_lattice(n_points=1000, target_beta=1.734, phason_offset=0.0, seed=42):
    """
    H3 Generator with Phason Steering and Shell Inflation.
    Generates a unique set of points from the E6 -> H3 projection.
    """
    phi = (1 + np.sqrt(5)) / 2
    # Basis vectors for the projection
    CP3 = list(product([-1, 1], repeat=3))
    fv = [np.array([0.5, phi/2, (phi-1)/2, 0]), 
          np.array([(phi-1)/2, 0.5, phi/2, 0]), 
          np.array([phi/2, (phi-1)/2, 0.5, 0])]
    
    all_points = []
    # Use 3 shells of inflation to ensure a deep unique point pool
    # This prevents the 'duplicate point' bug identified in review
    for k in [1, phi, phi**2]:
        xx = [f * np.concatenate((np.array(sign), [1])) * k for f in fv for sign in CP3]
        all_points.append(np.array(xx))
    
    combined = np.vstack(all_points)
    
    # Lie Group Automorphism: Rotation in the 3-4 plane (Phason Shift)
    # This mixes physical Z space with perpendicular W space
    theta = phason_offset
    rot = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, np.cos(theta), -np.sin(theta)],
        [0, 0, np.sin(theta), np.cos(theta)]
    ])
    # Apply rotation
    combined = (rot @ combined.T).T
    
    # Generate the full E6-family symmetry group via permutations
    MM = np.vstack((combined, combined[:, [1,0,3,2]], combined[:, [2,3,0,1]], combined[:, [3,2,1,0]]))
    norms = np.linalg.norm(MM, axis=1)
    
    # Stereographic Projection
    U_norm = MM / (norms[:, np.newaxis] + 1e-10)
    proj = U_norm[:, :3] / (1 - U_norm[:, 3, np.newaxis] + 1e-8)
    
    # Filter for unique points to ensure lattice integrity
    unique_proj = np.unique(np.round(proj, 8), axis=0)
    
    # Safety check for requested size
    if n_points > len(unique_proj):
        n_points = len(unique_proj)
        
    # Deterministic sampling using the seed
    np.random.seed(seed)
    indices = np.random.choice(len(unique_proj), n_points, replace=False)
    lattice = unique_proj[indices]
    
    # Scale to target Beta
    scale = target_beta / np.mean(np.linalg.norm(lattice, axis=1))
    return lattice * scale
