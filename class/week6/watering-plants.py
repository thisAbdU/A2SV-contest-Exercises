class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps, currCapacity = 0, capacity
        for i in range(len(plants)):
            if currCapacity >= plants[i]:
                currCapacity -= plants[i]
                steps += 1
            else:
                currCapacity = capacity
                currCapacity -= plants[i]
                steps += (2 * i) + 1
        return steps
    