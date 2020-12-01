class MyExcept(Exception):
    def __init__(self, txt):
        self.txt = txt


d1 = input("Insert first number: ")
d2 = input("Insert second number: ")

try:
    d1 = int(d1)
    d2 = int(d2)
    if d2 == 0:
        raise MyExcept("Cannot be divided by zero")
except MyExcept as err:
    print(err)
else:
    print(f"Result is: {d1 / d2}")
