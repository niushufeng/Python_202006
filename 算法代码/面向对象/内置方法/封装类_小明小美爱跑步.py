# 外界使用 类 创建对象，然后让对象调用方法
# 对象方法的细节都被 封装 在类的内部
# 需求
class Person:

    def __init__(self, name, weight):  # name和weight都是名词

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return " 我的名字叫 %s 体重是 %.2f 公斤" %  (self.name, self.weight)

    def run(self):

        print("%s 爱跑步，跑步锻炼身体" % self.name)

        self.weight -= 0.5

    def eat(self):
        
        print("%s 是吃货，吃完这顿再说" % self.name)

        self.weight += 1

# 创建一个对象
xiaoming = Person("小明", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

# 创建另一个对象小美
xiaomei = Person("小美",45)  # 在内存中分配另一个地址 ；同一个类创建的多个对象之间，属性互不干扰

xiaomei.eat()
xiaomei.run()

print(xiaomei)
print(xiaoming)
