# 别名 应使用大驼峰命名法
import 测试模块1 as DogModule
import 测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)
