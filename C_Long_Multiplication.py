for _ in range(int(input())):
    a = list(input())
    b = list(input())

    swapped = False

    for i in range(len(a)):
        if a[i] != b[i] and not swapped:
            a[i], b[i] = max(a[i], b[i]), min(a[i], b[i])
            swapped = True
        else:
            a[i], b[i] = min(a[i], b[i]), max(a[i], b[i])

    print("".join(a))
    print("".join(b))
