def find_factors(n):
    factors = []
    i = 2
    while i <=  n:
        while n%i == 0:
            factors.append(i)
            n //= i

        i += 1
    return factors


n = int(input())
fact = find_factors(n)
res = ""
for f in fact:
    res += 'x' + str(f)

print(res[1:])