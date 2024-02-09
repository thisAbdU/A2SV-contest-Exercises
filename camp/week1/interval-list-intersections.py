class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_index, second_index = 0, 0
        intersection = []
        
        while first_index < len(firstList) and second_index < len(secondList):
            start_first, end_first = firstList[first_index]
            start_second, end_second = secondList[second_index]
            
            start, end = max(start_first, start_second), min(end_first, end_second)
            if start <= end:
                intersection.append([start, end])
            
            if end_first < end_second:
                first_index += 1
            else:
                second_index += 1
                
        return intersection
    