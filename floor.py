import pygame
from pygame.locals import *
from random import choice,randint

from tile import Tile
from door import Door

class Floor(object):
    def __init__(self,images):
        self.level = 0
        self.images = images
        self.tiles = pygame.sprite.Group()
        self.interacts = pygame.sprite.Group()
        self.groups = [self.tiles,self.interacts]
        
        self.generate()
        
    def next(self):
        self.level += 1
        self.clear()
        self.generate()
        
    def generate(self):
        # set frequency of missing tiles
        prob = [False] + [True for i in range(5)]
        # place tiles
        for i in range(10):
            for j in range(10):
                if choice(prob):
                    self.tiles.add( Tile( self.images,(i*50,j*50) ) )
        # place trapdoor
        x, y = randint(0,10), randint(0,10)
        self.interacts.add( Door( self.images["door"], ( x*50, y*50 ) ) )
        
    def clear(self):
        for group in self.groups:
            group.empty()