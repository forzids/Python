my_list = [3, 45, 6, 7, 23, 65, 55, 3, 67, 100]
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(f"Old list: {my_list}")
print(f"New list: {new_list}")
