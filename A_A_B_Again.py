def sum(a, b):
    return a + b

test = int(input())
for t in range(test):
    num = int(input())
    a = num//10
    b = num - (a*10)
    print(sum(a, b))