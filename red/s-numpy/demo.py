import numpy as np

# 列表转矩阵
array = np.array([[1, 2, 3], [2, 3, 4]])
print(array, type(array), array.ndim, array.shape, array.size)

array2 = np.array([1, 2, 3])
print(array2, type(array2), array2.ndim, array2.shape, array2.size)

array3 = np.array((1, 2, 3))
print(array3, type(array3), array3.ndim, array3.shape, array3.size)

array4 = np.array([[[1, 2, 3], [2, 3, 4]], [1, 2, 3]])
print(array4, type(array4), array4.ndim, array4.shape, array4.size)

array5 = np.array(1)
print(array5, type(array5), array5.ndim, array5.shape, array5.size)
# ndim：维度
# shape：行列
# size：个数
# type -> ndarry
