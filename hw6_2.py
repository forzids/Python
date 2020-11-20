class Road:
    _length = ""
    _width = ""

    def __init__(self):
        Road._length = int(input("Insert length: "))
        Road._width = int(input("Insert width: "))

    def mass(self):
        result = int((Road._length * Road._width * 25 * 5) / 1000)
        print(f"Result in tons: {result}")


a = Road()
a.mass()
