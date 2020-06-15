import  matplotlib.pyplot as plt
import numpy as np  # 多维数组和矩阵函数,用来产生数据

n = 1024  #  1024个数据
X = np.random.normal(0,1,n)  # 平均值是0,方差是1，1024个
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)  # for color value
# T = np.arctan(Y,X)

plt.scatter(X,Y,s=75,c=T,alpha=0.5)  # scatter 散点函数 alpha=0.5指的是透明度为50%

plt.xlim(-1.5,1.5)  # 取值范围  
plt.ylim(-1.5,1.5)
plt.xticks(())  # 标记为空
plt.yticks(())

plt.show()
