#
import numpy as np

# 一维计算
a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = a - b
print(c)
c = a + b
print(c)
c = b**2
print(c)
c = 10 * np.sin(a)
print(c)
c = b < 3
print(c)

# 二维计算
a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape((2, 2))

c = np.dot(a, b)
print(c)
c = a.dot(b)
print(c)
c = a * b
print(c)
a = np.random.random((2, 4))
print(a)
print(a.max(), a.min(), a.sum())
# 默认为列计算axis=0
print(a.min(axis=1), a.min(axis=0))
