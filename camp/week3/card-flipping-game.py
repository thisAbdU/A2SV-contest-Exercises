from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cant_taken = set()
        min_good = float('inf')
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                cant_taken.add(fronts[i])
        for card in (fronts + backs):
            if card not in cant_taken:
                min_good = min(min_good, card)
        return min_good if min_good != float('inf') else 0