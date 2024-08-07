def is_beautiful_array(n, arr):
    if n < 3:
        return False

    arr.sort()
    min1 = arr[0]
    min2 = None

    for num in arr[1:]:
        if num % min1 != 0:
            min2 = num
            break

    if min2 is None:
        return True

    for num in arr:
        if num % min1 != 0 and num % min2 != 0:
            return False
    return True

t = int(input())

results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if is_beautiful_array(n, arr):
        results.append("Yes")
    else:
        results.append("No")

# Print all results
for result in results:
    print(result)
