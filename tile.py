import pygame
from pygame.locals import *
        
class Tile (pygame.sprite.Sprite):
    def __init__(self, images, pos):
        super().__init__()
        self.images = images
        self.image = self.images["tile"]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.health = 3
    
    def smash(self):
        self.health -= 1
        if self.health == 0:
            self.kill()
        elif self.health == 1:
            self.image = self.images["tile3"]
        elif self.health == 2:
            self.image = self.images["tile2"]
