import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. 读取数据
# 读取csv文件
data = pd.read_csv('./house_price.csv')
# 构造 X 和 Y
X = []
Y = []
for single_square_feet, single_price_value in zip(data['square_feet'], data['price']):
    X.append([float(single_square_feet)])
    Y.append([float(single_price_value)])

# 2. 构造回归对象
linear = LinearRegression()
linear.fit(X, Y)

# 3. 绘图
# 绘出已知数据散点图
plt.scatter(X, Y, color='blue')
# 绘制线性回归线
plt.plot(X, linear.predict(X), color='red', linewidth=4)
plt.title('the house price')
plt.xlabel('square feet')
plt.ylabel('price')
plt.show()

# 4.输出回归方程
print('回归方程为：y = ', round(linear.coef_[
      0][0], 2), 'x + ', round(linear.intercept_[0], 2))
