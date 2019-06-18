import numpy as np

"""
array：创建数组
dtype：指定数据类型
zeros：数据全是0
ones：数据全是1
empty：数据接近0
arange：指定范围创建数据
linspace：创建线段
"""

a = np.array([1, 33, 2])
print(a)

b = np.array([3, 22, 1], dtype=np.float)
print(b, b.dtype)

c = np.zeros((3, 4))
print(c)

e = np.ones((3, 4))
print(e)

d = np.empty((3, 4), dtype=np.float32)
print(d)

f = np.arange(10, 20, 2)
print(f)

g = np.arange(12).reshape(3, 4)
print(g)

h = np.linspace(1, 10, 20)
print(h)

m = np.linspace(1, 10, 20).reshape((5, 4))
print(m)
