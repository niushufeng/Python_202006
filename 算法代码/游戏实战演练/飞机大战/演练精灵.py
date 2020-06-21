"""
精灵：
    封装图像image、位置rect、和速度speed
    提供update方法，根据游戏需求，更新位置rect
精灵组：
    包含多个精灵对象
    update方法，让精灵组中的所有精灵调用update方法更新位置
    draw(screen) 方法，在screen上绘制精灵组中的所有精灵
"""

import pygame
from plane_sprites import *



# 游戏的初始化
pygame.init()

screen = pygame.display.set_mode((480,700))  # 初始化游戏显示窗口
 
# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))  # (0,0)是位置

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")  # png格式的图像是支持透明的，在绘制图像时，透明区域不会显示任何内容
screen.blit(hero,(100,500))  # 起始坐标点

pygame.display.update()   # 可以理解为油画的画布

# 创建时钟对象
clock = pygame.time.Clock()


# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,500,102,126)


# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)



# 游戏循环
while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(160)  # 60帧是人眼可识别的，越高越好

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit 卸载所有模块
            pygame.quit()

            # exit()
            exit()  # 退出整个while循环；break只退出if循环


    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y + hero_rect.height <= 0:  # 当飞机底部接触图片上面时，回到底部
        hero_rect.y = 700

    # 3. 调用blit方法绘制图像
    screen.blit(bg,(0,0))  # 先绘制背景图像，就遮挡之前绘制的英雄的飞机
    screen.blit(hero,hero_rect)

    # 让精灵组调用两个方法
    # update - 让组中的所有精灵更新位置
    enemy_group.update()

    # draw  - 在screen上绘制所有的精灵
    enemy_group.draw(screen)


    # 4. 调用update方法更新显示
    pygame.display.update()

pygame.quit()  # 卸载pygame模块
