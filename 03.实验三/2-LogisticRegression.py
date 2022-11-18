import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# 1.加载数据
data = np.genfromtxt("LR-dataset.csv", delimiter=",")
x = data[:, :-1]
y = data[:, -1]

x0 = []
x1 = []
y0 = []
y1 = []
# 按照标签切分两个类别的数据
for i in range(len(x)):
    if y[i] == 0:
        x0.append(x[i, 0])
        y0.append(x[i, 1])
    else:
        x1.append(x[i, 0])
        y1.append(x[i, 1])

logistic = linear_model.LogisticRegression()
logistic.fit(x, y)

# 画原始数据的散点图
scatter0 = plt.scatter(x0, y0, c='b', marker='x')
scatter1 = plt.scatter(x1, y1, c='r', marker='o')
# 画图例
plt.legend(handles=[scatter0, scatter1], labels=[
           'label 0', 'label 1'], loc='best')

# 2.画决策边界
# 定义一个点
x_test = np.array([[-1], [2]])
# 用回归方程计算该点的y值
y_test = (-logistic.intercept_ - x_test *
          logistic.coef_[0][0])/logistic.coef_[0][1]

plt.plot(x_test, y_test, 'k')
plt.show()

print('逻辑回归方程是：y = - (', round((-logistic.intercept_[0]/logistic.coef_[
      0][1]), 2), round((logistic.coef_[0][0]/logistic.coef_[0][1]), 2), 'x)')
