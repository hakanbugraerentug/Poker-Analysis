import sys
import os
import pytest
import inspect

sys.path.append(os.getcwd())

try:
    from lib.card import Deck
except:
    raise ImportError("./lib folder could not be imported")


def test_deck():
    deck = Deck()

    print(deck)
