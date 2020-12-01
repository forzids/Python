class ComplexNum:

    def __init__(self, cnum):
        self.cnum = cnum

    def __add__(self, other):
        real = self.cnum.real + other.cnum.real
        imag = self.cnum.imag + other.cnum.imag
        return f'{real} + {imag}j'

    def __mul__(self, other):
        real = self.cnum.real * other.cnum.real - self.cnum.imag * other.cnum.imag
        imag = self.cnum.real * other.cnum.imag + self.cnum.imag * other.cnum.real
        return f'{real} * {imag}j'


cnum1 = ComplexNum(12 + 3j)
cnum2 = ComplexNum(4 + 2j)
print(cnum1 + cnum2)
print(cnum1 * cnum2)
