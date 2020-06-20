from distutils.core import setup

setup(name= "message",  # 包名
    version="1.0",  # 版本
    description="niushufeng's发送和接收消息模块",   # 描述信息
    long_description="完整的发送和接收消息模块",  # 完整描述信息
    author="iteima",   # 作者
    author_email="niushufeng@163.com",  # 作者邮箱
    url="www.github.com/niushufeng/" ,  # 主页
    py_modules=["message.send_message",
                "message.receive_message" ] )
