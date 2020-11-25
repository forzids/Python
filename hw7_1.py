class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def __add__(self, other):
       return Matrix(list(map(lambda x, y: list(map(lambda z, w: z + w, x, y)),
                        self.matrix, other.matrix)))


a1 = Matrix([[1, 2], [3, 4], [5, 6]])
a2 = Matrix([[2, 3], [3, 4], [4, 5]])
a3 = a1 + a2
print(f"First Matrix \n{a1}")
print(f"Second Matrix \n{a2}")
print(f"Summa \n{a3}")

