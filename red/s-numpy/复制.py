#
import numpy as np

a = np.arange(0, 20, 2).reshape((2, 5))
print(a)

b = a
c = np.copy(a)
