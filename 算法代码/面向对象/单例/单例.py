# 输出两个相同的对象地址
class MusicPlayer(object):

    # 记录第一个类被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
 
        # 3.返回类属性保存的对象引用
        return cls.instance  


# 创建多个对象
# 在每次使用类名()创建对象时，Python 的解释器都会自动调用两个方法
# __new__分配空间
# __init__ 对象初始化

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
