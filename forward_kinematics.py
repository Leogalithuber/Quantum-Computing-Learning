import numpy as np

def create_dh_matrix(theta_degree, link_length):
    theta = np.radians(theta_degree)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0.0, link_length * c], [s, c, 0.0, link_length * s], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])

T1 = create_dh_matrix(30.0, 1.0)
T2 = create_dh_matrix(45.0, 0.8)
T_total = T1 @ T2
print("【MIT 6.832 報告：Day 6 機械手臂末端點總變換矩陣】")
print(T_total)
