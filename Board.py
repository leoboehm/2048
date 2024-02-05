import pygame

class Board:
    width: 100
    height: 100

    grid = []
    
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
        self.draw_grid()
    
    def draw_grid(self) :  
        width = 55
        height = 55
        margin = 5

        #create a 2 dimensional array
        for row in range(4):
            self.grid.append([])
            for col in range(4):
                self.grid[row].append(0)
        clock = pygame.time.Clock()

        done = False

        #main loop
        while not done:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True     
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #user clicks the mouse + get the position
                    pos = pygame.mouse.get_pos()
                    #change the x/y screen coordinates to self.grid coordinates
                    col = pos[0] //(width + margin)
                    row = pos[1] // (height + margin)

                    # double value
                    if self.grid[row][col] > 0:
                        self.grid[row][col] = self.doubleValue(self.grid[row][col])
                    else: self.grid[row][col] = 2

                    print("Click", pos, "self.grid coordinates: ", row, col, "Grid: ", self.grid)
           

            for row in range(4):
                for col in range(4):
                    color = self.getTileColor(self.grid[row][col])
                    pygame.draw.rect(self._display,
                                    color,
                                    [(margin + width)* col + margin,
                                    (margin + height)* row + margin,
                                    width,
                                    height])

            clock.tick(60)

            pygame.display.flip()

    def canMove(self):
        # check whether tile movement is possible
        return True

    # def spawnTile(self):
    #     # spawn single tile on random free position
        
    def getTileColor(self, value):
        return self.colordict[value]
    
    def doubleValue(self, value):
        return value * 2
    
    # def moveTiles(self):
    #     # move tiles and save new coordinates
    
    # def mergeTiles(self):
    #     # merge tiles on movement if their values are identical

    def sumScore(self):
        # calculate score
        return 0
        