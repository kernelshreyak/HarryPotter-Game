import characters
import effects
import pygame,math
from pygame.locals import *

clock = pygame.time.Clock()
FPS = 60

COLOR=(0,224,250)

# Global Initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Harry Potter Game v2')

ADDGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(ADDGHOST, 1000)

player=characters.HarryPotter()
ghost=characters.Ghost()

everything=pygame.sprite.Group()
spells=pygame.sprite.Group()
enemies=pygame.sprite.Group()

everything.add(player)


run=True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run= False
        elif event.type == QUIT:
            run = False
        elif event.type==ADDGHOST:
            new_ghost=characters.Ghost()
            enemies.add(new_ghost)
            everything.add(new_ghost)
        
    keypress=pygame.key.get_pressed()
    
    direction=player.move(keypress)
 
    
    if keypress[K_g]:
        spell=effects.spell1(player)
        player.spellcast(keypress,screen,spell)
        spells.add(spell)
        everything.add(spell)
        spell.cast(player.direction)
        
    deltat = clock.tick(FPS)
    
    screen.fill(COLOR)


    for i in everything:
        screen.blit(i.image, i.rect)
        
    for k in spells:
        k.move()
        
    for j in enemies:
        j.move(player)
        if pygame.sprite.spritecollideany(j,spells):
            j.health-=50


    if pygame.sprite.spritecollideany(player,enemies):
        print("Harry is HIT!")
        player.health -= 20

    if player.health==0:
        print("Harry is DEAD!!! Resetting....")
        player.health = 100
        
    pygame.display.flip()
    
