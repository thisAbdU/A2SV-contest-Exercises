class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        output = []
        for point in points:
            distances.append([math.pow(point[0]**2 + point[1]**2, 0.5), point[0], point[1]])
        distances.sort()
        for i in range(k):
            output.append([distances[i][1], distances[i][2]])
        return output