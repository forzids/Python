seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']
seasons_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}
month_num = int(input("Please input number of month(1-12): "))
if month_num == 1 or month_num == 12 or month_num == 2:
    print(f'It is a {seasons_dict.get(1)}, very cold {seasons_list[0]}')
if month_num == 3 or month_num == 4 or month_num == 5:
    print(f'It is a {seasons_dict.get(2)}, blooming {seasons_list[1]}')
if month_num == 6 or month_num == 7 or month_num == 8:
    print(f'It is a {seasons_dict.get(3)}, hot {seasons_list[2]}')
if month_num == 9 or month_num == 10 or month_num == 11:
    print(f'It is a {seasons_dict.get(4)}, rainy {seasons_list[3]}')
else:
    print("We have no such month yet")
