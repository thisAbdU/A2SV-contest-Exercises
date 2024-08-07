def ribbo(arr):
    memo = {}
    def dp(n):
        if n == 1:
            return 