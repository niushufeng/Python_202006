# 模块的概念
# 模块是Python 程序架构的一个核心概念
# 每一个以扩展名 py 结尾的 python 源代码文件都是一个模块
import 测试模块1
import 测试模块2

测试模块1.say_hello()
测试模块2.say_hello()

dog = 测试模块1.Dog()
print(dog)

cat = 测试模块2.Cat()
print(cat)
