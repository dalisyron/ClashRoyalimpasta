import pygame, selector, Util

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

GRASS_SURFACE     = pygame.image.load('Images/grass.png')
STONE_SURFACE     = pygame.image.load('Images/stone.png')
LIGHTWOOD_SURFACE = pygame.image.load('Images/lightwood.png')
DARKWOOD_SURFACE  = pygame.image.load('Images/darkwood.png')

img_surface = {'g':GRASS_SURFACE, 's':STONE_SURFACE, 'l':LIGHTWOOD_SURFACE, 'd':DARKWOOD_SURFACE}

mapMat = Util.buildGrid('map.txt')

TILE_WIDTH = 50
TILE_HEGIHT = 85

CARD_STACK_SIZE = 50

BOARD_WIDTH = TILE_WIDTH * len(mapMat[0]) + 2 * CARD_STACK_SIZE
BOARD_HEIGHT = TILE_WIDTH * len(mapMat)

def blitMap(d):
  for i in range(0, BOARD_HEIGHT, TILE_WIDTH):
      for j in range(CARD_STACK_SIZE, BOARD_WIDTH - CARD_STACK_SIZE, TILE_WIDTH):
        mat_row = i // TILE_WIDTH
        mat_col = (j // TILE_WIDTH) - 1
        tmp_image = img_surface[mapMat[mat_row][mat_col]]
        d.blit(tmp_image, (j, i - (TILE_HEGIHT - TILE_WIDTH)))

def blitLeftSelector(s, d):
  for i in range(len(s.card_list)):
    pygame.draw.rect(d, RED, (BOARD_WIDTH - CARD_STACK_SIZE, i * CARD_STACK_SIZE , CARD_STACK_SIZE, CARD_STACK_SIZE))

def blitRightSelector(s, d):
  for i in range(len(s.card_list)):
    pygame.draw.rect(d, GREEN, (0, i * CARD_STACK_SIZE , CARD_STACK_SIZE, CARD_STACK_SIZE))