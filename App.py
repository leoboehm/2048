import pygame, sys, time
from pygame.locals import *
from Board import *

class App:
    windowWidth = 500
    windowHeight = 500

    score = 0

    # colors
    black = (0,0,0)  
    white = (255, 255, 255)
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

                if self.board.canMove():
                    if event.type == pygame.KEYDOWN:
                        rotations = self.getKeyPressed()
                        for i in range(0,rotations):
                            self.board.rotateMatrix()
 
                        if self.board.canMove():
                            self.board.moveTiles()
                            self.board.mergeTiles()
                            self.board.spawnTile()
 
                        for j in range(0,(4-rotations)%4):
                            self.board.rotateMatrix()
                            
                        self.board.drawGrid()
                            
                else: self.endGame()

                pass
                pygame.display.update()

        pygame.quit()

    def getScore(self):
        self.score = self.board.score
    
    def getKeyPressed(self):
        # check which key gets pressed and return rotations
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            return 1
        if keys[K_RIGHT]:
            return 3
        if keys[K_UP]:
            return 0
        if keys[K_DOWN]:
            return 2
        
        # end game on esc
        if keys[K_ESCAPE]:
            self._running = False

    def endGame(self):
        # end the game
        self._running = False
    
    def resetGame(self):
        # reset the game
        self.score = 0
        self.board = Board(self._display)


if __name__ == "__main__":
    app = App()
    app.main() 
