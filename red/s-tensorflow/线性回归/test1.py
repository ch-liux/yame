import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

rng = np.random

# 参数
learning_rate =  0.01
training_epochs =  1000
display_step =  50

# 培训数据
train_X = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]

# TF图形输入
X = tf.placeholder("float")
Y = tf.placeholder("float")

# 设置模型权重
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")

# 构建一个线性模型: y = wx + b
pred = tf.add(tf.multiply(X, W), b)

# 误差损失函数
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)

# 梯度下降
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# 将所有变量交给init用于后面统一初始化
init = tf.global_variables_initializer()

# 开始训练
with tf.Session() as sess:
    # 使用cpu/gpu
    with tf.device("/cpu:0"):
        # 初始化变量
        sess.run(init)

        # 训练次数
        for epoch in range(training_epochs):
            # 训练数据
            for x, y in zip(train_X, train_Y):
                # 将数据放入梯度下降中
                sess.run(optimizer, feed_dict={X:x, Y:y})
            # 每运行50次打印损失
            if (epoch+1) % display_step == 0:
                c = sess.run(cost, feed_dict={X:train_X, Y:train_Y})
                print("Epoch:", (epoch+1), "cost=", c, "W=", sess.run(W), "b=", sess.run(b))

        # 训练完成
        print("Optimization Finished!")
        training_cost = sess.run(cost, feed_dict={X:train_X, Y:train_Y})
        print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b))

        # matplotlib显示
        plt.plot(train_X, train_Y, 'ro', label='Original data')
        plt.plot(train_X, sess.run(W)*train_X + sess.run(b), label='Fitted line')
        plt.legend()
        plt.show()

        # 测试校验
        test_X = np.asarray([6.83, 4.668, 8.9, 7.91, 5.7, 8.7, 3.1, 2.1])
        test_Y = np.asarray([1.84, 2.273, 3.2, 2.831, 2.92, 3.24, 1.35, 1.03])

        test_cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*test_X.shape[0])
        testing_cost = sess.run(test_cost, feed_dict={X:test_X, Y:test_Y})
        print("Testing cost:", testing_cost)
        # 损失
        print("abc loss:", abs(training_cost - testing_cost))
        plt.plot(test_X, test_Y, 'bo', label='Testing data')
        plt.plot(train_X, sess.run(W)*train_X+sess.run(b), label='Fitted line')
        plt.legend()
        plt.show()
