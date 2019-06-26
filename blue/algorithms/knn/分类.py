#
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
iris = pd.read_csv("iris.csv", names=names)
# print(iris)

# 抽取头部
# iris.head()
# 抽取末尾
# iris.tail()
# 随机抽取
# print(iris.sample(5))

iris["class"] = iris["class"].map({"setosa": 1, "virginica": 0, "versicolor": 2})
# print(iris)
# 删除列, inplace:是否替换原地址
# iris.drop("Id", axis=1, inplace=True)
# 查看是否存在重复值
# print(iris.duplicated().any())
iris.drop_duplicates(inplace=True)
# 查看类别汇总
# print(iris["class"].value_counts())


class KNN(object):
    """K近临算法
        惰性学习方式
    """
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        """训练方法"""
        self.X = np.asarray(X)
        self.y = np.asarray(y)

    def predict(self, X):
        """预测"""
        X = np.asarray(X)
        result = []
        
        for x in X:
            # 欧式距离
            dis = np.sqrt(np.sum((x - self.X)**2, axis=1))
            # 获取排序前的索引
            index = dis.argsort()
            # 只取k个近的元素
            index = index[:self.k]
            # 统计元素出现次数
            count = np.bincount(self.y[index])
            # 返回最大值索引, 最大值就是出现次数最多
            result.append(count.argmax())

        return np.asarray(result)


# 获取不同类别
t0 = iris[iris["class"] == 0]
t1 = iris[iris["class"] == 1]
t2 = iris[iris["class"] == 2]
# 打乱顺序
t0 = t0.sample(len(t0), random_state=0)
t1 = t1.sample(len(t1), random_state=0)
t2 = t2.sample(len(t2), random_state=0)
# 构建训练集和测试集
train_X = pd.concat([t0.iloc[:40, :-1], t1.iloc[:40, :-1], t2.iloc[:40, :-1]], axis=0)
train_Y = pd.concat([t0.iloc[:40, -1], t1.iloc[:40, -1], t2.iloc[:40, -1]], axis=0)
test_X = pd.concat([t0.iloc[40:, :-1], t1.iloc[40:, :-1], t2.iloc[40:, :-1]], axis=0)
test_Y = pd.concat([t0.iloc[40:, -1], t1.iloc[40:, -1], t2.iloc[40:, -1]], axis=0)
# 进行训练与测试
knn = KNN(k=3)
knn.fit(train_X, train_Y)
r = knn.predict(test_X)
# print(test_Y)
# print(r)
# print(r == test_Y)
# print(np.sum(r == test_Y))
# print(len(r))
# print(np.sum(r == test_Y)/len(r))
# 设置字体和符号(-)
mpl.rcParams['font.family'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False
# 设置高宽
plt.figure(figsize=(10, 10))
# 训练集数据
plt.scatter(x=t0["sepal-length"][:40], y=t0["petal-length"][:40], color="r", label="iris-virginica")
plt.scatter(x=t1["sepal-length"][:40], y=t1["petal-length"][:40], color="b", label="iris-setosa")
plt.scatter(x=t2["sepal-length"][:40], y=t2["petal-length"][:40], color="g", label="iris-versicolor")
# 测试集数据
right = test_X[r == test_Y]
wrong = test_X[r != test_Y]
plt.scatter(x=right["sepal-length"], y=right["petal-length"], color="c", marker="*", label="iris-right")
plt.scatter(x=wrong["sepal-length"], y=wrong["petal-length"], color="m", marker="x", label="iris-wrong")
plt.xlabel("sepal length")
plt.ylabel("petal length")
plt.title("knn result")
plt.legend(loc="best")
plt.show()
