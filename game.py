import pygame
from pygame.locals import *

from player import Player
from tile import Tile
from door import Door
from floor import Floor

class Game(object):
    def __init__(self,screen_rect):
        # set screen_rect
        self.screen_rect = screen_rect
        # load images
        self.load_images()
        # setup player
        self.player = Player(self.images["player"])
        # teleport player to starting position
        self.player.teleport((200,200))
        # create starting level
        self.floor = Floor(self.images,screen_rect)

        self.running = True

    def update(self,keys,time_passed):
        ''' update the objects
        
        Game.update(keys): return Bool
        
        Updates all game objects, checks for collisions. Returns alive status.
        '''
        # update player with keyboard input and passed time
        self.player.update(keys,time_passed)
        # handle collisions
        self.floor.collide(self.player)
        # interact with objects
        if keys[K_SPACE]:
            self.floor.interact(self.player)
        
        #### debugging / cheating ####
        if keys[K_n]:
            self.floor.next()
        if keys[K_m]:
            self.floor.tiles.empty()
        if keys[K_COMMA]:
            print(self.floor.level)
            
        return self.running
        
    def draw(self,screen):
        ''' draw the objects on the screen
        
        Game.draw(screen): return None
        '''
        # fill screen with background surface
        screen.blit(self.images["bg"],(0,0))
        # draw objects in right order
        self.floor.interacts.draw(screen)
        self.floor.tiles.draw(screen)
        self.player.draw(screen)

    def load_images(self):
        ''' load all images
        
        Game.load_images(): return None
        
        Loads all images and stores them into the self.images dictionary.
        '''
        self.images = {}
        # load images and scale them
        for name in ["tile","tile2","tile3","ground","door"]:
            self.images[name] = pygame.image.load("images/%s.bmp" % name).convert()
            self.images[name] = pygame.transform.scale(self.images[name],(50,50))
        # load player image and scale it
        self.images["player"] = pygame.image.load("images/player.bmp").convert()
        self.images["player"] = pygame.transform.scale(self.images["player"],(30,30))
        # set black as transparent
        self.images["player"].set_colorkey((0,0,0))
        # create background surface
        self.images["bg"] = pygame.Surface((self.screen_rect.size))
        for i in range(10):
            for j in range(10):
                self.images["bg"].blit(self.images["ground"],(i*50,j*50))
    
    def end(self):
        self.running = False
    