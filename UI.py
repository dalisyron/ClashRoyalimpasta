import pygame, UI, Util

WHITE    = (255, 255, 255)

GRASS_SURFACE     = pygame.image.load('grass.png')
STONE_SURFACE     = pygame.image.load('stone.png')
LIGHTWOOD_SURFACE = pygame.image.load('lightwood.png')
DARKWOOD_SURFACE  = pygame.image.load('darkwood.png')

img_surface = {'g':GRASS_SURFACE, 's':STONE_SURFACE, 'l':LIGHTWOOD_SURFACE, 'd':DARKWOOD_SURFACE}

grid = Util.buildGrid('map.txt')

TILE_WIDTH = 50
TILE_HEGIHT = 85

BOARD_WIDTH = TILE_WIDTH * len(grid[0])
BOARD_HEIGHT = TILE_WIDTH * len(grid)

def blitBackground(d):
  for i in range(0, BOARD_HEIGHT, TILE_WIDTH):
      for j in range(0, BOARD_WIDTH, TILE_WIDTH):
        mat_row = i // TILE_WIDTH
        mat_col = j // TILE_WIDTH
        tmp_image = img_surface[grid[mat_row][mat_col]]
        d.blit(tmp_image, (j, i - (TILE_HEGIHT - TILE_WIDTH)))