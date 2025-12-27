import numpy as np

def get_h3_projection():
    """Defines the E6 to H3 folding matrix using the golden ratio."""
    phi = (1 + np.sqrt(5)) / 2
    delta = phi - 1
    return np.array([
        [1, 0, 0, delta, 0, 0],
        [0, 1, 0, 0, delta, 0],
        [0, 0, 1, 0, 0, delta]
    ])

def calculate_strain(vertices, proj_matrix):
    """Calculates perpendicular space strain (Phason Strain)."""
    x_parallel = vertices @ proj_matrix.T
    # Simple reconstruction for perp-space mapping
    x_perp = vertices - (x_parallel @ proj_matrix)
    return np.linalg.norm(x_perp, axis=1)

