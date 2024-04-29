def Harmony(len_, arr1, arr2, x):
    for i in range(len_):
        if arr1[i] + arr2[len_-i-1] > x:
            return "No"
    return "Yes"

testCase = int(input())
for test in range(testCase):
    len_x = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(Harmony(len_x[0], arr1, arr2, len_x[1]))
    if test < testCase - 1:
        empty = input()


        