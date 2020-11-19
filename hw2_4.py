input_string = input("Enter a list elements separated by space ")
mylist = input_string.split()
for el in mylist:
    print(el[:10])
