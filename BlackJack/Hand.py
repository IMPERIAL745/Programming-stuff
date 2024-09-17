class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def value(self) -> int:
        total = 0
        for card in self.cards:
            total += card.value()
        return total

    def isBlackjack(self) -> bool:
        return len(self.cards) == 2 and self.has(1) and self.has(10)

    def has(self, value) -> bool:
        for card in self.cards:
            if card.hasValue(value):
                return True
        return False

    def busted(self) -> bool:
        return self.value() > 21

    def beats(self, other) -> bool:
        return (not self.busted()) and (self.value() > other.value() or other.busted())

    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.cards)
