import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Go")

    def stop(self):
        print("Stop")

    def turn(direction):
        items = ['right', 'left', 'forward', 'back']
        direction = random.choice(items)
        return direction

    def show_speed(self):
        return self


class TownCar(Car):
    def show_speed(self):
        if self.speed > '60':
            speed = "Please decrease the speed"
        return speed


class SportCar(Car):
    def show_speed(self):
        return self


class WorkCar(Car):
    def show_speed(self):
        if self.speed > '40':
            speed = "Please decrease the speed"
        return speed


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > '60':
            x = ""
            print(f"Is he on duty? y/n {x}")
            x = input().lower()
            if x == 'y':
                speed = "All is ok, he is on duty"
            elif x == 'n':
                speed = "Please decrease the speed"
        return speed


a = Car("20", "blue", "Lexus", False)
print(f"Car's direction is : {a.turn()}")
print("\n")
b = PoliceCar("70", "blue", "Mercedes", True)
print(f"Car with name {b.name} rides with speed {b.speed}")
print(b.show_speed())
print("\n")
c = WorkCar("80", "white", "Lada", False)
print(f"Car with name {c.name} rides with speed {c.speed}")
print(c.show_speed())
