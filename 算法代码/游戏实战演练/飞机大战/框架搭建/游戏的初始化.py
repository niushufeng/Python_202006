import pygame
from plane_sprites import *


class PlaneGame(object):
    # 飞机大战主游戏
    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__creat_sprites()

    def __creat_sprites(self):
        pass


    def start_game(self):
        print("游戏开始...")

        while True:

             # 监听事件
            for event in pygame.event.get():

                # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    print("游戏退出...")

                    # quit 卸载所有模块
                    pygame.quit()

                    # exit()
                    exit()  

if __name__ == "__main__":  # 对__name__的判断
    
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
