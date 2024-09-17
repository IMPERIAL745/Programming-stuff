from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def drawCard(self, deck):
        self.hand.add(deck.removeCard())
        if self.hand.busted():
            print(f"{self.name} busts with {self.hand} !")

    @abstractmethod
    def haveTurn(self, deck):
        choice = ''
        while not self.hand.busted() and (choice := self.readChoice()) != 's':
            if choice == 'd':
                self.drawCard(deck)
            else:
                self.help()
    def __str__(self):
        return super().__str__()