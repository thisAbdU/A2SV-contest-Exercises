import sys
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import inf, ceil
import math
from heapq import *

# Read a single integer input
read_int = lambda: int(sys.stdin.readline().strip())

# Read a list of integers from a single input line
read_int_list = lambda: list(map(int, sys.stdin.readline().strip().split()))

# Read a tuple of integers from a single input line
read_int_tuple = lambda: tuple(map(int, sys.stdin.readline().strip().split()))

# Read a list of strings from a single input line
read_str_list = lambda: sys.stdin.readline().strip().split()

# Read a list of integers, each digit as a separate element
read_digit_list = lambda: list(map(int, sys.stdin.readline().strip()))

# Read a list of characters from a single input line
read_char_list = lambda: list(sys.stdin.readline().strip())

# Read a single string input
read_str = lambda: sys.stdin.readline().strip()

# Check if a number is even
is_even = lambda x: x & 1 == 0

test = read_int()
for _ in range(test):
    n = read_int()
    arr = read_int_list()
    
    new_sort = sorted(arr)

    if len(set(arr)) == 1:
        print(0)
    elif new_sort[0] != new_sort[-1] and new_sort[0] == 1:
        print(-1)
    else:
        ope = 0
        min_val = min(arr)
        indx = arr.index(min_val)
        ans = []
        while True:
            for i, num in enumerate(arr):
                if min_val != num:
                    arr[i] = ceil(num / min_val)
                    ope += 1
                    ans.append((i, indx))
                    
                if min_val > arr[i]:
                    min_val = arr[i]
                    indx = i
                    break
            if len(set(arr)) == 1:
                break
    
        print(ope)
        for x, y in ans:
            print(x+1, y+1)

            