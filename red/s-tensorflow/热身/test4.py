import tensorflow as tf 

m1 = tf.constant(3.0)
m2 = tf.constant(2.0)
m3 = tf.constant(5.0)
# 相加
m4 = tf.add(m2, m3)
# 相乘
m5 = tf.multiply(m1, m4)

with tf.Session() as sess:
    result = sess.run([m4, m5])
    print(result)

n1 = tf.placeholder(tf.float32)
n2 = tf.placeholder(tf.float32)
n3 = tf.multiply(n1, n2)

with tf.Session() as sess:
    # tf.float32会自动转换字符型数据
    result = sess.run([n3], feed_dict={n1:['3.'], n2:[7.]})
    print(result)
