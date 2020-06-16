class Cat:

    def __init__(self,new_name):

        self.name = new_name

        print("%s 来了" % self.name)
    
    def __del__(self):  # 自动调用，_del_一旦调用，生命周期结束

        print("%s 我去了" % self.name)

# tom是一个全局变量，当所有的代码执行完之后，系统才对tom进行回收
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个变量
del tom

print("-"*50)
