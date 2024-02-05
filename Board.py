import pygame

class Board:
    width: 100
    height: 100
    
    def __init__(self):
        self._display = self.createDisplay()

    def createDisplay(self):
        return pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
    
    def draw_grid(self) :  
        width = 55
        height = 55
        margin = 5

        #create a 2 dimensional array
        grid = []
        for row in range(4):
            grid.append([])
            for column in range(4):
                grid[row].append(0)
        clock = pygame.time.Clock()

        done = False

        #main loop
        while not done:
            for event in pygame.event.get(): #User did something
                if event.type == pygame.QUIT: #If user clicked close
                    done = True      #exit this loop  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #user clicks the mouse + get the position
                    pos = pygame.mouse.get_pos()
                    #change the x/y screen coordinates to grid coordinates
                    column = pos[0] //(width + margin)
                    row = pos[1] // (height + margin)
                    #Set location to one
                    grid[row][column] = 1
                    print("Click", pos, "Grid coordinates: ", row, column)
           

        for row in range(4):
            for column in range(4):
                color = self.white
                pygame.draw.rect(self._display,
                                color,
                                [(margin + width)* column + margin,
                                (margin + height)* row + margin,
                                width,
                                height])

        clock.tick(60)

        pygame.display.flip()




        