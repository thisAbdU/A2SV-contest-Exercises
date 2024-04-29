def seeking_odd(num):
    if num%2 != 0:
        return "YES"
    i = 2
    while i * i < num:
        while num%i == 0:
            if i % 2 != 0:
                return "YES"
            num  = num//i
        i += 1

        if num > 1 and num%2 != 0:
            return "YES"
    return "NO"

test = int(input())
for t in range(test):
    n = int(input())
    print(seeking_odd(n))