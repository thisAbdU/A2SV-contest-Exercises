class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        totalsum = sum(distance)
        oneWay = sum(distance[min(start, destination):max(start, destination)])
        return min(abs(totalsum - oneWay), oneWay)