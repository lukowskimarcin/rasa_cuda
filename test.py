print("test")

for x in range(1, 9):
    print(x * x)


import tensorflow as tf

x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")
f = x * x + y * y + 2

tf.print(f)