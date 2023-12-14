class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # Use a set to keep track of seen numbers and detect cycles
        
        while n != 1 and n not in seen:
            seen.add(n)
            square_sum = sum(int(digit) ** 2 for digit in str(n))
            n = square_sum
        
        return n == 1
