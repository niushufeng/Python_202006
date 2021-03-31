# 导入标准库
import math
n = math.sin(0.5) # 求0.5的正弦  
print(n)

import random 
n = random.random()
n = random.randint(1,100) # 获得[1，100]区间上的随机整数
print(n)
n = random.randrange(1,100) # 返回[1，100)区间中的随机整数 
print(n)

import numpy as np
a = np.array([1,2,3,4])
print(a)
