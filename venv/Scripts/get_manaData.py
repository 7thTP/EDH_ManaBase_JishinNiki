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
    df_d = listToPD(dl)  # Reformat list
    deck = [nameToCardData(item['name'], cards) for index, item in df_d.iterrows()]  # Get deck card data
    df_mana = pd.DataFrame()
    for card in deck:
        df_mana.loc[card.name] = 0
        if card.mana_cost in ' ':
            mc_buf = card.mana_cost.split(' ')
            #いったんSpritはあとで
        else:
            mana = card.mana_cost.replace('{', '').replace('}', '')
            if df_mana.columns.values in mana: #既にある場合
                df_mana.at[card.name,mana] = 1
            else:
                df_mana[mana]=0
                df_mana.at[card.name, mana] = 1



def get_kingyo_DeckList(TP):
    dl = []
    with open(TP, "r", encoding='UTF-8') as file:
        for i in file:
            dl.append(i.rstrip('\n'))
    return dl


def listToPD(dl):  # MTG decklist format re-format ['number', 'name']
    dl2 = []
    for l in dl:
        dl2.append(l.split(' ', 1))
    dfDeck = pd.DataFrame(dl2, columns=['number', 'name'])
    return dfDeck


def nameToCardData(c_name, cards):
    if c_name:
        for card in cards:
            if '//' in card.name:  # Processing double-faced cards
                sName = card.name.split(' // ')
                if sName[0] == c_name or sName[1] == c_name:
                    return card
            elif card.name == c_name:  # Processing one-faced cards
                return card
        return 'not found'
    else:
        return 0


def manaAnalyze(mana_cost):


if __name__ == "__main__":
    main()
