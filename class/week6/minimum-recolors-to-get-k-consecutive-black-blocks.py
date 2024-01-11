class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        operation = 0
        min_operation = float('inf')
        for right in range(len(blocks)):
            if blocks[right] == "W":
                operation += 1

            while right - left + 1 > k:
                if blocks[left] == "W":
                    operation -= 1
                left += 1

            if right - left + 1 == k:
                min_operation = min(min_operation, operation)

        return min_operation

