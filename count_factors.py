from collections import defaultdict

def count(n):
    factors = defaultdict(int)
    count = 1

    i = 2
    while i * i <= n:
        while n%i == 0:
            factors[i] += 1
            n //= i
        
        i += 1

    if n > 1:
        factors[i] += 1

    for val in factors.values():
        count *= (val + 1)
    
    return count

n = int(input())
for _ in range(n):
    num = int(input())
    print(count(num))
    