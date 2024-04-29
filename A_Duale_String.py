from typing import Counter


def duale(s):
    if len(s)%2 != 0:
        return "NO"
    
    check = []
    for i in range(len(s)//2):
        check.append(s[i])

    check = "".join(check)

    if s.count(check) == 2:
        return "YES"

    return "NO"

n = int(input())
for i in range(n):
    s = input()
    print(duale(s))

