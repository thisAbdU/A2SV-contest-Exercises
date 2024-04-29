from collections import defaultdict


def last_digit(n , arr):
    digits = []
    for i in range(n):
        digits.append(int(str(arr[i])[-1]))
    digits.sort()
    num_dict = defaultdict(int)
    i, j = 0, n-1
    while i <= j:
        if (digits[i] + digits[j])%10 - 3 in num_dict:
            return "YES"
        else:
            num_dict[digits[i]] += 1
        i += 1
    return "NO"

test = int(input())
for i in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    print(last_digit(n, arr))