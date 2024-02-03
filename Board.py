import pygame

class Board:
    width: 100
    height: 100
    
    def __init__(self):
        self._display = self.createDisplay()

    def createDisplay(self):
        return pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)


