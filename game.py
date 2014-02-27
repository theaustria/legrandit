import pygame
from pygame.locals import *
from player import Player
from tile import Tile

class Game(object):
    def __init__(self,screensize):
        # set screen_rect
        width, height = screensize
        self.screen_rect = Rect(0, 0, width, height)
        # load images
        self.load_images()
        # setup player and players group
        self.player = Player(self.images["player"])
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        # teleport player to starting position
        self.player.teleport((200,200))
        # setup tiles
        self.tiles = pygame.sprite.Group()
        for i in range(10):
            for j in range(10):
                self.tiles.add( Tile( self.images["tile"],(i*50,j*50) ) )

    def update(self,keys):
        ''' update the objects
        
        Game.update(keys): return None
        '''
        # move player with keyboard input
        wasd = (keys[K_w], keys[K_a], keys[K_s], keys[K_d])
        self.player.set_dir(wasd)
        self.players.update()
        # detect collisions with walls or edge of screen
        edge = not self.screen_rect.contains(self.player.rect)
        collision = pygame.sprite.spritecollide(self.player,self.tiles,True)
        # if colliding, move the player back to it's former position
        if collision or edge:
            self.player.undo()

    def draw(self,screen):
        ''' draw the objects on the screen
        
        Game.draw(screen): return None
        '''
        screen.fill((0,0,0))
        self.tiles.draw(screen)
        self.players.draw(screen)

    def load_images(self):
        ''' load all images
        
        Game.load_images(): return None
        
        Loads all images and stores them into the self.images dictionary.
        '''
        self.images = {}
        for name in ["player","tile","ground"]:
            self.images[name] = pygame.image.load("images/%s.bmp" % name).convert()
