for _ in range(int(input())):
    n = int(input())
    num = input()

    if len(num) <= 2:
        print(int(num))

    max_2d = float('inf')
    min_ind = []

    for i in range(1, n):
        if num[i-1] == '0' or num[i] == '1':
            continue
        if int(num[i-1:i+1]) < max_2d:
            max_2d = int(num[i-1:i+1])
            min_ind = [i-1, i]

    
    nu = []
    i = 0
    while i < n:
        if i not in min_ind:
            nu.append(num[i])
            i += 1
        else:
            nu.append(num[i:i+2])
            i += 2

    total = 0
    # print(nu)
    for i in range(1, len(nu)):
        if nu[i] == '1':
            continue
        total += min(int(nu[i]) * int(nu[i-1]), int(nu[i]) + int(nu[i-1]))

    print(total)


