import pygame
from pygame.locals import *
import game
pygame.init()

VERSION = "0.06"
FPS = 40
TITEL = "Legrandit %s" % VERSION
WINDOWSIZE = (500,500)
ICON = pygame.image.load("images/icon.png")

class Engine(object):
    '''
    The Engine manages keyboard input, game state, screen drawing, updating.
    '''
    def __init__(self):
        self.running = True
        self.state = 0
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode(WINDOWSIZE)
        pygame.display.set_caption(TITEL)
        self.clock = pygame.time.Clock()
        self.last_time = pygame.time.get_ticks()
        self.game = game.Game(self.screen.get_rect())
    
    def loop(self):
        ''' run the main game loop
        
        Engine.loop(): return None
        '''
        while self.running:
            keys = self.input()
            current_time = pygame.time.get_ticks()
            time_passed = current_time - self.last_time
            self.last_time = current_time
            game_running = self.game.update(keys,time_passed)
            self.running = self.running and game_running
            self.game.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)
    
    def __del__(self):
        pygame.quit()
        
    def input(self):
        ''' get keyboard input
        
        Engine.input(): return list
        
        If the window is closed or the Escape button is pressed, the engine terminates itself.
        '''
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
        return pygame.key.get_pressed()
