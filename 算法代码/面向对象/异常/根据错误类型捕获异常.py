# 需求
try:
    # 1.提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 2.使用8除以用户输入的整数并且输出
    result = 8 / num

    print(result)

except ZeroDivisionError:  # 错误类型1
    print("除0错误")   # 针对错误类型1 ，对应的代码处理
except ValueError:
    print("请输入正确整数")
