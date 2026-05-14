import numpy as np
from .core import direct_tan

def solve_sas(a: float, c: float, beta_deg: float):
    """
    Full SAS Triangle Solver
    Given sides a, c and included angle β, returns:
    alpha, side_b, gamma
    """
    # Compute alpha using your direct tangent identity
    alpha = direct_tan(a, c, beta_deg)
    
    # Compute side b using Law of Cosines (stable version)
    beta_rad = np.deg2rad(beta_deg)
    b = np.sqrt(a**2 + c**2 - 2 * a * c * np.cos(beta_rad))
    
    # Compute gamma
    gamma = 180.0 - alpha - beta_deg
    
    return alpha, b, gamma


def solve_sas_full(a: float, b: float, c: float, known_angle: str = "beta"):
    """Future extension - placeholder for now"""
    pass
