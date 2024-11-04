#!python3

"""
Strings are iterable.  Use for loops to iterate through both strings to create a list to represent a deck of cards. 
Note: We can also use list comprehension as strings are still iterable!
"""

ranks = "A23456789TJQK"
suits = "CDHS"

def createDeck():
  CARD_LIST = []
  for suit in suits:
    for rank in ranks:
        CARD = rank + suit
        CARD_LIST += [CARD] 
  print(CARD_LIST)

  assert "AS" in CARD_LIST
  assert "KC" in CARD_LIST
  assert CARD_LIST.count("TC") == 1
  
if __name__ == "__main__":
  createDeck()

#DONE