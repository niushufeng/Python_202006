import matplotlib.pyplot as plt 
import numpy as np  # 多维数组矩阵

x = y = np.arange(-4, 4, 0.1)
x,y = np.meshgrid(x,y)
plt.contour(x, y, x**2 + y**2 , [9])  #  x**2 + y**2 = 9 的圆形

plt.axis('scaled')  # 等比例缩放
plt.show()
