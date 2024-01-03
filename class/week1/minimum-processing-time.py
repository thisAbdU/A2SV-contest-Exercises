class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        i, j = 0, 0
        while j < len(tasks) - 3:
            processorTime[i] += tasks[j]
            j += 4
            i += 1

        minProcessingTime = max(processorTime)
        return minProcessingTime