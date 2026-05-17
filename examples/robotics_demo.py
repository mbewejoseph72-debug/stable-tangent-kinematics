"""
Stable Tangent Kinematics - Robotics Demo
2-Link Planar Robotic Arm Inverse Kinematics
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from stable_tangent.robotics import two_link_ik
import numpy as np

print("🤖 2-Link Robotic Arm Demo\n")

# Test different target positions
targets = [
    (80, 40),
    (30, 60),
    (90, 10),
    (0, 80)
]

for x, y in targets:
    print(f"Target position: ({x}, {y})")
    theta1, theta2 = two_link_ik(x, y, l1=50, l2=50, elbow_up=True)
    
    if theta1 is None:
        print("   → Unreachable\n")
    else:
        print(f"   → Theta1 (Base)  = {theta1:8.2f}°")
        print(f"   → Theta2 (Elbow) = {theta2:8.2f}°\n")
