import copy
from Game import *
from shapes import *
from drawText import *
from drawScreen import *


# 刷新帧率
FRAME_PER_SEC = 7


class Tetris(object):
    """main Game"""
    def __init__(self, screen):

        self.screen = screen

        # 时钟对象
        self.clock = pygame.time.Clock()

        # 判断条件 是否需要新的方块
        self.NeedShape = True

        # 制作游戏内部方格
        self.grid = [[0 for _ in range(10)] for _ in range(20)]

        # 游戏分数
        self.score = 0




    def run(self):

        # 运行时显示的屏幕网格
        currentGrid = copy.deepcopy(self.grid)

        randNum = random.randint(0, len(SHAPES_SET) - 1)

        # 生成下一个俄罗斯方块
        nextShape = getShape(4,0,randNum)
        currentShape = nextShape

        while True:

            # 游戏里的帧率
            self.clock.tick(FRAME_PER_SEC)

            # 判断是否需要添加新的俄罗斯方块
            if self.NeedShape:

                copyArray(self.grid, currentGrid)

                # 将下一个俄罗斯方块添加到运行时屏幕
                currentShape = nextShape

                # 生成下一个俄罗斯方块
                randNum = random.randint(0, len(SHAPES_SET) - 1)
                nextShape = getShape(4,0, randNum)

                self.NeedShape = False

                if self.__gameOver(self.grid, currentShape) is False:
                    # 刷新屏幕
                    updateGrid(self.grid, currentGrid, currentShape)
                    # 游戏结束
                    self.screen.fill((0,0,0))

                    label = drawText("Game Over", 60, (255, 255, 255), self.screen)
                    self.screen.blit(label, (SCREEN_RECT.width / 2 - label.get_width() / 2, 150))

                    label = drawText(f"Your score: {str(self.score)}", 60, (255, 255, 255), self.screen)
                    self.screen.blit(label, (SCREEN_RECT.width / 2 - label.get_width() / 2, SCREEN_RECT.height / 2 - label.get_height() / 2))

                    label = drawText("Thanks for playing", 60, (255, 255, 255), self.screen)
                    self.screen.blit(label, (SCREEN_RECT.width / 2 - label.get_width() / 2, 450))


                    pygame.display.flip()
                    break

            else:
                # 向下移动
                currentShape.y += 1

                # 判断是否到底
                if isMove(self.grid, currentShape) is False:
                    # 删除行
                    self.__deleteRow(currentGrid)

                    # 生成新的俄罗斯方块
                    currentShape.y -= 1
                    self.NeedShape = True
                    continue


            # 监听按键
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.Game_Over()

                if event.type == pygame.KEYDOWN:
                    # 向左移动
                    if event.key == pygame.K_LEFT:
                        currentShape.x -= 1
                        if isMove(self.grid, currentShape) is False:
                            currentShape.x += 1
                    # 向右移动
                    if event.key == pygame.K_RIGHT:
                        currentShape.x += 1
                        if isMove(self.grid, currentShape) is False:
                            currentShape.x -= 1
                    # 向下移动
                    if event.key == pygame.K_DOWN:
                        currentShape.y += 1
                        if isMove(self.grid, currentShape) is False:
                            currentShape.y -= 1
                    # 旋转
                    if event.key == pygame.K_UP:
                        nextRotation = (currentShape.rotation + 1) % len(currentShape.shape)
                        oldRotation = currentShape.rotation
                        currentShape.rotation = nextRotation

                        if isMove(self.grid, currentShape) is False:
                            currentShape.rotation = oldRotation

            # 刷新屏幕
            updateGrid(self.grid, currentGrid, currentShape)

            # 背景填充为黑色
            self.screen.blit(pygame.image.load("./images/backgroundArea.png"), (0, 0))

            # 用二维数组填充窗口
            drawScreen(currentGrid, self.screen, 60, 0)

            # 显示分数
            label = drawText(str(self.score), 30, (0, 0, 0), self.screen)
            self.screen.blit(label, (400,460))

            drawScreen(nextShape.shape[nextShape.rotation], self.screen, 430, 130)


            pygame.display.flip()
            print("im running")


    def __deleteRow(self, currentgrid):
        # 计算删除的行
        level = 0

        for index, row in enumerate(currentgrid):
            # 判断整行
            if 0 not in row:
                level += 1
                vertical_pos = index
                while 0 <= vertical_pos:
                    # 未到下标0的情况
                    if 0 <= vertical_pos-1:
                        currentgrid[vertical_pos] = copy.deepcopy(currentgrid[vertical_pos-1])
                    # 达到到下标0的情况
                    else:
                        currentgrid[vertical_pos] = [0 for _ in range(len(currentgrid[0]))]
                    vertical_pos -= 1

        if 0 < level:
            self.score += (2**(level-1))*10


    # 判断是否结束游戏
    def __gameOver(self, grid, shapes):
        return isMove(grid, shapes)
        # 献给未来的我
        # “Never forget why you started, and your mission can be accomplished.” -- Your game never ends