import numpy as np

def calculate_inverse_kinematics(X, Y, L1, L2):
    cos_theta2 = (X**2 + Y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    theta2 = np.arccos(cos_theta2)
    k1 = L1 + L2 * cos_theta2
    k2 = L2 * np.sin(theta2)
    theta1 = np.arctan2(Y, X) - np.arctan2(k2, k1)
    return np.degrees(theta1), np.degrees(theta2)

t1, t2 = calculate_inverse_kinematics(1.0731, 1.2727, 1.0, 0.8)
print("【MIT 6.832 報告：Day 7 機械手臂逆運動學反求角度】")
print(f"關節 1: {t1:.2f} 度 | 關節 2: {t2:.2f} 度")
