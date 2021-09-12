
import random
from block import *

class Shape(object):
    # 定义俄罗斯方块
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.rotation = random.randint(0,len(shape)-1)
        self.shape = shape
        self.color = color




def getShape(x,y, randNum):
    return Shape(x, y, SHAPES_SET[randNum], randNum)



def isMove(grid, shape):
    for vertical, line in enumerate(shape.shape[shape.rotation]):
        for horizontal, block in enumerate(list(line)):
            # 如果遇到空行 可以直接返回True
            if 'x' not in list(line):
                return True

            # 判断俄罗斯方块是否可以移动
            if ('x' == block) and (
                                    # 是否到达底部
                                    shape.y + vertical >= len(grid) or
                                    # 是否超出屏幕左右边界
                                    shape.x+horizontal < 0 or shape.x+horizontal >= len(grid[0]) or
                                    # 当前位置已经有方块
                                    grid[shape.y+vertical][shape.x+horizontal] == 1 or
                                    grid[shape.y+vertical][shape.x+horizontal] == 2 or
                                    grid[shape.y+vertical][shape.x+horizontal] == 3 or
                                    grid[shape.y+vertical][shape.x+horizontal] == 4 or
                                    grid[shape.y+vertical][shape.x+horizontal] == 5 or
                                    grid[shape.y+vertical][shape.x+horizontal] == 6 or
                                    grid[shape.y+vertical][shape.x+horizontal] == 7):
                return False

    return True



