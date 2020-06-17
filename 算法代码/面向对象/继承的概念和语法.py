# 继承的概念：子类 拥有 父类 的所有 方法 和 属性
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
    # def eat(self):
    #     print("吃")

    # def drink(self):
    #     print("喝")

    # def run(self):
    #     print("跑")

    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("汪汪叫")

# 创建一个对象 - 狗对象
wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
