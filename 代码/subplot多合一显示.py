import  matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,1,1)  #  分成两行两列,第一张图
plt.plot([0,1],[0,1])

plt.subplot(2,3,4)  #  分成两行两列，第二张图
plt.plot([0,1],[0,1])

plt.subplot(2,3,5)  #  分成两行两列，第三张图,逗号可去
plt.plot([0,1],[0,1])

plt.subplot(2,3,6)  #  分成两行两列，第四张图
plt.plot([0,1],[0,1])

plt.show()
