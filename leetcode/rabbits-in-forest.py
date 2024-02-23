class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        countR = Counter(answers)
        noRabbit = 0
        for num in countR:
            noRabbit += math.ceil(countR[num]/(num + 1)) * (num + 1)
        return noRabbit