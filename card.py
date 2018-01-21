import random, Data

names = ['Big_Hero', 'Knight']

class Card:
  def __init__(self, t = names[random.randint(0, len(names) - 1)]):
    self.card_type = t
    self.image = Data.Heros_Dic[t]["IMAGE"]