# 打开文件
file = open("readme.txt")


while True:   # 不知道循环条件，无限循环
    # 读取一行内容
    text = file.readline()

    # 判读是否读取到内容
    if not text:
        break

    # 每读取一行的末尾已经有了一个'\n'
    print(text)

# 关闭文件
file.close()
