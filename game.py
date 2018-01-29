import pygame, UI, sys, time, random, grid, card, Hero,Bullet,startMode, KeyboardCardSelector
from PIL import Image, ImageDraw
from pygame.locals import *
from UI import *

pygame.init()
pygame.display.set_caption('Clash Impasta')

Display = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
Grid = grid.Grid()
Selector = [selector.CardSelector(0), selector.CardSelector(1)]
CardPointer = KeyboardCardSelector.CardPointer(Selector[0], Grid)

currentHeros = [[], []]
currentBullets = []
error_sound = pygame.mixer.Sound('Sounds/badswap.wav')

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

def addHero(x,y,Name,Side,is_tower):
    new_hero = Hero.Hero(x,y,Name,Side,is_tower)
    currentHeros[Side].append(new_hero)
    Grid.mat[y][x] = new_hero

background_surface = UI.buildBackground()

def updateUI():
    Display.blit(background_surface, (0, 0))
    UI.blitLeftSelector(Selector[0], Display, pygame.time.get_ticks())
    UI.blitRightSelector(Selector[1], Display, pygame.time.get_ticks())
    UI.blitGrid(Grid, Display)
    UI.blitKeyboardSelector(CardPointer, Display)
    #new
    UI.blitBullets(currentBullets,Display)
    UI.blitDecorations(Display)

def init():
    for i in range(4):
        Selector[0].addCard(card.Card(side_ = 0))
        Selector[1].addCard(card.Card(side_ = 1))
    addHero(0,  2, "Small_Tower", 0, True)
    addHero(0,  5, "Big_Tower",   0, True)
    addHero(0, 10, "Small_Tower", 0, True)

    addHero(19,  2, "Small_Tower", 1, True)
    addHero(19,  5, "Big_Tower",   1, True)
    addHero(19, 10, "Small_Tower", 1, True)

def errorSound():
    error_sound.play()

init()

mouseX, mouseY = 0, 0
dX, dY = 0, 0

mouseClicked = False

selected_card = None

cnt = 0

clock = pygame.time.Clock()
clock.tick(60)

isGameStarted = False
if isGameStarted == False:
    startMode.main(Display)

# 0 ------> player vs player
# 1 ------> player vs computer

while True:
    cnt += 1
    Display.fill(LIGHT_YELLOW)
    updateUI()
    checkForQuit()
    mouseX, mouseY = pygame.mouse.get_pos()
    Hero.herosProcess(Grid,currentHeros, currentBullets, cnt)
    Bullet.bulletsProcess(Grid,currentBullets)
    grid.updateGrid(Grid, currentHeros)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            mouseClicked = True
            selected_card = selector.getSelectorCard(mouseX, mouseY, Selector[0])
            if selected_card == None:
                selected_card = selector.getSelectorCard(mouseX, mouseY, Selector[1])
            if (selected_card != None):
                dX, dY = mouseX - selected_card.box[0], mouseY - selected_card.box[1]
                if (pygame.time.get_ticks() - selected_card.av_time > Data.Heros_Dic[selected_card.name]["LOADTIME"]):
                    selected_card.av_time = pygame.time.get_ticks()
                else:
                    selected_card = None

            #print(selected_card)
        elif event.type == MOUSEBUTTONUP:
            pos = Grid.getCellByPixel(mouseX, mouseY)
            if (pos[1] >= Grid.height or pos[0] >= Grid.width or pos[1] < 0 or pos[0] < 0):
                errorSound()
                mouseClicked = False
                selected_card = None
            if (selected_card != None):
                if (Grid.get(pos[1], pos[0]) == 0 and ((selected_card.side == 0 and pos[0] < Grid.width // 2) or (selected_card.side == 1 and pos[0] >= Grid.width // 2))):
                    addHero(pos[0], pos[1], selected_card.name, selected_card.side, False)
                else:
                    errorSound()
            mouseClicked = False
            selected_card = None
        elif event.type == KEYDOWN:
          if (event.key == K_DOWN):
            CardPointer.down()
          elif (event.key == K_UP):
            CardPointer.up()
          elif (event.key == K_RIGHT):
            CardPointer.right()
          elif (event.key == K_LEFT):
            CardPointer.left()
    if mouseClicked == True and selected_card != None:
        Display.blit(selected_card.image, (mouseX - dX, mouseY - dY))
    pygame.display.update()