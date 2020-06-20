"""
概念：
包是一个包含多个模块的特殊目录
目录下有一个特殊的文件 __init__.py
包名的命名方式 和变量名一致，小写字母+_
好处：
使用import 包名可以一次性导入 包 中所有模块
"""
import message

message.send_message.send("hello")
txt = message.receive_message.receove()
print(txt)
