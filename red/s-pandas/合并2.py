#
import numpy as np
import pandas as pd

left = pd.DataFrame({
    "key": ["k0", "k1", "k2", "k3"],
    "A": ["a0", "a1", "a2", "a3"],
    "B": ["b0", "b1", "b2", "b3"]
})
right = pd.DataFrame({
    "key": ["k0", "k1", "k2", "k3"],
    "C": ["c0", "c1", "c2", "c3"],
    "d": ["d0", "d1", "d2", "d3"]
})
print(left)
print(right)

res = pd.merge(left, right, on="key")
print(res)

######
left = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']})

# inner, outer, left, right
res = pd.merge(left, right, on=["key1", "key2"], how="inner")
print(res)
res = pd.merge(left, right, on=["key1", "key2"], how="outer")
print(res)
# indicator=True会将合并的记录放在新的一列
# left_index=True依据index合并
# 使用suffixes解决overlapping的问题
