import pygame
from pygame.locals import *
        
class Player (pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.dir = [0,0]
        self.velocity = 5
        self.range = 25
        self.cooldown = 0
        self.attack_rect = AttackRect()
        
    def update(self,time_passed):
        self.rect.move_ip(self.dir)
        self.cooldown -= time_passed
        
    def set_dir(self,wasd):
        if wasd[0] != wasd[2]:
            if wasd[0]:
                self.dir[1] = -self.velocity
            else:
                self.dir[1] = self.velocity
        else:
            self.dir[1] = 0
        if wasd[1] != wasd[3]:
            if wasd[1]:
                self.dir[0] = -self.velocity
            else:
                self.dir[0] = self.velocity
        else:
            self.dir[0] = 0

    def undo(self):
        self.rect.move_ip(-self.dir[0],-self.dir[1])
      
    def teleport(self,pos):
        self.rect.topleft = pos
        
    def recoil(self):
        self.undo()
        
    def draw(self,screen):
        #screen.fill((50,50,50), self.attack_rect.rect)
        screen.blit(self.image,self.rect)
        
    def attack(self,keys):
        self.attack_rect.rect = self.rect.copy()
        if not self.cooldown > 0:
            if keys[0] != keys[2]:
                if keys[0]:
                    self.attack_rect.rect.top -= self.range
                else:
                    self.attack_rect.rect.bottom += self.range
            if keys[1] != keys[3]:
                if keys[1]:
                    self.attack_rect.rect.left -= self.range
                else:
                    self.attack_rect.rect.right += self.range
            
            self.cooldown = 500
            
class AttackRect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0,0,0,0)
