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
        self.floor = Floor(self.images)

        self.running = True

    def update(self,keys,time_passed):
        ''' update the objects
        
        Game.update(keys): return Bool
        
        Updates all game objects, checks for collisions. Returns alive status.
        '''
        # move player with keyboard input
        wasd = (keys[K_w], keys[K_a], keys[K_s], keys[K_d])
        if keys[K_UP] or keys[K_LEFT] or keys[K_DOWN] or keys[K_RIGHT]:
            arrowkeys = (keys[K_UP],keys[K_LEFT],keys[K_DOWN],keys[K_RIGHT])
            self.player.attack(arrowkeys)
        self.player.set_dir(wasd)
        self.player.update(time_passed)
        #### debugging ####
        if keys[K_n]:
            self.floor.next()
        # detect collisions with walls, edge of screen
        edge = not self.screen_rect.contains(self.player.rect)
        tile_collisions = pygame.sprite.spritecollide(self.player,self.floor.tiles,False)
        attack_collisions = pygame.sprite.spritecollide(self.player.attack_rect,self.floor.tiles,False)
        # something door
        door = False
        # smash the tiles
        for tile in attack_collisions:
            tile.smash()
            #self.player.recoil()
        # if colliding, move the player back to it's former position
        if tile_collisions or edge:
            self.player.undo()
        # if player stands completely on trapdoor, next level
        if door:
            self.floor.next()
            self.player.teleport((200,200))
            
        return self.running
        
    def draw(self,screen):
        ''' draw the objects on the screen
        
        Game.draw(screen): return None
        '''
        # fill screen with background surface
        screen.blit(self.images["bg"],(0,0))
        # draw objects in right order
        #self.door.draw(screen)
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
    