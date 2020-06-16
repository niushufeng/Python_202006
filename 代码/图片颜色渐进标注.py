import  matplotlib.pyplot as plt
import numpy as np  # 多维数组和矩阵函数,用来产生数据

# image data
a = np.array([0.314,0.365,0.424,
            0.365,0.440,0.525,
            0.424,0.525,0.652]).reshape(3,3)  #reshape以三行三列的数组形式显示

"""
interpolation 的网站
http://matplotlib.org/examples/images_comtours_and_fields/interpolation_methods.html
"""
plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')  # original是原始的，有lower和upper  ;interpolation 是涂写的意思
plt.colorbar(shrink=0.9)  # 旁边的标注 shrink 是缩小

plt.xticks(())  # 标记为空
plt.yticks(())

plt.show()
