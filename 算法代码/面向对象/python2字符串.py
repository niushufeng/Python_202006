# *-* coding:utf8 *-*

hello_str = u"hello世界"  # 引号前面的u告诉解释器这是一个utf8编码格式的字符串

print(hello_str)

for c in hello_str:  # 遍历一遍hello_str
    print(c)
