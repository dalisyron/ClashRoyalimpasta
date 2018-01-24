import pygame, UI, sys, time, random, grid, card, Hero

from pygame.locals import *
from UI import *

pygame.init()
pygame.display.set_caption('Clash Impasta')

Display = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
Grid = grid.Grid()
Selector = [selector.CardSelector(0), selector.CardSelector(1)]

currentHeros = [[], []]
currentBullets = []

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

def addHero(x,y,Name,Side):
    new_hero = Hero.Hero(x,y,Name,Side)
    currentHeros[Side].append(new_hero)
    Grid.mat[y][x] = new_hero

def updateUI():
    UI.blitMap(Display)
    UI.blitLeftSelector(Selector[0], Display)
    UI.blitRightSelector(Selector[1], Display)
    UI.blitGrid(Grid, Display)

def init():
    for i in range(4):
        Selector[0].addCard(card.Card(side_ = 0))
        Selector[1].addCard(card.Card(side_ = 1))

init()

mouseX, mouseY = 0, 0
dX, dY = 0, 0

mouseClicked = False

selected_card = None

cnt = 0

while True:
    cnt += 1
    if cnt % 100 == 0:
        for i in Grid.mat:
            print(i)
    Display.fill(WHITE)
    updateUI()
    checkForQuit()
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            mouseClicked = True
            selected_card = selector.getSelectorCard(mouseX, mouseY, Selector[0])
            if selected_card == None:
                selected_card = selector.getSelectorCard(mouseX, mouseY, Selector[1])
            if (selected_card != None):
                dX, dY = mouseX - selected_card.box[0], mouseY - selected_card.box[1]
            #print(selected_card)
        elif event.type == MOUSEBUTTONUP:
            pos = Grid.getCellByPixel(mouseX, mouseY)
            if (selected_card != None):
                addHero(pos[0], pos[1], selected_card.name, selected_card.side)
            mouseClicked = False
            selected_card = None
    if mouseClicked == True and selected_card != None:
        Display.blit(selected_card.image, (mouseX - dX, mouseY - dY))
    pygame.display.update()