import pygame, selector, Util, Data, Hero

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
LIGHT_YELLOW = (255, 255, 204)

GRASS_SURFACE      = pygame.image.load('Images/grass.png')
STONE_SURFACE      = pygame.image.load('Images/stone.png')
LIGHTWOOD_SURFACE  = pygame.image.load('Images/lightwood.png')
DARKWOOD_SURFACE   = pygame.image.load('Images/darkwood.png')
TALL_TREE_SURFACE  = pygame.image.load('Images/Tree_Tall.png')
SHORT_TREE_SURFACE = pygame.image.load('Images/Tree_Short.png')
TALL_TOWER         = pygame.image.load('Images/tall_tower.png')
SMALL_TOWER        = pygame.image.load('Images/small_tower.png')

img_surface = {'g':GRASS_SURFACE, 's':STONE_SURFACE, 'l':LIGHTWOOD_SURFACE, 'd':DARKWOOD_SURFACE,
               't':SHORT_TREE_SURFACE, 'T':TALL_TREE_SURFACE, 'B':TALL_TOWER, 'S':SMALL_TOWER, 
               'P':TALL_TOWER, 'Q':SMALL_TOWER}

mapMat = Util.buildGrid('map.txt')
decMat = Util.buildGrid('decorations.txt')

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

def blitDecorations(d):
  for i in range(0, BOARD_HEIGHT, TILE_WIDTH):
      for j in range(CARD_STACK_SIZE, BOARD_WIDTH - CARD_STACK_SIZE, TILE_WIDTH):
        mat_row = i // TILE_WIDTH
        mat_col = (j // TILE_WIDTH) - 1
        if (decMat[mat_row][mat_col] != '0'):
          dec_image = img_surface[decMat[mat_row][mat_col]]
          d.blit(dec_image, (j, i - (TILE_HEGIHT - TILE_WIDTH)))

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
#+++++++ok dadash faghat yezare yavash tar


def blitBullets(currentBullets,d):
  for bullet in currentBullets:
    if bullet.is_destroyed == False :
      pygame.draw.circle(d,(0,0,0),(int(bullet.position_x) , int(bullet.position_y)),6,3)
