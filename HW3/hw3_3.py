def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    a = max(my_list)
    my_list.remove(a)
    b = max(my_list)
    return a + b


print(f"Sum of two max arguments is: {my_func(10, 40, 30)}")
