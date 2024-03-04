class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = max_score = 0
        n = len(tokens)
        tokens.sort()
        left, right = 0, n - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                max_score = max(score, max_score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return max_score

            
        