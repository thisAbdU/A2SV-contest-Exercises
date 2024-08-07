def split_set(n, arr):
    even_count = 0
    for num in arr:
        if num%2 == 0:
            even_count += 1
    if n - even_count:
        return "No"
    return "Yes"

test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    print(split_set(n, arr))
