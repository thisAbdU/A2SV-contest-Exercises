class Solution:
    def maxScore(self, s: str) -> int:
        no_of_ones = 0
        for num in s:
            if num == '1':
                no_of_ones += 1
        score = 0
        max_score = -float('inf')
        no_of_zero = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                no_of_zero += 1
            else:
                no_of_ones -= 1
            score = no_of_zero + no_of_ones
            max_score = max(score, max_score)
        return max_score
