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
        self.font = pygame.font.Font("freesansbold.ttf",24)

    def on_init(self):
        pygame.display.set_caption('2048')
        self._display.fill(self.beige)
        self._gridDisplay = pygame.Surface((245,245))
        self.board = Board(self._gridDisplay)
        self.draw()
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
                            
                        self.draw()    
                else: self.endGame()

                pass
                pygame.display.update()

        pygame.quit()

    def getScore(self):
        self.score = self.board.score
    
    def displayScore(self):
        score_text = self.font.render(f'Score: {self.getScore()}',True, (255,255,255))
        self._display.blit(score_text,(305,30))
    
    def getKeyPressed(self):
        # check which key gets pressed and return rotations
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            return 0
        if keys[K_RIGHT]:
            return 2
        if keys[K_UP]:
            return 1
        if keys[K_DOWN]:
            return 3
        
        # end game on esc
        if keys[K_ESCAPE]:
            self._running = False
        
        if keys[K_RETURN]:
           self.resetGame() 

    def endGame(self):
        # end the game
        self._running = False
        self.resetGame()
    
    # def resetGame(self):
    #     # reset game
        
    def resetGame(self):
        # reset the game
        pygame.draw.rect(self._display,(0,0,0),pygame.Rect(50,50,300, 300))
        game_over_text1 = self.font.render("Game over!",True,(255,255,255))
        game_over_text2 = self.font.render("Press Enter to Restart",True,(255,255,255))
        self._display.blit(game_over_text1,(130,65))
        self._display.blit(game_over_text2,(70,105))

        self.score = 0
    
    def draw(self):
        # set up position of the grid and text
        self.displayScore()
        self.board.drawGrid()
        self._display.blit(self._gridDisplay,(40,60))


if __name__ == "__main__":
    app = App()
    app.main() 
