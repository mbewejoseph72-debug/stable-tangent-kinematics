"""
Stable Tangent Kinematics
Numerically robust SAS triangle solver using Direct Tangent Identities.
Author: Joseph Mbewe
"""

from .core import direct_tan, sas_angle
from .solver import solve_sas
from .robotics import two_link_ik
from .torch import DirectTangentAngle

__version__ = "0.1.0"
__author__ = "Joseph Mbewe"

__all__ = [
    "direct_tan",
    "sas_angle",
    "solve_sas",
    "two_link_ik",
    "DirectTangentAngle"
]

print(f"✅ Stable Tangent Kinematics v{__version__} loaded successfully!")
