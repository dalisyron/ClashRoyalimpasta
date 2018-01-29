import pygame, selector, Util, Data, Hero
from PIL import Image, ImageDraw

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
GREY  = (138, 128, 128)
YELLOW =( 255, 255, 0  )
BLUE  = (  0,   0, 255)
LIGHT_YELLOW = (255, 255, 204)
YELLOW       = (255, 255,   0)

TILE_WIDTH = 50
TILE_HEGIHT = 85

GRASS_SURFACE      = pygame.image.load('Images/grass.png')
STONE_SURFACE      = pygame.image.load('Images/stone.png')
LIGHTWOOD_SURFACE  = pygame.image.load('Images/lightwood.png')
DARKWOOD_SURFACE   = pygame.image.load('Images/darkwood.png')
TALL_TREE_SURFACE  = pygame.image.load('Images/Tree_Tall.png')
SHORT_TREE_SURFACE = pygame.image.load('Images/Tree_Short.png')
TALL_TOWER         = pygame.image.load('Images/tall_tower.png')
SMALL_TOWER        = pygame.image.load('Images/small_tower.png')
KEYBOARD_SELECTOR  = pygame.Surface((TILE_WIDTH, TILE_WIDTH))

KEYBOARD_SELECTOR.fill(RED)

img_surface = {'g':GRASS_SURFACE, 's':STONE_SURFACE, 'l':LIGHTWOOD_SURFACE, 'd':DARKWOOD_SURFACE,
               't':SHORT_TREE_SURFACE, 'T':TALL_TREE_SURFACE, 'B':TALL_TOWER, 'S':SMALL_TOWER, 
               'P':TALL_TOWER, 'Q':SMALL_TOWER}

mapMat = Util.buildGrid('map.txt')
decMat = Util.buildGrid('decorations.txt')

CARD_STACK_SIZE = 50

BOARD_WIDTH = TILE_WIDTH * len(mapMat[0]) + 2 * CARD_STACK_SIZE
BOARD_HEIGHT = TILE_WIDTH * len(mapMat)

def blitAlpha(target, source, location, opacity):
  x = location[0]
  y = location[1]
  temp = pygame.Surface((source.get_width(), source.get_height())).convert()
  temp.blit(target, (-x, -y))
  temp.blit(source, (0, 0))
  temp.set_alpha(opacity)        
  target.blit(temp, location)

def blitKeyboardSelector(ks, d):
  if (ks.on_grid):
    blitAlpha(d, KEYBOARD_SELECTOR, (ks.c * TILE_WIDTH + CARD_STACK_SIZE, ks.r * TILE_WIDTH + (TILE_HEGIHT - TILE_WIDTH)), 80)
  else:
    blitAlpha(d, KEYBOARD_SELECTOR, (ks.c * TILE_WIDTH, ks.r * TILE_WIDTH), 80)


def buildBackground():
  background_surface = pygame.Surface([BOARD_WIDTH,BOARD_HEIGHT], pygame.SRCALPHA, 32)
  background_surface = background_surface.convert_alpha()
  for i in range(0, BOARD_HEIGHT, TILE_WIDTH):
    for j in range(CARD_STACK_SIZE, BOARD_WIDTH - CARD_STACK_SIZE, TILE_WIDTH):
      mat_row = i // TILE_WIDTH
      mat_col = (j // TILE_WIDTH) - 1
      tmp_image = img_surface[mapMat[mat_row][mat_col]]
      background_surface.blit(tmp_image, (j, i - (TILE_HEGIHT - TILE_WIDTH)))
  return background_surface

def blitBackground(background_surface, d):
  d.blit(background_surface, (CARD_STACK_SIZE, 0))

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

def drawPie(d, r, angle, center):

  pil_size = r
  pil_image = Image.new("RGBA", (pil_size, pil_size))
  pil_draw = ImageDraw.Draw(pil_image)
  pil_draw.pieslice((0, 0, pil_size-1, pil_size-1), angle, 0, fill=GREY)
  mode = pil_image.mode
  size = pil_image.size
  data = pil_image.tobytes()
  image = pygame.image.fromstring(data, size, mode)
  d.blit(image, center)

def blitLeftSelector(s, d, tm):
  for i in range(len(s.card_list)):
    c = s.card_list[i]
    d.blit(c.image, (0, i * CARD_STACK_SIZE))
    pygame.draw.rect(d, BLACK, (c.box[0], c.box[1], c.box[2] - c.box[0], c.box[3] - c.box[1]), 4)
    val = int(((tm - c.av_time) / c.reload_time) * 360)
    if (val >= 360):
      val = 0
    drawPie(d, CARD_STACK_SIZE, val, ((c.box[0]), (c.box[1])))

def blitRightSelector(s, d, tm):
  for i in range(len(s.card_list)):
    c = s.card_list[i]
    d.blit(c.image, (BOARD_WIDTH - CARD_STACK_SIZE, CARD_STACK_SIZE * i))
    pygame.draw.rect(d, BLACK, (c.box[0], c.box[1], c.box[2] - c.box[0], c.box[3] - c.box[1]), 4)
    val = int(((tm - c.av_time) / c.reload_time) * 360)
    if (val >= 360):
      val = 0
    drawPie(d, CARD_STACK_SIZE, val, ((c.box[0]), (c.box[1])))

def blitGrid(g, d):
  for i in range(len(g.mat)):
    for j in range(len(g.mat[0])):
      if (type(g.mat[i][j]) == Hero.Hero):
        health = (g.mat[i][j].health / Data.Heros_Dic[g.mat[i][j].name]["HEALTH"])
        if health >= 0.65:
          color = GREEN
        if health < 0.65:
          color = YELLOW
        if health <= 0.25:
          color =RED
        d.blit(Data.Heros_Dic[g.mat[i][j].name]["IMAGE"][g.mat[i][j].side], (CARD_STACK_SIZE + (j * TILE_WIDTH), i * TILE_WIDTH - TILE_WIDTH // 4))
        k = 1
        if g.mat[i][j].is_tower == True:
          k += 1
        pygame.draw.rect(d,color,( CARD_STACK_SIZE + (j * TILE_WIDTH) , i * TILE_WIDTH - TILE_WIDTH // 4 ,health*TILE_WIDTH*k,4))



#-------Bayad bezanim
#+++++++ok dadash faghat yezare yavash tar


def blitBullets(currentBullets,d):
  for bullet in currentBullets:
    if bullet.is_destroyed == False :
      pygame.draw.circle(d,(0,0,0),(int(bullet.position_x) , int(bullet.position_y)),6,3)

def blitTimer(d,time):
  time //= 1000
  minute = str(time // 60)
  second = str(time % 60)
  timeStr = minute + ":" + second
  fontObj = pygame.font.Font('freesansbold.ttf', 33)
  textSurfaceObj = fontObj.render(timeStr, True, GREEN, BLUE)
  textRectObj = textSurfaceObj.get_rect()
  w, h = d.get_size()
  textRectObj.center = (w//2,h - 20)
  d.blit(textSurfaceObj,textRectObj)
