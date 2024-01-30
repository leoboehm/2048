import pygame
from pygame.locals import *

class App:
    windowWidth = 0
    windowHeight = 0

    def __init__(self):
        pygame.init()
        pinfo = pygame.display.Info()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

        # self.windowWidth = pinfo.current_w -10
        # self.windowHeight = pinfo.current_h -100

        self._running = True
    
    def on_init(self):
        self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)


if __name__ == "__main__":
    app = App()
    # app.start() 
    
    black = (0,0,0)  
    espresso = (54,17,0)
    burlywood4 = (139,1115,85)
    lightbrown = (190,149,111)
    beige = (243,217,177) 
    redbrown = (139,35,35)
    
    background_colour = beige

    display = pygame.display.set_mode((800,700))

    pygame.display.set_caption('2048')

    display.fill(background_colour)

    pygame.display.flip()

    #variable to keep our game loop running
    running = True

    #game loop
    while running:

        for event in pygame.event.get():
            #check for quit event
            if event.type == pygame.QUIT:
                running = False

    #quit pygame after closing window
                pygame.quit()