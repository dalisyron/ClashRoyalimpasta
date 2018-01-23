import random, Data

names = ['Big_Hero', 'Knight']

class Card:
  def __init__(self, side_ = None, type_ = None):
    if side_ == None:
      side = random.choice([0, 1])
    if type_ == None:
      type_ = random.choice(names)
    self.card_type = type_
    self.side = side_
    self.image = Data.Heros_Dic[type_]["IMAGE"][side_]
    self.box = (0, 0, 0, 0)

def getRandomCard():
  return Card()