class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        pileSum = 0
        i, j = 0, len(piles) - 2
        while j > i:
            pileSum += piles[j]
            i += 1
            j -= 2
        return pileSum