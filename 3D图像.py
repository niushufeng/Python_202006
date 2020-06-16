import  matplotlib.pyplot as plt
import numpy as np  # 多维数组和矩阵函数,用来产生数据
from mpl_toolkits.mplot3d import Axes3D  # 3D坐标轴

fig = plt.figure()  # 图片的窗口
ax = Axes3D(fig)  # 在fig里面添加三维坐标轴
# X,Y value
x = np.arange(-4,4,0.25)  #数组
y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(x,y)  # 利用x,y生成矩阵[X,Y]
R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)  # Z轴,利用[X,Y]生成Z轴

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')  #投影到Z轴上，dir指的是direction
ax.set_zlim(-2,2)  # 限制Z轴

ax.set_xlabel('x')  # 加标注
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(40,35)  # 调整观察角度和方位角。这里将俯仰角设为40度，把方位角调整为35度

plt.show()
