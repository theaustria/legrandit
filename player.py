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
        self.damage = 1
        self.health = 5
        self.money = 0
        self.cooldown = 300
        self.cooldowntime = 0
        self.attack_rect = AttackRect()
        
    def update(self,keys,time_passed):
        # set the player's attack rect
        arrowkeys = (keys[K_UP],keys[K_LEFT],keys[K_DOWN],keys[K_RIGHT])
        self.attack(arrowkeys)
        # set the player's direction
        wasd = (keys[K_w], keys[K_a], keys[K_s], keys[K_d])
        self.set_dir(wasd)
        # move the player
        self.rect.move_ip(self.dir)
        # reduce cooldowntime
        self.cooldowntime -= time_passed
        
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
        if [True for key in keys if key]:
            if not self.cooldowntime > 0:
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
                
                self.cooldowntime = self.cooldown
            
class AttackRect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0,0,0,0)
