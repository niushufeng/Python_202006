# 不同的父类存在同名的情况应该避免使用多继承
class A:

    def test(self):
        print("A --- test 方法")

    def demo(self):
        print("A --- demo 方法")


class B:

    def test(self):
        print("B --- test 方法")

    def demo(self):
        print("B --- demo 方法")


class C(A,B):  # 多继承
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass 

# 创建子类对象
c = C()

c.test()
c.demo()

# 确定C类对象调用方法的顺序
print(C.__mro__)  # ；__mro__是内置属性
# object 是 Python 为所有提供的基类  ，提供有一些内置的属性和方法，可以使用dir函数查看
