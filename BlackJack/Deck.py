import random
from Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["C", "D", "H", "S"]:
            for number in range(1, 14):
                self.cards.append(Card(number, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def removeCard(self) -> Card:
        return self.cards.pop()
