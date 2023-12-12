class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges)
        for i in range(len(ranges)):
            if ranges[i][0] <= left <= ranges[i][1]:
                left = ranges[i][1] + 1
        return left > right
                
        