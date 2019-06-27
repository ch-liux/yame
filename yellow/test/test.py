import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = pd.read_csv("Advertising.csv")
print(data.head())
print(data.columns)

# 可视化
plt.figure(figsize=(16, 8))
plt.scatter(data["TV"], data["sales"], c="black")
plt.xlabel("TV ads")
plt.ylabel("sales")
# plt.show()

#
X = data["TV"].values.reshape(-1, 1)
y = data["sales"].values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(X, y)
print(reg.coef_[0][0])
print(reg.intercept_[0])
print("线性模型：Y = {:.5}X + {:.5}".format(reg.coef_[0][0], reg.intercept_[0]))

predict = reg.predict([[100], [200]])
print("投入一亿-销售量：", predict[0][0])
# 线性回归，广告投入


