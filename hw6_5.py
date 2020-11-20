class Stationery():
    title = ""

    def __init__(self, title):
        self.title = title

    def draw(self):
        draw = "Drawing start"
        return draw


class Pen(Stationery):

    def draw(self):
        draw = "Draw like in school"
        return draw


class Pencil(Stationery):

    def draw(self):
        draw = "Draw like an artist"
        return draw


class Handle(Stationery):

    def draw(self):
        draw = "Draw like a modern artist"
        return draw


a = Stationery("Start")
print(a.draw())
print("\n")
b = Pen("Pen")
print(f"Draw with {b.title}")
print(b.draw())
print("\n")
c = Pencil("Pencil")
print(f"Draw with {c.title}")
print(c.draw())
print("\n")
d = Handle("Handle")
print(f"Draw with {d.title}")
print(d.draw())


