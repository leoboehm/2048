import pygame
from pygame.locals import *
from Tile import *
from Board import *
class App:
    windowWidth = 500
    windowHeight = 500

    # colors
    black = (0,0,0)  
    espresso = (54,17,0)
    burlywood4 = (139,1115,85)
    lightbrown = (190,149,111)
    beige = (243,217,177) 
    redbrown = (139,35,35)

    def __init__(self):
        pygame.init()
        self._running = True
        
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight))
    
    def on_init(self):
        pygame.display.set_caption('2048')
        self._display.fill(self.beige)
        pygame.display.flip()
    
    def main(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                #check for quit event
                if event.type == pygame.QUIT:
                    self._running = False
        
        pygame.quit()



if __name__ == "__main__":
    app = App()
    app.main() 
