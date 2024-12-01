import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定数の定義
k = 1.0    # バネ定数
m = 1.0    # O原子の質量
M = 12.0   # C原子の質量

# 運動方程式
def equations(y, t, k, m, M):
    x1, v1, x2, v2, x3, v3 = y
    dydt = [
        v1,
        -k * (x1 - x2) / m,
        v2,
        (-k * (x2 - x1) + k * (x3 - x2)) / M,
        v3,
        -k * (x3 - x2) / m
    ]
    return dydt

# 初期条件
x1_0 = 0.1  # 左側O原子の初期位置
v1_0 = 0.0  # 左側O原子の初期速度
x2_0 = 0.0  # 中央C原子の初期位置
v2_0 = 0.0  # 中央C原子の初期速度
x3_0 = -0.1 # 右側O原子の初期位置
v3_0 = 0.0  # 右側O原子の初期速度

y0 = [x1_0, v1_0, x2_0, v2_0, x3_0, v3_0]

# 時間範囲
t = np.linspace(0, 10, 1000)

# ODEの解を求める
sol = odeint(equations, y0, t, args=(k, m, M))

# 結果のプロット
plt.plot(t, sol[:, 0], label='x1 (O1)')
plt.plot(t, sol[:, 2], label='x2 (C)')
plt.plot(t, sol[:, 4], label='x3 (O2)')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.show()

# 初期条件
x1_0 = 0.1  # 左側O原子の初期位置
v1_0 = 0.0  # 左側O原子の初期速度
x2_0 = 0.0  # 中央C原子の初期位置
v2_0 = 0.0  # 中央C原子の初期速度
x3_0 = 0.1 # 右側O原子の初期位置
v3_0 = 0.0  # 右側O原子の初期速度

y0 = [x1_0, v1_0, x2_0, v2_0, x3_0, v3_0]

# 時間範囲
t = np.linspace(0, 10, 1000)

# ODEの解を求める
sol = odeint(equations, y0, t, args=(k, m, M))

# 結果のプロット
plt.plot(t, sol[:, 0], label='x1 (O1)')
plt.plot(t, sol[:, 2], label='x2 (C)')
plt.plot(t, sol[:, 4], label='x3 (O2)')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.show()