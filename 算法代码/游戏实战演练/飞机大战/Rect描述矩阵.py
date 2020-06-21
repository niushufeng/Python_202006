"""
理解游戏中的坐标系：
坐标系：
    原点在左上角(0,0)
    x轴水平方向向右，逐渐增加
    y轴垂直方向向下，逐渐增加
"""

import pygame

hero_rect = pygame.Rect(100,500,120,125)

print("英雄的原点 %d %d" % (hero_rect.x,hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width,hero_rect.height))
print("%d %d" % hero_rect.size)   # 也是英雄的尺寸
