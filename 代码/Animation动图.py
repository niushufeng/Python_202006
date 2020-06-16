import matplotlib.pyplot as plt 
import numpy as np  # 多维数组矩阵
from matplotlib import animation

fig,ax = plt.subplots()

# 产生图像
x = np.arange(0,2*np.pi,0.01)
line,= ax.plot(x,np.sin(x))  # sin函数

# 产生动画
def animate(i):  #  定义
    line.set_ydata(np.sin(x+i/10))
    return line,

def init():   
    line.set_ydata(np.sin(x))  #python 对缩进有严格要求
    return line,

ani = animation.FuncAnimation(fig=fig,func=animate, frames=100,init_func=init, interval=20, blit=True)  # frames是100帧，init_func指的是最开始的那个帧，interval指的是间隔20秒更新一次

plt.show()
