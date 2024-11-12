import sys
from collections import defaultdict

input = sys.stdin.read

def main():
    data = input().split()
    x = int(data[1])
    arr = map(int, data[2:])

    prefix = 0
    check = defaultdict(int)
    check[0] = 1
    cnt = 0

    for num in arr:
        prefix += num
        cnt += check[prefix - x]
        check[prefix] += 1

    sys.stdout.write(str(cnt) + '\n')

if __name__ == "__main__":
    main()