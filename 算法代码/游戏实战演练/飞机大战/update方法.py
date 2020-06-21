import pygame

pygame.init()


screen = pygame.display.set_mode((480,700))  # 初始化游戏显示窗口


# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))  # (0,0)是位置
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")  # png格式的图像是支持透明的，在绘制图像时，透明区域不会显示任何内容
screen.blit(hero,(200,500))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()   # 可以理解为油画的画布

while True:
    pass

pygame.quit()  # 卸载pygame模块
