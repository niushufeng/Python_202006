import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec

# method 3: easy to define structure
##########################################
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2, sharex=True,sharey= True)  # subplot多一个s  ;sharex指的是共享x轴
ax11.scatter([1,2],[0,3])  # 第一个图的散点

plt.tight_layout()  # 自动紧凑布局
plt.show()
