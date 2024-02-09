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

                if self.board.canMove():
                    if event.type == pygame.KEYDOWN:
                        direction = self.getKeyPressed()
                        if direction != "":
                            self.board.moveAndMergeTiles(direction)
                            direction = ""
                            self.board.spawnTile()
                            
                        self.board.drawGrid()
                            
                else: self.endGame()

                pass
                pygame.display.update()

        pygame.quit()

    def getScore(self):
        self.score = self.board.score
    
    def getKeyPressed(self):
        # check which key gets pressed and return direction
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            return "L"
        if keys[K_RIGHT]:
            return "R"
        if keys[K_UP]:
            return "U"
        if keys[K_DOWN]:
            return "D"
        
        # end game on esc
        if keys[K_ESCAPE]:
            self._running = False
        
        if keys[K_RETURN]:
           self.resetGame() 

    def endGame(self):
        # end the game
        self._running = False
        self.board.drawRestart
    
    # def resetGame(self):
    #     # reset game
        
    def resetGame(self):
        # reset the game
        self.board.drawRestart
        self.score = 0
        self.board = Board(self._display)
        
        self.endGame()
        

if __name__ == "__main__":
    app = App()
    app.main() 
