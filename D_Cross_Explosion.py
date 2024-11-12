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

directions = [(1 , 0 ) , (0 , 1) , (-1 , 0) , (0 , -1)]

h, w, q = read_int_list()
def inbound(row , col):
    return (1 <= row <= h) and (1 <= col <= q)


queries = []
for _ in range(q):
    queries.append(read_int_tuple())

destroyed = set()
for x, y in queries:
    if (x, y) not in destroyed:
        destroyed.add((x, y))
    else:
        for r, c in directions:
            newx, newy = x + r, y + c
            if inbound(newx, newy):
                destroyed.add((newx, newy))

print(destroyed)