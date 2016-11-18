import pygame,time,random
from pygame.locals import *
import effects

clock = pygame.time.Clock()

COLOR=(0,224,250)

class HarryPotter(pygame.sprite.Sprite):  #Harry Potter (player)
    def __init__(self):
        super(HarryPotter, self).__init__()
        self.image=pygame.image.load("sprites/harrybase_right.png").convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.position=20,100
        self.health=100
        self.direction='right'
        
        
    def move(self, pressed_key):
        if pressed_key[K_w]:
            self.direction='up'
            self.rect.move_ip(0, -2.0)
        if pressed_key[K_s]:
            self.direction='down'
            self.rect.move_ip(0, 2.0)
        if pressed_key[K_a]:
            self.direction='left'
            self.rect.move_ip(-2.0, 0)
        if pressed_key[K_d]:
            self.direction='right'
            self.rect.move_ip(2.0, 0)

    def spellcast(self,pressed_keys,surf,spell):
        if self.direction=='right':
            for i in range(7):
                img=pygame.image.load("sprites/spellcast_right.png").convert()
                img.set_clip(pygame.Rect(22*i,0,21,44))
                self.image=img.subsurface(img.get_clip())
                self.image.set_colorkey((255, 255, 255), RLEACCEL)
                surf.blit(self.image,self.rect)
                pygame.display.update()
                clock.tick(20)
                self.image.fill(COLOR)
                surf.blit(self.image,self.rect)
                pygame.display.update()
                
            self.image=pygame.image.load("sprites/harrybase_right.png").convert()
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
                
        if self.direction=='left':
            for i in range(7):
                img=pygame.image.load("sprites/spellcast_left.png").convert()
                img.set_clip(pygame.Rect(21*i,0,22-i,44))
                self.image=img.subsurface(img.get_clip())
                self.image.set_colorkey((255, 255, 255), RLEACCEL)   
                surf.blit(self.image,self.rect)
                pygame.display.update()
                clock.tick(20)
                self.image.fill(COLOR)
                surf.blit(self.image,self.rect)
                pygame.display.update()
                
            self.image=pygame.image.load("sprites/harrybase_left.png").convert()
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
                            
        if self.direction=='up':
            for i in range(7):
                img=pygame.image.load("sprites/spellcast_up.png").convert()
                img.set_clip(pygame.Rect(21*i,0,21,44))
                self.image=img.subsurface(img.get_clip())
                self.image.set_colorkey((255, 255, 255), RLEACCEL)
                surf.blit(self.image,self.rect)
                pygame.display.update()
                clock.tick(20)
                self.image.fill(COLOR)
                surf.blit(self.image,self.rect)
                pygame.display.update()

            self.image=pygame.image.load("sprites/harrybase_up.png").convert()
            self.image.set_colorkey((255, 255, 255), RLEACCEL)

        if self.direction=='down':
            for i in range(6):
                img=pygame.image.load("sprites/spellcast_down.png").convert()
                img.set_clip(pygame.Rect(22*i,0,21,44))
                self.image=img.subsurface(img.get_clip())
                self.image.set_colorkey((255, 255, 255), RLEACCEL)
                surf.blit(self.image,self.rect)
                pygame.display.update()
                clock.tick(20)
                self.image.fill(COLOR)
                surf.blit(self.image,self.rect)
                pygame.display.update()

            self.image=pygame.image.load("sprites/harrybase_down.png").convert()
            self.image.set_colorkey((255, 255, 255), RLEACCEL)










class Ghost(pygame.sprite.Sprite):    #Ghost (enemy)
    def __init__(self):
        super(Ghost, self).__init__()
        self.image=pygame.image.load("sprites/ghost.png").convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(
            center=(random.randint(0,2)*350, random.randint(0,2)*250))
        self.health=200
        
    def move(self,target):
        a=random.randint(-1,1)
        velx=10
        vely=10
        self.rect.move_ip(velx*random.randint(-1,1),vely*random.randint(-1,1))
        
        if self.health==0:
            self.kill()











        
