class Equipment:
    def __init__(self, brand, snum, model, name, *args):
        self.brand = brand
        self.snum = int(snum)
        self.model = model
        self.name = name
        self.all_equip = []
        self.unit = {'Model': self.model, 'Brand': self.brand, 'Serial number': self.snum, 'Name': self.name}

    def menu(self):
        menu_list = input(f'What do you want to do? \n'
                          f'1 - See all warehouse \n'
                          f'2 - Add printer \n'
                          f'3 - Add scanner \n'
                          f'4 - Add copier \n'
                          f'5 - Exit \n'
                          f'Please insert number: ')
        if menu_list == '1':
            print(self.all_equip)
            self.menu()
        elif menu_list == '2':
            Printer.add_print(self)
            self.add_to_warehouse()
            print('Thank you')
            print()
            self.menu()
        elif menu_list == '3':
            Scanner.add_scanner(self)
            self.add_to_warehouse()
            print('Thank you')
            print()
            self.menu()
        elif menu_list == '4':
            Copier.add_copier(self)
            self.add_to_warehouse()
            print('Thank you')
            print()
            self.menu()
        elif menu_list == '5':
            exit()

    def add_to_warehouse(self):
        model = input('Insert model: ')
        brand = input('Insert brand: ')
        snum = int(input('Insert serial number: '))
        new_unit = {'Model': model, 'Brand': brand, 'Serial number': snum}
        self.unit.update(new_unit)
        self.all_equip.append(self.unit)


class Printer(Equipment):

    def add_print(self):
        name = input("Insert name, name should start with prefix Pr_: ")
        if not name.startswith('Pr_'):
            name = 'Pr_' + name
        pr_name = {'Name': name}
        self.unit.update(pr_name)


class Scanner(Equipment):

    def add_scanner(self):
        name = input("Insert name, name should start with prefix Sc_: ")
        if not name.startswith('Sc_'):
            name = 'Sc_' + name
        sc_name = {'Name': name}
        self.unit.update(sc_name)


class Copier(Equipment):

    def add_copier(self):
        name = input("Insert name, name should start with prefix Cp_: ")
        if not name.startswith('Cp_'):
            name = 'Cp_' + name
        cp_name = {'Name': name}
        self.unit.update(cp_name)


equip = Printer('Canon', '12345', 'PrHtDc', 'Pr_printer')
print(equip.menu())
