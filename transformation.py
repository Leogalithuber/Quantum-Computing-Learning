import numpy as np

def get_homogeneous_transform(theta_degree, tx, ty, tz):
    theta = np.radians(theta_degree)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0.0, tx], [s, c, 0.0, ty], [0.0, 0.0, 1.0, tz], [0.0, 0.0, 0.0, 1.0]])

T_matrix = get_homogeneous_transform(45.0, 0.5, 0.2, 0.0)
print("【MIT 6.832 報告：Day 5 機器人 4x4 齊次變換矩陣】")
print(T_matrix)
