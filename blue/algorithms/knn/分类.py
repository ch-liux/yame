#
import numpy as np
import pandas as pd

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

