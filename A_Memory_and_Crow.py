n = int(input())
arr = list(map(int, input().split()))

arr.reverse()
res = []
even_ = [arr[0]]
odd_ = [arr[1]]
res.append(arr[0])

for i in range(1, n):
    val = arr[i] - res[i - 1]
    if i%2 == 0:
        even_.append(arr[i] + even_[- 1])
        res.append(even_[-1] - res[-1])
    else:
        odd_.append(arr[i] + odd_[- 1])
        res.append(odd_[-1] - res[-1])

    print(odd_, even_)
res.reverse()
print(*res) 