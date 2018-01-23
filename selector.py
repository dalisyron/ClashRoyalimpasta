import card

class CardSelector:
  CARD_SIZE = 50
  def __init__(self, side_):
    self.side = side_
    self.card_list = []
  def addCard(self, card_ = None):
    self.card_list.append(card_)