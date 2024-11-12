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

for _ in range(read_int()):
    n, k = read_int_tuple()
    s = read_str()

    i, j = 0, n - 1

    changed = False

    while i < j - 1:
        if k > 0 and s[i] != s[j]:
            changed = True
            print("NO")
            break
        if k < 0:
            break
        i += 1
        j -= 1
        k -= 1
    
    if not changed:
        if k <= 0:
            print("YES")
        else:
            print("NO")

