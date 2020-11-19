with open("text_4_1.txt", "w", encoding="utf-8") as file_obj_1:
    with open("text_4.txt", "r", encoding="utf-8") as file_obj:
        my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
        new_list = []
        for lines in file_obj:
            list = lines.split()
            list[0] = my_dict.get(list[0])
            new_list.append(' '.join(list))
        file_obj_1.writelines('\n'.join(new_list))
        print(new_list)
