import mtgsdk
import pandas as pd
import numpy as np
from mtgsdk import Card


def main():
    TP = r'C:\temp\Deck - Gipsy Danger.txt'
    print('input data path')
    dl = get_kingyo_DeckList(TP)
    set_ListToPD(dl)

def get_kingyo_DeckList(TP):
    f = open(TP, 'r', encoding='UTF-8')
    dl = f.readlines()
    f.close()
    print('fech decklist')
    return dl


def set_ListToPD(dl):
    dl2 =[]
    for l in dl:
        dl2.append(l.split(' ',1))
    dfDeck = pd.DataFrame(dl2)
    print('get deck')
    return dfDeck
if __name__ == "__main__":
    main()

cards = Card.where(name='Bloodbraid Elf').all()
print(cards[0].mana_cost)
