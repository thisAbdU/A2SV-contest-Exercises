class Solution:
    def minimumSteps(self, s: str) -> int:
        zero_count, moves = 0, 0
        for i in range(len(s)):
            if s[i] == "0":
                zero_count += 1
                moves += i - zero_count + 1
        return moves
        