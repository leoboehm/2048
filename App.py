import pygame
from pygame.locals import *
from Board import *

class App:
    windowWidth = 500
    windowHeight = 500

    direction = ""

    # colors
    white = (255, 255, 255)
    beige = (243,217,177)
    tan = (210,180,140)
    red = (230, 0, 0)

    def __init__(self):
        pygame.init()
        self._running = True
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        self.fontNormal = pygame.font.Font("freesansbold.ttf",28)
        self.fontBig = pygame.font.Font("freesansbold.ttf",32)

    # set initial params
    def on_init(self):
        pygame.display.set_caption('2048')
        self._gridDisplay = pygame.Surface((245,245))
        self.board = Board(self._gridDisplay)
        self.drawIngameScreen()
        pygame.display.flip()

    # main loop
    def main(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                #check for quit event
                if event.type == pygame.QUIT:
                    self._running = False
                
                self.getKeyPressed()

                if self.board.canMove():
                    if self.direction != "":
                        self.board.moveAndMergeTiles(self.direction)
                        self.direction = ""
                        self.board.spawnTile()
                        
                    self.drawIngameScreen()

                else: self.drawGameOverScreen()

                pass
                pygame.display.update()

        pygame.quit()

    # check which key gets pressed and perform action
    def getKeyPressed(self):
        keys = pygame.key.get_pressed()

        # save move direction
        if keys[K_LEFT]:
            self.direction = "L"
        if keys[K_RIGHT]:
            self.direction = "R"
        if keys[K_UP]:
            self.direction = "U"
        if keys[K_DOWN]:
            self.direction = "D"
        
        # end game on esc
        if keys[K_ESCAPE]:
            self._running = False
        # reset game on return
        if keys[K_RETURN]:
           self.resetGame()

    # set up grid position & ingame texts
    def drawIngameScreen(self):
        self._display.fill(self.beige)
        scoreText = self.fontNormal.render("Score: " + str(self.board.score),True, self.white)
        self._display.blit(scoreText,(315,60))
        pygame.draw.rect(self._display,self.tan,pygame.Rect(40,350,350,100))
        restartText = self.fontNormal.render("Press Enter to Restart",True,self.white)
        self._display.blit(restartText,(50,385))
        self.board.drawGrid()
        self._display.blit(self._gridDisplay,(40,60))

    # draw game over screen overlay
    def drawGameOverScreen(self):
        gameOverText = self.fontBig.render("GAME OVER!",True,self.red)
        self._display.blit(gameOverText,(60,165))

    # reset board & score and start over
    def resetGame(self):
        self.on_init()

    # def startMenu(self):
    #     game_start = False

    #     while True :
    #         pygame.display.set_caption("Start Menu")
    #         self._display.fill(self.beige)

    #         #check if space is pressed
    #         if game_start == True:
    #             self.main()
    #         else:
    #             startText = self.fontNormal.render("Play",True,self.white)
    #             instructionText = self.fontNormal.render("How to play: ",True,self.white)
    #             startTextRect = startText.get_rect()
    #             instructionTextRect = instructionText.get_rect()
    #             self._display.blit(startTextRect,(200,200))
    #             self._display.blit(instructionTextRect,(100,250))


    #         for event in pygame.event.get():
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE:
    #                     self._display
    #                     print("Start") 
    #             if event .type == pygame.QUIT:
                    
    #                 pygame.quit()
    #                 quit()
    #             pygame.display.update()
                

if __name__ == "__main__":
    app = App()
    app.main()
