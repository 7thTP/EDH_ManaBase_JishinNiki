import pickle
from mtgsdk import Card
cards = Card.all()
# output bin file
with open('cardlist.bin', 'wb') as f:
    pickle.dump(cards, f)
