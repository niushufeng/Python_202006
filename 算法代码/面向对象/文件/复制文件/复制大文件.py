# 大文件读取会对内存造成太大的压力
# 解决方法是按行读取

# 1.打开
file_read = open("readme.txt")  # 原文件  只读
file_write = open("readme[复件].txt","w")  # 目标文件  只写

# 2.读、写
while True:
    # 读取一行内容
    text = file_read.readline()

    # 判读是否读取到内容
    if not text:
        break

    # 写入
    file_write.write(text)

# 3.关闭
file_read.close()
file_write.close()
