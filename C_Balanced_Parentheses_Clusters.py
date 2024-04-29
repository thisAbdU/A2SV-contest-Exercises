def balanced_para(n, arr):
    ans = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            if arr[i] == "(":
                ans += 1
    return ans

test = int(input())
for t in range(test):
    n = int(input())
    arr = input()
    print(balanced_para(n, arr))
