import pygame
import pygame.gfxdraw
from pygame import *

pygame.init()

WHITE = (255, 255, 255)

display = pygame.display.set_mode((600, 600))

pygame.gfxdraw.pie(display, 100, 100, 10, 0, 60, (255, 255, 0))

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
  display.fill(WHITE)
  checkForQuit()
