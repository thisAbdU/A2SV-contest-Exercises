class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, len(cardPoints) - k
        current_sum = sum(cardPoints[right:])
        max_score = current_sum
        
        while right < len(cardPoints):
            current_sum += -cardPoints[right] + cardPoints[left]
            max_score = max(max_score, current_sum)
            right += 1
            left += 1
            
        return max_score