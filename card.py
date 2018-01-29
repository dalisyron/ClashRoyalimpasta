import random, Data

names = ['Soldier', 'Knight', 'Viking', 'Zombie', 'Ninja']

class Card:
  def __init__(self, side_ = None, name_ = None):
    if side_ == None:
      side_ = random.choice([0, 1])
    if name_ == None:
      name_ = random.choice(names)
    self.av_time = -100000000 #WORLD CREATION TIME?
    self.remaining_time = 0
    self.reload_time = Data.Heros_Dic[name_]["LOADTIME"]
    self.name = name_
    self.side = side_
    self.image = Data.Heros_Dic[name_]["IMAGE"][side_]
    self.box = (0, 0, 0, 0)
  def available(self):
    return remaining_time == 0

def getRandomCard():
  return Card()
