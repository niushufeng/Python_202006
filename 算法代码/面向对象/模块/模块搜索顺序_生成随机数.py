# python 在导入模块时,会
# 1.搜索当前目录指定模块的问价
# 2.如果没有，再搜索系统目录
import random

print(random.__file__)  # python 中每一个模块都有一个内置属性 __file__可以查看模块的完整路径

# 生成一个 0~100 的数字
rand = random.randint(0,100)

print(rand)
