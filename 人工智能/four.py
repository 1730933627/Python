import tensorflow as tf
import tensorflow.keras as keras
from sklearn.datasets import load_iris
import numpy as np
import threading
import matplotlib.pyplot as plt
import os;os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def data_init():
    x_data = load_iris().data
    y_data = load_iris().target

    np.random.seed(1)
    tf.random.set_seed(1)
    np.random.shuffle(x_data)
    np.random.shuffle(y_data)

    x, x_ = x_data[:30], x_data[-30:]
    y, y_ = y_data[:30], y_data[-30:]
    x = tf.cast(x, dtype=tf.float32)
    x_ = tf.cast(x_, dtype=tf.float32)
    return x,x_,y,y_    # x_train,x_test,y_train,y_test
    # return {"train_db":train_db,"test_db":test_db}


x_train,x_test,y_train,y_test = data_init()
loss = keras.losses.mse(x_train,x_test)
print(loss)
