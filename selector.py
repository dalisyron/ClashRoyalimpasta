import card, UI

class CardSelector:
  CARD_SIZE = 50
  def __init__(self, side_):
    self.side = side_
    self.card_list = []
  def addCard(self, card_ = None):
    card_.box = ((UI.BOARD_WIDTH - UI.CARD_STACK_SIZE) * card_.side, len(self.card_list) * UI.CARD_STACK_SIZE, 
                (UI.BOARD_WIDTH - UI.CARD_STACK_SIZE) * card_.side + UI.CARD_STACK_SIZE, (len(self.card_list) + 1) * (UI.CARD_STACK_SIZE))
    self.card_list.append(card_)