import pygame
import random

class Board:
    width: 100
    height: 100
    # size: 4

    grid = []

    # directions
    # 1 = "left"
    # 3 = "right"
    # 0 = "up"
    # 2 = "down"
    
    colordict = {
        0: (255,255,255), # white
        2: (255,0,0), # red
        4: (0,128,0), # green
        8: (156,39,176), # purple
        16: (103,58,183), # deep purple
        32: (255,87,34), # deep orange
        64: (0,150,136), # teal
        128: (139,195,74), # light green
        256: (234,30,99), # pink
        512: (255,152,0), # orange
        1024: (33,150,136), # blue
        2048: (121,85,72) # brown
    }
    
    def __init__(self, display):
        self._display = display
        self.initGrid()
    
    def initGrid(self):
        # create a 4x4 matrix
        self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
        # spawn two tiles
        self.spawnTile()
        self.spawnTile()

        self.drawGrid()

    def drawGrid(self) :  
        width = 55
        height = 55
        margin = 5

        for row in range(4):
            for col in range(4):
                color = self.getTileColor(self.grid[row][col])
                pygame.draw.rect(self._display, color, [(margin + width)* col + margin,
                                                        (margin + height) * row + margin,
                                                        width, height])

        # pygame.display.flip()

    def spawnTile(self):
        # spawn single tile on random free position
        i = random.randint(0,3)
        j = random.randint(0,3)

        if self.grid[i][j] == 0:
            self.grid[i][j] = random.choice([2, 4])
        else: self.spawnTile()
       
    def canMove(self):
        # check whether tile movement is possible
        for row in range(4):
            for col in range(4):
                if self.grid[row][col] == 2048: return False

        for i in range(4):
            for j in range(1,4):
                if self.grid[i][j-1] == 0 and self.grid[i][j] > 0:
                    return True 
                elif (self.grid[i][j-1] == self.grid[i][j]) and self.grid[i][j-1] != 0:
                    return True
        return False

    def moveTiles(self):
        # move tiles and save new coordinates
        for i in range(4):
            for j in range(3):
                
                while self.grid[i][j] == 0 and sum(self.grid[i][j:]) > 0:
                    for k in range(j,3):
                        self.grid[i][k] = self.grid[i][k+1]
                        self.grid[i][3] = 0
    
    def mergeTiles(self):
        # merge tiles and double their value if their values are identical 
        for i in range(4):
            for k in range(3):
                if self.grid[i][k] == self.grid[i][k+1] and self.grid[i][k] != 0:
                    self.grid[i][k] = self.doubleValue(self.grid[i][k])
                    self.grid[i][k+1] = 0
                    self.sumScore(self.grid[i][k])
                    self.moveTiles()
    
    def rotateMatrix(self):
        for i in range(2):
            for k in range(i,3 - i):
                temp1 = self.grid[i][k]
                temp2 = self.grid[3 - k][i]
                temp3 = self.grid[3 - i][3 - k]
                temp4 = self.grid[k][3 - i]
    
                self.grid[3 - k][i] = temp1
                self.grid[3 - i][3 - k] = temp2
                self.grid[k][3 - i] = temp3
                self.grid[i][k] = temp4
 
    def getTileColor(self, value):
        return self.colordict[value]
    
    def doubleValue(self, value):
        return value * 2
    
    def sumScore(self):
        # calculate score
        return 0
        