import pygame
import sys
from players import Player 
#MAKING THE CAMERA
class Cam(pygame.sprite.Group):
    def __init__(self , screen):
        super().__init__()
        self.dis = screen
        self.offset = pygame.math.Vector2()
        self.bg = pygame.image.load("/Users/zeeldarji/Desktop/python files/game/resources/bg/map.png")

    def movin(self):
        self.offset.x = Player.rect.centerx-625
        self.offset.y = Player.rect.centery-425
        self.dis.blit(self.bg , (-self.offset.x , -self.offset.y))

class Game(pygame.sprite.Sprite):
    def __init__(self):
        self.screen = pygame.display.set_mode((1120 , 850))
        #GETTING THE BACKGROUND IMAGE
        
        pygame.display.set_caption("the detect")
        self.group = Cam(self.screen)
        self.player = Player((50 , 50) , self.group)

#MAKING THE GAME RUNf
        
    def runnin(self):
        while True:
            self.screen.fill("red")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.group.movin()
            self.group.update()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.runnin()