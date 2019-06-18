import tensorflow as tf


# 创建两个常量
m1 = tf.constant([[3., 3.]])
m2 = tf.constant([[2.], [2.]])

# 矩阵相乘
p = tf.matmul(m1, m2)

"""
# 启动默认图
sess = tf.Session()

# 返回值, numpy对象
result = sess.run(p)
print(result)

# 关闭会话
sess.close()
"""
"""
with tf.Session() as sess:
    result = sess.run(p)
    print(result)
"""
with tf.Session() as sess:
    # cpu:0=第一个cpu, gpu:0=第一个gpu
    with tf.device("/cpu:0"):
        n1 = tf.constant([[3., 3.]])
        n2 = tf.constant([[2.], [2.]])
        w = tf.matmul(n1, n2)
        result = sess.run(w)
        print(result)

