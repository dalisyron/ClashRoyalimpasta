import selector

def buildGrid(dest):
  f = open(dest, 'r')
  f_str = f.read()
  return [list(x) for x in f_str.split('\n')][0:-1]

def pointCollide(point, rect):
  if (point[0] > rect[0] and point[0] < rect[2] and point[1] > rect[1] and point[1] < rect[3]):
    return True
  else:
    return False

def getSelectorCard(x, y, selector_):
  for i in selector_.card_list:
    if (pointCollide((x, y), i.box)):
      return i
  return None
