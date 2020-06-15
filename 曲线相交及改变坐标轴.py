import  matplotlib.pyplot as plt
import numpy as np#多维数组和矩阵函数

x = np.linspace(-3,3,50)#-1到1之间的20个点 
y1 = 5*x+1
y2 = x**2

plt.figure(figsize=(8,10))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0, linestyle='--' )

plt.xlim((-1,10))#取值范围
plt.ylim((-2.8))
plt.xlabel("I am x")#坐标轴的注释
plt.ylabel("I am y")

new_ticks = np.linspace(-1,10,10)#-1和10之间均分20等分
print(new_ticks)#新标记
plt.xticks(new_ticks) #替换x轴间距
plt.yticks([-2,-1.5,-1,4.5,6],#替换y的名字
           [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
            #\加空格输出是空格，\+alpha输出是阿尔法

# gca = 'get current axis'把轴拿出来
ax = plt.gca() #ax是轴代指整个图片
ax.spines['right'].set_color('none')#spines轴的脊梁，竖线，让其颜色消失
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#bottom代替x轴
ax.yaxis.set_ticks_position('left')#left代替y轴
ax.spines['bottom'].set_position(('data',0))#横坐标与纵坐标0对齐
ax.spines['left'].set_position(('data',0))#纵坐标与横坐标0对齐

plt.show()
