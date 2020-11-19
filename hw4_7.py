def factor(n):
    start = 1
    fact = 1
    while start <= n:
        yield fact
        start = start + 1
        fact = fact * start


for i in factor(5):
    print(i)
