#
import numpy as np
import pandas as pd

dates = pd.date_range("20190613", periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=list("ABCD"))
print(df)

df.iloc[2, 2] = np.nan
df.iloc[3, 3] = np.nan
print(df)

# 0=行，1=列
# any=删，all=全为nan才删
df = df.dropna(axis=0, how="any")
print(df)

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
df = df.fillna(value="#")
print(df)

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df.isnull())
print(np.any(df.isnull()))
