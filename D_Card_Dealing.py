for _ in range(int(input())):
    n = int(input())

    upto = 1
    arr = []
    prefix = 0
    while prefix + upto + 1 <= n:
        arr.append(upto)
        prefix += upto
        upto += 1
    
    if prefix < n:
        arr.append(n - prefix)

    alice = arr[0]
    bob = 0

    i = 1
    Flag = True
    while i < len(arr):
        if Flag:
            bob += arr[i]
            if i + 1 < len(arr):
                bob += arr[i + 1]
            Flag = False
        else:
            alice += arr[i]
            if i + 1 < len(arr):
                alice += arr[i + 1]
            Flag = True
        i += 2

    print(alice, bob)