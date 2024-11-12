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
    cnt = 0
    if n < k:
        print(n)
    else:
        while n%k == 0:
            n //= k
            if n <= 1:
                break
        else:
            n -= 1
        cnt += 1
    
    if cnt:
        print(cnt)

        
def find_fractions(n):
    # Step 1: Find all divisors of n that are greater than 1 and less than n
    divisors = [b for b in range(2, n) if n % b == 0]
    
    # Step 2: Prepare the fractions
    fractions = []
    for b in divisors:
        a = b - 1  # Choose a = b - 1
        fractions.append((a, b))
    
    # Step 3: Output the result
    if fractions:
        print("YES")
        print(len(fractions))
        for a, b in fractions:
            print(a, b)
    else:
        print("NO")

# Example usage
n = int(input())
find_fractions(n)
