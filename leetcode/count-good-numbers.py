class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = 10**9 + 7
        def count(x, n):
            result = 1
            while n > 0:
                if n%2 == 1:
                    result = (result * x)% modulo
                x = (x * x)% modulo
                n //= 2
            return result
        return (count(5, (n+1)//2) * count(4, n//2))% modulo