import numpy as np

def direct_tan(opposite: float, adjacent: float, included_angle: float, tol: float = 1e-10) -> float:
    """
    Core function: Direct Tangent Identity
    Computes angle α using your formula: tan α = (a sin β) / (c - a cos β)
    """
    inc = np.deg2rad(included_angle)
    num = opposite * np.sin(inc)
    den = adjacent - opposite * np.cos(inc)

    if abs(den) < tol:
        if abs(num) < tol:
            return 0.0
        return 180.0 if num > 0 else 0.0

    return np.rad2deg(np.arctan2(num, den))


def sas_angle(opposite: float, adjacent: float, included_angle: float) -> float:
    """Main user function - easy to remember"""
    return direct_tan(opposite, adjacent, included_angle)
