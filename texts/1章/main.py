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