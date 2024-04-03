from curses import COLOR_YELLOW
from itertools import combinations
from lib.game import Game
from lib.card import Card, Deck
from time import perf_counter
import pandas as pd
import numpy as np
from lib.win import theWinnerIs


CYPHER_MATRIX = None


def generateAllPossibleGames(player_number=2):
    # Deck
    global CYPHER_MATRIX
    deck = Deck(-1)

    all2Combinations = [str(list(hand)) for hand in combinations(deck.deck, 2)]
    combination52of2 = len(all2Combinations)

    CYPHER_MATRIX = pd.DataFrame(np.zeros((combination52of2, combination52of2)),
                                 columns=all2Combinations, index=all2Combinations)
    # print(df)

    allPossibleGames = [[hands] for hands in combinations(deck.deck, 4)]
    return allPossibleGames


# Generate all possible hands before iterating on combination of table
start = perf_counter()

allPossibilities = generateAllPossibleGames()
# To be iterated
for possible in allPossibilities:
    unshuffledDeck = Deck(-1)
    print("Total Futures", len(allPossibilities))
    # Cypher
    card1 = unshuffledDeck.removeCard(possible[0][0])
    card2 = unshuffledDeck.removeCard(possible[0][1])
    cypher_hand = [card1, card2]

    # Nora
    card3 = unshuffledDeck.removeCard(possible[0][2])
    card4 = unshuffledDeck.removeCard(possible[0][3])
    nora_hand = [card3, card4]

    hands = [cypher_hand, nora_hand]

    # Combination of tables
    COUNTER = [0, 0]
    counter = 0
    print(f"Hands:{hands}")

    for sample_table in combinations(unshuffledDeck.deck, 5):
        sample_table = list(sample_table)

        COUNTER[theWinnerIs(hands, sample_table)] += 1
        counter += 1
        if counter % 10_000 == 0:
            print(counter)

    count = COUNTER[0] + COUNTER[1]
    row = CYPHER_MATRIX.columns.tolist().index(str(cypher_hand))
    col = CYPHER_MATRIX.columns.tolist().index(str(nora_hand))

    CYPHER_MATRIX.iloc[row, col] = COUNTER[0] / (count)
    print('P(Cypher) =', CYPHER_MATRIX.iloc[row, col], end="")

    end = perf_counter()
    print(" Elapsed Time", end-start)
    start = perf_counter()


# Save before anything
CYPHER_MATRIX.to_csv('probs.csv')
