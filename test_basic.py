import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from stable_tangent.core import direct_tan, sas_angle
from stable_tangent.solver import solve_sas
from stable_tangent.robotics import two_link_ik

print("🚀 Testing Stable Tangent Kinematics...\n")

# Test 1: Your Direct Tangent Identity
print("Test 1: Direct Tangent Identity")
alpha = direct_tan(opposite=50, adjacent=60, included_angle=45)
print(f"   Angle α = {alpha:.4f}°\n")

# Test 2: Full SAS Solver
print("Test 2: Full SAS Solver")
alpha, b, gamma = solve_sas(a=50, c=60, beta_deg=45)
print(f"   Alpha = {alpha:.4f}°")
print(f"   Side b = {b:.4f}")
print(f"   Gamma = {gamma:.4f}°\n")

# Test 3: Robotics - 2-Link IK
print("Test 3: 2-Link Inverse Kinematics")
theta1, theta2 = two_link_ik(x=80, y=40, l1=50, l2=50, elbow_up=True)
print(f"   Theta1 (Base)  = {theta1:.4f}°")
print(f"   Theta2 (Elbow) = {theta2:.4f}°\n")

print("✅ All tests completed successfully!")
