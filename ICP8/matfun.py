import tensorflow as tf


x = tf.constant([[2, 2], [3, 3]])

y = tf.constant([[8, 2], [4, 3]])

z = tf.constant([[30, 50], [55, 80]])

p = tf.constant(2)

sqrX = tf.pow(x, p)

mulmat = tf.matmul(y, sqrX)

final = tf.add(mulmat, z)

with tf.Session() as sess:
    result = sess.run(sqrX)
    multir = sess.run(mulmat, feed_dict={sqrX: result})
    finalr = sess.run(final, feed_dict={mulmat: multir})
    print(result)
    print(multir)
    print(finalr)

