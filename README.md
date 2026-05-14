# Stable Tangent Kinematics

**Numerically robust planar kinematics library powered by direct tangent identities**

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A high-performance library for SAS triangle resolution and planar robotics using **direct tangent identities**. Superior numerical stability near singularities and 2.5–3× faster than traditional Law of Cosines methods.

## Features

- Full set of direct tangent identities with `atan2` robustness
- Stable 2-Link Inverse Kinematics (elbow up/down)
- Differentiable PyTorch module
- Benchmark suite + stability plots
- Medical imaging utilities (Costophrenic angle)

## Installation

```bash
pip install git+https://github.com/josephmbewe/stable-tangent-kinematics.git
