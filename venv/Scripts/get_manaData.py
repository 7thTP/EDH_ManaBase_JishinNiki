import pandas as pd
import numpy as np
from mtgsdk import Card
import pickle
import re


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
    df_mana = pd.DataFrame(index=[], columns=['number'])
    for card in deck:
        df_mana.loc[card.name] = 0
        if '//' in card.name:  # Trap double-faced cards
            dfc = splitDoubleFaceCard(card.name)
            df_mana.at[card.name, 'number'] = df_d.at[df_d.index[df_d['name'] == dfc[0]].tolist()[0], 'number']
        else:
            df_mana.at[card.name, 'number'] = df_d.at[df_d.index[df_d['name'] == card.name].tolist()[0], 'number']
        if card.mana_cost:
            for mana in manaSplit(card.mana_cost):
                if mana in df_mana.columns.values:  # 既にある場合
                    df_mana.at[card.name, mana] += 1
                else:
                    df_mana[mana] = 0
                    df_mana.at[card.name, mana] += 1
    print(df_mana)
    printSumMana(df_mana)


def printSumMana(df):
    for cl in df.columns[1:]:
        print('{}: {}'.format(cl, df[cl].sum()))
    return


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
                dfc = splitDoubleFaceCard(card.name)
                if c_name in dfc:
                    return card
            elif card.name == c_name:  # Processing one-faced cards
                return card
        return 'not found'
    else:
        return 0


def manaSplit(manaCost):
    op = []
    gm = 0
    manas = re.findall("(?<=\{).+?(?=\})", manaCost)
    for mana in manas:
        if mana.isdigit():
            gm = int(mana)
        else:
            op.append(mana)
    if gm:
        op[0:0] = ['GM'] * gm
    return op


def splitDoubleFaceCard(name):
    return name.split(' // ')


if __name__ == "__main__":
    main()
