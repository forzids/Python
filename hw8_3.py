val = 0


class MyExcept(Exception):

    def __init__(self, *args):
        self.my_list = []

    def my_func(self):
        global val
        while True:
            try:
                val = input("Input numbers and press Enter, to exit write 'stop': ")
                if val == 'stop':
                    print(f'List is: {self.my_list} \n ')
                    exit()
                if val.isdigit():
                    self.my_list.append(int(val))
                    print(f'List is: {self.my_list} \n ')
                if not val.isdigit():
                    raise MyExcept("Numbers only")
            except MyExcept as err:
                print(err)


d1 = MyExcept(1)
print(d1.my_func())
