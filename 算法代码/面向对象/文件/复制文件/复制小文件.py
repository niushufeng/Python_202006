# 1.打开
file_read = open("readme.txt")  # 原文件  只读
file_write = open("readme[复件].txt","w")  # 目标文件  只写

# 2.读、写
text = file_read.read()
file_write.write(text)

# 3.关闭
file_read.close()
file_write.close()
