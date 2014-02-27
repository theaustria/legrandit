import pygame
from pygame.locals import *
import game
pygame.init()

VERSION = "0.03"
FPS = 40
TITEL = "*TESTING* Legrandit %s" % VERSION
WINDOWSIZE = (500,500)

class Engine(object):
    '''
    The Engine manages keyboard input, game state, screen drawing, updating.
    '''
    def __init__(self):
        self.running = True
        self.state = 0
        self.screen = pygame.display.set_mode(WINDOWSIZE)
        pygame.display.set_caption(TITEL)
        self.clock = pygame.time.Clock()
        self.game = game.Game(WINDOWSIZE)
    
    def loop(self):
        ''' run the main game loop
        
        Engine.loop(): return None
        '''
        while self.running:
            keys = self.input()
            self.game.update(keys)
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
