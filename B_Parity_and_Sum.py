import heapq

def parity_sum(a, arr):
    even_only, max_odd = [], -float('inf')

    for num in arr:
        if num%2 == 0:
            heapq.heappush(even_only, num)
        else:
            max_odd = max(max_odd, num)

    if len(even_only) == len(arr):
        return 0
    
    cnt = 0

    while even_only:
        eve = heapq.heappop(even_only)
        if eve <= max_odd:
            cnt += 1
        else:
            cnt += 2
        
        max_odd = max(max_odd, eve + max_odd)

    return cnt

test = int(input())
for _ in range(test):
    num = int(input())
    arr = list(map(int, input().split()))
    print(parity_sum(num, arr))

        

    


  
    

