import pygame
from pygame.locals import *

class Door(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)