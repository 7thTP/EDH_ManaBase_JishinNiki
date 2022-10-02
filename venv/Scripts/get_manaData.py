import pandas as pd
import numpy as np
from mtgsdk import Card
import pickle


def main():
    # open cardlist.bin
    with open('cardlist.bin', 'rb') as f:
        cards = pickle.load(f)
    # inport deck data
    TP = r'C:\temp\Deck - Gipsy Danger.txt'
    print('input data path')
    dl = get_kingyo_DeckList(TP)  # get Kingyo format data
    df_d = set_ListToPD(dl)  # Reformat list

    for index, item in df_d.iterrows():
        manaCost = get_manaCost(item['name'],cards)
        print(item['name'], manaCost)


def get_kingyo_DeckList(TP):
    dl = []
    with open(TP, "r", encoding='UTF-8') as file:
        for i in file:
            dl.append(i.rstrip('\n'))
    return dl


def set_ListToPD(dl):  # MTG decklist format re-format ['number', 'name']
    dl2 = []
    for l in dl:
        dl2.append(l.split(' ', 1))
    dfDeck = pd.DataFrame(dl2, columns=['number', 'name'])
    print('get deck')
    return dfDeck


def get_manaCost(c_name,cards):
    if c_name:
        for card in cards:
            if card.name == c_name:
                if card.mana_cost:
                    return card.mana_cost
                else:
                    return '{0}'
    else:
        return 0




if __name__ == "__main__":
    main()
