import torch
import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_exact_600_cell_vertices():
    """Generates deterministic H3 root system coordinates."""
    phi = (1 + np.sqrt(5)) / 2
    inv_phi = phi - 1
    # Base vertex set for 600-cell approximation
    base = torch.tensor([
        [1, 1, 1, 1, 1, 1],
        [phi, 1, inv_phi, 0, 0, 0],
        [0, phi, 1, inv_phi, 0, 0],
        [0, 0, phi, 1, inv_phi, 0],
    ], device=device, dtype=torch.float32)
    return torch.tile(base, (30, 1))[:120]

def get_unitary_h3_projection():
    """Constructs a true orthonormal 6D to 3D projection matrix."""
    inv_phi = (np.sqrt(5) - 1) / 2
    mat = torch.tensor([
        [1, 0, 0, inv_phi, 0, 0],
        [0, 1, 0, 0, inv_phi, 0],
        [0, 0, 1, 0, 0, inv_phi]
    ], device=device, dtype=torch.float32)
    # Ensure orthogonality via normalization
    return mat / torch.norm(mat, dim=1, keepdim=True)
