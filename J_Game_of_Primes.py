import math


MAX = (10**6)+7

prime = [True for i in range(MAX)]
p = 2
while (p * p <= MAX):
    if (prime[p] == True):
        for i in range(p * p, MAX, p):
            prime[i] = False
    p += 1

def find_divisor(n):
        i = 2
        while i * i <= n:
            if n%i == 0:
                return n//i
            i += 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    not_primes = []

    for i in a:
        if prime[i] or i == 1:
            cnt += 1
        else:
            not_primes.append(i)

    ncnt = 0
    for n in not_primes:
        if prime[find_divisor(n)] and prime[n//find_divisor(n)]:
            not_primes.remove(n)
            cnt += 1
        elif prime[find_divisor(n)] or prime[n//find_divisor(n)]:
            ncnt += 1

    cnt += math.ceil(ncnt/2)

    print(cnt)
