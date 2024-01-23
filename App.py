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
