# 计算0-100之间所有数字的累计求和结果
# 0. 定义最终变量的结果
result = 0

# 1.定义一个整数变量记录循环的次数
i = 0  # 计算机计数从0开始

# 2. 开始循环
while i <= 100:
    print(i)

    # 每一次循环都让result这个变量和i这个计数器相加
    result += i

    # 处理技术器
    i += 1

print("result = %d" % result)
