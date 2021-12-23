import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 张量生成 #
a = tf.zeros([2, 3])  # 二行三列，全0
b = tf.ones([3, 2])  # 三行二列，全1
c = tf.fill([4, 6], 5)  # 四行三列，全5
d = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)  # 生成张量
e = tf.random.normal([2, 4], 0.5, 1)  # 参数为维度，均值，随机数
f = tf.random.truncated_normal([2, 4], 0.5, 1)  # 正态分布
g = tf.random.uniform([2, 2], 0, 1)  # 均匀分布的张量

# 运算 #
tf.add(a, b)  # 加
tf.subtract(a, b)  # 减
tf.multiply(a, b)  # 乘
tf.divide(a, b)  # 除
tf.pow(a, 2)  # 乘方
tf.sqrt(a)  # 开方
tf.math.log(a)  # 求指数
tf.matmul(a, b)  # 矩阵乘
