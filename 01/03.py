
# * <https://baike.baidu.com/item/%E8%8A%B1%E8%89%B2/15500441>

# * 黑桃（spades），方块（diamonds）梅花（clubs），红桃（hearts）

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [ Card(rank, suit) for suit in self.suits
                                     for rank in self.ranks]
    
  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]
  
if __name__ == '__main__':
  deck = FrenchDeck()
  print(len(deck))
  print(choice(deck))