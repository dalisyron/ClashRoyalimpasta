import Util, UI

mapMat = Util.buildGrid('map.txt')

class Grid:
  def __init__(self):
    self.height = len(mapMat)
    self.width = len(mapMat[0])
    self.mat = [[0 for j in range(self.width)] for i in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        if (mapMat[i][j] in ['d', 'l']):
          self.mat[i][j] = 1
  def get(self, r, c):
    return self.mat[r][c]
  def getCellByPixel(self, x, y):
    ret = (x - UI.CARD_STACK_SIZE) // UI.TILE_WIDTH, y // UI.TILE_WIDTH
    return ret

def updateGrid(g, hero_list):
  for i in range(g.height):
    for j in range(g.width):
      if (g.mat[i][j] != 1):
        g.mat[i][j] = 0
  for hero_listi in hero_list:
    for hero in hero_listi:
      g.mat[hero.position_y][hero.position_x] = hero
