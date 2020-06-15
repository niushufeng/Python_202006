import  matplotlib.pyplot as plt
import numpy as np  # 多维数组和矩阵函数,用来产生数据

# 利用x,y生成高度
def f(x,y):
    # the height function 
    return(1 - x/2 + x**5 + y**3) * np.exp(-x**2 -y**2)  # 高度生成函数

n = 256 
x = np.linspace(-3,3,n)  # -3 到 3 等分为50份，X为长度为n的数组
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)  # meshgrid 用于三维曲面的分割线坐标，产生格点矩阵,也就是将x、y,揉合成矩阵[X,Y]

# use plt.contourf to filling contours
# X,Y and value for (X,Y) point
plt.contourf(X,Y,f(X,Y),8,alpha=0.75, cmap= plt.cm.hot)  # f(X,Y)指的是Z轴, 8指的是平分的等高线数量，cmp=是填充的颜色有hot和cool

# use plt.contour to add contour lines
C = plt.contour(X,Y,f(X,Y),8,colors='black',linwidth=.5)

# adding label
plt.clabel(C,inline=True,fontsize=10)  # True是填在等高线中间

plt.xticks(())  # 标记为空
plt.yticks(())

plt.show()
