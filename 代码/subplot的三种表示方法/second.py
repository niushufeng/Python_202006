import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec  # grid 是网格

# method 2:gridspec
##########################
plt.figure()
gs = gridspec.GridSpec(3,3)  # 3行3列
ax1 = plt.subplot( gs[0,:] )
ax2 = plt.subplot( gs[1,:2] )
ax3 = plt.subplot( gs[1:,2] )
ax4 = plt.subplot( gs[-1,0] )
ax5 = plt.subplot( gs[-1,-2] )

plt.tight_layout()  # 自动紧凑布局
plt.show()
