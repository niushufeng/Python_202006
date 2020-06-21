

import pygame

class GameSprite(pygame.sprite.Sprite):
         """   飞机大战精灵  """
    
    def __init__(self,image_name,speed = 1):  # 属性

        # 调用父类的初始化方法，因为父类不是基于object
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()  # rect图像的大小 image的get_rect()方法，可以返回pygame.Rect(0,0,图像宽，图像高)的对象
        self.speed = speed

    def update(self):  # 重写父类update方法

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed
