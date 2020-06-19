def demo1():
    return int(input("输入整数："))

def demo2():
    return demo1()

# 主程序   ；利用异常的传递性，在主程序中捕获异常
try:
    print(demo2())  # 异常最后传递到主程序

except Exception as result:
    print("未知错误 %s" % result)
