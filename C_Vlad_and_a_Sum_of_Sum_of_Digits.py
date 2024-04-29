
prerfix = [0] * (2 * (10 ** 5) + 1)
for i in range(1, 2 * (10 ** 5) + 1):
    prerfix[i] = sum(map(int, list(str(i)))) + prerfix[i-1]


tesst = int(input())
for i in range(tesst):
    num = int(input())
    print(prerfix[num])