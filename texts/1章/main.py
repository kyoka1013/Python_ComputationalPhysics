import numpy as np
# 1.2.2
array1 = np.zeros(10, dtype=float)
array2 = np.zeros((10,2), dtype=int)
array3 = np.zeros((4,3), dtype=complex)
array4 = np.zeros((10,2))

print(array1)
print(array2)
print(array3)
print(array4)

print(array4.dtype)

array3[0,2] = 0.5j
print(array3)

array1 = np.empty(10, dtype=int)
print(array1)

array1 = np.array([[0, -1j], [1j, 0]], dtype=complex)
print(array1)

# 1.2.3
v = np.zeros((3,10), dtype = complex)
print(v)
print(v.dtype)
print(v.shape)
print(v.ndim)
print(v.size)

# 1.2.4
x = np.arange(6)
print(x)
y = x * 10
print(y)
print(x + y)
print(x * y)
'''
異なる形同士に演算するとどうなる？
a = np.empty((4,3), dtype = int)
b = np.empty((3,4), dtype = int)
print(a)
print(b)
print(a + b)
print(a * b)
'''
print(x * 2)
print(x ** 2)
print(x == 2)
x = np.linspace(0, 1, 5) * np.pi / 2
print(np.linspace(0, 1, 5))
print(x)
y = np.sin(x)
print(y)
'''
mathモジュールの場合と比較
import math
def x_math():
    li = [0.0, 0.25, 0.5, 0.75, 1.0]
    newli = []
    for i in li:
        newli.append(i * math.pi / 2)
    return newli
print(x_math())
y_math = [math.sin(x) for x in x_math()]
print(y_math)
'''

# 1.2.5
matrix = np.arange(4).reshape(2,2)
print(matrix)
vector = np.array([1, -1])
print(vector)
print(matrix @ matrix)
print(matrix @ vector)
print(vector @ matrix)
print(vector @ vector)

# 1.3 
from scipy import linalg
from scipy import integrate, optimize

