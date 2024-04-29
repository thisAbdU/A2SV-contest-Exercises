from typing import Counter


def nene_and_card(arr):
    count = Counter(arr)
    
    c = count.values()
    counter =  0
    max_ = max(c)
    if max_ > 1:
        for x in c:
            if x == max_:
                counter += 1
        return counter
    else:
        return 0


test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    print(nene_and_card(arr))