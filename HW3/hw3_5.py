sum_items = 0


def my_func(**kwargs):
    global sum_items
    my_list = list(map(int, input("Please insert numbers: ").split()))
    res = 0
    for el in range(len(my_list)):
        res = res + int(my_list[el])
    print(f"Intermediate result is: {res}")
    x = input("Do you want to continue? y/n: ")
    if x.lower() == 'y':
        sum_items = sum_items + res
        my_func()
    elif x.lower() == 'n':
        sum_items = sum_items + res
        return
    print(f"Final result is: {sum_items}")


my_func()
