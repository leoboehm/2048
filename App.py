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
    
    beige = (243,217,177) 
    background_colour = beige
    #define dimensions of screen object
    display = pygame.display.set_mode((800,700))

    #set the caption of the screen
    pygame.display.set_caption('2048')

    #fill the background colour to the screen
    display.fill(background_colour)

    #update the display using flip
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