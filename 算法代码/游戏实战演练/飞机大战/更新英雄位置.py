import pygame

# 游戏的初始化  ; 在游戏初始化里要设置游戏时钟
pygame.init()

# 创建游戏窗口  480 * 700
screen = pygame.display.set_mode((480,700))  # 初始化游戏显示窗口
 

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))  # (0,0)是位置
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")  # png格式的图像是支持透明的，在绘制图像时，透明区域不会显示任何内容
screen.blit(hero,(100,500))  # 起始坐标点

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()   # 可以理解为油画的画布

# 创建时钟对象
clock = pygame.time.Clock()


# 游戏循环 ->意味着游戏的正式开始！ 
"""
设置刷新帧率
检测用户交互
更新所有图像位置
更新屏幕显示
"""
# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)

while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(160)  # 60帧是人眼可识别的，越高越好

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y + hero_rect.height <= 0:  # 当飞机底部接触图片上面时，回到底部
        hero_rect.y = 700

    # 3. 调用blit方法绘制图像
    screen.blit(bg,(0,0))  # 先绘制背景图像，就遮挡之前绘制的英雄的飞机
    screen.blit(hero,hero_rect)

    # 4. 调用update方法更新显示
    pygame.display.update()

    for event in pygame.event.get():  # 对窗口命令做出响应
        if event.type ==  pygame.QUIT:
            sys.exit()

pygame.quit()  # 卸载pygame模块
