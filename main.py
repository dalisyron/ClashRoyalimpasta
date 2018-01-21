import pygame, sys, time, random

from pygame.locals import *
from UI import *

pygame.init()

Display = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

while True:
    Display.fill(WHITE)
    UI.blitBackground(Display)
    checkForQuit()
    pygame.display.update()