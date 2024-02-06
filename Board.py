import pygame
import random

class Board:
    width: 100
    height: 100

    grid = []

    # directions
    # 1 = "left"
    # 2 = "right"
    # 3 = "up"
    # 4 = "down"
    
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

        pygame.display.flip()

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
        return True

    def moveTiles(self, direction):
        # move tiles and save new coordinates
        print("moveTiles - direction: ", direction)
    
    # input tile: [first level grid index, second level grid index]
    def mergeTiles(self, direction):
        # merge tiles and double their value if their values are identical
        return None
 
    def getTileColor(self, value):
        return self.colordict[value]
    
    def doubleValue(self, value):
        return value * 2
    
    def sumScore(self):
        # calculate score
        return 0
        