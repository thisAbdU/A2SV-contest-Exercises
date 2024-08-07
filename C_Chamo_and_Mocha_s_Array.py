def chamo_Mocha(arr):
    arr.sort()
    return arr[-2]


test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    print(chamo_Mocha(arr))

    