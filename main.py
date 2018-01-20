import pygame, sys, time, random

from pygame.locals import *


pygame.init()

def buildGrid(dest):
  f = open(dest, 'r')
  f_str = f.read()
  return [list(x) for x in f_str.split('\n')][0:-1]

WHITE    = (255, 255, 255)

GRASS_SURFACE     = pygame.image.load('grass.png')
STONE_SURFACE     = pygame.image.load('stone.png')
LIGHTWOOD_SURFACE = pygame.image.load('lightwood.png')
DARKWOOD_SURFACE  = pygame.image.load('darkwood.png')

img_surface = {'g':GRASS_SURFACE, 's':STONE_SURFACE, 'l':LIGHTWOOD_SURFACE, 'd':DARKWOOD_SURFACE}

grid = buildGrid('map.txt')

TILE_WIDTH = 50
TILE_HEGIHT = 85

BOARD_WIDTH = TILE_WIDTH * len(grid[0])
BOARD_HEIGHT = TILE_WIDTH * len(grid)

print((BOARD_WIDTH, BOARD_HEIGHT))

def buildGrid(dest):
  f = open(dest, 'r')
  f_str = f.read()
  return [list(x) for x in f_str.split('\n')][0:-1]
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
    for i in range(0, BOARD_HEIGHT, TILE_WIDTH):
      for j in range(0, BOARD_WIDTH, TILE_WIDTH):
        mat_row = i // TILE_WIDTH
        mat_col = j // TILE_WIDTH
        tmp_image = img_surface[grid[mat_row][mat_col]]
        Display.blit(tmp_image, (j, i - (TILE_HEGIHT - TILE_WIDTH)))
    checkForQuit()
    pygame.display.update()
