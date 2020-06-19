# 输出两个相同的对象地址
class MusicPlayer(object):

    # 记录第一个类被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
 
        # 3.返回类属性保存的对象引用
        return cls.instance  

    def __init__(self):

        # 1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:  # 如果为真，就不执行下列代码
            return

        # 2.如果没有执行过，再执行初始化动作

        print("初始化播放器")

        # 3. 修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象
# 在每次使用类名()创建对象时，Python 的解释器都会自动调用两个方法
# __new__分配空间
# __init__ 对象初始化

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
