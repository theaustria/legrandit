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
        # load font
        self.font = pygame.font.SysFont(None,44)
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
        if keys[K_b]:
            self.player.money += 5
          
        if self.player.health <= 0:
            self.end()

        return self.running
        
    def draw(self,screen):
        ''' draw the objects on the screen
        
        Game.draw(screen): return None
        '''
        # fill screen with background surface
        screen.blit(self.images["bg"],(0,0))
        # draw objects in right order
        self.floor.interacts.draw(screen)
        self.floor.enemies.draw(screen)
        self.floor.collectables.draw(screen)
        self.floor.tiles.draw(screen)
        self.player.draw(screen)
        
        # draw status bar
        screen.fill((100,70,30),(0,500,500,25))
        screen.blit(self.images["coin"],(0,500))
        coins = self.font.render( "%03d" % self.player.money, False, (255,255,255) )
        screen.blit(coins,(30,500))
        for i in range(self.player.health):
            screen.blit( self.images["heart"], (100+i*30,500) )

    def load_images(self):
        ''' load all images
        
        Game.load_images(): return None
        
        Loads all images and stores them into the self.images dictionary.
        '''
        self.images = {}
        # load images and scale them
        for name in ["tile","tile2","tile3","ground","door","enemy"]:
            self.images[name] = pygame.image.load("images/%s.bmp" % name).convert()
            self.images[name] = pygame.transform.scale(self.images[name],(50,50))
        # load player image and scale it
        self.images["player"] = pygame.image.load("images/player2.bmp").convert()
        self.images["player"] = pygame.transform.scale(self.images["player"],(30,30))
        # load symbols
        symbols = pygame.image.load("images/symbols.bmp").convert()
        self.images["coin"] = pygame.Surface((26,25))
        self.images["heart"] = pygame.Surface((26,25))
        self.images["coin"].blit(symbols, (0,0), pygame.Rect(0,0,26,25) )
        self.images["heart"].blit(symbols, (0,0), pygame.Rect(26,0,26,25) )
        # set black as transparent
        for name in ["player","enemy","heart","coin"]:
            self.images[name].set_colorkey((0,0,0))
        # create background surface
        self.images["bg"] = pygame.Surface((self.screen_rect.size))
        for i in range(10):
            for j in range(10):
                self.images["bg"].blit(self.images["ground"],(i*50,j*50))
    
    def end(self):
        self.running = False
    