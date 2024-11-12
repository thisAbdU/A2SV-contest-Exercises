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


s = read_str()
k = read_int()

counter = Counter()
left = 0
max_length = -float('inf')

for right, ch in enumerate(s):
    counter[ch] += 1
    while len(counter) > k:
        counter[s[left]] -= 1
        if counter[ch] == 0:
            counter.pop(ch)
        left += 1
    max_length = max(max_length, right - left + 1)

print(max_length)