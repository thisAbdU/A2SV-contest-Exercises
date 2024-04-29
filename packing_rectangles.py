def packing_rectnagle(w, h, n):
    def check(s, n):
        if (s//w ) * (s//h) > n:
            return True
        return False
    left, right = min(h, w) * n, max(h, w)*n
    while left < right:
        mid = left + (right - left)//2
        if check(mid, n):
            right = mid 
        else:
            left = mid + 1
    return left

w = int(input())
h = int(input())
n = int(input())

print(packing_rectnagle(w, h, n))
