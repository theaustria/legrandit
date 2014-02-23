import pygame
from pygame.locals import *
from objects import *

class Game(object):
    def __init__(self):
        self.player = Monster()
        self.players = pygame.sprite.Group()
        self.stones = pygame.sprite.Group()
        self.players.add(self.player)
        for i in range(50):
            self.stones.add(Stone(True))
    
    def update(self,keys):
        wasd = (keys[K_w], keys[K_a], keys[K_s], keys[K_d])
        self.player.set_dir(wasd)
        self.players.update()
        collisions = pygame.sprite.spritecollide(self.player,self.stones,True)
        for c in collisions:
            self.player.velocity+=1
        
    def draw(self,screen):
        screen.fill((0,0,0))
        self.players.draw(screen)
        self.stones.draw(screen)
        
