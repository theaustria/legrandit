import pygame
from pygame.locals import *
        
class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/monster2.bmp").convert()
        self.image = pygame.transform.scale(self.image,(25,25))
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

    def undo(self):
        self.rect.move_ip(-self.dir[0],-self.dir[1])
      
    def teleport(self,pos):
        self.rect.topleft = pos