class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def value(self) -> int:
        if self.number > 10:
            return 10
        else:
            return self.number

    def hasValue(self, value) -> bool:
        return self.value() == value

    def __str__(self) -> str:
        return f"{self.number} of {self.suit}"

    def name(self) -> str:
        if self.number == 1:
            return "A"
        elif self.number == 11:
            return "J"
        elif self.number == 12:
            return "Q"
        elif self.number == 13:
            return "K"
        else:
            return str(self.number)

