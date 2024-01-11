from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        INF = float('inf')
        best = INF
        
        for i, c in enumerate(cards):
            if c in seen:
                best = min(best, i - seen[c])
                
            seen[c] = i
            
        return -1 if best == INF else best + 1
