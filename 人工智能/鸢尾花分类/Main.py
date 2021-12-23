import tensorflow as tf
import numpy as np
from sklearn import datasets
from matplotlib import pyplot as plt
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

x_data = datasets.load_iris().data      # 从sklearn库里加载数据data
y_data = datasets.load_iris().target    # 从sklearn库里加载数据target

# 设置随机种子
np.random.seed(116)
tf.random.set_seed(116)
# 打乱数据
np.random.shuffle(x_data)
np.random.shuffle(y_data)
# 数据截取
x_train = x_data[:-30]
y_train = y_data[:-30]
x_test = x_data[-30:]
y_test = y_data[-30:]
# 数据格式化
x_train = tf.cast(x_train, dtype=tf.float32)
x_test = tf.cast(x_test, dtype=tf.float32)
# 生成对比数据
train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)
# 创建权重和偏置
w1 = tf.Variable(tf.random.truncated_normal([4, 3], stddev=0.5, seed=1))
b1 = tf.Variable(tf.random.truncated_normal([3], stddev=0.5, seed=1))
# 初始化一系列数据  学习率，学习损失结果，学习次数，所有损失
lr = 0.1
train_loss_results = []
test_acc = []
epoch = 500
loss_all = 0

for epoch in range(epoch):
    for step, (x_train, y_train) in enumerate(train_db):
        with tf.GradientTape() as tape:
            y = tf.matmul(x_train, w1) + b1             # 公式 y=x*w+b
            y = tf.nn.softmax(y)                        # 进行softmax运算
            y_ = tf.one_hot(y_train, depth=3)           # 转换为独热编码
            loss = tf.reduce_mean(tf.square(y, y_))     # 获得损失结果
            loss_all += loss.numpy()                    # 总结全部损失
            grade = tape.gradient(loss, [w1, b1])       # 进行梯度优化
            w1.assign_sub(lr * grade[0])                # 进行优化
            b1.assign_sub(lr * grade[1])
    train_loss_results.append(loss_all / 4)
    loss_all = 0
    total_correct, total_number = 0, 0
    for x_test, y_test in test_db:                      # 进行训练
        y = tf.matmul(x_test, w1) + b1
        y = tf.nn.softmax(y)
        pred = tf.argmax(y, axis=1)
        pred = tf.cast(pred, dtype=y_test.dtype)
        correct = tf.cast(tf.equal(pred, y_test), dtype=tf.int32)
        correct = tf.reduce_sum(correct)
        total_correct = total_correct + int(correct)
        total_number += x_test.shape[0]
        acc = total_correct / total_number
        test_acc.append(acc)
    if epoch % 50 == 0:
        print("epoch:{},loss:{}".format(epoch, loss))  # 打印
        print("acc:{}".format(acc))
        print("==========================================")


def plt_run():      # 运行视窗
    global test_acc, train_loss_results
    plt.figure()
    plt.title('Acc curve')
    plt.xlabel('epoch')
    plt.ylabel('Acc')
    plt.plot(test_acc, label="$Accuracy$")
    plt.legend()

    plt.figure()
    plt.title('loss')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.plot(train_loss_results, label="$Loss$")
    plt.legend()
    plt.show()


plt_run()
