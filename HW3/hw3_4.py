def my_func(x, y):
    exp = x ** y
    return exp


def my_func2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    res = 1 / res

    return res


print(f"Result with using **: {my_func(2, -3)}")
print(f"Result without using **: {my_func2(2, -3)}")
