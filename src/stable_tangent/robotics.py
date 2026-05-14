import numpy as np
from .core import direct_tan

def two_link_ik(x: float, y: float, l1: float, l2: float, elbow_up: bool = True):
    """
    Stable 2-Link Planar Inverse Kinematics using Direct Tangent Identities.
    
    Parameters:
        x, y : Target position
        l1, l2 : Lengths of the two robotic arm links
        elbow_up : True for elbow up solution, False for elbow down
    
    Returns:
        (theta1, theta2) in degrees or (None, None) if unreachable
    """
    r2 = x*x + y*y
    
    # Check if target is reachable
    if r2 > (l1 + l2)**2 or r2 < (l1 - l2)**2 or r2 == 0:
        return None, None
    
    # Compute elbow angle (theta2)
    cos_theta2 = (r2 - l1**2 - l2**2) / (2 * l1 * l2)
    cos_theta2 = np.clip(cos_theta2, -1.0, 1.0)
    theta2 = np.rad2deg(np.arccos(cos_theta2))
    
    if not elbow_up:
        theta2 = -theta2
    
    # Target angle
    target_angle = np.rad2deg(np.atan2(y, x))
    
    # Use your direct tangent identity for the base angle adjustment
    if abs(theta2) > 1e-6:
        adjustment = direct_tan(l2, np.sqrt(r2), 180.0 - theta2)
    else:
        adjustment = 0.0
    
    if elbow_up:
        theta1 = target_angle - adjustment
    else:
        theta1 = target_angle + adjustment
    
    return theta1, theta2
