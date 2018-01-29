import pygame, UI, sys, time, random, grid, card, Hero,Bullet,startMode
from PIL import Image, ImageDraw
from pygame.locals import *
from UI import *


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
GREY  = (138, 128, 128)
YELLOW =( 255, 255, 0  )
BLUE  = (  0,   0, 255)
LIGHT_YELLOW = (255, 255, 204)
YELLOW       = (255, 255,   0)

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

def main(d,winBool):

    selectedItem = None

    X, Y = pygame.mouse.get_pos()
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    w,h = d.get_size()

    if winBool == True :
        str = "Right Player Won the Game"
    else:
        str = "Left Player Won the Game"

    textSurfaceObj1 = fontObj.render(str, True, GREEN, BLUE)
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (w//2, h//3 + h//6)

    textSurfaceObj2 = fontObj.render('Quit', True, GREEN, BLUE)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (w//2, 2 * h//3)

    def check():
        selectedItem = None
        selectionColor = RED



        if textRectObj2.collidepoint(X , Y):
            pygame.draw.rect(d,selectionColor,(textRectObj2.left - 5 , textRectObj2.top -5 , textRectObj2.width+10 , textRectObj2.height+10) , 4)
            selectedItem=2

        return selectedItem


    while True:

        X, Y = pygame.mouse.get_pos()
        d.fill(LIGHT_YELLOW)
        d.blit(textSurfaceObj1, textRectObj1)
        d.blit(textSurfaceObj2, textRectObj2)
        check()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP :
                if check() == 2:
                    terminate()
        checkForQuit()
        pygame.display.update()


