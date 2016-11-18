import pygame
from pygame.locals import *

clock = pygame.time.Clock()

COLOR=(0,224,250)

class spell1(pygame.sprite.Sprite):
    def __init__(self,sprite):
        super(spell1, self).__init__()
        self.x=sprite.rect.x
        self.y=sprite.rect.y-10
        self.image=pygame.image.load("sprites/spell.png").convert()
        self.rect=self.image.get_rect(center=(self.x,self.y))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.velx=5
        self.vely=5
        self.A=(0,0)
        
    def cast(self,head):
        if head=='right':
            self.A=(1,0)
        if head=='left':
            self.A=(-1,0)
        if head=='up':
            self.A=(0,-1)
        if head=='down':
            self.A=(0,1)

    def move(self):
        self.rect.move_ip(self.velx*self.A[0],self.vely*self.A[1])
                
        if self.rect.right > 800 or self.rect.right < 0 or self.rect.top > 600 or self.rect.top <0:
            self.kill()
        pygame.display.update()
