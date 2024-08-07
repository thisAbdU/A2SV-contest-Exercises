def distribute_cards(n, cards):
    total_sum = sum(cards)
    target_sum = total_sum // (n // 2)
    
    card_indx = []
    for i, c in enumerate(cards):
        card_indx.append([c, i + 1])
    
    card_indx.sort()
    pairs = []
    left, right = 0, n - 1
    while left < right:
        if card_indx[left][0] + card_indx[right][0] == target_sum:
            pairs.append((card_indx[left][1], card_indx[right][1]))
            left += 1
            right -= 1
        elif card_indx[left][0] + card_indx[right][0] < target_sum:
            left += 1
        else:
            right -= 1
    
    return pairs

# Input
n = int(input())
cards = list(map(int, input().split()))

# Output
pairs = distribute_cards(n, cards)
for pair in pairs:
    print(pair[0], pair[1])