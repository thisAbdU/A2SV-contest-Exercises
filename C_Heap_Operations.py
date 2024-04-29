import heapq

def heap_operation(arr):
    store = []
    heapq.heapify(store)
    res = []

    for op, num in arr:
        if op == 'insert':
            heapq.heappush(store, num)
            res.append((op, num))
        elif op == 'removeMin':
            if store:
                heapq.heappop(store)
            else:
                res.append(("insert", 0))
            res.append((op))
        elif op == 'getMin':
            while store and store[0] < num:
                heapq.heappop(store)
                res.append(("removeMin"))
            if not store or store[0] > num:
                heapq.heappush(store, num)
                res.append(("insert", num))
            res.append((op, num))

    n = len(res)
    print(n)
    for i in range(n):
        if len(res[i]) == 2:
            print(*res[i])
        else:
            print(res[i][0])

n = int(input())
arr = []
for i in range(n):
    s = input().split(" ")
    if len(s) > 1:
        arr.append((s[0], int(s[1])))
    else:
        arr.append((s[0], 0))
heap_operation(arr)
