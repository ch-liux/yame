import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("height.vs.temperature.csv")
print(data.head())
print(data.columns)

# 可视化
plt.figure(figsize=(12, 6))
plt.scatter(data["height"], data["temperature"], c="red")
plt.ylabel("温差")
plt.xlabel("海拔")
plt.show()

X = data["height"].values.reshape(-1, 1)
y = data["temperature"].values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(X, y)
print(reg.coef_[0][0])
print(reg.intercept_[0])
print("线性模型：Y = {:.5}X + {:.5}".format(reg.coef_[0][0], reg.intercept_[0]))

predict = reg.predict([[8000]])
print("8000米海拔温差：", predict[0][0])
