__author__ = 'akmishra'

import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window

infoObject = pygame.display.Info()
DISPLAYSURF=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),0,32)
 #= pygame.display.set_mode((1900, 1080), 0, 32)
pygame.display.set_caption('Twinkle')

WHITE = (255, 255, 255)
BLACK=(0,0,0)
#starImg = pygame.image.load('newstar.png')
#spaceimg= pygame.image.load('space.jpg')
#starImg1=pygame.image.load('newstar1.png')

#s/5t2=a
stary = infoObject.current_h/2
starx = infoObject.current_w/2
direction = 'down'
num=1

while True:
    DISPLAYSURF.fill(BLACK)
    pygame.draw.circle(DISPLAYSURF, WHITE,(starx,stary ), 115, 0 )# the main game loop
    stary-=15
    starx-+5


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
