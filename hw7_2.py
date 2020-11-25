class Clothes:

    def __init__(self, size, height):
        self.size = size
        self.height = height

    def coat_outgo(self):
        return self.size / 6.5 + 0.5

    def suit_outgo(self):
        return 2 * self.height + 0.3

    @property
    def common_outgo(self):
        return str(f"Common cloth: {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}")


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.coat_outgo = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f"Cloth to coat {self.size}"


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.suit_outgo = round(2 * self.height + 0.3)

    def __str__(self):
        return f"Cloth to suit {self.height}"

coat = Coat(10, 5)
suit = Suit(15, 4)
print(coat)
print(suit)
print(suit.common_outgo)
