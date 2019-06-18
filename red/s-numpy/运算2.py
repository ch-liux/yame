#
import numpy as np

a = np.arange(2, 14).reshape((3, 4))
print(a)
# 最大/小值索引
print(np.argmin(a), np.argmax(a))
# 平均值
print(a.mean())
# 中位数
print(np.median(a))
# 累加
print(np.cumsum(a))
# 累减
print(np.diff(a))
print(np.nonzero(a))
print(a[np.nonzero(a)])
# 排序
a = np.arange(14, 2, -1).reshape((3, 4))
print(a)
print(np.sort(a))
# 转置
print(np.transpose(a))
print(a.T)
print(np.clip(a, 9, 12))
#
print(a.flatten())
print(a[1])
print(a[1][1])
