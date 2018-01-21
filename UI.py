import pygame, Util

WHITE    = (255, 255, 255)

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

def blitBackground(d):
  for i in range(0, BOARD_HEIGHT, TILE_WIDTH):
      for j in range(CARD_STACK_SIZE, BOARD_WIDTH - CARD_STACK_SIZE, TILE_WIDTH):
        mat_row = i // TILE_WIDTH
        mat_col = (j // TILE_WIDTH) - 1
        tmp_image = img_surface[mapMat[mat_row][mat_col]]
        d.blit(tmp_image, (j, i - (TILE_HEGIHT - TILE_WIDTH)))