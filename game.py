import pygame, UI, sys, time, random, grid

from pygame.locals import *
from UI import *

pygame.init()

Display = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
Grid = grid.Grid()
Selector = [selector.CardSelector(), selector.CardSelector()]

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
    UI.blitMap(Display)
    UI.blitRightSelector(Selector[0], Display)
    UI.blitLeftSelector(Selector[1], Display)
    checkForQuit()
    pygame.display.update()