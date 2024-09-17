from Hand import Hand


class Player:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hand = Hand()

    def drawCard(self, deck):
        self.hand.add(deck.removeCard())
        if self.hand.busted():
            print(f"{self.name}  busts with {self.hand} !")

    def haveTurn(self, deck):
        choice = ''
        while not self.hand.busted() and (choice := self.readChoice()) != 's':
            if choice == 'd':
                self.drawCard(deck)
            else:
                self.help()

    def readChoice(self) -> str:
        print(f"{self.name} has {self.hand} - choice (d/s): ")
        return input()

    def decide(self, dealerHand):
        if self.hand.beats(dealerHand):
            print(f"{self.name} wins with {self.hand} !")
        elif not self.hand.busted():
            print(f"{self.name} loses with {self.hand}.")

    def help(self):
        print("Player menu options:")
        print("d = draw")
        print("s = stand")

    def __str__(self) -> str:
        return f"{self.name} has {self.hand} for a total of {self.hand}"
