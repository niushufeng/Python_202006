class Women:

    def __init__(self,name):

        self.name = name
        self.__age = 18  # aga前面加“__”就是指的私有属性；对名称进行了特殊处理，使外界无法访问

    def __secret(self):  # 加“__”指的就是私有方法
        # 在对象的方法内部是可以访问私有属性的
        print("%s 年龄是 %d" % (self.name,self.__age))

# 创建一个对象
xiaofang = Women("小芳")

# 私有属性，在外部不能够被直接访问
print(xiaofang._Women__age)

# 私有方法同样在外界不能够直接访问
xiaofang._Women__secret()  # 伪私有，python是没有真正的私有的
