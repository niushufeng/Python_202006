class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):  # 继承的语法

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):  # 传递性，子类 继承 父类 以及 父类的父类 的属性和方法

    def fly(self):
        print("我会飞")


# 创建一个哮天犬的对象
xtq = XiaoTianQuan()

xtq.fly()
xtq.bark()
xtq.eat()
