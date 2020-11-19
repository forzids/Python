input_string = input("Enter a list elements separated by space ")
mylist = input_string.split()
print("user list is ", mylist)
item = 0
while item < len(mylist) - 1:
    mylist[item], mylist[item + 1] = mylist[item + 1], mylist[item]
    item = item + 2
    print(mylist)
    continue
