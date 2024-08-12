import math


MAX = (10**6)+7

prime = [True for i in range(MAX)]
p = 2
while (p * p <= MAX):
    if (prime[p] == True):
        for i in range(p * p, MAX, p):
            prime[i] = False
    p += 1


primeFactor = [True for i in range(MAX)]
p = 2
while p * p <= MAX:
    if primeFactor[p]:
        for i in range(p * p, MAX + 1, p):
            primeFactor[i] = (p , i)
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
        if prime[i]:
            cnt += 1
        else:
            not_primes.append(i)

    for n in not_primes:
        if not primeFactor[n]:
            a, b = primeFactor[n]
            if prime[n//2] and prime[a]:
                not_primes.remove(n)
                cnt += 1

    if cnt%2 == 1:
        cnt += len(not_primes)//2
    else:
        cnt += math.ceil(len(not_primes)/2)