from collections import defaultdict
import random
import sys
rand = random.randint(1217, 2000)

def mp():
    return list(map(int, sys.stdin.readline().strip().split()))
def num():
    return int(sys.stdin.readline().strip())
def st():
    return sys.stdin.readline().strip()
def mc():
    return map(int, input().split())

def chk():
    n_m_k = mp()
    return "YES" if (n_m_k[0] * n_m_k[1]) - 1 == n_m_k[2] else "NO"

c = num()
for i in range(c):
    print(chk())