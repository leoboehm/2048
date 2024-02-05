import pygame

class Board:
    width: 100
    height: 100

    grid = []
    
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
            for column in range(4):
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
                    column = pos[0] //(width + margin)
                    row = pos[1] // (height + margin)

                    #Set location to one
                    self.grid[row][column] = 1
                    print("Click", pos, "self.grid coordinates: ", row, column)
           

            for row in range(4):
                for column in range(4):
                    color = (255, 255, 255)
                    if self.grid[row][column] == 1:
                        color = (255, 0, 0)
                    pygame.draw.rect(self._display,
                                    color,
                                    [(margin + width)* column + margin,
                                    (margin + height)* row + margin,
                                    width,
                                    height])

            clock.tick(60)

            pygame.display.flip()




        