for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input()))
    prev = sorted(num)

    diff = 0
    for i,j in zip(prev, num):
        if i != j:
            diff += 1
    
    total = 0
    for i in range(1, n):
        fs = str(prev[i-1]) + str(prev[i])
        total += int(fs)

    print((diff + 1)//2, total)
   
