import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow.keras as keras
from sklearn.preprocessing import StandardScaler
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # 修改报错频率
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 下载数据集
fashion_mnist = keras.datasets.fashion_mnist
# 拆分训练集与测试集
(x_train_all, y_train_all), (x_test, y_test) = fashion_mnist.load_data()
# 对训练集进行拆分，前5000个数据集作为验证集，其余的作为数据集
x_valid, x_train = x_train_all[:5000], x_train_all[5000:]
y_valid, y_train = y_train_all[:5000], y_train_all[5000:]

# 初始化scaler对象
scaler = StandardScaler()
# x_train: [None, 28, 28] -> [None, 784]
# 因为数据是int型，但是归一化要做除法，所以先转化为float32型
# 训练集数据使用的是 fit_transform，和验证集与测试集中使用的 transform 是不一样的
# fit_transform 可以计算数据的均值和方差并记录下来
# 验证集和测试集用到的均值和方差都是训练集数据的，所以二者的归一化使用 transform 即可
# 归一化只针对输入数据， 标签不变
x_train_scaled = scaler.fit_transform(
    x_train.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28, 1)
x_valid_scaled = scaler.transform(
    x_valid.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28, 1)
x_test_scaled = scaler.transform(
    x_test.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28, 1)

# tf.keras.models.Sequential()用于将各个层连接起来
model = keras.models.Sequential()

# 第一层卷积层
model.add(keras.layers.Conv2D(filters=32,  # 卷积核数量
                              kernel_size=3,  # 卷积核尺寸
                              padding='same',  # padding补齐，让卷积之前与之后的大小相同
                              activation='relu',  # 激活函数relu
                              input_shape=(28, 28, 1)))  # 输入维度是1通道的28*28

# 第二层卷积层
model.add(keras.layers.Conv2D(filters=32,  # 卷积核数量
                              kernel_size=3,  # 卷积核尺寸
                              padding='same',  # padding补齐，让卷积之前与之后的大小相同
                              activation='relu'))  # 激活函数relu

# 最大池化层
model.add(keras.layers.MaxPool2D(pool_size=2))

# 第三层卷积层
model.add(keras.layers.Conv2D(filters=64,  # 卷积核数量
                              kernel_size=3,  # 卷积核尺寸
                              padding='same',  # padding补齐，让卷积之前与之后的大小相同
                              activation='relu'))  # 激活函数relu

# 第四层卷积层
model.add(keras.layers.Conv2D(filters=64,  # 卷积核数量
                              kernel_size=3,  # 卷积核尺寸
                              padding='same',  # padding补齐，让卷积之前与之后的大小相同
                              activation='relu'))  # 激活函数relu

# 最大池化层
model.add(keras.layers.MaxPool2D(pool_size=2))

# 第五层卷积层
model.add(keras.layers.Conv2D(filters=128,  # 卷积核数量
                              kernel_size=3,  # 卷积核尺寸
                              padding='same',  # padding补齐，让卷积之前与之后的大小相同
                              activation='relu'))  # 激活函数relu

# 第六层卷积层
model.add(keras.layers.Conv2D(filters=128,  # 卷积核数量
                              kernel_size=3,  # 卷积核尺寸
                              padding='same',  # padding补齐，让卷积之前与之后的大小相同
                              activation='relu'))  # 激活函数relu
# 最大池化层
model.add(keras.layers.MaxPool2D(pool_size=2))

# 全连接层
model.add(keras.layers.Flatten())  # 展平输出
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dense(10, activation="softmax"))  # 输出为 10的全连接层
model.summary()

model.compile(loss="sparse_categorical_crossentropy",  # 稀疏分类交叉熵损失函数
              optimizer=keras.optimizers.SGD(0.01),  # 优化函数为随机梯度下降 ，学习率为0.01
              metrics=["accuracy"])  # 优化指标为准确度

history = model.fit(x_train_scaled, y_train,  # 训练数据
                    epochs=10,  # 训练周期，数据分为10次进行训练
                    validation_data=(x_valid_scaled, y_valid), )  # 验证集


def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()


plot_learning_curves(history)
model.evaluate(x_test_scaled, y_test, verbose=0)
