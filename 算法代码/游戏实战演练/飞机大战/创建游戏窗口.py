import pygame

pygame.init()

# 创建游戏窗口
# set_mode(resolution(0,0),flag=0.depth=0) ->  resolution指定屏幕的宽和高
# flags参数指定屏幕是附加选项，例如是否全屏，是否有边框等等，默认不需要传递
# depth参数表示颜色的位数，默认自动匹配
# surface暂时可以理解为游戏的屏幕，游戏元素都需要被绘制到游戏的屏幕上
screen = pygame.display.set_mode((480,700))  # 初始化游戏显示窗口

while True:
    pass

pygame.quit()
