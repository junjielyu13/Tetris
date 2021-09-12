from tetris import *
from drawText import *

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 600, 600)



class Game(object):
    """main Game"""
    def __init__(self):
        pygame.init()
        print("游戏初始化")

        # 创建窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        pygame.display.set_caption("*************俄罗斯勇往无前方块删减版-plus.v3.0.2")
        pygame.display.set_icon(pygame.image.load("./images/icono.png"))

        self.tetris = Tetris(self.screen)


    def startGame(self):
        print("游戏开始")

        pygame.display.flip()

        # 按下任意键开始游戏字体
        label = drawText("Press any key to start Game", 60, (255, 255, 255), self.screen)
        self.screen.blit(label, (SCREEN_RECT.width / 2 - label.get_width() / 2, 100))

        label = drawText("Press <- to LEFT", 60, (255, 255, 255), self.screen)
        self.screen.blit(label, (SCREEN_RECT.width / 2 - label.get_width() / 2, 200))

        label = drawText("Press -> to RIGHT", 60, (255, 255, 255), self.screen)
        self.screen.blit(label, (SCREEN_RECT.width / 2 - label.get_width() / 2, 300))

        label = drawText("Press UP to Change direction", 60, (255, 255, 255), self.screen)
        self.screen.blit(label, (SCREEN_RECT.width / 2 - label.get_width() / 2, 400))

        label = drawText("Press Down to accelerate", 60, (255, 255, 255), self.screen)
        self.screen.blit(label, (SCREEN_RECT.width / 2 - label.get_width() / 2, 500))


        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Game_Over()

                # 按下任意键开始游戏
                if event.type == pygame.KEYDOWN:
                    self.tetris.run()

            pygame.display.update()
            pygame.display.flip()


    @staticmethod
    def Game_Over():
        print("游戏结束")
        pygame.quit()
        exit()





