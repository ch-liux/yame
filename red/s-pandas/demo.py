#
import pandas as pd
import numpy as np

# pandas:Series和DataFrame
# Series的字符串表现形式为：索引在左边，值在右边。由于我们没有为数据指定索引
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
# DataFrame是一个表格型的数据结构，它包含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值等）。
# DataFrame既有行索引也有列索引， 它可以被看做由Series组成的大字典
dates = pd.date_range("20190612", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["a", "b", "c", "d"])
print(df)
print(df['b'])

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)

df2 = pd.DataFrame({
    "A": 1,
    "B": pd.Timestamp("20190612"),
    "C": pd.Series(1, index=list(range(4)), dtype='float32'),
    "D": np.array([3] * 4, dtype='int32'),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": 'foo'
})
print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)
print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_values(by="B"))
