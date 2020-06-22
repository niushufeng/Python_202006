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

        # 4.设置定时器 - 创建敌机  1s,
        pygame.time.set_timer(CREAT_ENEMY_EVENT,1000)  # 1000指1000毫秒
        pygame.time.set_timer(HERO_FIRE_EVENT,300)

    def __creat_sprites(self):

         # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)  # 交替背景
        
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")

        while True:

            # 1.设置刷新帧率
            self.clock.tick(FRAM_PRE_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check__collide()
            # 4.更新/绘制精灵组
            self.__update__sprites()
            # 5.更新显示
            pygame.display.update()
          
    def __event_handler(self):
        
        for event in pygame.event.get():

                # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    PlaneGame.__game__over()

                elif event.type == CREAT_ENEMY_EVENT:
                    # print("敌机出场...")
                    # 创建敌机精灵
                    enemy = Enemy()

                    # 将敌机精灵添加到敌机精灵组
                    self.enemy_group.add(enemy)
                elif event.type == HERO_FIRE_EVENT:
                    self.hero.fire()

        # 使用键盘提供的方法获取键盘按键
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        # elif keys_pressed[pygame.K_UP]:
        #     self.hero.speed = -1
        # elif keys_pressed[pygame.K_DOWN]:
        #     self.hero.speed = 1
        else:
            self.hero_speed = 0
                
    def __check__collide(self):

        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        # 2.敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        # 判断列表是否有内容
        if len(enemies) > 0:

            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game__over()

    def __update__sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
    
    @staticmethod
    def __game__over():
        print("游戏结束")

        pygame.quit()
        exit()   

if __name__ == "__main__":  # 对__name__的判断
    
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
