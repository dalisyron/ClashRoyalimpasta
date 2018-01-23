import random, Data

names = ['Big_Hero', 'Knight']

class Card:
  def __init__(self, side_ = None, name_ = None):
    if side_ == None:
      side = random.choice([0, 1])
    if name_ == None:
      name_ = random.choice(names)
    self.name = name_
    self.side = side_
    self.image = Data.Heros_Dic[name_]["IMAGE"][side_]
    self.box = (0, 0, 0, 0)

def getRandomCard():
  return Card()