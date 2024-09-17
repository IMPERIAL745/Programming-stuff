
from Deck import Deck
from Hand import Hand
from Player import Player


class Dealer:

    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        self.players = []

        self.players.append(Player("Jack"))
        self.players.append(Player("Jill"))

    def use(self) -> None:
        self.shuffle()
        self.deal()
        self.deal()
        if not self.hand.isBlackjack():
            self.goRound()
        self.decide()

    def shuffle(self) -> None:
        self.deck.shuffle()

    def deal(self) -> None:
        for player in self.players:
            player.drawCard(self.deck)
        self.drawCard(self.deck)

    def drawCard(self, deck) -> None:
        self.hand.add(deck.removeCard())
        if self.hand.busted():
            print(f"Dealer busts with {self.hand} !")

    def goRound(self) -> None:
        print(self)
        for player in self.players:
            player.haveTurn(self.deck)
        self.haveTurn()

    def haveTurn(self) -> None:
        while self.hand.value() < 17:
            self.drawCard(self.deck)

    def decide(self) -> None:
        if not self.hand.busted():
            print(self)
        for player in self.players:
            player.decide(self.hand)

    def __str__(self) -> str:
        return f"Dealer has {self.hand}"


if __name__ == '__main__':
    dealer = Dealer()
    dealer.use()
