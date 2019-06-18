#
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=list("abcd"))
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=list("abcd"))
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=list("abcd"))

res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=list("abcd"), index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=list("acde"), index=[2, 3, 4])
# 并集
res = pd.concat([df1, df2], axis=0, join="outer")
print(res)
# 交集
res = pd.concat([df1, df2], axis=0, join="inner", ignore_index=True)
print(res)

res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print(res)
res = pd.concat([df1, df2], axis=1)
print(res)

res = df1.append([df2], ignore_index=True)
print(res)

s1 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
res = df1.append(s1, ignore_index=True)
print(res)


