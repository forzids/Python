def my_func(user_num1, user_num2):
    try:
        divis = user_num1 / user_num2
    except ZeroDivisionError:
        return "Please don't use zero"
    return divis


print(my_func(user_num1=int(input("Please insert first number: ")),
              user_num2=int(input("Please insert second number(but not 0): "))))
