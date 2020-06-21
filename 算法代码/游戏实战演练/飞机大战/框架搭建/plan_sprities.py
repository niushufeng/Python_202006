import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)  # 常量的命名应该所有的字母都使用大写，单词与单词之间用下划线连接
# 刷新的帧率
FRAM_PRE_SEC = 60

class GameSprite(pygame.sprite.Sprite):
      #   """   飞机大战精灵  """
    
    def __init__(self,image_name,speed=1):

        # 调用父类的初始化方法，因为父类不是基于object
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()  # rect图像的大小 image的get_rect()方法，可以返回pygame.Rect(0,0,图像宽，图像高)的对象
        self.speed = speed

    def update(self):  # 重写父类update方法

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    # 游戏背景精灵

    def __init__(self,is_alt=False):

        # 1.调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        
