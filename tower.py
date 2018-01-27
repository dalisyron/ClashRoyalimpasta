import Data

class Tower:
  def __init__(self, name, side, pos):
    self.name = name
    self.side = side
    tower_data = Data.tower_dic[name]
    self.health = tower_data["HEALTH"]
    #here pos refers to the lower left point of the rectangle
    #instead of the usual upper-left point in order to avoid collision with other UI elements
    self.pos = pos
    self.image = tower_data["IMAGE"][side]