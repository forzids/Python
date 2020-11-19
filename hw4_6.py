from itertools import cycle, count, islice

my_list = [el for el in islice(count(3), 10)]
print(my_list)
my_iter = cycle(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
