import pandas as pd
import numpy as np
from mtgsdk import Card
import pickle

def main():

    TP = r'C:\temp\Deck - Gipsy Danger.txt'
    print('input data path')
    dl = get_kingyo_DeckList(TP)
    df_d=set_ListToPD(dl) #Reformat list
    for index, item in df_d.iterrows():
        manaCost = get_manaCost(item['name'])
        print(item['name'],manaCost)

def get_kingyo_DeckList(TP):
    dl = []
    with open(TP, "r",encoding='UTF-8') as file:
        for i in file:
            dl.append(i.rstrip('\n'))
    return dl


def set_ListToPD(dl):   #MTG decklist format re-format ['number', 'name']
    dl2 = []
    for l in dl:
        dl2.append(l.split(' ', 1))
    dfDeck = pd.DataFrame(dl2, columns=['number', 'name'])
    print('get deck')
    return dfDeck


def get_manaCost(c_name):
    if c_name:
        cards = Card.where(name=c_name).all()
        if cards[0].mana_cost:
            return cards[0].mana_cost
        else:
            return '{0}'
    else:
        return 0
def get_deck(c_name):


if __name__ == "__main__":
    main()
