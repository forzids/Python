class Cell:

    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return self.cell - other.cell if (self.cell - other.cell) > 0 else print("Cannot be negative")

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def __str__(self):
        return f"{self.cell}"

    def make_order(self, cell_in_row):
        row = ''
        for i in range(int(self.cell / cell_in_row)):
            row += f'{"*" * cell_in_row}\n'
        row += f'{"*" * (self.cell % cell_in_row)}'
        return row


cell1 = Cell(12)
cell2 = Cell(13)
print(cell1)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1.make_order(5))
print()
print(cell2.make_order(4))
