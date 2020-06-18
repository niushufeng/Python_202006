#  在 类方法 内部可以直接访问类属性 或者调用其他的类方法
class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod  # 类方法需要用修饰器 @classmethid 来标识， 告诉解释器这是一个类方法
    def show_tool_count(cls):  # 类方法的第一个参数必须是cls ，由哪一个类调用的方法，方法内的 cls 就是哪一个类的引用 可以访问当前对象的属性
    
    # 在方法内部
    # 可以通过cls. 访问类的属性
    # 也可以通过 cls. 调用其他类的方法
    
        print("工具对象的数量 %d" % cls.count)

    def __init__(self,name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1

# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()



