import  matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)#-1到1之间的20个点 
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))#figure名字和长宽
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0, linestyle='--' )

plt.show()
