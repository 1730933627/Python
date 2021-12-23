import numpy as np

x = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

x_mean = np.mean(x)     # x的平均值
y_mean = np.mean(y)     # y的平均值
x_mse = ((x - x_mean) ** 2).mean()  # x的均方差
print("x_mean:{}\ny_mean:{}\nx_mse:{}".format(x_mean,y_mean,x_mse))

w = np.divide(np.cov((x-x_mean,y-y_mean),bias=True),x_mse)
print("w:",w)
b = np.subtract(y_mean,np.multiply(w,x_mean))
print("b:",b)
