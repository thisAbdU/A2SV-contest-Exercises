import math


def prime_factor(n):
    factor_list = ""

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        while n%i == 0:
            factor_list += str(i)
            factor_list += "*"
            n /= i
    return factor_list[:len(factor_list)-1] if factor_list else str(n)


n = int(input())
print(prime_factor(n))