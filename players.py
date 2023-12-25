import pygame
from os import walk
import sys
from os import walk

class Player(pygame.sprite.Sprite):
    def __init__(self , pos , group):
        super().__init__(group)
        self.animate()
        self.framerate = 0
        self.image = self.animation[self.frame][self.framerate]
        self.rect = self.image.get_rect(center = pos)
        #setting the direction
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 1
        



#MAKING THE ANIMATION
    def animate(self):
        self.animation = {}
        for index,file in enumerate(walk("/Users/zeeldarji/Desktop/python files/game/resources/player")):
            if index == 0:
                for name in file[1]:
                    self.animation[name] = []
            else:
                for name in file[2]:
                    path = str(file[0])+"/"+ name
                    image = pygame.image.load(path)
                    keys = file[0].split("/")[-1]
                    self.animation[keys].append(image)

        self.frame = "down"
      


        return self.animation

#THE LEG GAME
    def leg(self):
        if self.framerate <= len(self.animation[self.frame]):
            self.framerate+=0.01
            if self.framerate >= len(self.animation[self.frame]):
                self.framerate = 0
        self.image = self.animation[self.frame][int(self.framerate)]
                            

            

    

    #ASKING THE PLAYER TO MOVE
    def movin(self):
        self.pos += self.direction*self.speed
        self.rect.center = (round(self.pos.x) , round(self.pos.y))

    def input(self):
        #GETTING A VARIABLE FOR THE KEY PRESSED
        g = pygame.key.get_pressed()

        #THE MOVEMENTS OF ALL THE PLAYERS
        if g[pygame.K_w]:
            self.direction.y = -1
            self.frame = "up"
        if g[pygame.K_s]:
            self.direction.y = 1
            self.frame = "down"
        if g[pygame.K_a]:
            self.direction.x = -1
            self.frame ="left"
        if g[pygame.K_d]:
            self.direction.x = 1
            self.frame = "right"

        if g[pygame.K_0]:
            self.direction.x = 0
            self.direction.y = 0

        self.pos.x += self.direction.x*self.speed
        self.pos.y += self.direction.y*self.speed
        self.rect.center = (round(self.pos.x) , round(self.pos.y))

    def update(self):
        
        self.input()
        self.movin()
        self.leg()