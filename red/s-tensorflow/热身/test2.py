import tensorflow as tf 

# 交互式会话
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
y = tf.constant([3.0, 3.0])

# 初始化x
x.initializer.run()

# 相减
sub = tf.subtract(x, y)
print(sub)
print(sub.eval())

