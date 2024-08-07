def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def can_be_sorted(arr):
    n = len(arr)
    for i in range(n):
        cyclic_permutation = arr[i:] + arr[:i]
        if is_sorted(cyclic_permutation):
            return True
    return False

t = int(input())

results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if can_be_sorted(arr):
        results.append("Yes")
    else:
        results.append("No")
        
for result in results:
    print(result)
