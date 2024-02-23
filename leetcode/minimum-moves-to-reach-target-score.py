class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_operation = 0
        while maxDoubles > 0 and target > 1:
            if target%2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            min_operation += 1
        min_operation += target - 1
        return min_operation 
        
        