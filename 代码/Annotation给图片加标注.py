import  matplotlib.pyplot as plt
import numpy as np  # 多维数组和矩阵函数
 
x = np.linspace(-4,3,50)  # -1到1之间的20个点 
y = 2*x + 1

plt.figure(figsize=(10,5))
plt.plot(x,y)  # plot是指绘制

ax = plt.gca()   # ax是轴代指整个图片
ax.spines['right'].set_color('none')  # spines轴的脊梁，竖线，让其颜色消失
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # bottom代替x轴
ax.yaxis.set_ticks_position('left')  # left代替y轴
ax.spines['bottom'].set_position(('data',0))  # 横坐标与纵坐标0对齐
ax.spines['left'].set_position(('data',0))  # 纵坐标与横坐标0对齐

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0,y0,s=50,color='b')  # 显示x0,y0这个点，scatter 是指分散的点
# s是大小,b是蓝色
plt.plot([x0,x0],[y0,0],'k--',lw=2.5) # k代表black，'--'代表虚线，lw代表linewidth

# method 1
##########################
plt.annotate(r'$2x+1=3$',xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
        fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
# $是指符号, "data"是基准, xytext指的是文字描述, textcoords指的是开始偏移点,即打印起始点,fontsize指文本的大小
# arrowprops指的是箭头，dict指的是字典,就是类型限制, connectionstyle指的是关系，剩余的其他关系

# method 2
plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
        fontdict={'size':16,'color':'r'})  # fontdictionary 指的是字体字典

plt.show()  # 显示图片:blush:
