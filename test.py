import tensorflow as tf

for x in range(1, 100000):
    y = tf.reduce_sum(tf.random.normal([1000, 1000]))

print("end")    
