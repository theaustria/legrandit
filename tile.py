import pygame
from pygame.locals import *
        
class Tile (pygame.sprite.Sprite):

    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
