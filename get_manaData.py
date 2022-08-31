import mtgsdk
from mtgsdk import Card

cards = Card.where(name = 'Bloodbraid Elf').all()
print(cards[0].mana_cost)