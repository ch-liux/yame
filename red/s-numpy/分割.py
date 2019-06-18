#
import numpy as np

a = np.arange(12).reshape((3, 4))
print(a)
# 纵向分割, 只能等量对分
print(np.split(a, 2, axis=1))
# 横向分割
print(np.split(a, 3, axis=0))
# 不等量的分割
print(np.array_split(a, 3, axis=1))
# 其他的分割方式
print(np.vsplit(a, 3))
print(np.hsplit(a, 2))
