#
import numpy as np
import pandas as pd

dates = pd.date_range("20190613", periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=list("ABCD"))
print(df)

# loc具体位置，iloc索引位置
df.iloc[2, 2] = 100
df.loc["20190615", "D"] = 111
print(df)

df.B[df.A > 8] = df.B * 2
print(df)

df["F"] = np.nan
print(df)

df["E"] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20190613", periods=6))
print(df)

