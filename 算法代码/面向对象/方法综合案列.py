# 需求
# 1.设计一个Game类
# 2.属性：
#     定义一个类属性 top_score 记录游戏的历史最高分  ； 和类方法没有关系
#     定义一个实例属性 player_name 记录当前游戏玩家的姓名
# 3.方法
#     静态方法show_help 显示游戏帮助信息  ；不需要访问任何属性
#     类方法 show_top_score显示历史最高峰 ； 历史最高分是一个类属性
#     实例方法 start_game 开始当前玩家的游戏   
# 4.主程序步骤
#    1)查看帮助信息
#    2)查看历史最高分
#    3)创建游戏对象,开始游戏
 
class Game(object):

     # 历史最高分
    top_socre = 0

     # 定义一个实例属性，在初始化方法内部来定义
    def __init__(self, player_name):
         self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_socre)

    # 定义一个实例方法
    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)

# 1.查看游戏帮助信息
Game.show_help()

# 2.查看历史最高fen
Game.show_top_score()

# 3.创建游戏对象
game = Game("小明")

game.start_game()
