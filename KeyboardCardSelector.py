import pygame

class CardPointer:
  def __init__(self, selector, grid):
    self.r = 0
    self.c = 0
    self.on_grid = False
    self.card_selector = selector
    self.grid = grid
  def down(self):
    if (self.on_grid == False):
      if (self.r < len(self.card_selector.card_list) - 1):
        self.r += 1
    else:
      if (self.r < self.grid.height - 3):
        self.r += 1
  def up(self):
    if (self.r > 0):
      self.r -= 1
  def right(self):
    if (self.on_grid == False):
      self.on_grid = True
  def left(self):
    if (self.on_grid == True):
      if (self.c > 0):
        self.c -= 1
      else:
        self.on_grid = False
  def right(self):
    if (self.on_grid == True):
      if (self.c < self.grid.width - 1):
        self.c += 1
    else:
      self.on_grid = True
