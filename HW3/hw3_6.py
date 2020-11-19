def int_func(str):
    str = input("Please insert string with latin symbols only: ").title()
    if not str.isascii() and not str.isalpha():
        print("Only latin symbols please")
        int_func(str)
    else:
        print(str)


int_func(str)
