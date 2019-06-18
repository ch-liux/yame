#
import numpy as np


a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
# 合并
c = np.vstack((a, b))
print(c)
print(a.shape, b.shape, c.shape)
# 合并
d = np.hstack((a, b))
print(d)
# 转置行
print(a[np.newaxis, :])
# 转置列
print(a[:, np.newaxis])

m = a[:, np.newaxis]
n = b[:, np.newaxis]
x = np.hstack((m, n))
print(x)

y = np.concatenate((a, b, b, a), axis=0)
y1 = np.concatenate((m, n, n, m), axis=1)
print(y, y1)
