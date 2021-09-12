


import pygame
from block import *

empty = pygame.image.load("./images/black.png")

def drawScreen(grid, screen, x, y):
    for vertical, line in enumerate(grid):
        for horizontal, block in enumerate(line):
            # 如果是1 显示方块
            if block == 1 or block == 'x':
                # 根据坐标上色
                screen.blit(pygame.image.load(BLOCK_COLOR[0]),(x+horizontal*BLOCK_SIZE, y+vertical*BLOCK_SIZE))
            if block == 2 or block == 'x':
                # 根据坐标上色
                screen.blit(pygame.image.load(BLOCK_COLOR[1]),(x+horizontal*BLOCK_SIZE, y+vertical*BLOCK_SIZE))
            if block == 3 or block == 'x':
                # 根据坐标上色
                screen.blit(pygame.image.load(BLOCK_COLOR[2]),(x+horizontal*BLOCK_SIZE, y+vertical*BLOCK_SIZE))
            if block == 4 or block == 'x':
                # 根据坐标上色
                screen.blit(pygame.image.load(BLOCK_COLOR[3]),(x+horizontal*BLOCK_SIZE, y+vertical*BLOCK_SIZE))
            if block == 5 or block == 'x':
                # 根据坐标上色
                screen.blit(pygame.image.load(BLOCK_COLOR[4]),(x+horizontal*BLOCK_SIZE, y+vertical*BLOCK_SIZE))
            if block == 6 or block == 'x':
                # 根据坐标上色
                screen.blit(pygame.image.load(BLOCK_COLOR[5]),(x+horizontal*BLOCK_SIZE, y+vertical*BLOCK_SIZE))
            if block == 7 or block == 'x':
                # 根据坐标上色
                screen.blit(pygame.image.load(BLOCK_COLOR[6]),(x+horizontal*BLOCK_SIZE, y+vertical*BLOCK_SIZE))



def updateGrid(grid, currentGrid, shape):
    # 将有效的屏幕填充到运行的屏幕中
    copyArray(currentGrid, grid)

    for vertical, line in enumerate(shape.shape[shape.rotation]):
        for horizontal, block in enumerate(list(line)):
            if block == 'x':
                currentGrid[shape.y+vertical][shape.x+horizontal] = shape.color+1



def copyArray(src, dest):
    for vertical, line in enumerate(dest):
        for horizontal, block in enumerate(list(line)):
            src[vertical][horizontal] = block