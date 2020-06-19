# python 的解释器获得对象的引用后， 将引用作为第一个参数， 传递给__init__方法
#  重写__new__方法的代码非常固定
# 重写__new__方法一定要return super().__new__(cls)
# 否则Python 的解释器 得不到分配空间的对象引用，就不会调用对象的初始化方法
# 注意： __new__ 是一个静态方法，在调用时需要主动传递(cls)参数
class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):  # 一个*表示这个参数是一个多指的元组参数；两个**表示这个参数是一个多值的字典参数

        # 1.创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 2.为对象分配空间
        instance = super().__new__(cls)  # 调用父类方法super

        # 3.返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)
