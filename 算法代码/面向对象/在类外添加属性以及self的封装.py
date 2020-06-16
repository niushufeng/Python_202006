# coding = utf-8   ## 中文包

class Cat: # 类的命名，大驼峰法  ；解释器看见class，不立即执行

    def eat(self):  # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)

# 创建对象 是主程序
tom = Cat()  # 先执行等号右侧代码，在等号右侧执行是在内存中创建一个变量， 等号左侧 tom负责引用变量

# 可以使用.属性名 利用赋值语句就可以了
tom.name = "Tom"  # 添加的属性

tom.eat()
tom.drink()

print(tom)

# 再创建一个猫对象
lazy_cat = Cat()  

lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)
