import  matplotlib.pyplot as plt
import numpy as np  # 多维数组和矩阵函数,用来产生数据

n = 12
X = np.arange(n)  # 在n内返回均匀间隔的值，这里有12个值
Y1 = (1 - X/float(n)) * np.random.uniform(0.5,1.0,n)  # Y是相应的均匀分布的随机数据
Y2 = (1 - X/float(n)) * np.random.uniform(0.5,1.0,n)

# 画柱状图函数bar
plt.bar(X, +Y1,facecolor='#9999ff',edgecolor='white')  # +Y1是正Y1，facecolor指的是主体颜色，edgecolor指的是边框颜色
plt.bar(X, -Y2,facecolor='#ff9999',edgecolor='white')

# 加数字标签
for x,y in zip(X,Y1):  # zip的意思是可以将每个数值分别赋值
    # ha: horizontal alignment 横向对齐校准，这里是居中对齐
    # va: vertical alignment 纵向对齐校准
    plt.text(x + 0.1, y + 0.05, '%.2f' % y ,ha='center',va='bottom')  # x+0.1 向右偏移0.1，y+0.05,向上偏移0.05，'%.2f' % y 的意思是y保留两位小数

for x,y in zip(X,Y2):  # zip的意思是可以将每个数值分别赋值
    # ha: horizontal alignment 横向对齐校准，这里是居中对齐
    # va: vertical alignment 纵向对齐校准
    plt.text(x + 0.1, -(y + 0.05), '-%.2f' % y ,ha='center',va='top')  # top是纵向顶部对齐

#  限定取值范围
plt.xlim(-.5,n)  # 取值范围  
plt.ylim(-1.25,1.25)
plt.xticks(())  # 标记为空
plt.yticks(())

plt.show()
