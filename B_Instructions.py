from collections import defaultdict
import sys, threading


def instructions(n, arr):
    max_cnt = 0
    cnt = 0
    for i, v in enumerate(arr):
        if v > n:
            max_cnt = max(max_cnt, v)

        cnt = v
        curr = i + arr[i]
        while curr < n:
            # print(curr)
            cnt += arr[curr]
            curr += arr[curr]
   
        max_cnt = max(cnt, max_cnt)
    return max_cnt


def main():
    test = int(input())
    for t in range(test):
        n = int(input())
        arr = list(map(int, input().split()))
        print(instructions(n, arr))



if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
