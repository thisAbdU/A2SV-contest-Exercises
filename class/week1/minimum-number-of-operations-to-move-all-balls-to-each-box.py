class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0 for num in boxes]
        operation, count = 0, 0
        
        for i in range(len(boxes)):
            result[i] += operation
            count += int(boxes[i])
            operation += count
        
        operation, count = 0, 0
        
        for i in range(len(boxes) - 1, -1, -1):
            result[i] += operation
            count += int(boxes[i])
            operation += count
        
        return result