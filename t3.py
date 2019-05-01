
import os
import shutil
import tensorflow as tf
try:
    shutil.rmtree('/home/xixi/文档/tb')
    os.mkdir('/home/xixi/文档/tb')
except:
    os.mkdir('/home/xixi/文档/tb')


a = tf.constant([1.0,2.0,3.0],name='input1')
b = tf.Variable(tf.random_uniform([3]),name='input2')
add = tf.add_n([a,b],name='addOP')
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter("/home/xixi/文档/tb",sess.graph)
    print(sess.run(add))
writer.close()






import tensorflow as tf

# 定义一个计算图，实现两个向量的减法操作

# 定义两个输入，a为常量，b为变量

a=tf.constant([10.0, 20.0, 40.0], name='a')

b=tf.Variable(tf.random_uniform([3]), name='b')

output=tf.add_n([a,b], name='add')

# 生成一个具有写权限的日志文件操作对象，将当前命名空间的计算图写进日志中

writer=tf.summary.FileWriter('/home/xixi/文档/tb', tf.get_default_graph())

writer.close()









os.system('tensorboard --logdir=/home/xixi/文档/tb')
