from typing import Counter


def coin_game(s):
    cs = Counter(s)
    
    if cs["U"] % 2!= 0:
        return "YES"
    return "NO"

test = int(input())
for t in range(test):
    n = int(input())
    s = input()
    print(coin_game(s))


