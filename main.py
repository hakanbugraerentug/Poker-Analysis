from lib.card import *
from lib.game import Game
from lib.player import Player
import time


NUMBER_OF_PLAYERS = 5

x = 0
while x < 1:

    pokerGame = Game(player_number=NUMBER_OF_PLAYERS)

    hands = pokerGame.dealFirstCards()

    pokerGame.openFlopCards()

    pokerGame.openTurnCard()
    pokerGame.openRiverCard()

    #g.set_table([Card(0, 5), Card(0, 3), Card(0, 4), Card(0, 2), Card(0, 6)])
    pokerGame.godMode()

    pokerGame.deck.describe()
    
    x += 1
    time.sleep(3)
    """
    cypher = Player()
    print(cypher.balance)

    cypher.takeCards(hands[0])
    # print(cypher.hand)

    information = {
        "player_number": NUMBER_OF_PLAYERS,
        "hand": cypher.hand,
        "table": pokerGame.table
    }
    print(pokerGame.table + cypher.hand)

    """
    pass
