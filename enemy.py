import pygame
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.health = 2
        
    def smash(self,damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()