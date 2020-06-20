# 别名 应使用大驼峰命名法  ; 单词的首字母大写,单词与单词之间不要有下划线
import 测试模块1 as DogModule
import 测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)
