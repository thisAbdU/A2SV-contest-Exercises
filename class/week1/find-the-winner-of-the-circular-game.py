class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [num for num in range(1, n + 1)]
        index = 0

        while len(friends) > 1:
            index = (index + k - 1) % n
            friends.pop(index)
            n -= 1

        return friends[0]
