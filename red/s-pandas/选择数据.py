#
import numpy as np
import pandas as pd


dates = pd.date_range("20190613", periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=list("ABCD"))
print(df)

print(df["A"])
print(df.A)
print(df[0:3])
print(df["20190613":"20190614"])

# 选择行
print(df.loc["20190614"])
print(df.loc[:, ["A", "B"]])
print(df.loc["20190614", ["A", "C"]])

# 定位某个数据
print(df.iloc[3, 1])
print(df.iloc[3:5, 1:3])
print(df.iloc[[1, 3, 5], 1:3])

# 混合选择
print(df.ix[:3, ["A", "C"]])

# 判断选择
print(df[df.A > 8])
