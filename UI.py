import pygame, selector, Util, Data, Hero

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
LIGHT_YELLOW = (255, 255, 204)

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
    c = s.card_list[i]
    d.blit(c.image, (0, i * CARD_STACK_SIZE))
    pygame.draw.rect(d, BLACK, (c.box[0], c.box[1], c.box[2] - c.box[0], c.box[3] - c.box[1]), 4)

def blitRightSelector(s, d):
  for i in range(len(s.card_list)):
    c = s.card_list[i]
    d.blit(c.image, (BOARD_WIDTH - CARD_STACK_SIZE, CARD_STACK_SIZE * i))
    pygame.draw.rect(d, BLACK, (c.box[0], c.box[1], c.box[2] - c.box[0], c.box[3] - c.box[1]), 4)

def blitGrid(g, d):
  for i in range(len(g.mat)):
    for j in range(len(g.mat[0])):
      if (type(g.mat[i][j]) == Hero.Hero):
        d.blit(Data.Heros_Dic[g.mat[i][j].name]["IMAGE"][g.mat[i][j].side], (CARD_STACK_SIZE + (j * TILE_WIDTH), i * TILE_WIDTH - TILE_WIDTH // 4))



#-------Bayad bezanim


def blitBullets(currentBullets,d):
  pass