class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sortedcost = []
        n = max(costs) + 1
        countCosts = [0 for i in range(n)]
        for cost in costs:
            countCosts[cost] += 1
        for i in range(len(countCosts)):
            if countCosts[i] == 0:
                continue
            else:
                for k in range(countCosts[i]):
                    sortedcost.append(i)
        count = 0
        i = 0
        while i < len(sortedcost):
            coins -= sortedcost[i]
            if coins < 0:
                break
            else:
                count += 1
            i += 1
        return count
        