import pygame
from pygame.locals import *
from Board import *

class App:
    windowWidth = 500
    windowHeight = 500

    score = 0

    # colors
    black = (0,0,0)  
    white = (255, 255, 255)
    beige = (243,217,177) 


    def __init__(self):
        pygame.init()
        self._running = True
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight))
    
    def on_init(self):
        pygame.display.set_caption('2048')
        self._display.fill(self.beige)
        self.board = Board(self._display)
        pygame.display.flip()
    
    def main(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                #check for quit event
                if event.type == pygame.QUIT:
                    self._running = False
                else:
                    if self.board.canMove():
                        self.board.moveTiles(self.getKeyPressed())

                pass
                self.board.drawGrid()
                self.updateScore()

        pygame.quit()

    def updateScore(self):
        self.score += self.board.sumScore()
    
    def getKeyPressed(self):
        # check which key gets pressed and respond correspondingly
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            return 1
        if keys[K_RIGHT]:
            return 2
        if keys[K_UP]:
            return 3
        if keys[K_DOWN]:
            return 4
        
        if keys[K_ESCAPE]:
            self._running = False

    # def gameOver(self):
    #     # end the game (Without closing the window)
    
    # def resetGame(self):
    #     # reset game


if __name__ == "__main__":
    app = App()
    app.main() 
