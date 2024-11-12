import math

def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if is_prime[p]]

def count_divisors(a, max_value):
    divisors = []
    divisor_count = [0] * (max_value + 1)
    primes = set(sieve(max_value))
    
    for num in a:
        if num in primes:
            divisors.extend([1, num])
        else:
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisor_count[i] += 1
                    if i != num // i:
                        divisor_count[num // i] += 1
    divisors.sort()
    for i in range(1, max_value + 1):
        divisors.extend([i] * divisor_count[i])
    
    return divisors

def solve():
    with open('macarie.in', 'r') as fin:
        n, q = map(int, fin.readline().strip().split())

        a = list(map(int, fin.readline().strip().split()))

        pos = list(map(int, fin.readline().strip().split()))

    # n, q = read_int_tuple()
    # a = read_int_list()
    # pos = read_int_list()

    max_value = max(a)

    divisors = count_divisors(a, max_value)
    print(divisors)

    res = []
    for p in pos:
        res.append(divisors[p - 1])

    with open('macarie.out', 'w') as fout:
        fout.write(' '.join(map(str, res)) + '\n')
    # print(res)

def main():
    solve()

if __name__ == "__main__":
    main()
