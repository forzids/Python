max_dig = 0
user_num = int(input("Please insert number: "))
while user_num != 0:
    i = user_num // 10
    a = user_num % 10
    if max_dig < a:
        max_dig = a
    else:
        max_dig = max_dig
    user_num = i
    continue
print("Max digit is:", max_dig)
