import pygame
from pygame.locals import *
from random import randint
        
class Monster (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("redplayer.png").convert()
        self.rect = self.image.get_rect()
        self.dir = [0,0]
        self.velocity = 5
        
    def update(self):
        self.rect.move_ip(self.dir)
        
    def set_dir(self,wasd):
        if wasd[0] != wasd[2]:
            if wasd[0]:
                self.dir[1] = -self.velocity
            else:
                self.dir[1] = self.velocity
        else:
            self.dir[1] = 0
        if wasd[1] != wasd[3]:
            if wasd[1]:
                self.dir[0] = -self.velocity
            else:
                self.dir[0] = self.velocity
        else:
            self.dir[0] = 0

class Stone (pygame.sprite.Sprite):
    def __init__(self,randpos=False):
        super().__init__()
        self.image = pygame.image.load("stone.png").convert()
        self.rect = self.image.get_rect()
        if randpos:
            self.rect.topleft = (randint(0,400),randint(0,400))
    def update():
        pass