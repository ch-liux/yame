import tensorflow as tf 
import numpy as np
import tensorflow.contrib.eager as tfe

print("Setting Eager mode...")
tfe.enable_eager_execution()

a = tf.constant(2)
print(a)
b = tf.constant(3)
print(b)
c = a + b
print(c)
d = a * b
print(d)

a = tf.constant([[2., 1.], [1., 0.]], dtype=tf.float32)
print(a)
b = np.array([[3., 0.], [5., 1.]], dtype=np.float32)
print(b)
c = a + b
print(c)
# a-r * b-l
d = tf.matmul(a, b)
print(d)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        print(a[i][j])