import  matplotlib.pyplot as plt
import numpy as np  # 多维数组和矩阵函数
 
x = np.linspace(-4,3,50)  # -1到1之间的20个点 
y = 0.1*x

plt.figure(figsize=(8,5))
plt.plot(x,y,linewidth = 10,zorder = 1)  # plot是指绘制
plt.ylim(-2,2)

ax = plt.gca()   # ax是轴代指整个图片
ax.spines['right'].set_color('none')  # spines轴的脊梁，竖线，让其颜色消失
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # bottom代替x轴
ax.yaxis.set_ticks_position('left')  # left代替y轴
ax.spines['bottom'].set_position(('data',0))  # 横坐标与纵坐标0对齐
ax.spines['left'].set_position(('data',0))  # 纵坐标与横坐标0对齐

for label in ax.get_xticklabels() + ax.get_yticklabels():  # 把x,y的label拿出来
    label.set_fontsize(12)  # 放大字体
    label.set_zorder(100)  # 设置对象的顺序
    label.set_bbox(dict(facecolor='green',edgecolor='None',alpha=0.7))
    # bbox是后面的方框 , edgecolor指的是边缘，边框颜色,alpha指的是透明度

plt.show()
