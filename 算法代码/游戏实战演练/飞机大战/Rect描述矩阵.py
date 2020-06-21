"""
理解游戏中的坐标系：
坐标系：
    原点在左上角(0,0)
    x轴水平方向向右，逐渐增加
    y轴垂直方向向下，逐渐增加
"""

import pygame

# 提示：pygame.Rect 是一个比较特殊的类，内部只是封装了一些数字计算，不执行pygame.init()方法同样能够直接使用
hero_rect = pygame.Rect(100,500,120,125)

print("英雄的原点 %d %d" % (hero_rect.x,hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width,hero_rect.height))
print("%d %d" % hero_rect.size)   # 也是英雄的尺寸
