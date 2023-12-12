class Solution:
    @staticmethod
    def findWinners(matches: List[List[int]]) -> List[List[int]]:
        # Identify the winners and the losers
        winners = [match[0] for match in matches]
        losers = [match[1] for match in matches]

        # Remove winners that were losers at some point
        winners_count = Counter(winners)
        losers_to_remove = []
        for loser in losers:
            if loser in winners_count:
                losers_to_remove.append(loser)

        for loser in losers_to_remove:
            del winners_count[loser]

        # Remove losers that lost more than once
        loser_count = Counter(losers)
        losers_to_remove = [loser for loser, count in loser_count.items() if count > 1]
        for loser in losers_to_remove:
            del loser_count[loser]

        return [sorted(list(winners_count.keys())), sorted(list(loser_count.keys()))]
        