import pygame
from pygame.locals import *
from player import Player
from tile import Tile

class Game(object):
    def __init__(self):
        # setup Player and players group
        self.player = Player()
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        self.player.teleport((200,200))
        # setup Map
        self.tiles = pygame.sprite.Group()
        for i in range(10):
            for j in range(10):
                if not ((i==4 and j == 4) or (i==5 and j==4)):
                    self.tiles.add(Tile((i*50,j*50)))
    
    def update(self,keys):
        # move player with keyboard input
        wasd = (keys[K_w], keys[K_a], keys[K_s], keys[K_d])
        self.player.set_dir(wasd)
        self.players.update()
        # detect collision
        collision = pygame.sprite.spritecollide(self.player,self.tiles,True)
        if collision:
            self.player.undo()
        
    def draw(self,screen):
        screen.fill((0,0,0))
        self.tiles.draw(screen)
        self.players.draw(screen)
        
