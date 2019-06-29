import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
data = pd.read_csv("iris.csv", names=names)
# 删除列
# data.drop(["class"], axis=1, inplace=True)
# 删除重复
# print(data.head())
data["class"] = data["class"].map({"setosa": 1, "virginica": 0, "versicolor": 2})
data.drop_duplicates(inplace=True)


class KNN(object):
    """用于回归预测
    根据前3个属性，寻找邻居；再根据邻居找下一个特征并预测值
    """
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X = np.asarray(X)
        self.y = np.asarray(y)

    def predict(self, X):
        X = np.asarray(X)
        result = []
        for x in X:
            dis = np.sqrt(np.sum((x - self.X) ** 2, axis=1))
            index = dis.argsort()
            index = index[:self.k]
            result.append(np.mean(self.y[index]))
        return np.array(result)

    def predict2(self, X):
        X = np.asarray(X)
        result = []
        for x in X:
            dis = np.sqrt(np.sum((x - self.X)**2, axis=1))
            index = dis.argsort()
            index = index[:self.k]
            p = 1.0 / (dis[index] + 0.001)
            s = np.sum(p)
            # 每个节点的倒数之和，得到权重
            w = p / s
            r = np.sum(self.y[index] * w)
            result.append(r)
        return np.array(result)


t = data.sample(len(data), random_state=0)
train_X = t.iloc[:120, :-1]
train_y = t.iloc[:120, -1]
test_X = t.iloc[120:, :-1]
test_y = t.iloc[120:, -1]

knn = KNN(k=3)
knn.fit(train_X, train_y)
result = knn.predict2(test_X)
print(result)
print(np.mean(np.sum((result - test_y)**2)))
print(np.mean((result - test_y)**2))
print(test_y.values)

# 可视化
mpl.rcParams['font.family'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False
#
plt.figure(figsize=(10, 8))
plt.plot(result, "ro-", label="预测值")
plt.plot(test_y.values, "go--", label="真实值")
plt.title("KNN预测展示")
plt.xlabel("节点序号")
plt.ylabel("花瓣宽度")
plt.legend()
# plt.show()
