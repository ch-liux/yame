import tensorflow as tf 

# 计数器
state = tf.Variable(0, name="counter")

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 将变量放入init_op
init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    # 初始化变量
    sess.run(init_op)

    # print(sess.run(state))
    for _ in range(3):
        sess.run(update)
    
    print(sess.run(state))


