for _ in range(int(input())):
    a, b = list(map(int, input().split()))

    total = a + 2 * b

    if total%2 != 0:
        print("NO")
    else:
        need = total//2

        curr = min(need, b)

        