class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow_count, last = 0, float('-inf')
        sorted_points = sorted(points, key=lambda x:x[1])
        for start, end in sorted_points:
            if start > last:
                arrow_count += 1
                last = end

        return arrow_count