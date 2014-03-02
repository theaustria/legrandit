import pygame
from pygame.locals import *
import random
from random import randint,choice

from tile import Tile
from door import Door

class Floor(object):
    def __init__(self,images,screen_rect):
        self.level = 0
        self.images = images
        self.screen_rect = screen_rect
        self.tiles = pygame.sprite.Group()
        # interacts must have self.name attribute !
        self.interacts = pygame.sprite.Group()
        self.groups = [self.tiles,self.interacts]
        
        random.seed(42)
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
        x, y = randint(0,9), randint(0,9)
        self.interacts.add( Door( self.images["door"], ( x*50, y*50 ) ) )
        
    def clear(self):
        for group in self.groups:
            group.empty()
            
    def collide(self,player):
        # detect collisions with walls, edge of screen and attack_rect
        edge = not self.screen_rect.contains(player.rect)
        tile_collisions = pygame.sprite.spritecollide(player,self.tiles,False)
        attack_collisions = pygame.sprite.spritecollide(player.attack_rect,self.tiles,False)
        # smash the tiles
        for tile in attack_collisions:
            tile.smash()
        # if colliding, move the player back to it's former position
        if tile_collisions or edge:
            player.undo()
            
    def interact(self,player):
        interactions = pygame.sprite.spritecollide(player,self.interacts,False)
        for object in interactions:
            if object.name == "door":
                self.next()
