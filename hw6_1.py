import time
from itertools import count


class TrafficLight:
    __color = ""

    def running(self):
        for el in count():
            print("\033[31m", "Stop!")
            time.sleep(1)
            self.__color = "red"
            print("\033[31m", self.__color)
            time.sleep(7)
            self.__color = "yellow"
            print("\033[33m", self.__color)
            time.sleep(2)
            self.__color = "green"
            print("\033[32m", self.__color)
            time.sleep(1)
            print("You can go now")
            time.sleep(7)
            self.__color = "yellow"
            print("\033[33m", self.__color)
            print("Attention!")
            time.sleep(2)


a = TrafficLight()
a.running()
