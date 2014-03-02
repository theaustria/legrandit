import pygame
from pygame.locals import *
import random
from random import randint,choice

from tile import Tile
from door import Door
from enemy import Enemy
from collectable import Coin, Heart

TILEPROB = [False] + [True for i in range(3)]
ENEMYPROB = [True] + [False for i in range(6)]
COINPROB = [True] + [False for i in range(4)]
HEARTPROB = [True] + [False for i in range(9)]
COINS = [1 for i in range(20)] + [2 for i in range(15)] + [5 for i in range(8)] + [10 for i in range(4)] + [50 for i in range(1)]

class Floor(object):
    def __init__(self,images,screen_rect):
        self.level = 0
        self.images = images
        self.screen_rect = screen_rect
        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        # interacts must have self.name attribute !
        self.interacts = pygame.sprite.Group()
        self.collectables = pygame.sprite.Group()
        self.groups = [self.tiles,self.interacts,self.enemies,self.collectables]
        
        random.seed(42)
        self.generate()
        
    def next(self):
        self.level += 1
        self.clear()
        self.generate()
        
    def generate(self):
        # place tiles and enemies
        for i in range(10):
            for j in range(10):
                if choice(TILEPROB):
                    self.tiles.add( Tile( self.images,(i*50,j*50) ) )
                elif choice(COINPROB):
                    self.collectables.add ( Coin ( self.images["coin"], (i*50+12,j*50+13) ) )
                elif choice(ENEMYPROB):
                    self.enemies.add( Enemy( self.images["enemy"],(i*50,j*50) ) )
                elif choice(HEARTPROB):
                    self.collectables.add( Heart( self.images["heart"],(i*50+12,j*50+13) ) )
                
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
        enemy_collisions = pygame.sprite.spritecollide(player,self.enemies,False)
        collectable_collisions = pygame.sprite.spritecollide(player,self.collectables,True)
        tile_attack = pygame.sprite.spritecollide(player.attack_rect,self.tiles,False)
        enemy_attack = pygame.sprite.spritecollide(player.attack_rect,self.enemies,False)
        # if colliding, move the player back to it's former position
        if tile_collisions or edge:
            player.undo()
        if enemy_collisions:
            player.health -= 1
            player.undo()
            player.recoil()
        # smash the attacked tiles/enemies
        for tile in tile_attack:
            tile.smash(player.damage)
        for enemy in enemy_attack:
            enemy.smash(player.damage)
        # get the money from the coins
        for object in collectable_collisions:
            if object.name == "coin":
                player.money += choice(COINS)
            elif object.name == "heart":
                player.health += 1

            
    def interact(self,player):
        interactions = pygame.sprite.spritecollide(player,self.interacts,False)
        for object in interactions:
            if object.name == "door":
                self.next()
