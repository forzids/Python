user_info = []
while True:
    line = input("Please insert some strings, to Exit press Enter: ")
    if line == '':
        exit()
    else:
        new_line = line + '\n'
        user_info.append(new_line)

    with open("test_hw5_1.txt", "w", encoding="utf-8") as file_obj:
        file_obj.writelines(user_info)
