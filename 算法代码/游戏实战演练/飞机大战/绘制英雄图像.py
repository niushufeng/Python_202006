import pygame

pygame.init()

# 创建游戏窗口
# set_mode(resolution(0,0),flag=0.depth=0) ->  resolution指定屏幕的宽和高
# flags参数指定屏幕是附加选项，例如是否全屏，是否有边框等等，默认不需要传递
# depth参数表示颜色的位数，默认自动匹配
# surface暂时可以理解为游戏的屏幕，游戏元素都需要被绘制到游戏的屏幕上
screen = pygame.display.set_mode((480,700))  # 初始化游戏显示窗口


# 绘制背景图像
# 1>加载图像数据
bg = pygame.image.load("./images/background.png")

# 2> blit 绘制图像
screen.blit(bg,(0,0))  # (0,0)是位置

# 3> update 更新屏幕显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")  # png格式的图像是支持透明的，在绘制图像时，透明区域不会显示任何内容
screen.blit(hero,(200,500))
pygame.display.update()

while True:
    pass

pygame.quit()
