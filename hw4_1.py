from sys import argv

name, w_hour, s_hour, bon = argv
try:
    w_hour = int(w_hour)
    s_hour = int(s_hour)
    bon = int(bon)
    res = int((w_hour * s_hour) + bon)
    print(res)
except TypeError:
    print('Error')
