my_list = [7, 5, 3, 3, 3, 2]
user_num = int(input("Please insert number: "))
for list_el in range(len(my_list)):
    if user_num in my_list:
        i = len(my_list) - 1 - my_list[::-1].index(user_num)
        my_list.insert(i + 1, user_num)
        break
    elif user_num > max(my_list):
        my_list.insert(0, user_num)
        break
    elif user_num < min(my_list):
        my_list.append(user_num)
        break
    elif my_list[list_el] > user_num and my_list[list_el + 1] < user_num:
        my_list.insert(list_el + 1, user_num)
        break
print(my_list)
