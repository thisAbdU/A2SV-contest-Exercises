class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        cards =deque()
        for card in sorted(deck, reverse=True):
            if cards:
                cards.appendleft(cards.pop())
            cards.appendleft(card)
        return list(cards)
        
        