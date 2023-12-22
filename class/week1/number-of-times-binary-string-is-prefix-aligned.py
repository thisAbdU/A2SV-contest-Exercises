class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        currentMax = flips[0]
        flipp = 0
        count = 0
        for flip in range(len(flips)):
            flipp += 1
            currentMax = max(currentMax, flips[flip])
            if flipp == currentMax:
                count += 1
        return count