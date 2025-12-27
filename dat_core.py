import numpy as np
from itertools import product

def get_h3_lattice(n_points=1000, target_beta=1.734, seed=42):
    """The 'Gold Master' H3 Generator for all DAT-E6 Pillars."""
    phi = (1 + np.sqrt(5)) / 2
    CP3 = list(product([-1, 1], repeat=3))
    fv = [np.array([0.5, phi/2, (phi-1)/2, 0]), 
          np.array([(phi-1)/2, 0.5, phi/2, 0]), 
          np.array([phi/2, (phi-1)/2, 0.5, 0])]
    xx = [f * np.concatenate((np.array(sign), [1])) for f in fv for sign in CP3]
    mm = np.array(xx)
    MM = np.vstack((mm, mm[:, [1,0,3,2]], mm[:, [2,3,0,1]], mm[:, [3,2,1,0]]))
    norms = np.linalg.norm(MM, axis=1)
    U_norm = MM / norms[:, np.newaxis]
    proj = U_norm[:, :3] / (1 - U_norm[:, 3, np.newaxis] + 1e-8)
    unique_proj = np.unique(np.round(proj, 10), axis=0)
    scale = target_beta / np.mean(np.linalg.norm(unique_proj, axis=1))
    h3_pool = unique_proj * scale
    norms_h3 = np.linalg.norm(h3_pool, axis=1)
    h3_pool = h3_pool[(norms_h3 > 1.0) & (norms_h3 < 2.5)]
    np.random.seed(seed)
    return h3_pool[np.random.randint(0, len(h3_pool), n_points)]
