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
    tan = (210,180,140)


    def __init__(self):
        pygame.init()
        self._running = True
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        self.font = pygame.font.Font("freesansbold.ttf",24)

    def on_init(self):
        pygame.display.set_caption('2048')
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
                        direction = self.getKeyPressed()
                        if direction != "":
                            self.board.moveAndMergeTiles(direction)
                            direction = ""
                            self.board.spawnTile()
                        
                        self.draw()
                        self.resetGame()
                else: self.endGame()

                pass
                pygame.display.update()

        pygame.quit()

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
        self.resetGame()

    def resetGame(self):
        # reset the game
        pygame.draw.rect(self._display,self.tan,pygame.Rect(90,310,290,290))
        game_over_text1 = self.font.render("Game over!",True,self.white)
        game_over_text2 = self.font.render("Press Enter to Restart",True,self.white)
        self._display.blit(game_over_text1,(100,380))
        self._display.blit(game_over_text2,(100,420))

        self.score = 0

    def draw(self):
        # set up position of the grid and text
        self._display.fill(self.beige)
        score_text = self.font.render("Score: " + str(self.board.score),True, self.white)
        self._display.blit(score_text,(305,30))
        self.board.drawGrid()
        self._display.blit(self._gridDisplay,(40,60))

    def startMenu(self):
        game_start = False

        while True :
            pygame.display.set_caption("Start Menu")
            self._display.fill(self.beige)

            #check if space is pressed
            if game_start == True:
                self.main()
            else:
                startText = self.font.render("Play",True,self.white)
                instructionText = self.font.render("How to play: ",True,self.white)
                startTextRect = startText.get_rect()
                instructionTextRect = instructionText.get_rect()
                self._display.blit(startTextRect,(200,200))
                self._display.blit(instructionTextRect,(100,250))


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._display
                        print("Start") 
                if event .type == pygame.QUIT:
                    
                    pygame.quit()
                    quit()
                pygame.display.update()
                

if __name__ == "__main__":
    app = App()
    app.main()
