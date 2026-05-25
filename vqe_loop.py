import numpy as np
def quantum_backend(theta): return -1.5 + 2.0 * (np.sin(theta / 2.0) ** 2)
current_theta = 2.0000
for step in range(8):
    energy = quantum_backend(current_theta)
    grad = (quantum_backend(current_theta + 0.001) - quantum_backend(current_theta - 0.001)) / 0.002
    current_theta -= 0.1 * grad
    print(f"【Day 9 VQE 迭代 Step {step+1:02d}】能量: {energy:.4f}")
