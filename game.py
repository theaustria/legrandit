import pygame
from pygame.locals import *
from player import Player
from tile import Tile
from door import Door

class Game(object):
    def __init__(self,screensize):
        # set screen_rect
        width, height = screensize
        self.screen_rect = Rect(0, 0, width, height)
        # load images
        self.load_images()
        # setup player
        self.player = Player(self.images["player"])
        # teleport player to starting position
        self.player.teleport((200,200))
        # setup tiles
        self.tiles = pygame.sprite.Group()
        tile_images = (self.images["tile"],self.images["tile2"],self.images["tile3"])
        for i in range(10):
            for j in range(10):
                self.tiles.add( Tile( tile_images,(i*50,j*50) ) )
        # spawn trapdoor
        self.door = Door(self.images["door"],(150,300))
        
        self.running = True

    def update(self,keys):
        ''' update the objects
        
        Game.update(keys): return Bool
        
        Updates all game objects, checks for collisions. Returns alive status.
        '''
        # move player with keyboard input
        wasd = (keys[K_w], keys[K_a], keys[K_s], keys[K_d])
        self.player.set_dir(wasd)
        self.player.update()
        # detect collisions with walls, edge of screen or trapdoor
        edge = not self.screen_rect.contains(self.player.rect)
        collisions = pygame.sprite.spritecollide(self.player,self.tiles,False)
        exit = self.door.rect.contains(self.player.rect)
        # smash the tiles
        for tile in collisions:
            tile.smash()
            self.player.recoil()
        # if colliding, move the player back to it's former position
        if collisions or edge:
            self.player.undo()
        # if player stands completely on trapdoor, next level (or right now: exit game)
        if exit:
            self.end()
            
        return self.running
        
    def draw(self,screen):
        ''' draw the objects on the screen
        
        Game.draw(screen): return None
        '''
        # fill screen with background color
        screen.fill((0,0,0))
        # draw objects in right order
        self.door.draw(screen)
        self.tiles.draw(screen)
        self.player.draw(screen)

    def load_images(self):
        ''' load all images
        
        Game.load_images(): return None
        
        Loads all images and stores them into the self.images dictionary.
        '''
        self.images = {}
        for name in ["tile","tile2","tile3","ground","door"]:
            self.images[name] = pygame.image.load("images/%s.bmp" % name).convert()
            self.images[name] = pygame.transform.scale(self.images[name],(50,50))
        self.images["player"] = pygame.image.load("images/player.bmp").convert()
        self.images["player"] = pygame.transform.scale(self.images["player"],(30,30))
    
    def end(self):
        self.running = False
    