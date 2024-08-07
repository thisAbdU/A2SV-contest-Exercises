import sys


def num():
    return int(sys.stdin.readline().strip())

def min_sum(s):
    if s > 45: 
        return -1
    result = []
    for digit in range(9, 0, -1):  
        if s >= digit:
            result.append(digit)
            s -= digit

    result.reverse()
    return int(''.join(map(str, result)))

test = num()
for t in range(test):
    s = num()
    print(min_sum(s))