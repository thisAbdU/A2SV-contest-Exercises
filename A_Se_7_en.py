def seven(n):
    if not n%7:
        return n
    modulo = n%7
    if modulo <=3:
        n -= modulo
    else:
        n -= modulo
    return n
test = int(input())
for _ in range(test):
    n = int(input())
    print(seven(n))
