import pygame
import random

class Board:
    width: 100
    height: 100

    grid = []
    score = 0
    
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
        self.font = pygame.font.Font("freesansbold.ttf",24)

        self.initGrid()
    
    # initialize grid
    def initGrid(self):
        # create an empty 4x4 matrix
        self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
        # spawn 2 tiles
        self.spawnTile()
        self.spawnTile()

    # draw board
    def drawGrid(self) :  
        width = 55
        height = 55
        margin = 5

        for row in range(4):
            for col in range(4):
                color = self.getTileColor(self.grid[row][col])
                # draw tile
                pygame.draw.rect(self._display, color, [(margin + width)* col + margin,
                                                        (margin + height) * row + margin,
                                                        width, height])
                # draw tile value
                if(self.grid[row][col] > 0):
                    value_text = self.font.render(str(self.grid[row][col]), True, "black")
                    text_rect = value_text.get_rect(center=((margin + width)* col + margin + int(width/2), (margin + height) * row + margin + int(height/2)))
                    self._display.blit(value_text, text_rect)

    # spawn single tile on random free position
    def spawnTile(self):
        row = random.randint(0,3)
        col = random.randint(0,3)

        if self.grid[row][col] == 0:
            self.grid[row][col] = random.choice([2, 4])
        else: self.spawnTile()
       
    # check whether tile movement is possible
    def canMove(self):
        for row in range(4):
            for col in range(4):
                # check whether 2048 is reached
                if self.grid[row][col] == 2048: return False
                # check for empty fields
                if self.grid[row][col] == 0: return True 
                # check for possible merges
                # up or down
                if row > 0:
                    if self.grid[row - 1][col] == self.grid[row][col]:
                        return True
                # left or right
                if col > 0:
                    if self.grid[row][col - 1] == self.grid[row][col]:
                        return True
        # return false per default if none of the conditions are met
        return False

    # move tiles and save new coordinates
    def moveAndMergeTiles(self, direction):
        # direction up
        if direction == "U":
            self.moveUp()
        # direction down
        if direction == "D":
            self.moveDown()
        # direction left
        if direction == "L":
            self.moveLeft()
        # direction right
        if direction == "R":
            self.moveRight()

    def moveUp(self):
        # remember merged positions to prevent multiple merges in one move
        mergedPositions = [[False for _ in range(4)] for _ in range(4)]

        for row in range(4):
            for col in range(4):
                moveRange = 0
                if row > 0:
                    # check how many rows the tile can move upwards
                    for rowA in range(row):
                        if self.grid[rowA][col] == 0:
                            moveRange += 1
                    # move tile upwards
                    if moveRange > 0:
                        self.grid[row - moveRange][col] = self.grid[row][col]
                        self.grid[row][col] = 0
                    # check whether the tile and it's neighbour have the same value and have not already merged
                    if self.grid[row - moveRange - 1][col] == self.grid[row - moveRange][col] \
                        and not mergedPositions[row - moveRange - 1][col] \
                            and not mergedPositions[row - moveRange][col]:
                        # merge tiles
                        self.grid[row - moveRange - 1][col] *= 2
                        self.grid[row - moveRange][col] = 0
                        mergedPositions[row - moveRange - 1][col] = True

    def moveDown(self):
        # remember merged positions to prevent multiple merges in one move
        mergedPositions = [[False for _ in range(4)] for _ in range(4)]

        for row in range(3):
            for col in range(4):
                moveRange = 0
                # check how many rows the tile can move downwards
                for rowA in range(row + 1):
                    if self.grid[3 - rowA][col] == 0:
                        moveRange += 1
                # move tile downwards
                if moveRange > 0:
                    self.grid[2 - row + moveRange][col] = self.grid[row][col]
                    self.grid[2 - row][col] = 0
                # check whether the tile and it's neighbour have the same value and have not already merged
                if 3 - row + moveRange <= 3:
                    if self.grid[2 - row + moveRange][col] == self.grid[3 - row + moveRange][col] \
                        and not mergedPositions[2 - row + moveRange][col] \
                            and not mergedPositions[3 - row + moveRange][col]:
                        # merge tiles
                        self.grid[3 - row + moveRange][col] *= 2
                        self.grid[2 - row + moveRange][col] = 0
                        mergedPositions[3 - row + moveRange][col] = True

    def moveLeft(self):
        # remember merged positions to prevent multiple merges in one move
        mergedPositions = [[False for _ in range(4)] for _ in range(4)]
        
        for row in range(4):
            for col in range(4):
                moveRange = 0
                # check how many rows the tile can move to the left
                for colA in range(col):
                    if self.grid[row][colA] == 0:
                        moveRange += 1
                # move tile to the left
                if moveRange > 0:
                    self.grid[row][col - moveRange] = self.grid[row][col]
                    self.grid[row][col] = 0
                # check whether the tile and it's neighbour have the same value and have not already merged
                if self.grid[row][col - moveRange] == self.grid[row][col - moveRange - 1] \
                    and not mergedPositions[row][col - moveRange - 1] \
                        and not mergedPositions[row][col - moveRange]:
                    # merge tiles
                    self.grid[row][col - moveRange - 1] *= 2
                    self.grid[row][col - moveRange] = 0
                    mergedPositions[row][col - moveRange - 1] = True
    
    def moveRight(self):
        # remember merged positions to prevent multiple merges in one move
        mergedPositions = [[False for _ in range(4)] for _ in range(4)]
    
        for row in range(4):
            for col in range(4):
                moveRange = 0
                # check how many rows the tile can move to the right
                for colA in range(col):
                    if self.grid[row][3 - colA] == 0:
                        moveRange += 1
                # move tile to the right
                if moveRange > 0:
                    self.grid[row][3 - col + moveRange] = self.grid[row][3 - col]
                    self.grid[row][3 - col] = 0
                # check whether the tile and it's neighbour have the same value and have not already merged
                if 4 - col + moveRange <= 3:
                    if self.grid[row][4 - col + moveRange] == self.grid[row][3 - col + moveRange] \
                        and not mergedPositions[row][4 - col + moveRange] \
                            and not mergedPositions[row][3 - col + moveRange]:
                        # merge tiles
                        self.grid[row][4 - col + moveRange] *= 2
                        self.grid[row][3 - col + moveRange] = 0
                        mergedPositions[row][4 - col + moveRange] = True

    def getTileColor(self, value):
        return self.colordict[value]