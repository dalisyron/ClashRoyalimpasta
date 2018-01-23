import pygame, UI, sys, time, random, grid, card

from pygame.locals import *
from UI import *

pygame.init()

Display = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
Grid = grid.Grid()
Selector = [selector.CardSelector(0), selector.CardSelector(1)]
Heroes = [[], []]

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

def updateUI():
    UI.blitMap(Display)
    UI.blitLeftSelector(Selector[0], Display)
    UI.blitRightSelector(Selector[1], Display)

def init():
    for i in range(4):
        Selector[0].addCard(card.Card(side_ = 0))
        Selector[1].addCard(card.Card(side_ = 1))

init()

while True:
    Display.fill(WHITE)
    updateUI()
    checkForQuit()
    for event in pygame.event.get():
        if event.mouse
    pygame.display.update()