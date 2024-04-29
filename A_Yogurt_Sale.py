def yogurt_sale(n_a_b):
    n, a, b= n_a_b

    if n%2 == 0:
        return min(n*a, (n//2)*b)
    else:
        return min(n*a, ((n-1)//2)*b + a)


test = int(input())
for t in range(test):
    n_a_b = list(map(int, input().split()))
    print(yogurt_sale(n_a_b))
