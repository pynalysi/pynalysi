
import os
import shutil
import tensorflow as tf
try:
    shutil.rmtree('/home/xixi/文档/tb')
    os.mkdir('/home/xixi/文档/tb')
except:
    os.mkdir('/home/xixi/文档/tb')

with tf.name_scope('graph') as scope:
     matrix1 = tf.constant([[3, 3]],name ='matrix1')  #1 row by 2 column
     matrix2 = tf.constant([[2],[2]],name ='matrix2') # 2 row by 1 column
     product = tf.matmul(matrix1, matrix2,name='product')

sess = tf.Session()

writer = tf.summary.FileWriter("/home/xixi/文档/tb", sess.graph)

init = tf.global_variables_initializer()

sess.run(init)


os.system('tensorboard --logdir=/home/xixi/文档/tb')
