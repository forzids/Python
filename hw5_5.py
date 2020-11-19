with open("text_5.txt", "w", encoding="utf-8") as file_obj_1:
    numbs = input("Please insert numbers: ")
    my_list = [num for num in numbs.split()]
    print(my_list)
    amount = 0
    for num in my_list:
        amount += int(num)

    file_obj_1.write(f"Sum is: {amount}")
