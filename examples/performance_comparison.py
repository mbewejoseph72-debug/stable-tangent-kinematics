"""
Performance & Stability Comparison
Direct Tangent Identities vs Traditional Law of Cosines
"""

import sys
from pathlib import Path
import time
import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from stable_tangent.core import direct_tan
from stable_tangent.solver import solve_sas

def traditional_sas_alpha(a, c, beta_deg):
    """Traditional method using Law of Cosines + arccos"""
    beta = np.deg2rad(beta_deg)
    # Compute side b
    b2 = a**2 + c**2 - 2*a*c*np.cos(beta)
    b = np.sqrt(max(b2, 0))
    # Compute angle alpha
    cos_alpha = (b**2 + c**2 - a**2) / (2 * b * c + 1e-12)
    cos_alpha = np.clip(cos_alpha, -1.0, 1.0)
    return np.rad2deg(np.arccos(cos_alpha))


print("⚡ Performance & Stability Comparison\n")
print("Method                  | Speed       | Stability")
print("-" * 55)

# Test with many triangles
N = 10000
a = np.random.uniform(20, 100, N)
c = np.random.uniform(20, 100, N)
beta = np.random.uniform(5, 175, N)

# Time Direct Tangent
start = time.perf_counter()
for i in range(N):
    direct_tan(a[i], c[i], beta[i])
direct_time = time.perf_counter() - start

# Time Traditional
start = time.perf_counter()
for i in range(N):
    traditional_sas_alpha(a[i], c[i], beta[i])
trad_time = time.perf_counter() - start

print(f"Direct Tangent          | {direct_time*1000:6.1f} ms   | Excellent")
print(f"Traditional (Law Cos)   | {trad_time*1000:6.1f} ms   | Good")
print(f"Speedup                 | {trad_time/direct_time:.2f}x faster\n")

# Near-degenerate test (critical case)
print("Near-Degenerate Test (β very small):")
beta_small = 0.0001
print(f"Direct Tangent α = {direct_tan(50, 50, beta_small):.6f}°")
try:
    trad = traditional_sas_alpha(50, 50, beta_small)
    print(f"Traditional    α = {trad:.6f}°")
except:
    print("Traditional    α = Unstable / Error")
