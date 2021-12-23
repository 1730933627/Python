import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # 修改报错频率
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# 不联网下的文件加载
def load_data(path='mnist.npz'):
    f = np.load(path)
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']
    f.close()
    return (x_train, y_train), (x_test, y_test)


# (x_train, y_train),(x_test, y_test) = load_data()     #上面的函数
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()  # 用keras下datasets里的数据
x_train = keras.utils.normalize(x_train, axis=1)  # 格式化
x_test = keras.utils.normalize(x_test, axis=1)

# 创建神经网络模型
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))  # 加入一系列神经元
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)  # 训练

val_loss, val_acc = model.evaluate(x_test, y_test)  # 训练完的值赋给val_loss和val_acc
# print("Val_loss:",val_loss,"\n","Val_acc:",val_acc)

predictions = model.predict(x_test)  # 预测
print(predictions)

model.save('epic_num_reader.model')  # 保存并加载该模型
new_model = keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict(x_test)
print(np.argmax(predictions[0]))

plt.imshow(x_test[0], cmap=plt.cm.binary)  # 显示识别图像
plt.show()
