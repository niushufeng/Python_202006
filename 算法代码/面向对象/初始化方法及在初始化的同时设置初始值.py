class Cat:
    def __init__(self,new_name):   # 加了一个new_name形参

        print("这是一个初始化方法")

        self.name =  new_name   # self.属性名 = 属性的初始值 ;所有的对象都默认拥有这个属性

    def eat(self):
        print("%s 爱吃鱼" % self.name)

# 使用类名()创建对象的时候，会自动调用初始化方法_init_
tom = Cat("Tom")  # 在创建对象时，使用类名(属性1，属性2...)调用 ；属性为实参

print(tom.name)

# 另一个对象
lazy_cat = Cat("大懒猫")
lazy_cat.eat()
