
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from collections import Counter

"""knn
分类：
回归：
---参数
模型：训练数据
超：不属于模型参数
---距离
欧式距离：
---决策边界
线性：
非线性：
---交叉验证
*测试数据不能用于调参
---特征缩放
线性归一化：(X-min(X))/(max(X)-min(X))
标准差标准化：(X-mean(X))/std(X),std标准差
"""

iris = datasets.load_iris()
X = iris.data       # 特征, 矩阵
y = iris.target     # 标签, 向量
# print(X, y)

# 默认测试数据0.25
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2003)

# 设置k
clf = KNeighborsClassifier(n_neighbors=3)
# 训练
clf.fit(X_train, y_train)
# # 检测
correct = np.count_nonzero((clf.predict(X_test) == y_test) == True)
# accuracy_score(y_test, clf.predict(X_test))
print(correct/len(X_test))


def euc_dis(ins1, ins2):
    """两点距离"""
    dist = np.sqrt(np.sum((ins1 - ins2)**2))
    return dist


def knn_classify(X, y, testInstance, k):
    # 时间复杂度：O(N)
    distances = [euc_dis(x, testInstance) for x in X]
    # O(NlogN)：优化->priority queue(O(NlogK))
    kneighbors = np.argsort(distances)[:k]
    count = Counter(y[kneighbors])
    return count.most_common()[0][0]


predict = [knn_classify(X_train, y_train, data, 3) for data in X_test]
correct = np.count_nonzero((predict == y_test) == True)
print(correct)
