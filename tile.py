import pygame
from pygame.locals import *
        
class Tile (pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/tile.bmp").convert(),(50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos