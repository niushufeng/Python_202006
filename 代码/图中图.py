import matplotlib.pyplot as plt 

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,7,9]

left,bottom,width,height = 0.1,0.1,0.8,0.8   # 参数
ax1 = fig.add_axes([left,bottom,width,height])  
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left,bottom,width,height = 0.2,0.6,0.25,0.25   # 参数 离左边20%的距离，离底边60%的距离
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(x,y,'green')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

plt.axes([.6,0.2,0.25,0.25])
plt.plot(y[::-1],x,'pink')  # y[::-1]把y逆序
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()
