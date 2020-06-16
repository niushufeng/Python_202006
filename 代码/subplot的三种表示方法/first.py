import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec  # grid 是网格

# method 1: subplot2grid
##########################
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)  # colspan的跨的列数为3,跨的行数为1
ax1.plot([1,2],[1,6])  # x的范围是1到2，y的范围是1到6
ax1.set_title('title1')
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
ax3 = plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
ax5 = plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1)

plt.show()
