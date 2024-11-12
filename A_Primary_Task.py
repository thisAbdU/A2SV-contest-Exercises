for _ in range(int(input())):
    n = input()
    print(n[:2], n[2:])
    if int(n[:2]) == 10 and int(n[2:]) >= 2:
        print("YES")
    else:
        print("NO")