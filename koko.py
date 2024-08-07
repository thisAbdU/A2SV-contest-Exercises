import math

def koko(a, b):
    if math.gcd(a, b) < 2:
        return "NO"
    else:
        return "YES"
    

test = int(input())
for _ in range(test):
    a, b = list(map(int, input().split()))
    print(koko(a, b))