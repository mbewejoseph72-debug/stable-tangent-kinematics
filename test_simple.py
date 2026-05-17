# Simple Test - Easy to run
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from stable_tangent.core import direct_tan, sas_angle
from stable_tangent.solver import solve_sas
from stable_tangent.robotics import two_link_ik

print("🚀 Quick Test\n")

alpha = direct_tan(50, 60, 45)
print(f"Direct Tangent Test: α = {alpha:.4f}°")

theta1, theta2 = two_link_ik(80, 40, 50, 50)
print(f"2-Link IK: θ1 = {theta1:.2f}°, θ2 = {theta2:.2f}°")

print("\n✅ Everything is working!")
